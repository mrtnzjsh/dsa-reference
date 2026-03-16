package main

import (
	"fmt"
	"time"

	"github.com/gomodule/redigo/redis"
)

type RateLimiterWindow struct {
	redis       redis.Conn
	windowSize  int
	maxRequests int
	prefix      string
}

func NewRateLimiterWindow(redisAddr string, windowSize int, maxRequests int) (*RateLimiterWindow, error) {
	conn, err := redis.Dial("tcp", redisAddr)
	if err != nil {
		return nil, err
	}
	return &RateLimiterWindow{
		redis:       conn,
		windowSize:  windowSize,
		maxRequests: maxRequests,
		prefix:      "rate_limit",
	}, nil
}

func (r *RateLimiterWindow) allowRequest(identifier string) (bool, string) {
	now := time.Now().Unix()
	key := fmt.Sprintf("%s:%s", r.prefix, identifier)
	windowStart := float64(now - r.windowSize)

	pipe := r.redis.pipeline()

	pipe.ZRangebyscore(key, windowStart, float64(now))
	pipe.ZCount(key, windowStart, float64(now))
	pipe.ZRange(key, 0, -1)
	pipe.ZAdd(key, map[string]float64{fmt.Sprintf("%d", now): float64(now)})
	pipe.ZRemRangeByScore(key, 0, windowStart-1)
	pipe.Expire(key, int64(r.windowSize))

	timestamps, currentCount, _, _, _, _, err := pipe.Execute()
	if err != nil {
		return false, fmt.Sprintf("Redis error: %v", err)
	}

	timeInWindow := float64(now - int(windowStart))
	rate := 0.0
	if timeInWindow > 0 {
		rate = float64(currentCount.(int64)) / timeInWindow
	}

	allowed := currentCount.(int64) < int64(r.maxRequests)
	message := fmt.Sprintf("Request %s (%d/%d requests in window, rate: %.2f/sec)",
		map[bool]string{true: "allowed", false: "denied"}[allowed],
		currentCount.(int64), r.maxRequests, rate)

	return allowed, message
}

func (r *RateLimiterWindow) getStatistics(identifier string) map[string]interface{} {
	key := fmt.Sprintf("%s:%s", r.prefix, identifier)
	windowStart := float64(time.Now().Unix() - r.windowSize)

	pipe := r.redis.pipeline()

	pipe.ZCount(key, windowStart, float64(time.Now().Unix()))
	pipe.ZRangebyscore(key, windowStart, float64(time.Now().Unix()))
	pipe.ZRange(key, 0, 0)
	pipe.ZRevRange(key, 0, 0)

	count, timestamps, oldest, newest, err := pipe.Execute()
	if err != nil {
		return map[string]interface{}{
			"identifier": identifier,
			"error":      "Failed to retrieve statistics",
		}
	}

	timestampsList, ok := timestamps.([]interface{})
	if !ok || len(timestampsList) == 0 {
		return map[string]interface{}{
			"identifier":           identifier,
			"allowed_requests":     0,
			"denied_requests":      0,
			"current_count":        0,
			"timestamp":            []float64{},
			"oldest_timestamp":     nil,
			"newest_timestamp":     nil,
			"window_usage_percent": 0.0,
		}
	}

	convertedTimestamps := make([]float64, len(timestampsList))
	for i, ts := range timestampsList {
		if t, ok := ts.([]interface{}); ok && len(t) > 1 {
			if val, ok := t[1].(float64); ok {
				convertedTimestamps[i] = val
			}
		}
	}

	allowed := int(count.(int64))
	denied := max(0, allowed-r.maxRequests)

	oldestTimestamp := oldest.([]interface{})
	newestTimestamp := newest.([]interface{})
	var oldestTS, newestTS *float64

	if len(oldestTimestamp) > 0 {
		if t, ok := oldestTimestamp[0].([]interface{}); ok && len(t) > 1 {
			if val, ok := t[1].(float64); ok {
				oldestTS = &val
			}
		}
	}

	if len(newestTimestamp) > 0 {
		if t, ok := newestTimestamp[0].([]interface{}); ok && len(t) > 1 {
			if val, ok := t[1].(float64); ok {
				newestTS = &val
			}
		}
	}

	return map[string]interface{}{
		"identifier":           identifier,
		"allowed_requests":     allowed,
		"denied_requests":      denied,
		"current_count":        allowed,
		"timestamp":            convertedTimestamps,
		"oldest_timestamp":     oldestTS,
		"newest_timestamp":     newestTS,
		"window_usage_percent": (float64(allowed) / float64(r.maxRequests)) * 100.0,
	}
}

