from collections import defaultdict
from exploring_data import paid_engagement_in_first_week
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
        total_minutes+=engagement_record['total_minutes_visited']
        total_minutes_by_account['account_key']=total_minutes

