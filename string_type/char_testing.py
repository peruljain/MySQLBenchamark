import mysql.connector
from datetime import datetime
import time


# Database configuration
db_config = {
    'user': 'root',
    'password': 'root_password',
    'host': 'localhost',
    'database': 'benchmark_db',
    'auth_plugin': 'caching_sha2_password'
}

# Connect to the database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# SQL query to insert data
insert_query = "INSERT INTO benchmark_char (char_column) VALUES (%s)"

start_time = time.time()

# Insert 10000 entries
for _ in range(100000):
    cursor.execute(insert_query, ('Hello',))

# Commit the transaction
conn.commit()

# Stop the timer
end_time = time.time()

# Calculate total time taken
total_time = end_time - start_time

# Close the cursor and connection
cursor.close()
conn.close()

print(f"Inserted 10000 entries into the benchmark_datetime table in {total_time:.2f} seconds.")