# Student Grade Manager

# Step 1: Get student scores
student_scores = input("Enter student scores separated by commas: ")

scores = [int(score) for score in student_scores.split(",")]

# Step 2: Assign Grades using List Comprehension
grades = [
    "A" if score >= 90 else
    "B" if score >= 80 else
    "C" if score >= 70 else
    "D" if score >= 60 else
    "F"
    for score in scores
]

# Step 3: Filter Passing and Failing Students
passing_students = [score for score in scores if score >= 60]
failing_students = [score for score in scores if score < 60]

# Step 4: Print Results
print("\n--- Student Grades ----")
for i, (score, grade) in enumerate(zip(scores, grades), start=1):
    print(f"Student {i}: Score = {score}, Grade = {grade}")

print("\n--- Passing and Failing Students ---")
print("Passing Students:", passing_students)
print("Failing Students:", failing_students)

# Step 5: Average Score
average = sum(scores) / len(scores) if scores else 0
print(f"\nAverage Score: {average:.2f}")

# Step 6: Ranking Scores
while True:
    order = input("\nDo you want to see the scores ranked (type 'asc' for ascending / 'desc' for descending / 'no' to skip)? ").strip().lower()
    if order == "asc":
        ranked = sorted(scores)
        print("Scores in ascending order:", ranked)
        break
    elif order == "desc":
        ranked = sorted(scores, reverse=True)
        print("Scores in descending order:", ranked)
        break
    elif order == "no":
        break
    else:
        print("Please enter 'asc', 'desc' or 'no'.")