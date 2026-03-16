# Greedy Algorithms

## Overview

Greedy algorithms are a class of algorithms that make locally optimal choices at each step with the hope of finding a global optimum. At each stage, the algorithm chooses the most attractive option without considering the future consequences. While not always correct, greedy algorithms are efficient and widely used in many practical applications.

## Core Characteristics

1. **Greedy Choice Property**: A globally optimal solution can be reached by making locally optimal (greedy) choices at each step
2. **Optimal Substructure Property**: An optimal solution contains optimal solutions to subproblems
3. **Deterministic**: Makes clear decisions at each step
4. **Simple Implementation**: Usually straightforward to implement

## Common Applications

### 1. Interval Scheduling
Finding the maximum number of non-overlapping intervals
**Time Complexity**: O(n log n) for sorting
**Space Complexity**: O(1)

### 2. Activity Selection
Selecting maximum number of activities that don't overlap
**Time Complexity**: O(n log n)
**Space Complexity**: O(1)

### 3. Fractional Knapsack
Maximizing value with fractional items in knapsack
**Time Complexity**: O(n log n) for sorting
**Space Complexity**: O(1)

### 4. Prim's Algorithm
Minimum spanning tree using greedy approach
**Time Complexity**: O(E log V)
**Space Complexity**: O(V)

### 5. Kruskal's Algorithm
Minimum spanning tree for weighted graphs
**Time Complexity**: O(E log E)
**Space Complexity**: O(V)

### 6. Huffman Coding
Data compression using optimal binary tree
**Time Complexity**: O(n log n)
**Space Complexity**: O(n)

### 7. Dijkstra's Algorithm
Shortest path in weighted graphs with non-negative weights
**Time Complexity**: O((V + E) log V)
**Space Complexity**: O(V)

### 8. Coin Change (Modified)
Making change with limited coins
**Time Complexity**: O(n) where n is number of coin denominations
**Space Complexity**: O(1)

## When to Use Greedy Algorithms

### Use Cases

1. **When Greedy Choice Property Holds**
   - Problems like activity selection, Huffman coding, and minimum spanning tree problems
   - When each decision leads directly to optimal solution

2. **When Optimality Can Be Guaranteed**
   - Fractional knapsack problem
   - Prim's and Kruskal's algorithms
   - When local optimal choices lead to global optimum

3. **When Implementation Simplicity Is Needed**
   - Quick implementations of problems with known greedy solutions
   - When the greedy approach produces efficient results

4. **When Problems Have Clear Structure**
   - Problems with sorted or structured inputs
   - Problems where greedy choices are evident

### Example: Activity Selection
```python
def activity_selection(activities):
    # Sort by finish time
    activities.sort(key=lambda x: x[1])
    
    selected = [activities\[0\]]
    last_end = activities\[0\][1]
    
    for start, end in activities\[1:\]:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    
    return selected
```

## When NOT to Use Greedy Algorithms

### Non-Use Cases

1. **When Greedy Choice Doesn't Lead to Optimal Solution**
   - Classic coin change problem (unlimited coins)
   - Traveling Salesman Problem
   - **Counterexample**: For coin change, greedy gives coins [10,10,1] for 21 when optimal is [10,10,1]

2. **When Problem Has Overlapping Subproblems**
   - 0/1 Knapsack problem (not fractional)
   - Dynamic programming problems
   - **Time Complexity**: O(n^2) vs O(n^3) for DP
   - **Trade-off**: Greedy O(n) but may be suboptimal

3. **When Need to Explore Multiple Choices**
   - Problems requiring backtracking
   - Problems where greedy choice is insufficient
   - When future dependencies matter

4. **When Problem Has Time-Dependent Constraints**
   - Problems with changing constraints
   - Problems where local choices affect future possibilities

### Example: 0/1 Knapsack Problem
```python
# Greedy approach (WRONG for 0/1 knapsack)
def greedy_knapsack(items, capacity):
    items.sort(key=lambda x: x[1]/x[0], reverse=True)  # value per weight
    total_value = 0
    remaining = capacity
    
    for weight, value in items:
        if weight <= remaining:
            total_value += value
            remaining -= weight
    
    return total_value
```

## Key Differences: Greedy vs Dynamic Programming

| Aspect | Greedy | Dynamic Programming |
|--------|--------|---------------------|
| **Approach** | Make local optimal choice | Store and reuse subproblem solutions |
| **Correctness** | Not always optimal | Always optimal |
| **Time Complexity** | Usually O(n) or O(n log n) | Usually O(n × m) or O(n^2) |
| **Space Complexity** | O(1) or O(n) | O(n × m) |
| **Use Case** | Problems with greedy property | Problems with overlapping subproblems |

## Implementation Tips

1. **Sort First**: Many greedy algorithms benefit from sorting inputs
2. **Identify Properties**: Look for greedy choice property and optimal substructure
3. **Test Greedy**: Always verify with examples
4. **Consider Alternatives**: Check if DP might give better results

## Real-World Examples

### 1. Network Routing
Greedy algorithms choose the next best hop without considering long-term network state

### 2. Scheduling
Task scheduling with priority scheduling (shortest job first)

### 3. Resource Allocation
CPU scheduling algorithms that make immediate resource allocation decisions

### 4. Financial Investments
Selecting investments based on highest return per dollar, ignoring diversification benefits

## Conclusion

Greedy algorithms offer efficient and simple solutions for many problems, but they must be used judiciously. Always verify that the greedy choice property holds for your problem, and consider alternative approaches like dynamic programming when the problem might require examining multiple paths.
