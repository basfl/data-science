import unicodecsv

"""
this is a method to read the 
complete csv records using unicodecsv

"""


def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)


"""
this is a method to calculate the number of unique students
from the csv files 

"""


def number_unique_students(records):
    key = "account_key"
    s = set()
    for record in records:
        # print(record[key])
        if record[key]:
            s.add(record[key])
    return (s)


enrollments = read_csv('enrollments.csv')  # read the records from csv file
enrollment_num_rows = len(enrollments)  # calculate the number of rows
# calculate the number of unique students
print(f'number of rows are {enrollment_num_rows}')
enrollment_num_unique_students = len(number_unique_students(enrollments))
print(
    f'enrollment_num_unique_students = {enrollment_num_unique_students}')
##############################################################################
print("###############daily_engagement#################")
# read the records from csv file
daily_engagement = read_csv('daily_engagement.csv')
"""
replacing acct key to accoumt_key
"""
for element in daily_engagement:
    element["account_key"] = element["acct"]
    del(element["acct"])
engagement_num_rows = len(daily_engagement)  # calculate the number of rows
print(f'engagement_num_rows={engagement_num_rows}')
engagement_num_unique_students = len(number_unique_students(
    daily_engagement))  # calculate the number of unique students
print(f'engagement_num_unique_students={engagement_num_unique_students}')
##############################################################################
print("###############project_submissions#################")
project_submissions = read_csv('project_submissions.csv')  # read  records
submission_num_rows = len(project_submissions)  # calculate the number of rows
print(f"submission_num_rows={submission_num_rows}")
submission_num_unique_students = len(number_unique_students(
    project_submissions))  # calculate the number of unique students
print(f"submission_num_unique_students={submission_num_unique_students}")
