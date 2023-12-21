from entities.job import Job
from entities.technology import Technology
import mysql.connector


class DbJob:
    def __init__(self, db_connection):
        self._db_connection = db_connection
        self._table_name = 'job'
        self._index_name = 'job_index'

    def create_table(self):
        try:
            request = f'CREATE TABLE {self._table_name}(id INT AUTO_INCREMENT PRIMARY KEY,experience VARCHAR(255),skills VARCHAR(2000),languages VARCHAR(2000),entreprise_name VARCHAR(255),date VARCHAR(255),address VARCHAR(255),contract_type VARCHAR(255), qualification VARCHAR(255), technology_id INT,FOREIGN KEY (technology_id) REFERENCES technology(id))'
            self._db_connection.get_connection()
            cursor = self._db_connection.create_cursor()
            cursor.execute(request)
            self._db_connection.connection.commit()
            self._db_connection.close_connection()
        except mysql.connector.Error:
            print('Table already exists !')

    def drop_table(self):
        try:
            request = f'DROP TABLE IF EXISTS {self._table_name} '
            self._db_connection.get_connection()
            cursor = self._db_connection.create_cursor()
            cursor.execute(request)
            self._db_connection.connection.commit()
            self._db_connection.close_connection()
        except mysql.connector.Error:
            print('Table does not exist !')

    def create_index(self):
        try:
            request = f'CREATE INDEX {self._index_name} ON {self._table_name} (id)'
            self._db_connection.get_connection()
            cursor = self._db_connection.create_cursor()
            cursor.execute(request)
            self._db_connection.connection.commit()
            self._db_connection.close_connection()
        except mysql.connector.Error:
            print('Index already exists !')

    def drop_index(self):
        try:
            request = f'DROP INDEX IF EXISTS {self._index_name} ON {self._table_name} '
            self._db_connection.get_connection()
            cursor = self._db_connection.create_cursor()
            cursor.execute(request)
            self._db_connection.connection.commit()
            self._db_connection.close_connection()
        except mysql.connector.Error:
            print('Index does not exist !')

    def insert_offer(self, offer):
        try:
            request = f'INSERT INTO {self._table_name} (experience,skills,languages,entreprise_name,date,address,contract_type,qualification,technology_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            self._db_connection.get_connection()
            cursor = self._db_connection.create_cursor()
            cursor.execute(request, (
                offer.experience, offer.skills, offer.languages, offer.enterprise_name, offer.date, offer.address,
                offer.contract_type,
                offer.qualification, offer.technology.id))
            self._db_connection.connection.commit()
            self._db_connection.close_connection()
        except mysql.connector.Error:
            print('An error has occurred !')

    def select_offer(self):
        try:
            request = f'SELECT * FROM {self._table_name} ORDER BY id'
            self._db_connection.get_connection()
            cursor = self._db_connection.create_cursor()
            cursor.execute(request)
            rows = cursor.fetchall()
            offers = []
            for row in rows:
                offers.append(
                    Job(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                        Technology(row[9], '')))
            self._db_connection.close_connection()
            return offers
        except mysql.connector.Error:
            print('Could not fetch jobs !')
            return []

    def select_one_offer_by_id(self, job_id):
        try:
            request = f'SELECT * FROM {self._table_name} WHERE id = %s ORDER BY id'
            self._db_connection.get_connection()
            cursor = self._db_connection.create_cursor()
            cursor.execute(request, (job_id,))
            row = cursor.fetchone()
            job = Job(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                      Technology(row[9], ''))
            self._db_connection.close_connection()
            return job
        except mysql.connector.Error:
            print(f'Could not fetch job {job_id} !')
            return None
