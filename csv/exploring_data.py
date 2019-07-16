from investigate_data import non_udacity_enrollments
from investigate_data import non_udacity_engagement
from investigate_data import non_udacity_submissions

"""
Create a dictionary named paid_students containing all students who either
haven't canceled yet or who remained enrolled for more than 7 days. The keys
should be account keys, and the values should be the date the student enrolled.

"""

paid_students = {}
for enrollment in non_udacity_enrollments:
    if not enrollment['is_canceled'] or enrollment['days_to_cancel'] > 7:
        account_key = enrollment['account_key']
        enrollment_date = enrollment['join_date']
        if account_key not in paid_students or enrollment_date > paid_students[account_key]:
            paid_students[account_key] = enrollment_date

# print(paid_students)
# print(len(paid_students))
"""
Create a list of rows from the engagement table including only rows where
the student is one of the paid students you just found, and the date is within
one week of the student's join date.
"""


def within_one_week(join_date, engagement_date):
    time_delta = engagement_date - join_date
    return time_delta.days < 7 and time_delta.days >= 0


def remove_free_trial_cancels(data):
    new_data = []
    for data_point in data:
        if data_point['account_key'] in paid_students:
            new_data.append(data_point)
    return new_data


paid_enrollment = remove_free_trial_cancels(non_udacity_enrollments)
paid_engagement = remove_free_trial_cancels(non_udacity_engagement)
paid_submissions = remove_free_trial_cancels(non_udacity_submissions)

# print(len(paid_enrollment))
#print(len(paid_engagement))
# print(len(paid_submissions))

for engagement in paid_engagement:
        
        if engagement['num_courses_visited']>0:
                engagement['has_visited']=1
        else:
                engagement['has_visited']=0


paid_engagement_in_first_week = []

for engagement in paid_engagement:
    account_key = engagement['account_key']
    join_date = paid_students[account_key]
    engagement_record_date = engagement['utc_date']
    if within_one_week(join_date, engagement_record_date):
        paid_engagement_in_first_week.append(engagement)

# print(len(paid_engagement_in_first_week))
