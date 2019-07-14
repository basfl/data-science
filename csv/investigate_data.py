import unicodecsv
from reading_data import CSVreader

"""
this is a method to read the 
complete csv records using unicodecsv

"""


def read_csv(filename):
    csv = CSVreader()
    return csv.read_csv_dict(filename)
   


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


# Given some data with an account_key field, removes any records corresponding to Udacity test accounts
def remove_udacity_accounts(data, udacity_test_accounts):
    non_udacity_data = []
    for data_point in data:
        if data_point['account_key'] not in udacity_test_accounts:
            non_udacity_data.append(data_point)
    return non_udacity_data


enrollments = read_csv('enrollments.csv')  # read the records from csv file
enrollment_num_rows = len(enrollments)  # calculate the number of rows
# calculate the number of unique students
#print(f'number of rows are {enrollment_num_rows}')
enrollment_num_unique_students = len(number_unique_students(enrollments))
# print(
#     f'enrollment_num_unique_students = {enrollment_num_unique_students}')
##############################################################################
# print("###############daily_engagement#################")
# read the records from csv file
daily_engagement = read_csv('daily_engagement.csv')
"""
replacing acct key to accoumt_key
"""
for element in daily_engagement:
    element["account_key"] = element["acct"]
    del(element["acct"])
engagement_num_rows = len(daily_engagement)  # calculate the number of rows
# print(f'engagement_num_rows={engagement_num_rows}')
engagement_num_unique_students = len(number_unique_students(
    daily_engagement))  # calculate the number of unique students
# print(f'engagement_num_unique_students={engagement_num_unique_students}')
##############################################################################
# print("###############project_submissions#################")
project_submissions = read_csv('project_submissions.csv')  # read  records
submission_num_rows = len(project_submissions)  # calculate the number of rows
# print(f"submission_num_rows={submission_num_rows}")
submission_num_unique_students = len(number_unique_students(
    project_submissions))  # calculate the number of unique students
# print(f"submission_num_unique_students={submission_num_unique_students}")

# checking for problems in enrollment

# Create a set of the account keys for all Udacity test accounts
#print("##############checking problem ####################")
udacity_test_accounts = set()
for enrollment in enrollments:
    if enrollment['is_udacity']:
        udacity_test_accounts.add(enrollment['account_key'])
#print(f"test data length is {len(udacity_test_accounts)}")
# Remove Udacity test accounts from all three tables
non_udacity_enrollments = remove_udacity_accounts(
    enrollments, udacity_test_accounts)
non_udacity_engagement = remove_udacity_accounts(
    daily_engagement, udacity_test_accounts)
non_udacity_submissions = remove_udacity_accounts(
    project_submissions, udacity_test_accounts)

# print(len(non_udacity_enrollments))
# print(len(non_udacity_engagement))
# print(len(non_udacity_submissions))
