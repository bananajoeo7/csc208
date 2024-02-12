import random

# Students List
students = [
    'Dane', 'Parker', 'Shangwen', 'Ved', 'Jackson', 'Liam', 'Cody', 'Johan',
    'Luis', 'Trostin', 'Turner', 'Anfal', 'Ivan', 'Anar', 'Akshay', 'Marin',
    'James', 'Caleb', 'Fikir', 'Jamethiel', 'Isaac', 'Adonis'
]

# List of questions that have no solutions (or have a hint)
questions = [
    'Question 1', 'Question 2', 'Question 3', 'Question 4', 'Question 5',
    'Question 6', 'Question 7', 'Question 8', 'Question 9', 'Question 10',
    'Question 11', 'Question 12', 'Question 13', 'Question 14', 'Question 15',
    'Question 16', 'Question 17', 'Question 18', 'Question 19', 'Question 20',
    'Question 21', 'Question 22', 'Question 23', 'Question 24', 'Question 25',
    'Question 26', 'Question 27', 'Question 28', 'Question 29', 'Question 30'
]

# Shuffle the questions
random.shuffle(questions)

# Calculate the number of questions each student should get
num_students = len(students)
num_questions_per_student = len(questions) // num_students
remaining_questions = len(questions) % num_students

# Assign questions to each student
assignments = {student: [] for student in students}
start = 0
for student in students:
    num_questions = num_questions_per_student + (1 if remaining_questions > 0 else 0)
    end = start + num_questions
    assignments[student] = questions[start:end]
    start = end
    remaining_questions -= 1

# Output assignments
for student, assigned_questions in assignments.items():
    print(f"{student}: {assigned_questions}")
