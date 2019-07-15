from collections import defaultdict
from exploring_data import paid_engagement_in_first_week
import numpy as np

"""
Create a dictionary of engagement grouped by student.
The keys are account keys, and the values are lists of engagement records.
"""
engagement_by_account = defaultdict(list)
for engagement_record in paid_engagement_in_first_week:
    account_key = engagement_record['account_key']
    engagement_by_account[account_key].append(engagement_record)
    # print(engagement_by_account)
    # break;


"""
Create a dictionary with the total minutes each student spent in the classroom during the first week.
The keys are account keys, and the values are numbers (total minutes)
"""
total_minutes_by_account = {}

for account_key, engagement_for_student in engagement_by_account.items():
    total_minutes = 0
    for engagement_record in engagement_for_student:
        total_minutes += engagement_record['total_minutes_visited']
        total_minutes_by_account[account_key] = total_minutes


# Summarize the data about minutes spent in the classroom
# need to convert the defaultdict values to list for numpy
total_minutes = list(total_minutes_by_account.values())

print(f'Mean: {np.mean(total_minutes)}')
print(f'Standard deviation: {np.std(total_minutes)}')
print(f'Minimum: {np.min(total_minutes)}')
print(f'Maximum: {np.max(total_minutes)}')
"""
looping through the dictionary extract key and value
perform simple compare to obtain the student with max minutes
"""
student_with_max_minutes = 0
max_minutes = 0
for student, total_minutes in total_minutes_by_account.items():
    if total_minutes > max_minutes:
        max_minutes = total_minutes
        student_with_max_minutes = student
print(f'student_with_max_minutes={student_with_max_minutes}')
