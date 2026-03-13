"""
Polygon Check Algorithms Implementation

This module implements algorithms for checking if a set of points forms a convex polygon,
validates if a polygon is simple (no self-intersections), and related geometric checks.
These algorithms are fundamental in computational geometry with numerous applications.

Polygon Check Algorithm Overview:
    Polygon checking algorithms are fundamental with numerous applications:
    - Computer graphics (rendering, collision detection)
    - Game development (level design, collision detection)
    - Robotics (path planning, obstacle detection)
    - GIS (Geographic Information Systems)
    - CAD (Computer-Aided Design)
    - Image processing (shape recognition)
    - Network analysis (graph algorithms)
    - Optimization problems

Algorithms Implemented:
    1. Is Convex: Check if a polygon is convex
    2. Is Simple: Check if a polygon has no self-intersections
    3. Is Clockwise: Determine the orientation of a polygon
    4. Is Counter-Clockwise: Determine the orientation of a polygon

Mathematical Foundation:
    For polygon checks, we use the concept of orientation and cross products:
    - Orientation of three consecutive vertices tells us if the polygon makes a left,
      right, or 180-degree turn
    - A convex polygon has consistent orientation (all left turns or all right turns)
    - A simple polygon has no self-intersections

Input:
    points: A list of tuples (x, y) representing the polygon vertices

Output:
    Returns boolean values indicating various properties of the polygon

Example:
    >>> is_convex([(0, 0), (1, 1), (2, 0)])
    True

    >>> is_convex([(0, 0), (2, 0), (1, 1), (2, 2)])
    False

    >>> is_clockwise([(0, 0), (2, 0), (1, 1)])
    False

    >>> is_counter_clockwise([(0, 0), (2, 0), (1, 1)])
    True

    >>> is_simple([(0, 0), (1, 1), (2, 0), (1, 2)])
    False

    >>> is_simple([(0, 0), (1, 1), (2, 0), (1, 0)])
    True

Complexity Analysis:
    Time Complexity: O(n)
    - For each algorithm, we need to check each vertex pair once
    - Space Complexity: O(1)
    - Only uses constant space for calculations

    Space Complexity:
    - O(1) for orientation and cross product calculations
    - Total: O(1)

    Note:
    These polygon checking algorithms are essential for many applications in computer
    graphics, robotics, and game development. The algorithms use the concept of
    "convexity" and "simplicity" of polygons, which are fundamental properties in
    computational geometry. Convex polygons are preferred in many applications because
    they have nice properties like the entire polygon being visible from any vertex.
    Simple polygons are those without self-intersections, which is a necessary condition
    for many geometric algorithms. These algorithms can be extended to work with
    3D polygons and more complex geometric structures.
"""

def is_convex(points: list[tuple[int, int]]) -> bool:
    """
    Check if a polygon defined by points is convex.

    Args:
        points: List of (x, y) tuples representing the polygon vertices

    Returns:
        True if the polygon is convex, False otherwise
    """
    # Remove duplicate points
    points = list(set(points))
    n = len(points)

    if n < 3:
        return False

    # Get the sign of the cross product for each consecutive triplet
    sign = 0
    for i in range(n):
        # Get three consecutive vertices
        a = points[i]
        b = points[(i + 1) % n]
        c = points[(i + 2) % n]

        # Calculate cross product
        cross_product = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

        # Check if cross product is zero (collinear)
        if cross_product != 0:
            # Update sign
            new_sign = 1 if cross_product > 0 else -1

            # If this is the first non-zero cross product, set the sign
            if sign == 0:
                sign = new_sign
            # If the sign changes, the polygon is concave
            elif sign != new_sign:
                return False

    return True


def is_clockwise(points: list[tuple[int, int]]) -> bool:
    """
    Check if a polygon is clockwise oriented.

    Args:
        points: List of (x, y) tuples representing the polygon vertices

    Returns:
        True if the polygon is clockwise, False otherwise
    """
    # Remove duplicate points
    points = list(set(points))
    n = len(points)

    if n < 3:
        return False

    # Calculate the cross product sum
    sum_cross = 0
    for i in range(n):
        a = points[i]
        b = points[(i + 1) % n]
        c = points[(i + 2) % n]

        # Calculate cross product
        cross_product = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

        sum_cross += cross_product

    # If sum_cross is negative, the polygon is clockwise
    return sum_cross < 0


def is_counter_clockwise(points: list[tuple[int, int]]) -> bool:
    """
    Check if a polygon is counter-clockwise oriented.

    Args:
        points: List of (x, y) tuples representing the polygon vertices

    Returns:
        True if the polygon is counter-clockwise, False otherwise
    """
    # A counter-clockwise polygon has a positive cross product sum
    return not is_clockwise(points)


def is_simple(points: list[tuple[int, int]]) -> bool:
    """
    Check if a polygon is simple (no self-intersections).

    Args:
        points: List of (x, y) tuples representing the polygon vertices

    Returns:
        True if the polygon is simple, False otherwise
    """
    # Remove duplicate points
    points = list(set(points))
    n = len(points)

    if n < 3:
        return False

    # Check each pair of non-adjacent edges
    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n]

        for j in range(i + 2, n):
            if (j + 1) % n == i:
                continue  # Skip adjacent edges

            p3 = points[j]
            p4 = points[(j + 1) % n]

            # Check if segments (p1, p2) and (p3, p4) intersect
            if line_intersection(p1, p2, p3, p4):
                return False

    return True
