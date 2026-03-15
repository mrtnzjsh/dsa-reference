# Line Intersection Algorithm

## Overview

This module implements algorithms for checking line segment intersections and finding line intersections in 2D space. These algorithms are fundamental in computational geometry with numerous applications including computer graphics, robotics, and path planning.

## Algorithm Steps

1. Calculate orientation of three points using cross product
   - Returns 0 if collinear, 1 if clockwise, 2 if counter-clockwise

2. Check if point lies on line segment
   - Verifies the point is within the bounding box of the segment

3. For line segment intersection:
   - Check general case: orientations are different
   - Check special cases: collinear points, overlapping segments, shared endpoints

## Input

- `p1`: Start point of first line segment (x, y)
- `q1`: End point of first line segment (x, y)
- `p2`: Start point of second line segment (x, y)
- `q2`: End point of second line segment (x, y)

## Output

Returns True if the line segments intersect, False otherwise

## Example

```python
>>> line_intersection((0, 0), (2, 2), (1, 1), (3, 3))
True
>>> line_intersection((0, 0), (1, 1), (1, 0), (2, 1))
False
>>> line_intersection((0, 0), (2, 0), (1, 0), (3, 0))
True
>>> line_intersection((0, 0), (1, 1), (1, 1), (2, 2))
True
```

### Step-by-step example for line_intersection((0, 0), (2, 2), (1, 1), (3, 3)):

1. o1 = orientation((0, 0), (2, 2), (1, 1)) = 0 (collinear)
2. o2 = orientation((0, 0), (2, 2), (3, 3)) = 0 (collinear)
3. o3 = orientation((1, 1), (3, 3), (0, 0)) = 0 (collinear)
4. o4 = orientation((1, 1), (3, 3), (2, 2)) = 0 (collinear)
5. All orientations are 0 (collinear), check on_segment cases
6. on_segment((0, 0), (1, 1), (2, 2)) = True
7. Return True

### Step-by-step example for line_intersection((0, 0), (1, 1), (1, 0), (2, 1)):

1. o1 = orientation((0, 0), (1, 1), (1, 0)) = 1 (clockwise)
2. o2 = orientation((0, 0), (1, 1), (2, 1)) = 2 (counter-clockwise)
3. o3 = orientation((1, 0), (2, 1), (0, 0)) = 2 (counter-clockwise)
4. o4 = orientation((1, 0), (2, 1), (1, 1)) = 1 (clockwise)
5. o1 != o2 and o3 != o4 → return True

## Complexity Analysis

### Time Complexity: O(1)

- All operations are constant time calculations
- Cross product and comparisons are O(1)
- No loops or recursion

### Space Complexity: O(1)

- Only uses constant space for calculations
- Uses minimal variables for intermediate results

## Notes

The line intersection algorithm handles both general cases and special cases including collinear points, overlapping segments, and segments sharing endpoints. The orientation function uses cross products to determine the relative position of points, which is fundamental in computational geometry. This algorithm is essential for collision detection in games, path planning in robotics, and many other applications that require checking if geometric objects intersect.
