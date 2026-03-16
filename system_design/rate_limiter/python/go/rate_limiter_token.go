package main

import (
	"time"
)

type RateLimiter struct {
	Capacity       int64
	RefillRate     int64
	Tokens         int64
	LastRefillTime int64
}

func NewRateLimiter(capacity int64, refill_rate int64) *RateLimiter {
	return &RateLimiter{
		Capacity:       capacity,
		RefillRate:     refill_rate,
		Tokens:         capacity,
		LastRefillTime: time.Now().UnixNano(),
	}
}

func (r RateLimiter) AllowRequest(tokens_requested int64) bool {
	now := time.Now().UnixMilli()

	elapsed := now - r.LastRefillTime
	if r.Capacity < r.Tokens+(elapsed*int64(r.RefillRate)) {
		r.Tokens = r.Capacity
	} else {
		r.Tokens = r.Tokens + (elapsed * int64(r.RefillRate))
	}
	r.LastRefillTime = now

	if r.Tokens > tokens_requested {
		r.Tokens -= tokens_requested
		return true
	}
	return false
}
