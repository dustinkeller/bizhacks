import sqlite3
from datetime import date
import pandas as pd

class  bizzHackBot_db():
        
    def create_question_table():
        """
        creates table if it doesnt exist
        """
        con = sqlite3.connect('bizzHack.db')
        cur = con.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name TEXT NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        con.commit()
        con.close()

    def create_question_answer_table():
        """
        creates table if it doesnt exist
        """
        con = sqlite3.connect('bizzHack.db')
        cur = con.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS questions_answers (
                qa_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name TEXT NOT NULL,
                date TEXT NOT NULL,
                question TEXT NOT NULL,
                answer TEXT NOT NULL,
                points INTEGER,
                FOREIGN KEY(user_name) REFERENCES questions(user_name)
            )
        ''')
        con.commit()
        con.close()

    def insert_question(user):
        """
        inserts user and registration date
        """
        con = sqlite3.connect('bizzHack.db')
        cur = con.cursor()
        today = date.today()
        current_date = today.strftime("%Y-%m-%d")
        cur.execute("INSERT INTO questions (user_name, date) VALUES (?, ?)", (user,current_date))
        con.commit()
        con.close()
    
    def insert_question_answer(user, question, answer, points):
        """
        inserts who answered the question, date, and answer into buzzhack db
        """
        con = sqlite3.connect('bizzHack.db')
        cur = con.cursor()
        today = date.today()
        current_date = today.strftime("%Y-%m-%d")
        cur.execute("INSERT INTO questions_answers (user_name, date, question, answer, points) VALUES (?, ?, ?, ?, ?)", (user,current_date,question, answer, points))
        con.commit()
        con.close()

    def individual_score(user):
        """
        select the user and the number of points they have from the db
        """
        con = sqlite3.connect('bizzHack.db')
        df = pd.read_sql_query(f"select user_name, date, points from questions_answers where user_name = '{user}'", con)
        con.close()
        return df
    
    def total_scores():
        """
        selects all users and their total score
        """
        con = sqlite3.connect('bizzHack.db')
        df = pd.read_sql_query(f"select user_name, date, count(points) as TotalScore from questions_answers group by user_name", con)
        con.close()
        return df