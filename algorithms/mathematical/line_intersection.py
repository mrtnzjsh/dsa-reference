"""
Line Intersection Algorithm Implementation

This module implements algorithms for checking line segment intersections and finding
line intersections in 2D space. These algorithms are fundamental in computational geometry
with numerous applications including computer graphics, robotics, and path planning.

Line Intersection Algorithm Overview:
    Line intersection algorithms are fundamental with numerous applications:
    - Computer graphics (rendering, collision detection)
    - Robotics (motion planning, path optimization)
    - GIS (Geographic Information Systems)
    - Game development (collision detection, level design)
    - CAD (Computer-Aided Design)
    - Network routing (intersection analysis)
    - Image processing (segmentation)
    - Video games (obstacle detection)

Algorithms Implemented:
    1. Line Intersection: Check if two line segments intersect
    2. Point Line Distance: Calculate the shortest distance from a point to a line

Mathematical Foundation:
    For line intersection, we use the concept of orientation and cross products:
    - Orientation of three points (p, q, r) tells us if q is clockwise, counter-clockwise,
      or collinear with p and r
    - Two line segments (p1, q1) and (p2, q2) intersect if:
      * General case: orientations of (p1, q1, p2) and (p1, q1, q2) are different
        and orientations of (p2, q2, p1) and (p2, q2, q1) are different
      * Special cases: points are collinear, segments overlap, or share an endpoint

Input:
    p1: Start point of first line segment (x, y)
    q1: End point of first line segment (x, y)
    p2: Start point of second line segment (x, y)
    q2: End point of second line segment (x, y)

Output:
    Returns True if the line segments intersect, False otherwise

Example:
    >>> line_intersection((0, 0), (2, 2), (1, 1), (3, 3))
    True

    >>> line_intersection((0, 0), (1, 1), (1, 0), (2, 1))
    False

    >>> line_intersection((0, 0), (2, 0), (1, 0), (3, 0))
    True

    >>> line_intersection((0, 0), (1, 1), (1, 1), (2, 2))
    True

Complexity Analysis:
    Time Complexity: O(1)
    - Uses cross product calculations which are constant time
    - Space Complexity: O(1)
    - Only uses constant space for calculations

    Space Complexity:
    - O(1) for the orientation and distance calculations
    - Total: O(1)

    Note:
    The line intersection algorithm handles both general cases and special cases
    including collinear points, overlapping segments, and segments sharing endpoints.
    The orientation function uses cross products to determine the relative position
    of points, which is fundamental in computational geometry. This algorithm is
    essential for collision detection in games, path planning in robotics, and
    many other applications that require checking if geometric objects intersect.
    For polygon intersection problems, more sophisticated algorithms are needed.
"""

def orientation(p: tuple[int, int], q: tuple[int, int], r: tuple[int, int]) -> int:
    """
    Calculate the orientation of three points.

    Args:
        p: First point (x, y)
        q: Second point (x, y)
        r: Third point (x, y)

    Returns:
        0 if collinear, 1 if clockwise, 2 if counter-clockwise
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    if val > 0:
        return 1  # Clockwise
    elif val < 0:
        return 2  # Counter-clockwise
    else:
        return 0  # Collinear


def on_segment(p: tuple[int, int], q: tuple[int, int], r: tuple[int, int]) -> bool:
    """
    Check if point q lies on line segment pr.

    Args:
        p: First point (x, y)
        q: Second point (x, y)
        r: Third point (x, y)

    Returns:
        True if q lies on segment pr, False otherwise
    """
    if (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
            min(p[1], r[1]) <= q[1] <= max(p[1], r[1])):
        return True
    return False


def line_intersection(p1: tuple[int, int], q1: tuple[int, int],
                       p2: tuple[int, int], q2: tuple[int, int]) -> bool:
    """
    Check if two line segments intersect.

    Args:
        p1: Start point of first line segment (x, y)
        q1: End point of first line segment (x, y)
        p2: Start point of second line segment (x, y)
        q2: End point of second line segment (x, y)

    Returns:
        True if the line segments intersect, False otherwise
    """
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if o1 != o2 and o3 != o4:
        return True

    # Special cases: p1, p2, q1 are collinear and q1 lies on segment p1p2
    if o1 == 0 and on_segment(p1, p2, q1):
        return True

    # Special case: p1, q2, q1 are collinear and q2 lies on segment p1q1
    if o2 == 0 and on_segment(p1, q2, q1):
        return True

    # Special case: p2, q1, q2 are collinear and q1 lies on segment p2q2
    if o3 == 0 and on_segment(p2, q1, q2):
        return True

    # Special case: p2, q2, p1 are collinear and p1 lies on segment p2q2
    if o4 == 0 and on_segment(p2, p1, q2):
        return True

    return False
