def calculate_grade(score):
    """
    Function to calculate the grade based on a given score using a detailed grading scale.
    
    Args:
    - score: Integer score of a student.
    
    Returns:
    - String: Grade corresponding to the score based on the grading scale.
    """
    if score >= 70:
        return 'A'
    elif score >= 60:
        return 'B'
    elif score >= 50:
        return 'C'
    elif score >= 40:
        return 'D'
    elif score >= 30:
        return 'E'
    else:
        return 'F'

def calculate_overall_grade(subject_scores):
    """
    Function to calculate Tolade's overall grade based on multiple subject scores.
    
    Returns:
    - String: Overall grade based on the average score across subjects.
    """
    total_score = sum(subject_scores.values())
    average_score = total_score / len(subject_scores)
    overall_grade = calculate_grade(int(average_score))
    return overall_grade

def calculate_rank_with_grades(class_scores, tolade_scores):
    """
    Function to calculate Tolade's standing in class based on grades using a detailed grading score

    """
    tolade_grade = calculate_overall_grade(tolade_scores)
    grades = {name: calculate_overall_grade(scores) for name, scores in class_scores.items()}
    sorted_grades = sorted(grades.items(),reverse=True)

# Tolade's scores
    tolade_scores = {
        "Mathematics": 60,
        "English": 45,
        "Commerce": 56,
        "Economics": 85,
        "Home Management": 62,
        "Agric": 71,
        "French": 52,
        "Chemistry": 36,
        "Visual Art": 67,
        "Yoruba": 69
    }