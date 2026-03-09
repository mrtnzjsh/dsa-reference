# Balanced Binary Search Tree

A balanced binary search tree (BST) is a binary search tree that automatically maintains its balance by performing rotations and color changes when necessary. These self-balancing trees ensure O(log n) time complexity for search, insertion, and deletion operations, regardless of the order of input.

## Why Balance Matters

In an unbalanced BST, operations can degrade to O(n) time complexity in the worst case (when tree becomes skewed). Balancing prevents this by ensuring the tree's height remains approximately log n, which is critical for maintaining efficiency in real-world applications with large datasets.

## Types of Balanced Binary Search Trees

### AVL Tree
- First self-balancing BST invented by Adelson-Velsky and Landis
- Uses height-balancing property: For every node, the heights of the two child subtrees differ by at most one
- More strictly balanced than other tree types
- Requires storing balance factor at each node

### Red-Black Tree
- Self-balancing BST with color-coded nodes (red or black)
- Enforces several properties to maintain balance:
  - Each node is either red or black
  - The root is black
  - All leaves (NIL nodes) are black
  - Red nodes have only black children
  - Every path from a node to its descendant NIL nodes contains the same number of black nodes
- More flexible than AVL trees in terms of rotations

## Comparison: AVL Tree vs Red-Black Tree

### Structure and Balance Properties

**AVL Tree:**
- Focuses on height balance: |height(left subtree) - height(right subtree)| ≤ 1
- Requires storing balance factor (left height - right height) at each node
- Guarantees maximum height of 1.44 * log(n + 2) - 1.47, providing tighter balance

**Red-Black Tree:**
- Uses color property rather than explicit balance factor
- Ensures height ≤ 2 * log(n + 1), providing looser but sufficient balance
- Rotations happen during insertion and deletion based on color patterns

### Rotations

**AVL Tree:**
- Uses simple 4 rotation types: left rotation, right rotation, left-right rotation, right-left rotation
- Rotations occur immediately after insertion/deletion to rebalance
- Fewer rotations per operation but more frequent rebalancing

**Red-Black Tree:**
- Uses only 2 rotation types: left rotation, right rotation
- Rotations may happen multiple times during insertion and deletion operations
- More rotations overall but less frequent rebalancing

### Memory Overhead

**AVL Tree:**
- Stores balance factor (1-2 bytes depending on implementation) at each node
- Additional memory overhead of O(n)
- Can be problematic for memory-constrained environments

**Red-Black Tree:**
- No explicit balance factor storage needed
- Only requires 1 bit per node for color information
- Better memory efficiency, uses space sparingly

### Performance Characteristics

**AVL Tree:**
- Slightly faster operations in practice
- More balanced structure means shallower trees
- Better for read-heavy workloads

**Red-Black Tree:**
- Slightly slower operations but more flexible
- Handles insertions/deletions more gracefully
- Better for write-heavy workloads

### Time Complexity

Both trees maintain O(log n) for all operations in the worst case:

- **Search:** O(log n) - both
- **Insertion:** O(log n) - both
- **Deletion:** O(log n) - both
- **Rebalancing:** O(1) - AVL, O(1) amortized - Red-Black

## Implementation Differences

### Node Structure

**AVL Tree:**
```javascript
class Node {
  key: T;
  left: Node | null;
  right: Node | null;
  height: number; // Stores the height of the node
}
```

**Red-Black Tree:**
```javascript
enum Color { RED, BLACK }

class Node {
  key: T;
  left: Node | null;
  right: Node | null;
  color: Color; // RED or BLACK
}
```

### Rebalancing Logic

**AVL Tree:**
1. After insertion or deletion, calculate balance factor
2. If imbalance found, perform appropriate rotation
3. Update heights of affected nodes

**Red-Black Tree:**
1. After insertion or deletion, perform recoloring
2. If red-red conflict or black height violation, perform rotations
3. May require multiple rotations and recolorings

## When to Use Each

### AVL Tree
- When you need maximum balance and fastest possible operations
- Read-heavy applications where frequent searches are the primary concern
- Applications requiring deterministic performance guarantees
- Memory is not a constraint
- When the dataset size is large enough to justify the overhead

### Red-Black Tree
- When memory efficiency is important
- Write-heavy applications with frequent insertions and deletions
- Situations where the dataset size is small or dynamic
- When you want a more flexible balancing algorithm
- Standard library implementations of balanced trees (e.g., Java TreeMap, C++ std::map)

## Common Applications

### AVL Tree Applications
- Database indexing systems
- High-performance search applications
- Applications requiring strict performance guarantees
- Network routing tables
- Computational geometry applications

### Red-Black Tree Applications
- In-memory data structures (maps and sets in many standard libraries)
- File systems
- Garbage collection algorithms
- Network routing protocols
- Network simulators and protocol stacks
- Databases (used in some implementations for B-trees)

## Trade-offs Summary

| Feature | AVL Tree | Red-Black Tree |
|---------|----------|----------------|
| Balance Factor | 1 | None (color-based) |
| Node Overhead | Height +2 bytes | Color 1 bit |
| Avg. Height | ~1.44 log n | ~2 log n |
| Rotations | 4 types, frequent | 2 types, looser |
| Search Speed | Slightly faster | Slightly slower |
| Insert/Delete Speed | Slightly slower | Slightly faster |
| Memory Usage | Higher | Lower |
| Implementation Complexity | Moderate | Moderate |
| Worst-case Operations | O(log n) | O(log n) |

## Modern Use Cases

### Popular AVL Tree Implementations
- Python's `bisect` module (balanced BST under the hood)
- Java's `java.util.TreeMap`
- C++ `std::map` (often implemented with red-black, but AVL is also used)

### Popular Red-Black Tree Implementations
- Java's `java.util.TreeMap`
- Java's `java.util.TreeSet`
- C++ `std::map`
- C++ `std::set`
- .NET `SortedDictionary` and `SortedSet`
- Perl `Tie::DB_File` (implementation)
- Rust's `BTreeMap` (uses red-black tree)

## Evolution and Research

Both AVL trees and red-black trees were introduced in 1962. AVL trees were the first self-balancing BSTs, followed by red-black trees as an evolution. Both remain fundamental data structures in computer science and continue to be studied for optimization purposes, particularly in concurrent implementations and memory management.

Modern research focuses on:
- Concurrent balanced BSTs
- Memory-efficient implementations
- Hybrid approaches combining properties of both
- Parallel processing of tree operations