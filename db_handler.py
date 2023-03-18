

class DbHandler:
    def __init__(self, creds):
        pass
        # get credentials like this
        # db_host = creds.get('mysql', 'host')
        # db_password = creds.get('mysql', 'password')

        # self.conn = SETUP DATABASE CONNECTION HERE

    def run_query(self, query):
        """
        run sql query on database with no return value

        :param query:
        :return: True: if query succeeds, else False
        """

    def run_query_return(self, query):
        """
        run sql query on database and return query results

        :param query:
        :return: Query result, else None if query fails
        """

    def close(self):
        pass
        # CLOSE DATABASE CONNECTION HERE

