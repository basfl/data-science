from exploring_data import paid_submissions
from exploring_data import paid_engagement_in_first_week

"""
Create two lists of engagement data for paid students in the first week.
The first list should contain data for students who eventually pass the
subway project, and the second list should contain data for students
who do not.
"""

subway_project_lesson_keys = ['746169184', '3176718735']
# getting list of student whom passed the subway project
passing_subway_project = [data_point["account_key"] for data_point in paid_submissions if data_point['lesson_key']
                          in subway_project_lesson_keys
                          and (data_point['assigned_rating'] == "PASSED" or data_point['assigned_rating'] == "DISTINCTION")]
passing_engagement = []
non_passing_engagement = []
for engagement_record in paid_engagement_in_first_week:
    if engagement_record['account_key'] in passing_subway_project:
        passing_engagement.append(engagement_record)
    else:
        non_passing_engagement.append(engagement_record)

print(len(passing_engagement))
print(len(non_passing_engagement))
