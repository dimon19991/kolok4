import cx_Oracle

class UserHelper:

    def __init__(self):
        self.db = cx_Oracle.connect('"Dima"', '01200120', "localhost:1521/xe")

    def delUser(self, AGE, NAME):

        # connection = cx_Oracle.connect('"Dima"', '01200120', "localhost:1521/xe")
        cursor = self.db.cursor()


        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("USER_DELL.NEW_USER", [status, AGE, NAME])
        cursor.close()
        self.db.close()

        return status.getvalue()



# if __name__ == "__main__":
  #   print(delUser(20, "Dimass"))
