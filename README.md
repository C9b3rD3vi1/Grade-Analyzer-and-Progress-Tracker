# Grade-Analyzer-and-Progress-Tracker

Students and educators often struggle to track and analyze academic performance over time. Manually calculating grades, identifying trends, and preThis program will automate the process of analyzing student grades, calculating averages, identifying trends, and providing actionable insights to help students improve their academic performance.


## Features

Grade Analysis: Calculate average and median grades.

Trend Identification: Identify trends (improving, declining, or stable) in academic performance.

Performance Prediction: Predict future grades using a simple linear prediction model.

Report Generation: Generate detailed reports for each student.

Data Visualization: Visualize grade trends over time using matplotlib.


## Installation

***Prerequisites***
Python 3.6 or higher.

Required Python libraries:

    csv
    statistics
    matplotlib
    datetime
    colorama


**Install Dependencies**
Install the required Python libraries using pip:

    pip install matplotlib colorama pandas


## Usage

Input CSV File Format
The tool reads student grades from a CSV file with the following format:

    student_id,name,grade,date
    1,John Doe,85,2023-01-01
    1,John Doe,88,2023-02-01
    1,John Doe,90,2023-03-01
    2,Jane Smith,78,2023-01-01
    2,Jane Smith,82,2023-02-01
    2,Jane Smith,80,2023-03-01


## Run the Program

Save your student grades in a CSV file (e.g., grades.csv).

**Run the program:**
    python grade_analyzer.py

Enter the path to the CSV file when prompted:
    Enter the path to the grades CSV file: grades.csv


## Output

**Console Output:**

    --- Student Report ---
    Name: John Doe
    Average Grade: 87.67
    Median Grade: 88.00
    Trend: Improving
    Predicted Next Grade: 91.00

## Testing Result

**Run command**
    Python3 test_grade_anyzer.py


**Graphical Output:**

A line graph showing the student's grade trend over time.

## Code Structure

**Reusable Functions**

read_grades(file_path: str) -> dict: Reads grades from a CSV file.

calculate_average(grades: list) -> float: Calculates the average of grades.

calculate_median(grades: list) -> float: Calculates the median of grades.

identify_trends(grades: list) -> str: Identifies trends in grades.

predict_future_performance(grades: list) -> float: Predicts future grades.

generate_report(student_data: dict) -> dict: Generates a summary report.


**Non-Reusable Functions**

display_report(report: dict): Displays the generated report.

plot_grades(student_data: dict): Visualizes grade trends.


**Main Function**
main(): Runs the program.


**Dependencies**
csv: For reading data from CSV files.

statistics: For calculating average and median grades.

matplotlib.pyplot: For visualizing grade trends.

datetime: For parsing and handling dates.

colorama: For adding colored text to the console output.


**Future Enhancements**

Error Handling: Add error handling for invalid or missing data.

Advanced Prediction: Implement more sophisticated prediction models (e.g., machine learning).

Enhanced Visualization: Add support for additional chart types (e.g., bar charts, pie charts).

User Interface: Develop a graphical user interface (GUI) for easier interaction.

Integration: Integrate with learning management systems (LMS) to automatically fetch data.
