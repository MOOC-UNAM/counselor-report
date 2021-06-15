from utilities.csv_operations import *
from utilities.db_operations import *
from utilities.html_operations import build_html
from setup.config import html_dir
from setup.config import url_location
from setup.config import pdf_dir
import pdfkit

table = create_students_table()
students = read_students()
populate_students_table(students)
grades = read_grades()
insert_student_grades(grades)
student_type = input("""
Selecciona el tipo de reporte:
    [1] Estudiante sin actividad o que no tiene actividad evaluable en plataforma
    [2] Estudiante con calificación no aprobatoria
    [3] Estudiante con calificación aprobatoria
""")
students_selected = select_students(int(student_type))
file_count = 0
for student in students_selected:
    html_skeleton = build_html(student)

    student_name = student[1].split(" ")
    student_lastname = student[0].split(" ")
    if(len(student_name) > 2):
        student_filename = student_lastname[0].lower() + "_" + student_lastname[1].lower() + "_" + student_name[0].lower() + "_" + student_name[1].lower()
    else:
        student_filename = student_lastname[0].lower() + "_" + student_lastname[1].lower() + "_" + student_name[0].lower()
    
    html_name = "{}{}.html".format(html_dir,student_filename)
    f = open(html_name,'w')
    f.write(html_skeleton)
    f.close()

    url_file = "{}{}.html".format(url_location,student_filename)
    pdf_name = "{}{}.pdf".format(pdf_dir,student_filename)
    pdfkit.from_url(url_file,pdf_name)
    file_count += 1

print("{} files were created".format(file_count))
