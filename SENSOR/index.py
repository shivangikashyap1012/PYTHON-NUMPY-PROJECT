import numpy as np

data = np.genfromtxt("sensor_data.csv", delimiter=",", skip_header=1)

time = data[:, 0]
temperature = data[:, 1]
distance = data[:, 2]
battery = data[:, 3]

avg_temp, min_temp, max_temp = np.mean(temperature), np.min(temperature), np.max(temperature)
avg_dist, min_dist, max_dist = np.mean(distance), np.min(distance), np.max(distance)
avg_batt, min_batt, max_batt = np.mean(battery), np.min(battery), np.max(battery)

time_highest_temp = time[np.argmax(temperature)]

low_battery_count = np.sum(battery < 30)

with open("sensor_results.txt", "w") as f:
    f.write("Sensor Data Analysis Results\n")
    f.write(f"Temperature -> Avg: {avg_temp:.2f}, Min: {min_temp}, Max: {max_temp}\n")
    f.write(f"Distance -> Avg: {avg_dist:.2f}, Min: {min_dist}, Max: {max_dist}\n")
    f.write(f"Battery -> Avg: {avg_batt:.2f}, Min: {min_batt}, Max: {max_batt}\n")
    f.write(f"Time of highest temperature: {time_highest_temp}\n")
    f.write(f"Battery < 30% count: {low_battery_count}\n")

