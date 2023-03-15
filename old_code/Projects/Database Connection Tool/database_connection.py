import pyodbc
import logging
from enum import Enum
from typing import Generator

# TODO
"""
Add doc strings 
Add sql sanitation - this is hard to impossible to do with the generic way this is built 
    sanitation utilizes parameters to help build the query string -> SELECT {user} FROM {users} WHERE {username} = '{Max}'
    No this can be done 
    with a little dynamic code with specific in the crud classes 
    -> read(select_param, table, where_clause, optional - group_by, order_by )
        this would implement sanitation while keeping the _execute as is 
        but this is hard to predict what is needed 
        this gets significant harder the more complex the query becomes
            for simple query's this is doable for more complex it is going to be hard 
    
    

"""


class CallType(Enum):
    SELECT = 'SELECT'
    CREATE = 'CREATE'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'
    DROP = 'DROP'


class DatabaseConnectionTool:
    def __init__(self, connection_string=None):
        self._connection = self._create_connection(connection_string)
        self._log = logging.getLogger("Database Connection Tool")  # add the connection string to the logger name?
        # not sure about the instance based logger - getting the logger will intern just get the same one anyway

    def create(self, query_string: str) -> Generator:
        return self._execute(query_string=query_string)

    def update(self, query_string: str) -> Generator:
        return self._execute(query_string=query_string)

    def read(self, query_string: str) -> Generator:
        return self._execute(query_string=query_string)

    def delete(self, query_string: str) -> Generator:
        return self._execute(query_string=query_string)

    def close(self):
        # I would like this to make noise -> return something
        if self._connection is not None:
            self._connection.close()  # should catch a close error and try again 
            self._log.debug('Connection Closed')
            return True
        else:
            self._log.debug("No Connection to close")
            return False  # this could be bad at informing the user

    def _execute(self, query_string: str) -> Generator:

        if self._connection is None:
            raise ValueError("Connection String has not been set")
        try:
            cursor: pyodbc.Cursor
            cursor = self._connection.cursor()
            self._log.debug(f'executing: {query_string}')
            cursor.execute(query_string)
            for value in cursor.fetchall():
                yield value
            cursor.commit()
            cursor.close()
        except pyodbc.Error as err:
            self._log.error(err)
            raise ConnectionError(err)

    def _create_connection(self, connection_string: str) -> pyodbc.connection:
        try:
            connection = pyodbc.connect(
                p_str=connection_string
            )
            if self._connection is None:
                self._log.debug(f'connected to {connection_string}')  # clean this -> connection string will have UsPs
                return connection
            else:
                raise ValueError("Connection is already created please close the connection")
        except ConnectionError as err:
            self._log.error(err)

    @staticmethod
    def sanitized_query_builder(call_type, call_params, table, joins=None, where=None, order_by=None, group_by=None):
        """
        if select, create, update, delete:
            call = select, create, update, or delete

        set call params
        set from params

        if join:
            set join params

        if where, order, and group:
            set where, order, and group

        return query
        """
        query_string = f'{call_type.name}'
        print(query_string)

    @staticmethod
    def drivers():
        """
        Helper function, Checks and returns for the newest SQL database driver.
        """
        found_drivers = pyodbc.drivers()
        return found_drivers[0] if len(found_drivers) >= 1 else "No Driver Found"
