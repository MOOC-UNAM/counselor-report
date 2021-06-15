import csv
from setup.config import report_file
from setup.config import grade_file

def read_students():
    students = []

    with open(report_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            students.append((row[0],row[3],row[2],row[4],row[5],row[6],row[7],row[8].lower(),row[9],row[10],row[11],row[12],'0.00'))
            line_count += 1
        print("Found {} students".format(line_count))
    return students


def read_grades():
    grades = []

    with open(grade_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            grades.append((row[2],row[3]))
            line_count += 1
        print("Found {} student grades".format(line_count))
    return grades
