import cx_Oracle

class update:
    def __init__(self):
        self.db = cx_Oracle.connect('"Dima"', '01200120', "localhost:1521/xe")

    def delUser(self, NAME, POPULATION):

        #connection = cx_Oracle.connect('"Dima"', '01200120', "localhost:1521/xe")
        cursor = self.db.cursor()

        status = cursor.var(cx_Oracle.STRING)
        NAME_D = cursor.var(cx_Oracle.STRING)

        cursor.callproc("COUNTRY_APDATE.apdate", [status, NAME, POPULATION])
        cursor.close()
        self.db.close()

        return status.getvalue()