func (r *RateLimiterWindow) reset(identifier string) bool {
	key := fmt.Sprintf("%s:%s", r.prefix, identifier)
	_, err := r.redis.Do("DEL", key)
	return err == nil
}

func (r *RateLimiterWindow) getRateLimitConfig(identifier string) map[string]interface{} {
	key := fmt.Sprintf("%s:%s", r.prefix, identifier)
	ttl, err := r.redis.Do("TTL", key)
	if err != nil {
		return map[string]interface{}{
			"identifier": identifier,
			"error":      "Failed to retrieve configuration",
		}
	}

	config := map[string]interface{}{
		"identifier":   identifier,
		"window_size":  r.windowSize,
		"max_requests": r.maxRequests,
		"current_ttl":  ttl,
		"rate":         0.0,
	}

	if ttl != nil {
		if rate, ok := ttl.(int64); ok && r.windowSize > 0 {
			config["rate"] = float64(r.maxRequests) / float64(r.windowSize)
		}
	}

	return config
}

func (r *RateLimiterWindow) Close() error {
	return r.redis.Close()
}

type RateLimiterWindowFixedSize struct {
	redis       redis.Conn
	windowSize  int
	maxRequests int
	prefix      string
}

func NewRateLimiterWindowFixedSize(redisAddr string, windowSize int, maxRequests int) (*RateLimiterWindowFixedSize, error) {
	conn, err := redis.Dial("tcp", redisAddr)
	if err != nil {
		return nil, err
	}
	return &RateLimiterWindowFixedSize{
		redis:       conn,
		windowSize:  windowSize,
		maxRequests: maxRequests,
		prefix:      "fixed_window",
	}, nil
}

func (r *RateLimiterWindowFixedSize) allowRequest(identifier string) (bool, string) {
	now := int64(time.Now().Unix())
	key := fmt.Sprintf("%s:%s:%d", r.prefix, identifier, now/r.windowSize)

	count, err := r.redis.Incr(key)
	if err != nil {
		return false, fmt.Sprintf("Redis error: %v", err)
	}

	allowed := count <= int64(r.maxRequests)
	message := fmt.Sprintf("Request %s (%d/%d requests in this window)",
		map[bool]string{true: "allowed", false: "denied"}[allowed],
		count, r.maxRequests)

	return allowed, message
}

func (r *RateLimiterWindowFixedSize) getStatistics(identifier string) map[string]interface{} {
	now := int64(time.Now().Unix())
	currentWindow := now / r.windowSize
	key := fmt.Sprintf("%s:%s:%d", r.prefix, identifier, currentWindow)

	count, err := r.redis.Do("GET", key)
	if err != nil {
		return map[string]interface{}{
			"identifier": identifier,
			"error":      "Failed to retrieve statistics",
		}
	}

	var countVal int64 = 0
	if count != nil {
		countVal = count.(int64)
	}

	return map[string]interface{}{
		"identifier":     identifier,
		"current_window": currentWindow,
		"current_count":  countVal,
		"window_size":    r.windowSize,
		"max_requests":   r.maxRequests,
		"current_ttl":    -2,
	}
}

func (r *RateLimiterWindowFixedSize) Close() error {
	return r.redis.Close()
}

func max(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}
