import sqlite3

from ProblemEntry import ProblemEntry
class Database:
    def __init__(self, company_name):
        self.company_name = company_name
        self.database_file = f"{company_name}/problems.db"

    def init_db(self):
        conn = sqlite3.connect(self.database_file)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS problems (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                url_link TEXT NOT NULL,
                tags TEXT,  -- Tags will be stored as a comma-separated string
                acceptance TEXT,
                difficulty TEXT,
                frequency REAL
            )
        ''')
        conn.commit()
        conn.close()

    def insert_problems(self, problems):
        for problem in problems:
            self.insert_problem(problem)

    def insert_problem(self, problem):
        conn = sqlite3.connect(self.database_file)
        cursor = conn.cursor()
        # Update this to insert the id and prevent duplication
        cursor.execute('''
            INSERT OR REPLACE INTO problems (id, title, url_link, tags, acceptance, difficulty, frequency)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (problem.problem_id, problem.title, problem.url_link, ','.join(problem.tags), problem.acceptance, problem.difficulty, problem.frequency))
        conn.commit()
        conn.close()

    def get_problems(self):
        conn = sqlite3.connect(self.database_file)
        cursor = conn.cursor()
        cursor.execute('SELECT id, title, url_link, tags, acceptance, difficulty, frequency FROM problems')
        rows = cursor.fetchall()
        conn.close()
        # Adjust the construction of ProblemEntry objects to match the updated class
        return [ProblemEntry(
            problem_id=row[0],
            title=row[1],
            url_link=row[2],
            tags=row[3].split(','),
            acceptance=row[4],
            difficulty=row[5],
            frequency=row[6]) for row in rows]

