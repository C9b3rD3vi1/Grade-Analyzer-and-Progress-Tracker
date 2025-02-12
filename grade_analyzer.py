import csv
import statistics
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from colorama import Fore, Style, init



# Reusable Functions
# Read student grades from CSV file and convert to dictionary format 
def read_grades(file_path: str) -> dict:
    """
    Reads grades from a CSV file and returns a dictionary of student data.
    CSV format: student_id, name, grade, date
    """
    students = {}
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            student_id = row['student_id']
            if student_id not in students:
                students[student_id] = {'name': row['name'], 'grades': [], 'dates': []}
            students[student_id]['grades'].append(float(row['grade']))
            students[student_id]['dates'].append(datetime.strptime(row['date'], '%Y-%m-%d'))
    return students


# function to calculate average of grades for students in the list
def calculate_average(grades: list) -> float:
    """Calculates the average of a list of grades."""
    return statistics.mean(grades)


# function to calculate median of grades for students in the list
def calculate_median(grades: list) -> float:
    """Calculates the median of a list of grades."""
    return statistics.median(grades)


# function to identify trends in grades for students in the list
def identify_trends(grades: list) -> str:
    """Identifies trends (improving, declining, stable) based on grade history."""
    if len(grades) < 2:
        return "Not enough data to determine trend"
    slope = (grades[-1] - grades[0]) / len(grades)
    if slope > 0:
        return "Improving"
    elif slope < 0:
        return "Declining"
    else:
        return "Stable"


# function to predict future performance of students based on historical data
def predict_future_performance(grades: list) -> float:
    """Predicts future performance based on historical data (simple linear prediction)."""
    if len(grades) < 2:
        return grades[0] if grades else 0
    slope = (grades[-1] - grades[0]) / len(grades)
    return grades[-1] + slope


# function to generate report for students based on historical data
def generate_report(student_data: dict) -> dict:
    """Generates a summary report for a student."""
    report = {
        'name': student_data['name'],
        'average': calculate_average(student_data['grades']),
        'median': calculate_median(student_data['grades']),
        'trend': identify_trends(student_data['grades']),
        'prediction': predict_future_performance(student_data['grades'])
    }
    return report


# function to plot grades of students # Non-Reusable Functions
def display_report(report: dict):
    """Displays the generated report to the user."""
    print("\n--- Student Report ---")
    print(f"Name: {report['name']}")
    print(f"Average Grade: {report['average']:.2f}")
    print(f"Median Grade: {report['median']:.2f}")
    print(f"Trend: {report['trend']}")
    print(f" Predicted Next Grade: {report['prediction']:.2f}")


# function to plot grades of students using matplotlib # Non-Reusable Functions
def plot_grades(student_data: dict):
    """Visualizes grade trends using matplotlib."""
    dates = student_data['dates']
    grades = student_data['grades']
    plt.figure(figsize=(10, 5))
    plt.plot(dates, grades, marker='o', linestyle='-', color='b')
    plt.title(f"Grade Trend for {student_data['name']}")
    plt.xlabel("Date")
    plt.ylabel("Grade")
    plt.grid(True)
    plt.show()


# Main function to run the program
def main():
    """Main function to run the program."""
    file_path = input("Enter the path to the grades CSV file: ")
    students = read_grades(file_path)

    for student_id, data in students.items():
        report = generate_report(data)
        display_report(report)
        plot_grades(data)

if __name__ == "__main__":
    main()