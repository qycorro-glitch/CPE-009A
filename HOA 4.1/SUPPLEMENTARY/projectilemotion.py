import math

def projectilemotion_solver(speed, angle_deg):
    g = 9.8  # acceleration due to gravity (m/s^2)

    # Convert angle to radians
    angle_rad = math.radians(angle_deg)

    # Range formula: R = (v^2 * sin(2θ)) / g
    range_distance = (speed ** 2 * math.sin(2 * angle_rad)) / g

    # Maximum height formula: h = (v^2 * sin^2(θ)) / (2g)
    max_height = (speed ** 2 * (math.sin(angle_rad) ** 2)) / (2 * g)

    return range_distance, max_height