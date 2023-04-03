from mysql.connector import connect, errors


class DbHandler:
    def __init__(self, creds):
        # get credentials like this
        db_host = creds.get('mysql', 'host')
        db_user = creds.get('mysql', 'user')
        db_password = creds.get('mysql', 'password')
        db_database = creds.get('mysql', 'database')

        self.conn = connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database
        )
        self.curs = self.conn.cursor()

    def run_query(self, query):
        """
        run sql query on database with no return value
        :param query:
        :return: True: if query succeeds, else False
        """
        # TODO fix return values
        try:
            self.curs.execute(query)
            return True
        except Exception as e:
            print(f'Query failed. reasons = {e}')
            return False

    def run_query_return(self, query):
        """
        run sql query on database and return query results

        :param query:
        :return: Query result, else None if query fails
        """
        try:
            self.curs.execute(query)
            result = self.curs.fetchall()
            return result
        except Exception as e:
            return False

    def close(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()