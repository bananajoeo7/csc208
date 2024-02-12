import random

# Students List
students = [
    'Dane', 'Parker', 'Shangwen', 'Ved', 'Jackson', 'Liam', 'Cody', 'Johan',
    'Luis', 'Trostin', 'Turner', 'Anfal', 'Ivan', 'Anar', 'Akshay', 'Marin',
    'James', 'Caleb', 'Fikir', 'Jamethiel', 'Isaac', 'Adonis'
]

# List of questions that have either no solutions or only a hint
questions = [
    'Question 1', 'Question 2', 'Question 3', 'Question 4', 'Question 5',
    'Question 6', 'Question 7', 'Question 8', 'Question 9', 'Question 10'
]

# Shuffling the questions
random.shuffle(questions)

# Calculate the number of questions each student should get
num_students = len(students)
num_questions_per_student = len(questions)

# Assign questions to each student
assignments = {student: [] for student in students}
for i, student in enumerate(students):
    start = i * num_questions_per_student
    end = (i + 1) * num_questions_per_student
    assignments[student] = questions[start:end]

# Print Assigned Questions
for student, assigned_questions in assignments.items():
    print(f"{student}: {assigned_questions}")
