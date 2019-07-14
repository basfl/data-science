import unicodecsv
from datetime import datetime as dt

class CSVreader():
  #  @staticmethod
    def read_csv_dict(self, csv_file_path):

        with open(csv_file_path, 'rb') as self.f:
            self.reader = unicodecsv.DictReader(self.f)
            self.records = list(self.reader)
        return self.clean_data(csv_file_path, self.records)

    def parse_date(self, date):
        if date == '':
            return None
        else:
            return dt.strptime(date, '%Y-%m-%d')

    def parse_maybe_int(self, i):
        if i == '':
            return None
        else:
            return int(i)

    def clean_data(self, csv_file_path, records):
        if csv_file_path == "./csv_files/enrollments.csv":
            for self.enrollment in records:
                self.enrollment['cancel_date'] = self.parse_date(
                    self.enrollment['cancel_date'])
                self.enrollment['days_to_cancel'] = self.parse_maybe_int(
                    self.enrollment['days_to_cancel'])
                self.enrollment['is_canceled'] = self.enrollment['is_canceled'] == 'True'
                self.enrollment['is_udacity'] = self.enrollment['is_udacity'] == 'True'
                self.enrollment['join_date'] = self.parse_date(
                    self.enrollment['join_date'])
            return records
        elif csv_file_path == "./csv_files/daily_engagement.csv":
            for self.engagement_record in records:
                self.engagement_record['lessons_completed'] = int(
                    float(self.engagement_record['lessons_completed']))
                self.engagement_record['num_courses_visited'] = int(
                    float(self.engagement_record['num_courses_visited']))
                self.engagement_record['projects_completed'] = int(
                    float(self.engagement_record['projects_completed']))
                self.engagement_record['total_minutes_visited'] = float(
                    self.engagement_record['total_minutes_visited'])
                self.engagement_record['utc_date'] = self.parse_date(
                    self.engagement_record['utc_date'])
            return records
        elif csv_file_path == "./csv_files/project_submissions.csv":
            for self.submission in records:
                self.submission['completion_date'] = self.parse_date(
                    self.submission['completion_date'])
                self.submission['creation_date'] = self. parse_date(
                    self.submission['creation_date'])
                return records
        else:
            return records


# if __name__ == "__main__":
#     csv_reader = CSVreader()

#     print(
#         f'daily_engagement->{csv_reader.read_csv_dict("daily_engagement.csv")[0]}\n')
#     print(f'enrollments->{csv_reader.read_csv_dict("enrollments.csv")[0]}\n')
#     print(
#         f'project_submissions->{csv_reader.read_csv_dict("project_submissions.csv")[0]}\n')
