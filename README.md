# SQLite Manager

SQLite Manager is a Python program that provides a command-line interface for managing SQLite databases. It allows users to create databases and tables, insert and update data, view table contents, and list all tables within a database.

## Features

- Create a new SQLite database
- Create tables with customizable columns
- Insert data into tables
- Update existing data in tables
- View the contents of a table
- List all tables in the database

## Requirements

- Python 3.x
- `tabulate` library (can be installed via `pip install tabulate`)

## Usage

1. **Run the Program:**
   ```bash
   python sqlite_manager.py
   ```

2. **Select an Option:**
   - 1: Create Database
   - 2: Create Table
   - 3: Insert Data
   - 4: Update Data
   - 5: View Table
   - 6: List Tables
   - 7: Exit

3. **Follow the Prompts:**
   - Enter the necessary information as prompted by the program.

## Functions

- `create_database(db_name)`: Creates a new SQLite database.
- `create_table(db_name, table_name, columns)`: Creates a new table with specified columns.
- `insert_data(db_name, table_name, data)`: Inserts data into the specified table.
- `update_data(db_name, table_name)`: Updates data in the specified table.
- `view_table(db_name, table_name)`: Views the contents of the specified table.
- `list_tables(db_name)`: Lists all tables in the specified database.
- `get_column_definitions()`: Helps user define columns for a new table.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
