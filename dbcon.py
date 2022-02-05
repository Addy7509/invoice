class DBcon:
    def __init__(self):
        import mysql.connector
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "invoice_1"
        )
        self.mycursor = self.mydb.cursor()
        #heheheheheheh 