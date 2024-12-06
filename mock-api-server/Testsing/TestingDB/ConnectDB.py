import psycopg2

try:
    conn = psycopg2.connect(
        dbname="mockdb",
        user="anton",
        password="password",
        host="localhost",
        port="5432"
    )
    print("Connected to the database!")
except Exception as e:
    print(f"Database connection error: {e}")
