class DbClass:
    def __init__(self):
        import mysql.connector as connector

        self.__dsn = {
            "host": "localhost",
            "user": "testconnect",
            "passwd": "testconnect",
            "db": "HomeSecurity"
        }

        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()

    def getlocaties(self):
        # Query zonder parameters
        sqlQuery = "SELECT * FROM locatie"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result
    def getlogs(self):
        # Query zonder parameters
        sqlQuery = "SELECT * FROM logs"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getcomments(self):
        # Query zonder parameters
        sqlQuery = "SELECT * FROM comments"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def gettypes(self):
        # Query zonder parameters
        sqlQuery = "SELECT * FROM types"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getusers(self):
        # Query zonder parameters
        sqlQuery = "SELECT * FROM users"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getDataFromDatabaseMetVoorwaarde(self, voorwaarde):
        # Query met parameters
        sqlQuery = "SELECT * FROM tablename WHERE columnname = '{param1}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=voorwaarde)
        
        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getuser(self, username, password):
        # Query met parameters
        sqlQuery = "SELECT * FROM users WHERE Username = '{param1}' and Password = '{param2}' "
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=username, param2=password)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result


    def setcomments(self, Naam, Voornaam, bericht):
        # Query met parameters
        sqlQuery = "INSERT INTO comments (Naam, Voornaam, Bericht) VALUES ('{param1}','{param2}','{param3}')"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=Naam, param2=Voornaam, param3=bericht)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def insertlog(self, LOCID, Tijdstip, Tp, File):
        # Query met parameters
        sqlQuery = "INSERT INTO logs (LOCID, Tijdstip, Tp, File) VALUES ('{param1}','{param2}','{param3}','{param4}')"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=LOCID, param2=Tijdstip, param3=Tp, param4=File)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def delcomment(self, COID):
        # Query met parameters
        sqlQuery = "DELETE FROM comments WHERE COID = '{param1}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=COID)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def dellog(self, LogID):
        # Query met parameters
        sqlQuery = "DELETE FROM logs WHERE LogID = '{param1}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=LogID)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def deluser(self, USERID):
        # Query met parameters
        sqlQuery = "DELETE FROM users WHERE USERID = '{param1}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=USERID)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def dellocatie(self, LOID):
        # Query met parameters
        sqlQuery = "DELETE FROM locatie WHERE LOID = '{param1}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=LOID)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def getlog(self, LogID):

        sqlQuery = "SELECT * FROM logs WHERE LogID = '{param1}'"
        sqlCommand = sqlQuery.format(param1=LogID)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def updatelog(self, LogID, notitie, belang):

        sqlQuery = "UPDATE logs SET Notitie = '{param2}', Belangrijk = '{param3}' WHERE LogID = '{param1}'"
        sqlCommand = sqlQuery.format(param1=LogID, param2=notitie, param3=belang)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()