from projectilemotion import projectilemotion_solver

# Given values
speed = 11.0  # m/s
angle = 20.0  # degrees

# Call the function
range_distance, max_height = projectilemotion_solver(speed, angle)

# Display results
print("Projectile Motion Results:")
print(f"Horizontal Distance (Range): {range_distance:.2f} meters")
print(f"Maximum Height: {max_height:.2f} meters")