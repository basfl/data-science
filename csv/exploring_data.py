from investigate_data import non_udacity_enrollments

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

print(len(paid_students))
