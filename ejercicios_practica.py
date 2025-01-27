#!/usr/bin/env python
'''
SQL Introducción [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import sqlite3
from sqlite3.dbapi2 import Cursor

# https://extendsclass.com/sqlite-browser.html


def create_schema():

    # Conectarnos a la base de datos
    # En caso de que no exista el archivo se genera
    # como una base de datos vacia
    conn = sqlite3.connect('secundaria.db')

    # Crear el cursor para poder ejecutar las querys
    c = conn.cursor()

    # Ejecutar una query
    c.execute("""
                DROP TABLE IF EXISTS estudiante;
            """)

    # Ejecutar una query
    c.execute("""
            CREATE TABLE estudiante(
                [id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [name] TEXT NOT NULL,
                [age] INTEGER NOT NULL,
                [grade] INTEGER,
                [tutor] TEXT
            );
            """)

    # Para salvar los cambios realizados en la DB debemos
    # ejecutar el commit, NO olvidarse de este paso!
    conn.commit()

    # Cerrar la conexión con la base de datos
    conn.close()


def fill():
    print('Completemos esta tablita!')
    # Llenar la tabla de la secundaria con al menos 5 estudiantes
    # Cada estudiante tiene los posibles campos:
    # id --> este campo es auto incremental por lo que no deberá completarlo
    # name --> El nombre del estudiante (puede ser solo nombre sin apellido)
    # age --> cuantos años tiene el estudiante
    # grade --> en que año de la secundaria se encuentra (1-6)
    # tutor --> nombre de su tutor

    # Se debe utilizar la sentencia INSERT.
    # Observar que hay campos como "grade" y "tutor" que no son obligatorios
    # en el schema creado, puede obivar en algunos casos completar esos campos

    conectar = sqlite3.connect("secundaria.db")
    cursor = conectar.cursor()

    datos = [("mirian", 44, 2, "javier"), 
             ("rafael", 12, 1, "juan"),
             ("ambar", 4, 1, "graciela"),
             ("pedro", 40, 3, "emma"),
             ("juana", 39, 2, "hernan")
             ]
    cursor.executemany("INSERT INTO estudiante VALUES(NULL,?,?,?,?)", datos)

    conectar.commit()
   
    conectar.close()

def fetch():
    print('Comprobemos su contenido, ¿qué hay en la tabla?')
    # Utilizar la sentencia SELECT para imprimir en pantalla
    # todas las filas con todas sus columnas
    # Utilizar fetchone para imprimir de una fila a la vez

    conectar = sqlite3.connect("secundaria.db")
    cursor = conectar.cursor()
    cursor.execute("SELECT * FROM estudiante")
    while True:
        data = cursor.fetchone()
        if data is None:
            break
        print(data)
    
    conectar.close()


def search_by_grade(grade):
    print('Operación búsqueda!')
    # Utilizar la sentencia SELECT para imprimir en pantalla
    # aquellos estudiantes que se encuentra en en año "grade"

    # De la lista de esos estudiantes el SELECT solo debe traer
    # las siguientes columnas por fila encontrada:
    # id / name / age

    conectar = sqlite3.connect('secundaria.db')
    cursor = conectar.cursor()
    for data in cursor.execute("SELECT id, name, age FROM estudiante WHERE grade =?", (grade,)):
        print(data)
    
    conectar.close()


def insert(grade):
    print('Nuevos ingresos!')
    # Utilizar la sentencia INSERT para ingresar nuevos estudiantes
    # a la secundaria
    conectar = sqlite3.connect('secundaria.db')
    cursor = conectar.cursor()
    nuevos = [("patricio", 25, 3, "nico"),
    ("dora", 60, 5, "laura"),
    ("franco", 45, 2, "javier")]

    cursor.executemany("INSERT INTO estudiante VALUES(NULL,?,?,?,?)", nuevos)
    conectar.commit()
    conectar.close()



def modify(id, name):
    print('Modificando la tabla')
    # Utilizar la sentencia UPDATE para modificar aquella fila (estudiante)
    # cuyo id sea el "id" pasado como parámetro,
    # modificar su nombre por "name" pasado como parámetro

    conectar = sqlite3.connect('personas.db')
    Cursor = conectar.cursor()

    modificar = conectar.execute("UPDATE estudiante SET id =? and name =? WHERE name =?",
                         (id, name)).modificar

    print(modificar)

    conectar.commit()
   
    conectar.close()



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    create_schema()   # create and reset database (DB)
    # fill()
    # fetch()

    grade = 3
    # search_by_grade(grade)

    new_student = ['You', 16]
    # insert(new_student)

    name = '¿Inove?'
    id = 2
    # modify(id, name)
