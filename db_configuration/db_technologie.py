from entities.technology import Technology
class DbTechnology:
    def __init__(self, db_connection):
        self._db_connection = db_connection
        self._select_request = 'select * from technology'
        self._select_find_request = 'select id,name from technology where id=%s'

    def create_table(self):
        request = 'CREATE TABLE technology(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255))'
        self._db_connection.get_connection()
        cursor = self._db_connection.create_cursor()
        cursor.execute(request)
        self._db_connection.connection.commit()
        self._db_connection.close_connection()

    def drop_table(self):
        request = 'DROP TABLE IF EXISTS technology '
        self._db_connection.get_connection()
        cursor = self._db_connection.create_cursor()
        cursor.execute(request)
        self._db_connection.connection.commit()
        self._db_connection.close_connection()

    def create_index(self):
        request = 'CREATE INDEX technology_index ON technology (id)'
        self._db_connection.get_connection()
        cursor = self._db_connection.create_cursor()
        cursor.execute(request)
        self._db_connection.connection.commit()
        self._db_connection.close_connection()

    def drop_index(self):
        request = 'DROP INDEX IF EXISTS technology_index ON technology '
        self._db_connection.get_connection()
        cursor = self._db_connection.create_cursor()
        cursor.execute(request)
        self._db_connection.connection.commit()
        self._db_connection.close_connection()

    def insert_technology(self, technology):
        request = 'INSERT INTO technology (name) VALUES (%s)'
        self._db_connection.get_connection()
        cursor = self._db_connection.create_cursor()
        cursor.execute(request, (technology.name,))
        self._db_connection.connection.commit()
        self._db_connection.close_connection()

    def select_technology(self):
        request = 'SELECT id,name FROM technology ORDER BY id'
        self._db_connection.get_connection()
        cursor = self._db_connection.create_cursor()
        cursor.execute(request)
        rows = cursor.fetchall()
        technologies=[]
        # Displaying fetched rows
        for row in rows:
            technologies.append(Technology(row[0],row[1]))
        self._db_connection.close_connection()
        return technologies

    def select_one_technology_by_id(self, technology_id):
        request = 'SELECT id,name FROM technology WHERE id = %s ORDER BY id'
        self._db_connection.get_connection()
        cursor = self._db_connection.create_cursor()
        cursor.execute(request, (technology_id,))
        row = cursor.fetchone()
        technology=Technology(row[0],row[1])
        self._db_connection.close_connection()
        return technology
