import unicodecsv


class CSVreader():
    @staticmethod
    def read_csv_dict(csv_file_path):

        with open(csv_file_path, 'rb') as f:
            reader = unicodecsv.DictReader(f)
            enrollments = list(reader)
        return enrollments


if __name__ == "__main__":
    csv_reader = CSVreader()
    print(
        f'daily_engagement->{csv_reader.read_csv_dict("daily_engagement.csv")[0]}\n')
    print(f'enrollments->{csv_reader.read_csv_dict("enrollments.csv")[0]}\n')
    print(
        f'project_submissions->{csv_reader.read_csv_dict("project_submissions.csv")[0]}\n')
