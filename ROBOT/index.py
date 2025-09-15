import numpy as np

# Load robot path (assuming CSV has headers: x, y)
path = np.genfromtxt("robot_path.csv", delimiter=",", skip_header=1)

x = path[:, 0]
y = path[:, 1]

# Calculate total distance traveled
dx = np.diff(x)
dy = np.diff(y)
distances = np.sqrt(dx**2 + dy**2)
total_distance = np.sum(distances)

# Farthest point from origin
dist_from_origin = np.sqrt(x**2 + y**2)
farthest_point = path[np.argmax(dist_from_origin)]

# Check if robot revisited the same position
unique_positions = np.unique(path, axis=0)
revisited = len(unique_positions) < len(path)

# Save results
with open("robot_results.txt", "w") as f:
    f.write("Robot Path Analysis Results\n")
    f.write(f"Total distance traveled: {total_distance:.2f}\n")
    f.write(f"Farthest point from origin: {farthest_point}\n")
    f.write(f"Revisited a position: {revisited}\n")
