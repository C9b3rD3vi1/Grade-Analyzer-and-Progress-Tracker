# Description: This file contains the unit tests for the functions in grade_analyzer.py

import pytest

# Import the functions to be tested
from grade_analyzer import calculate_average, calculate_median, identify_trends, predict_future_performance

# test the functions calculate_average, calculate_median, identify_trends, and predict_future_performance
def test_calculate_average():
    assert calculate_average([85, 88, 90]) == 87.67
    assert calculate_average([92, 91, 89]) == 90.67

def test_calculate_median():
    assert calculate_median([85, 88, 90]) == 88
    assert calculate_median([92, 91, 89]) == 91


# test the function identify_trends
def test_identify_trends():
    assert identify_trends([85, 88, 90]) == "Improving"
    assert identify_trends([92, 91, 89]) == "Declining"
    assert identify_trends([90, 90, 90]) == "Stable"


# test the function predict_future_performance
def test_predict_future_performance():
    assert predict_future_performance([85, 88, 90]) == pytest.approx(91.67, 0.01)
    assert predict_future_performance([92, 91, 89]) == pytest.approx(88.67, 0.01)