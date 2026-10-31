"""Steps:
Define a function that takes the student's name and scores.
Calculate the average score.
Check if the average is below 60.
If below 60, classify as At Risk.
Otherwise, classify as On Track.
Return the name, classification, and average.
Print the result."""

def student(name, scores):
    total = 0

    for i in scores:
        total = total + i

    average = total / len(scores)

    if average < 60:
        result = "At Risk"
    else:
        result = "On Track"

    return name, result, average


print(student("Sara", [70, 65, 64, 66]))

########################################################################################
"""Define a function that takes a list of student submissions.
Create an empty list to store late students.
Check each student's submission time.
If the submission time is after 23:00, add the student ID to the list.
Return the list of students who submitted late.
Print the final list."""

def late_students(submissions):
    late = []

    for i in submissions:
        if i[1] > "23:00":
            late.append(i[0])

    return late


students = [
    ["STU-001", "22:30"],
    ["STU-002", "23:30"],
    ["STU-003", "21:00"],
    ["STU-004", "23:45"]
]

print(late_students(students))

###############################################################################

"""Define a function that takes a new student's score and a list of known students' scores.
Set the best student ID and smallest difference.
Compare the new student's score with each known student's score.
Calculate the absolute difference between the two scores.
If the difference is smaller, update the smallest difference and best student ID.
Return the ID of the student with the closest score.
Print the final result."""




def closest_student(new_score, students):
    smallest = 1000
    best_id = ""

    for i in students:
        difference = abs(new_score - i[1])

        if difference < smallest:
            smallest = difference
            best_id = i[0]

    return best_id


students = [
    ["STU-010", 85],
    ["STU-011", 70],
    ["STU-012", 90]
]

print(closest_student(87, students))


#################################################################################

"""Define a function that takes a list of student scores.
Create an empty list to store cleaned scores.
Check each score in the list.
If the score is between 0 and 100, round it to the nearest whole number.
Add the rounded score to the cleaned list.
Return the cleaned list.
Print the final list of scores."""



def clean_scores(scores):
    clean = []

    for i in scores:
        if i >= 0 and i <= 100:
            clean.append(round(i))

    return clean


scores = [72.6, 88.2, -5, 110, 60.4]

print(clean_scores(scores))



##############################################################################################

"""Define a function to calculate the student's average score.
Check if the score list is empty; if it is, display an error.
Classify the student's performance as "Weak" if the average is below 60, or "Adequate" otherwise.
Check the attendance rate. If it is below 75%, classify it as "Low Attendance"; otherwise, classify it as "Adequate Attendance".
Assign "Priority Support" if the student has weak performance and low attendance.
Assign "Standard Support" if the student has either weak performance or low attendance.
Assign "No Support Needed" if the student has adequate performance and adequate attendance.
Print the average score, performance, attendance status, and support level."""


def student_support(scores, attendance):

    if len(scores) == 0:
        print("Error")
        return

    total = 0

    for i in scores:
        total = total + i

    average = total / len(scores)

    if average < 60:
        performance = "Weak"
    else:
        performance = "Adequate"

    if attendance < 75:
        attend = "Low Attendance"
    else:
        attend = "Adequate Attendance"

    if average < 60 and attendance < 75:
        support = "Priority Support"

    elif average < 60 or attendance < 75:
        support = "Standard Support"

    else:
        support = "No Support Needed"

    print("Average:", average)
    print("Performance:", performance)
    print("Attendance:", attend)
    print("Tier:", support)


student_support([50, 40, 60], 60)
