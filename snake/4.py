import sqlite3

# Function to create a connection to the SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

# Function to create a table for snakes in the SQLite database
def create_snakes_table(conn):
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS snakes
                     (id INTEGER PRIMARY KEY,
                     common_name TEXT NOT NULL,
                     scientific_name TEXT NOT NULL)''')
        conn.commit()
    except Error as e:
        print(e)

# Function to insert data into the snakes table
def insert_snake(conn, common_name, scientific_name):
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO snakes (common_name, scientific_name) VALUES (?, ?)", (common_name, scientific_name))
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)

# Main function to create the database and populate it with snake information
def main():
    database = r"snake_database.db"

    # Create a connection to the SQLite database
    conn = create_connection(database)

    # Create snakes table
    if conn is not None:
        create_snakes_table(conn)
    else:
        print("Error! cannot create the database connection.")

    # Insert data into the snakes table
    with conn:
        insert_snake(conn, "Cobra", "Naja naja")
        insert_snake(conn, "Russell's Viper", "Daboia russelii")
        insert_snake(conn, "Indian Python", "Python molurus")
        insert_snake(conn, "Spectacled Cobra", "Naja naja")
        # Add more snake information as needed

    conn.close()

# Run the main function to create the database and populate it with snake information
if __name__ == '__main__':
    main()
