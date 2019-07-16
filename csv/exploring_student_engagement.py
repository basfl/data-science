from collections import defaultdict
from exploring_data import paid_engagement_in_first_week
import numpy as np

"""
Create a dictionary of engagement grouped by student.
The keys are account keys, and the values are lists of engagement records.
"""


def group_data(data, key_name):
    group_data = defaultdict(list)
    for data_point in data:
        account_key = data_point[key_name]
        group_data[account_key].append(data_point)
        # print(engagement_by_account)
        # break;
    return group_data


"""
Create a dictionary with the total minutes each student spent in the classroom during the first week.
The keys are account keys, and the values are numbers (total minutes)
"""


def sum_grouped_data(grouped_data, field_name):
    sum_data = {}
    for key, data_point in grouped_data.items():
        total = 0
        for data_point in data_point:
            total += data_point[field_name]
        sum_data[key] = total
    return sum_data


"""
Summarize the data about minutes spent in the classroom
need to convert the defaultdict values to list for numpy
"""


def describe_data(data):
    print(f'Mean: {np.mean(data)}')
    print(f'Standard deviation: {np.std(data)}')
    print(f'Minimum: {np.min(data)}')
    print(f'Maximum: {np.max(data)}')


engagement_by_account = group_data(
    paid_engagement_in_first_week, "account_key")

total_minutes_by_account = sum_grouped_data(
    engagement_by_account, "total_minutes_visited")

total_minutes = list(total_minutes_by_account.values())

describe_data(total_minutes)


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
print(f'max_minutes={max_minutes}')
# print(paid_engagement_in_first_week[1])
for engagement in paid_engagement_in_first_week:
    if engagement['account_key'] == student_with_max_minutes:
        print(engagement)

print("###############exploring_student_engagement_completed_lesson")

lesson_completed_by_account = sum_grouped_data(
    engagement_by_account, "lessons_completed")

lesson_completed = list(lesson_completed_by_account.values())

describe_data(lesson_completed)

print("######################days visted by account")
days_visted_by_account = sum_grouped_data(engagement_by_account, 'has_visited')
days_visted_by_account_list = list(days_visted_by_account.values())
describe_data(days_visted_by_account_list)
