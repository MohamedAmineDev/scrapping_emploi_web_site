from entities.offer import Offer
from entities.technology import Technology

class DbOffer:
    def __init__(self, db_connection):
        self._db_connection = db_connection

    def create_table(self):
        request = 'CREATE TABLE offer(id INT AUTO_INCREMENT PRIMARY KEY,experience VARCHAR(255),skills VARCHAR(2000),languages VARCHAR(2000),entreprise_name VARCHAR(255),date VARCHAR(255),address VARCHAR(255),contract_type VARCHAR(255), qualification VARCHAR(255), technology_id INT,FOREIGN KEY (technology_id) REFERENCES technology(id))'
        self._db_connection.get_connection()
        cursor = self._db_connection.create_cursor()
        cursor.execute(request)
        self._db_connection.connection.commit()
        self._db_connection.close_connection()

    def drop_table(self):
        request = 'DROP TABLE IF EXISTS offer '
        self._db_connection.get_connection()
        cursor = self._db_connection.create_cursor()
        cursor.execute(request)
        self._db_connection.connection.commit()
        self._db_connection.close_connection()

    def create_index(self):
        request = 'CREATE INDEX offer_index ON offer (id)'
        self._db_connection.get_connection()
        cursor = self._db_connection.create_cursor()
        cursor.execute(request)
        self._db_connection.connection.commit()
        self._db_connection.close_connection()

    def drop_index(self):
        request = 'DROP INDEX IF EXISTS offer_index ON offer '
        self._db_connection.get_connection()
        cursor = self._db_connection.create_cursor()
        cursor.execute(request)
        self._db_connection.connection.commit()
        self._db_connection.close_connection()

    def insert_offer(self, offer):
        request = 'INSERT INTO offer (experience,skills,languages,entreprise_name,date,address,contract_type,qualification,technology_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        self._db_connection.get_connection()
        cursor = self._db_connection.create_cursor()
        cursor.execute(request, (
        offer.experience, offer.skills, offer.languages, offer.name, offer.date, offer.address, offer.contract_type,
        offer.qualification, offer.technology.id))
        self._db_connection.connection.commit()
        self._db_connection.close_connection()

    def select_offer(self):
        request = 'SELECT * FROM offer ORDER BY id'
        self._db_connection.get_connection()
        cursor = self._db_connection.create_cursor()
        cursor.execute(request)
        rows = cursor.fetchall()
        offers = []
        for row in rows:
            offers.append(Offer(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],Technology(row[9],'')))
        self._db_connection.close_connection()
        return offers

    def select_one_offer_by_id(self, offer_id):
        request = 'SELECT * FROM offer WHERE id = %s ORDER BY id'
        self._db_connection.get_connection()
        cursor = self._db_connection.create_cursor()
        cursor.execute(request, (offer_id,))
        row = cursor.fetchone()
        offer = Offer(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],Technology(row[9],''))
        self._db_connection.close_connection()
        return offer
