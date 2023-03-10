import pyodbc
import logging


class DatabaseConnection:

    def __init__(self):
        self._connection = None
        logging.getLogger('Database Connection')

    def __repr__(self):
        pass

    def __format__(self, format_spec):
        pass

    def __str__(self):
        pass

    # crude functions to simplify when reading
    def create(self, query_string):
        return self._execute(query_string)

    def select(self, query_string):
        return self._execute(query_string)

    def update(self, query_string):
        return self._execute(query_string)

    def delete(self, query_string):
        return self._execute(query_string)

    def drop(self, query_string):
        return self._execute(query_string)

    def insert(self, query_string):
        return self._execute(query_string)

    def alter(self, query_string):
        return self._execute(query_string)

    def connect(self, connection_string):
        """
        connect to the database using the connection string
        if the connection fails report the user
        """
        if self._connection is None:
            try:
                self._connection = pyodbc.connect(connection_string)
            except pyodbc.error as error:
                logging.error(error)
        else:
            raise ConnectionError("connection already exists")  # should this be an error or just False and log action

    def close(self):
        """
        close the open connection
        nothing if there is no connection
        """
        if self._connection is not None:
            # put in an error loop -> try to close the connection x time before raising an error
            self._connection.close()
            logging.debug('connection closed')

    @staticmethod
    def find_drivers():
        """
        search the machine for any SQL drivers
        return all drivers found

        """
        return pyodbc.drivers()  # could do this a bit better than just wrapping the call

    def _execute(self, query_string):
        """
        check if the connection is valid

        execute the query

        return the results of the query if any else empty list

        """
        if self._connection is None:
            raise ConnectionError("Connection has not been established")
        try:
            cursor = self._connection.cursor()
            logging.debug(f'executing: {query_string}')
            cursor.execute(query_string)
            for value in cursor.fetchall():
                yield value
            cursor.commit()
            cursor.close()
        except Exception as error:  # less generic error
            logging.error(error)


db = DatabaseConnection()

db.connect('connection_string')

db.select('')

db.close()

# SELECT - extracts data from a database
# UPDATE - updates data in a database
# DELETE - deletes data from a database
# INSERT INTO - inserts new data into a database
# CREATE DATABASE - creates a new database
# ALTER DATABASE - modifies a database
# CREATE TABLE - creates a new table
# ALTER TABLE - modifies a table
# DROP TABLE - deletes a table
# CREATE INDEX - creates an index (search key)
# DROP INDEX - deletes an index
