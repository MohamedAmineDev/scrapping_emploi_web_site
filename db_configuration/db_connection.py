import mysql.connector


class DbConnection:
    def __init__(self):
        self._host = f'127.0.0.1'
        self._database = 'jobs_db'
        self._user = 'user_scrapper_2'
        self._password = '123456789'
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def get_connection(self):
        try:
            self._connection = mysql.connector.connect(
                host=self._host,
                database=self._database,
                user=self._user,
                password=self._password
            )
        except mysql.connector.Error:
            print('Could connect to the database !')

    def is_connected(self):
        return self._connection.is_connected()

    def close_connection(self):
        self._connection.close()

    def create_cursor(self):
        return self._connection.cursor()
