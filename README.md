# NumPy Mini Project

This project contains two small tasks using **NumPy** for data analysis:

## 📌 Project 1: Sensor Data Analysis

The robot collects sensor readings such as **temperature, distance, and
battery level** during operation.\
The program:\
- Loads sensor readings from `sensor_data.csv`\
- Calculates **average, minimum, maximum** for each sensor\
- Finds the **time when temperature was highest**\
- Counts how many times **battery dropped below 30%**\
- Saves results into `sensor_results.txt`

## 📌 Project 2: Robot Path Analysis

The robot moves in a **2D grid world** with positions logged in
`robot_path.csv`.\
The program:\
- Loads robot positions from CSV\
- Calculates the **total distance traveled**\
- Finds the **farthest point from origin (0,0)**\
- Detects if the robot ever **revisited the same position**\
- Saves results into `robot_results.txt`

## 🛠 Requirements

-   Python 3.x\
-   NumPy

Install NumPy if not already installed:

``` bash
pip install numpy
```

## 🚀 How to Run

1.  Place the CSV files (`sensor_data.csv`, `robot_path.csv`) in the
    same folder as the scripts.\

2.  Run the Python scripts:

    ``` bash
    python project1_sensor.py
    python project2_robot.py
    ```

3.  Check the output files:

    -   `sensor_results.txt`\
    -   `robot_results.txt`

## 📂 File Structure

    ├── sensor_data.csv
    ├── robot_path.csv
    ├── project1_sensor.py
    ├── project2_robot.py
    ├── sensor_results.txt
    ├── robot_results.txt
    └── README.md

------------------------------------------------------------------------

✨ This project demonstrates **basic data analysis with NumPy** for both
sensor data and robot path tracking.
