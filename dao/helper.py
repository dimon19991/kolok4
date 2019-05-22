from dao.credentials import *
import cx_Oracle

def delUser(AGE, NAME):

    connection = cx_Oracle.connect('"Dima"', '01200120', "localhost:1521/xe")
    cursor = connection.cursor()

    status = cursor.var(cx_Oracle.STRING)

    cursor.callproc("USER_DELL.NEW_USER", [status, AGE, NAME])
    cursor.close()
    connection.close()

    return status.getvalue()



# if __name__ == "__main__":
  #   print(delUser(20, "Dimass"))
