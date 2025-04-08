import sqlite3
from tabulate import tabulate

def create_database(db_name):
    try:
        conn = sqlite3.connect(db_name)
        print(f"Database '{db_name}' created successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def create_table(db_name, table_name, columns):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        columns_def = ', '.join(columns.values())  # Sudah berisi semua definisi lengkap
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_def})"
        cursor.execute(sql)
        conn.commit()
        print(f"Table '{table_name}' created successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def insert_data(db_name, table_name, data):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?' for _ in data.values()])
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cursor.execute(sql, tuple(data.values()))
        conn.commit()
        print("Data inserted successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def view_table(db_name, table_name):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        if not cursor.fetchone():
            print(f"Table '{table_name}' does not exist.")
            return
        
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        if not rows:
            print(f"Table '{table_name}' is empty.")
        else:
            print(f"Contents of '{table_name}' table:")
            headers = [desc[0] for desc in cursor.description]
            print(tabulate(rows, headers=headers, tablefmt="grid"))
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def list_tables(db_name):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        if tables:
            print("Tables in the database:")
            print(tabulate(tables, headers=["Table Name"], tablefmt="grid"))
        else:
            print("No tables found in the database.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def get_column_definitions():
    columns = {}
    more_columns = True
    while more_columns:
        col_name = input("Enter column name: ")
        col_type = input("Enter column type (e.g., TEXT, INTEGER, REAL): ")
        constraints = []
        
        if input("Is this column a primary key? (yes/no): ").lower() == 'yes':
            constraints.append('PRIMARY KEY')
        if input("Should this column be not null? (yes/no): ").lower() == 'yes':
            constraints.append('NOT NULL')
        if input("Should this column be unique? (yes/no): ").lower() == 'yes':
            constraints.append('UNIQUE')
        default_value = input("Enter default value (or press Enter to skip): ")
        if default_value:
            constraints.append(f'DEFAULT {default_value}')
        check_constraint = input("Enter CHECK constraint (or press Enter to skip): ")
        if check_constraint:
            constraints.append(f'CHECK ({check_constraint})')
        
        column_definition = f"{col_name} {col_type} " + ' '.join(constraints)
        columns[col_name] = column_definition.strip()
        
        more_columns = input("Do you want to add another column? (yes/no): ").lower() == 'yes'
    
    print("\nColumn Definitions:")
    table = [[col_name, col_def] for col_name, col_def in columns.items()]
    print(tabulate(table, headers=["Column Name", "Definition"], tablefmt="grid"))
    
    return columns

def main_menu():
    while True:
        print("\nSQLite Manager")
        print("1. Create Database")
        print("2. Create Table")
        print("3. Insert Data")
        print("4. View Table")
        print("5. List Tables")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            db_name = input("Enter the database name: ")
            create_database(db_name)
        elif choice == '2':
            db_name = input("Enter the database name: ")
            table_name = input("Enter the table name: ")
            columns = get_column_definitions()
            create_table(db_name, table_name, columns)
        elif choice == '3':
            db_name = input("Enter the database name: ")
            table_name = input("Enter the table name: ")
            try:
                conn = sqlite3.connect(db_name)
                cursor = conn.cursor()
                cursor.execute(f"PRAGMA table_info({table_name})")
                columns = [col[1] for col in cursor.fetchall()]
            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
                continue
            finally:
                conn.close()
            
            data = {}
            for col_name in columns:
                value = input(f"Enter value for column '{col_name}': ")
                data[col_name] = value
            insert_data(db_name, table_name, data)
        elif choice == '4':
            db_name = input("Enter the database name: ")
            table_name = input("Enter the table name: ")
            view_table(db_name, table_name)
        elif choice == '5':
            db_name = input("Enter the database name: ")
            list_tables(db_name)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main_menu()