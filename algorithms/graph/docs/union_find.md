"""Union-Find / Disjoint Set Union (DSU)

The Union-Find data structure supports two operations efficiently:
1. Union(u, v): Merge the sets containing elements u and v
2. Find(x): Find the representative (root) of the set containing x

This structure is also known as Disjoint Set Union (DSU) and is a classic
problem-solving technique for problems involving partitioning elements into sets.

**Key Insight:**
Union-Find uses a tree-based representation where each set has a root element.
The Find operation finds the root (representative) of an element using path compression.
The Union operation merges two sets by attaching one root to another.

**Data Structures:**
- parent array: parent[i] stores the parent of element i
- rank array (or size array): helps keep the tree flat during union operations

**Find Operation with Path Compression:**
Traverse up the parent pointers from x to the root, then update all nodes
along the path to point directly to the root. This makes future Find operations faster.

**Union by Rank:**
When merging two sets, attach the smaller tree under the root of the larger tree
(using rank/size as a proxy for tree height). This keeps the tree balanced.

**Mathematical Foundation:**
Let find(x) return the representative r of the set containing x.
Let union(x, y) merge the sets containing x and y.

Find:
```
find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # Path compression
    return parent[x]
```

Union:
```
findRoot(x):
    while parent[x] != x:
        x = parent[x]
    return x

union(x, y):
    rootX = findRoot(x)
    rootY = findRoot(y)
    if rootX != rootY:
        if rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        elif rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        else:
            parent[rootY] = rootX
            rank[rootX] += 1
```

**Example - Building Connected Components:**

Initial state (5 elements, each in its own set):
```
parent: [0, 1, 2, 3, 4]
rank:   [0, 0, 0, 0, 0]
```

After union(0, 1):
```
parent: [1, 1, 2, 3, 4]
rank:   [0, 1, 0, 0, 0]
Set 0: {0, 1}  Set 1: {2}  Set 2: {3}  Set 3: {4}
```

After union(1, 2):
```
parent: [1, 1, 1, 3, 4]
rank:   [0, 1, 1, 0, 0]
Set 0: {0, 1, 2}  Set 1: {3}  Set 2: {4}
```

After union(3, 4):
```
parent: [1, 1, 1, 4, 4]
rank:   [0, 1, 1, 1, 1]
Set 0: {0, 1, 2}  Set 1: {3, 4}
```

Final state: Two sets {0, 1, 2} and {3, 4}

**Time Complexity:**
- Find: O(α(n)) amortized, where α(n) is the inverse Ackermann function
  - α(n) grows very slowly (~4 for any practical value of n)
  - Effectively constant time for all practical purposes
- Union: O(α(n)) amortized
- α(n) is sub-linear and grows so slowly it's considered constant

**Space Complexity:**
- O(n) for parent and rank arrays

**Path Compression Variations:**
1. **Simple Path Compression:** parent[x] = find(parent[x]) recursively
2. **Path Halving:** path[x] = path[path[x]] (faster than full compression)
3. **Full Compression:** Recursively compress entire path (what we use)

**Rank vs Size:**
**Rank:**
- Represents an upper bound on tree height
- Union by rank tends to create shallower trees
- Better when union operations are frequent

**Size:**
- Represents the actual number of nodes in the set
- Union by size creates balanced trees
- Better when we need to know the size of sets

**Trade-offs:**
**vs. Maintaining Connected Components Explicitly:**
- Union-Find: O(α(n)) operations, simpler implementation
- Explicit lists: O(1) operations but harder to maintain consistency

**vs. Graph Traversal (BFS/DFS):**
- Union-Find: Good for connectivity queries after edges are added
- BFS/DFS: Good for finding paths, connectivity with traversal

**vs. Segment Tree / DSU Offline:**
- Union-Find: O(α(n)) per operation, simpler
- Segment Tree: O(log n) per operation, more versatile

**Advantages:**
- Extremely fast operations (practically O(1))
- Simple implementation
- Handles dynamic connectivity well
- Low memory overhead

**Disadvantages:**
- Only supports connectivity queries, no path information
- Doesn't directly support dynamic edge queries
- Not as versatile as other data structures

**Applications:**
- Connected components in graphs
- Kruskal's algorithm for minimum spanning trees
- Image segmentation (connected components)
- Dynamic graph connectivity problems
- Social network analysis (friend groups)
- Maze generation and solving

**Kruskal's Algorithm Integration:**
Kruskal's algorithm uses Union-Find to efficiently check and merge sets of edges:
```
1. Sort all edges by weight
2. For each edge:
   If find(u) != find(v):
     Add edge to MST
     union(u, v)
3. Result is MST spanning all vertices
```

This works because if find(u) != find(v), vertices u and v are in different connected components,
so adding edge (u, v) won't create a cycle.
"""
