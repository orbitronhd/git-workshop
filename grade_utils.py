def calculate_average(marks):
    """
    Calculates the average of a list of numbers.
    """
    total = sum(marks)
    return total / len(marks)

def determine_grade(average):
    """
    Returns a letter grade based on the average.
    TODO: Students can modify the grading scale below.
    """
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'