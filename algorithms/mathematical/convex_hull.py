"""Convex Hull (Monotone Chain) Algorithm Implementation

# Algorithm: Monotone chain for convex hull
# Time: O(n log n), Space: O(n)
# Applications: Computer graphics, robotics, GIS, game development
# Method: Build lower and upper hulls from sorted points
# Notes: Returns convex hull in counter-clockwise order
"""
def convex_hull(points: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Find convex hull using Monotone Chain algorithm."""
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
    
    # Concatenate hulls, removing duplicate endpoints
    convex_hull = lower[:-1] + upper[:-1]
    
    return convex_hull


def is_convex(points: list[tuple[int, int]]) -> bool:
    """Check if polygon defined by points is convex."""
    # Remove duplicate consecutive points
    points = list(set(points))
    n = len(points)
    
    if n < 3:
        return False
    
    # Get sign of cross product for each consecutive triplet
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
            
            # If first non-zero cross product, set the sign
            if sign == 0:
                sign = new_sign
            # If sign changes, polygon is concave
            elif sign != new_sign:
                return False
    
    return True
