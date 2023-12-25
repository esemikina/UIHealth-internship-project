from sqlite3 import Error
from constants import TABLE_NAME
from bitcoin_timestamp import BitcoinTimestamp
from custom_util import create_database

class DatabaseConnection:

    def __init__(self):
        """
        class constructor: generates a database connection object
        """
        self.__db = create_database()

    def insert_timestamp(self, bitcoin: BitcoinTimestamp):
        """
        inserts a bitcoin timestamp into the database

        :param bitcoin_timestamp:
            the bitcoin timestamp
        :type bitcoin_timestamp:
            BitcoinTimestamp
        :return:
            boolean indicating if the operation was successful or not
        :rtype:
            bool
        """
        try:
            # get cursor
            cursor = self.__db.cursor()
        except Error as e:
            print(e)
            return False

        try:
            # TODO (5.3.2)  
            # insert sql query
            query = "INSERT INTO {} VALUES (?, ?)".format(TABLE_NAME)

            # execute sql query
            cursor.execute(query, (bitcoin.timestamp, bitcoin.price))

            # commit
            self.__db.commit()

            # close
            cursor.close()

            return True
        except Exception as e:
            print(e)
            return False
      
    def get_all_timestampes(self):
        """
        gets all bitcoin timestamps in the database

        :return:
            a list of bitcoin timestamps
        :rtype:
            list[BitcoinTimestamp]
        """
        try:
            output = []
            
            # TODO (5.3.1)
            # get cursor
            cursor = self.__db.cursor()
            
            # insert sql query
            query = "SELECT * FROM {};".format(TABLE_NAME)

            # execute sql query
            cursor.execute(query)

            # fetch all results obtained
            res = cursor.fetchall()

            # close
            cursor.close()

            # convert results to BitcoinTimestamp objects and append to output
            for result in res:
                timestamp = result[0]   # replace with the actual name of the timestamp field in your query results
                price = result[1]   # replace with the actual name of the price field in your query results
                bitcoin_timestamp = BitcoinTimestamp(timestamp, price)
                output.append(bitcoin_timestamp.to_json())
                
            return output
        except Error as e:
            print(e)
            return []