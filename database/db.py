# Se necesitan ciertos parámetros, como los que usamos para el Workbench
import pymysql

host = "inst-db.c1iac8cy2hmh.us-east-2.rds.amazonaws.com"
user = "daniel"
password = "!Nihonikimasu25."
db_name = "db_finanzas"

def connection_SQL():
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        print("Connection to database successful")
        return connection
    except Exception as e:
        print("Error connecting to the database:", e)
        return None

def insert_purchase(purchase_date, category, amount):
    try:
        connection = connection_SQL()
        if connection:
            cursor = connection.cursor()
            # SQL query to insert data into the purchases table
            query = "INSERT INTO purchases (purchase_date, category, amount) VALUES (%s, %s, %s)"
            cursor.execute(query, (purchase_date, category, amount))
            connection.commit()
            cursor.close()
            connection.close()
            print("Purchase added successfully")
            return True
        else:
            return False
    except Exception as e:
        print("Error inserting data:", e)
        return False

