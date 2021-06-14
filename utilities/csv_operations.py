import csv
from setup.config import report_file
from setup.config import grade_file

def populate():
    students = []

    with open(report_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            students.append((row[0],row[3],row[2],row[4],row[5],row[6],row[7],row[8].lower(),row[9],row[10],row[11],row[12],row[13]))
            line_count += 1
    return students