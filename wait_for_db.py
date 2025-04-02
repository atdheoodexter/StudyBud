import time
import psycopg2
from django.db import connections

def wait_for_db():
    """Wait for the database to be available before proceeding."""
    while True:
        try:
            conn = psycopg2.connect(
                dbname="db",
                user="myuser",
                password="password",
                host="db",
                port="5432"
            )
            conn.close()
            print("Database is ready!")
            break
        except psycopg2.OperationalError:
            print("Database unavailable, waiting...")
            time.sleep(3)

if __name__ == "__main__":
    wait_for_db()
