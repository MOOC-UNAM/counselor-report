from mysql.connector import connect, Error
from setup.config import DB_NAME
from setup.config import db_user
from setup.config import db_pass

def create_students_table():
    try:
        with connect(
            host = DB_NAME,
            user = db_user,
            password = db_pass,
        ) as connection:
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
                    return True
                except Error as e:
                    print(e)
                    return False            
    except Error as e:
        print(e)