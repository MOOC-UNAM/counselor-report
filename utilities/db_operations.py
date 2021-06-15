from mysql.connector import connect, Error
from setup.config import db_host
from setup.config import db_name
from setup.config import db_user
from setup.config import db_pass


connection = connect(
        host = db_host,
        database = db_name,
        user = db_user,
        password = db_pass,            
    )


def create_students_table():
    with connection.cursor() as cursor:
        try:
            cursor.execute("""
                CREATE TABLE students (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user VARCHAR(12),
                    lastname VARCHAR(300),
                    firstname VARCHAR(300),
                    email VARCHAR(100),
                    groupname VARCHAR(50),
                    consejero VARCHAR(300),
                    asesor VARCHAR(300),
                    estatus VARCHAR(500),
                    fortalezas VARCHAR(3000),
                    trabajo VARCHAR(3000),
                    mejorar VARCHAR(3000),
                    recomendaciones VARCHAR(3000),
                    calificacion FLOAT
                )
            """)
            print("The students table has been created")
            return True
        except Error as e:
            print(e)


def populate_students_table(students):
    with connection.cursor() as cursor:
        try:
            print("Clearing students table...")
            cursor.execute("TRUNCATE TABLE students")
        except Error as e:
            print(e)
        print("Inserting data...")
        insert_students_query = """
            INSERT INTO students
            (user,lastname,firstname,email,groupname,consejero,asesor,estatus,fortalezas,trabajo,mejorar,recomendaciones,calificacion)
            VALUE(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        try:
            cursor.executemany(insert_students_query, students)
            connection.commit()
            print("Student data has been inserted")
            return True
        except Error as e:
            print(e)
    

def insert_student_grades(grades):
    with connection.cursor() as cursor:
        try:
            for grade in grades:
                query = "UPDATE students SET calificacion={} WHERE email='{}'".format(grade[1],grade[0])
                print(query)
                cursor.execute(query)
                connection.commit()
            print("Student grades have been inserted")
            return True
        except Error as e:
            print(e)


def select_students(option):
    if(option == 1):
        select_query = """
                SELECT lastname,firstname,email,groupname,consejero,asesor,estatus,fortalezas,trabajo,mejorar,recomendaciones,calificacion FROM students WHERE estatus != '' ORDER BY lastname
            """
    elif(option == 2):
        select_query = """
                SELECT lastname,firstname,email,groupname,consejero,asesor,estatus,fortalezas,trabajo,mejorar,recomendaciones,calificacion FROM students WHERE calificacion < 6 AND estatus = '' ORDER BY calificacion DESC 
            """
    elif(option == 3):
        select_query = """
                SELECT lastname,firstname,email,groupname,consejero,asesor,estatus,fortalezas,trabajo,mejorar,recomendaciones,calificacion FROM students WHERE calificacion >= 6 AND estatus = '' ORDER BY calificacion DESC
            """
    
    with connection.cursor() as cursor:
        try:
            cursor.execute(select_query)
            students_selected = cursor.fetchall()
            connection.commit()
            return students_selected
        except Error as e:
            print(e)
