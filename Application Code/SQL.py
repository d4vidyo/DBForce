import psycopg2

class connection():
    def __init__(self):
        self.connection = None
        self.settings= None


    def getCurrentSchema(self):
        return self.quary("SELECT current_schema()")

    def getAllSchema(self):
        return self.quary("SELECT nspname FROM pg_namespace")

    def getAllTables(self):
        quary = """
        SELECT t.table_name, c.column_name
        FROM information_schema.tables t
        JOIN information_schema.columns c ON t.table_name = c.table_name
        WHERE t.table_schema = """+self.settings.Schema +"""
        ORDER BY t.table_name, c.ordinal_position
        """
        return self.quary(quary)

    def get(self):
        return self.quary("select * from event order by id")

    def quary(self, string):        
        cursor = self.connection.cursor()
        try:
            cursor.execute("SET search_path TO " + self.settings.Schema)
            cursor.execute(string)
            headers = [desc[0] for desc in cursor.description]
            data = cursor.fetchall()
        except(Exception) as e:
            print(e)
            cursor.close()
            return[(),((),())]
    
        cursor.close()
        return [headers, data]
    

    def connect(self, settings):
        self.settings = settings
        try:
            self.connection = psycopg2.connect(
                host = settings.host,
                database = settings.DB,
                user = settings.user,
                password = settings.pw)
        except(Exception) as e:
            print(e)
            return None
        return 1

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            