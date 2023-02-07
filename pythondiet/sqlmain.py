from sqlite3 import *
import os.path
from main import *

def Start():

    conn = sqlite3.connect('account.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS person(
       id INT PRIMARY KEY,
       dietary INT,
       weight INT,
       height INT,
       age INT,
       sex INT,
       phys_activity FLOAT,
       true_nutr_int FLOAT,
       water_int INT,
       daynutr FLOAT,
       weeknutr FLOAT);
    """)
    conn.commit()

    cur.execute("""CREATE TABLE IF NOT EXISTS meals(
       id INT PRIMARY KEY,
       id_meal INT !!!! KEY, 
       amount INT,
       when_added TEXT);
    """)
    conn.commit()

def End(meals, account):
    dietary, weight, height, age, sex, phys_activity, true_nutr_int, water_int, daynutr, weeknutr = main_account.write_info()
    cur.execute("INSERT INTO person(id, dietary, weight, height, age, sex, phys_activity, true_nutr_int, water_int, daynutr, weeknutr) VALUES( , ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", dietary, weight, height, age, sex, phys_activity, true_nutr_int, water_int, daynutr, weeknutr) #11 элементов
    conn.commit()
    cur.executemany("INSERT INTO person(id, id_meal, amount, when_added) VALUES( , ?, ?, ?)", meals)
    conn.commit()

def Get():
    pass