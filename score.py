import sqlite3
import datetime


class Score:

    def __init__(self):
        self.score = 0
        self.score_increase = 100
        self.record = self.get_records()

    def get_records(self):
        connection = sqlite3.connect("records.db")
        cursor = connection.cursor()
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS Records (
            name TEXT PRIMARY KEY,
            score INTEGER,
            date DATETIME) '''
        )
        connection.commit()
        x = list(cursor.execute('''SELECT name, score, date FROM records ORDER BY score DESC, date ASC LIMIT 13'''))
        connection.close()
        return x

    def set_record(self, name):
        self.today = datetime.datetime.today()
        connection = sqlite3.connect("records.db")
        cursor = connection.cursor()
        cursor.execute(
            '''INSERT INTO records 
            (name, score, date) 
            VALUES (?, ?, ?)
            ON CONFLICT (name)
            DO UPDATE SET score = (?), date =(?)
            WHERE name = (?) AND score < (?)''',
            [name, self.score, self.today.strftime("%Y-%m-%d-%H.%M.%S"), self.score,
             self.today.strftime("%Y-%m-%d-%H.%M.%S"), name, self.score]
        )
        connection.commit()
        connection.close()

    def set_current_score(self, score_increase):
        self.score += score_increase
        return self.score

    def restart(self):
        self.score_increase = 100
        self.record = self.get_records()

    def start_play(self):
        self.score = 0
