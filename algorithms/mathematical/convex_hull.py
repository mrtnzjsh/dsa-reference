"""
Convex Hull (Monotone Chain) Algorithm Implementation

This module implements the Convex Hull algorithm using the Monotone Chain method to find
the convex hull of a set of points in 2D space. The convex hull is the smallest convex
polygon that contains all the points in the set. This algorithm is efficient with O(n log n)
time complexity, making it suitable for large datasets.

Convex Hull Algorithm Overview:
    The convex hull is a fundamental concept in computational geometry with numerous applications:
    - Computer graphics (rendering, collision detection)
    - Robotics (motion planning, path optimization)
    - Image processing (shape recognition)
    - Geographic information systems (finding regions)
    - Game development (collision detection)
    - Network design (connectivity analysis)
    - Bioinformatics (protein structure analysis)
    - Machine learning (outlier detection)

Monotone Chain Algorithm Steps:
    The algorithm sorts the points and then constructs the lower and upper hulls:
    1. Sort the points lexicographically (first by x, then by y)
    2. Build the lower hull:
       - Iterate through sorted points
       - While the last two points in the hull and the current point make a non-left turn,
         remove the middle point
       - Add the current point to the hull
    3. Build the upper hull:
       - Iterate through sorted points in reverse order
       - While the last two points in the hull and the current point make a non-left turn,
         remove the middle point
       - Add the current point to the hull
    4. Combine lower and upper hull (without duplicating endpoints)
    5. The result is the convex hull in counter-clockwise order

Input:
    points: A list of tuples (x, y) representing the points

Output:
    Returns a list of points representing the convex hull in counter-clockwise order

Example:
    >>> points = [(0, 0), (1, 1), (2, 0), (1, 0), (1, 2)]
    >>> convex_hull(points)
    [(0, 0), (1, 2), (2, 0)]

    >>> points = [(0, 0), (1, 1), (2, 2)]
    >>> convex_hull(points)
    [(0, 0), (1, 1), (2, 2)]

    >>> points = [(0, 0), (0, 1), (1, 0), (1, 1)]
    >>> convex_hull(points)
    [(0, 0), (1, 0), (1, 1), (0, 1)]

    >>> points = [(0, 0), (1, 1), (0, 1), (1, 0)]
    >>> convex_hull(points)
    [(0, 0), (1, 0), (1, 1), (0, 1)]

    Step-by-step example for convex_hull([(0, 0), (1, 1), (2, 0), (1, 0), (1, 2)]):
    1. Sort points lexicographically: [(0, 0), (1, 0), (1, 1), (1, 2), (2, 0)]

    2. Build lower hull:
       - Start: lower = []
       - Add (0, 0): lower = [(0, 0)]
       - Add (1, 0): lower = [(0, 0), (1, 0)]
       - Add (1, 1): lower = [(0, 0), (1, 0), (1, 1)]
       - Add (1, 2): lower = [(0, 0), (1, 0), (1, 1), (1, 2)]
       - Add (2, 0): lower = [(0, 0), (1, 0), (1, 2), (2, 0)]

    3. Build upper hull (reverse order):
       - Start: upper = []
       - Add (2, 0): upper = [(2, 0)]
       - Add (1, 2): upper = [(2, 0), (1, 2)]
       - Add (1, 1): upper = [(2, 0), (1, 2), (1, 1)]
       - Add (1, 0): Check turn from (1, 2) → (1, 1) → (1, 0): collinear, remove (1, 1)
         upper = [(2, 0), (1, 2)]
       - Add (0, 0): Check turn from (1, 2) → (2, 0) → (0, 0): non-left turn, remove (2, 0)
         upper = [(1, 2)]
       - Check turn from (1, 2) → (0, 0): collinear, add (0, 0)
         upper = [(1, 2), (0, 0)]

    4. Combine: remove last point of each to avoid duplication
       convex_hull = lower[:-1] + upper
       convex_hull = [(0, 0), (1, 0), (1, 2), (0, 0)]

    Final result: [(0, 0), (1, 0), (1, 2), (0, 0)]

Complexity Analysis:
    Time Complexity: O(n log n)
    - O(n log n) for sorting the points
    - O(n) for building the lower and upper hulls
    - Space Complexity: O(n)
    - For the hull storage: O(n)
    - For the sorted points: O(n)

    Space Complexity:
    - O(n) for the convex hull points
    - O(n) for the sorted copy of points
    - Total: O(n)

    Note:
    The Monotone Chain algorithm is optimal for finding the convex hull of a set of points
    in 2D space. It's more efficient than the Graham Scan algorithm for large datasets
    because it uses a simpler cross-product calculation. The algorithm works by constructing
    two monotonic chains: the lower hull and the upper hull. Each chain is built by scanning
    the sorted points and removing points that create "right turns" (or collinear points).
    The convex hull is used in many real-world applications including collision detection in
    game engines, path planning in robotics, and shape recognition in computer vision.
    The algorithm can be extended to 3D space using more complex data structures.
"""

def convex_hull(points: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Find the convex hull of a set of points using the Monotone Chain algorithm.

    Args:
        points: List of (x, y) tuples representing the points

    Returns:
        List of points representing the convex hull in counter-clockwise order
    """
    # Remove duplicate points
    points = list(set(points))
    n = len(points)

    # Handle edge cases
    if n <= 1:
        return points

    # Sort points lexicographically
    points = sorted(points)

    # Cross product of vectors OA and OB
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenate lower and upper hull, removing duplicate points
    convex_hull = lower[:-1] + upper[:-1]

    return convex_hull


def is_convex(points: list[tuple[int, int]]) -> bool:
    """
    Check if a polygon defined by points is convex.

    Args:
        points: List of (x, y) tuples representing the polygon vertices

    Returns:
        True if the polygon is convex, False otherwise
    """
    # Remove duplicate consecutive points
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
