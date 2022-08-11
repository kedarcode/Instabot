import psycopg2


class PostgresDatabase:
    def __init__(self, **args):
        self.database = args['database']
        self.user = args['user']
        self.password = args['password']
        self.host = args['host']
        self.port = args['port']

    def create_cursor(self):
        print(self.database, self.user, self.password, self.host, self.port)
        conn = psycopg2.connect(
            database=self.database, user=self.user, password=self.password, host=self.host, port=self.port
        )
        conn.autocommit = True
        cursor = conn.cursor()
        return cursor

    def insert(self, table: str, column: list, values: list):
        cursor = self.create_cursor()
        query_val = ''
        query_col = ''
        for val in values:
            if type(val) == str:
                if query_val == '':
                    query_val = f"'{val}'"
                else:
                    query_val = f"{query_val},'{val}'"
            elif type(val) == set:
                val = str(val).replace("'", '"')
                if query_val == '':
                    query_val = f"'{val}'"
                else:
                    query_val = f"{query_val},'{val}'"
            else:
                if query_val == '':
                    query_val = f"{val}"
                else:
                    query_val = f"{query_val},{val}"
        for col in column:
            if query_col == '':
                query_col = f'"{col}"'
            else:
                query_col = f'{query_col},"{col}"'
        query = f'INSERT INTO public."{table}" ({query_col}) '\
                f'VALUES ({query_val})'
        print(query)
        print(cursor.execute(query))

    def select(self):
        cursor = self.create_cursor()
        cursor.execute('SELECT * FROM public."Niches"')
        return cursor.fetchall()


obj = PostgresDatabase(database="Socialbot", user='postgres', password='kedar2323',
                       host='127.0.0.1', port='5432')

