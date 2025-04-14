import sqlite3

def connectDb(dbName):
    # connectDb to the SQLite database and returns the dbConnection and dbExecute
    try:
        dbConnection = sqlite3.dbConnectionect(dbName)
        dbExecute = dbConnection.dbExecute()
        return dbConnection, dbExecute
    except sqlite3.Error as e:
        print(f"Database connectDb error: {e}")
        return None, None

def getTableNames(dbExecute):
    # Returns a list of table names in the database
    dbExecute.execute("Select name FROM sqlite_master WHERE type='table';")
    return [table[0] for table in dbExecute.fetchall()]

def getKey(dbExecute, tableName):
    # Returns the key column name for the given table
    dbExecute.execute(f"PRAGMA table_info({tableName})")
    for column in dbExecute.fetchall():
        if column[5]:  # column[5] is 'pk'
            return column[1]  # column[1] is the name
    return None

def displayTable(dbExecute, tableName):
    # Displays all rows of the selected table with column headers and row numbers
    try:
        dbExecute.execute(f"SELECT * FROM {tableName}")
        rows = dbExecute.fetchall()
        columns = [desc[0] for desc in dbExecute.description]

        colWidths = [len(col) for col in columns]
        for row in rows:
            for i, cellValue in enumerate(row):
                colWidths[i] = max(colWidths[i], len(str(cellValue)))

        print("\nRow | " + " | ".join(col.ljust(colWidths[i]) for i, col in enumerate(columns)))
        print("-" * (6 + sum(colWidths) + 3 * (len(columns) - 1)))

        for rowIndex, row in enumerate(rows):
            print(str(rowIndex+1).rjust(3) + " | " + " | ".join(str(cellValue).ljust(colWidths[i]) for i, cellValue in enumerate(row)))
    except sqlite3.Error as e:
        print(f"Error reading table {tableName}: {e}")

def insertRecord(dbExecute, dbConnection, tableName):
    # Inserts a new record into the table using what the user gave 
    try:
        dbExecute.execute(f"PRAGMA table_info({tableName})")
        columnsInfo = dbExecute.fetchall()
        columns = [col[1] for col in columnsInfo]

        print(f"\nEnter values for new {tableName} record:")
        values = []
        for col in columns:
            val = input(f"{col}: ")
            values.append(val)

        placeholders = ', '.join(['?'] * len(values))
        dbExecute.execute(f"INSERT INTO {tableName} VALUES ({placeholders})", values)
        dbConnection.commit()
        print("Record inserted successfully.")
    except sqlite3.Error as e:
        print(f"Insert failed: {e}")

def updateRecord(dbExecute, dbConnection, tableName):
     # Updates a field in a selected record using the key. 
    try:
        displayTable(dbExecute, tableName)
        Key = getKey(dbExecute, tableName)
        if not Key:
            print("Unable to identify key.")
            return

        recordId = input(f"\nEnter {Key} of the record to update: ")
        field = input("Enter the column name to update: ")
        newValue = input("Enter the new value: ")

        dbExecute.execute(f"UPDATE {tableName} SET {field} = ? WHERE {Key} = ?", (newValue, recordId))
        dbConnection.commit()
        print("Record updated successfully.")
    except sqlite3.Error as e:
        print(f"Update failed: {e}")

def deleteRecord(dbExecute, dbConnection, tableName):
     # Deletes a record using the key. 
    try:
        displayTable(dbExecute, tableName)
        Key = getKey(dbExecute, tableName)
        if not Key:
            print("Unable to identify key.")
            return

        recordId = input(f"\nEnter {Key} of the record to delete: ")
        dbExecute.execute(f"Delete from {tableName} where {Key} = ?", (recordId,))
        dbConnection.commit()
        print("Record deleted.")
    except sqlite3.Error as e:
        print(f"An error happened when deleting: {e}")

def modifyTable(dbExecute, dbConnection, tableName):
     # Handles insert, update, and delete operations. 
    print("\nChoose an operation: (I)nsert, (U)pdate, (D)elete, (Q)uit")
    userInput = input("Your userInput: ").strip().lower()
    if userInput == 'i':
        insertRecord(dbExecute, dbConnection, tableName)
    elif userInput == 'u':
        updateRecord(dbExecute, dbConnection, tableName)
    elif userInput == 'd':
        deleteRecord(dbExecute, dbConnection, tableName)
    elif userInput == 'q':
        return
    else:
        print("Invalid userInput.")

def main():
    dbName = "Northwind.sqlite"
    dbConnection, dbExecute = connectDb(dbName)
    if not dbConnection:
        return

    while True:
        print("\n Northwind Database ")
        tables = getTableNames(dbExecute)
        for rowIndex, name in enumerate(tables):
            print(f"{rowIndex + 1}. {name}")
        print("Exit")

        try:
            userInput = int(input("\nSelect a table by number: "))
            if userInput == 0:
                break
            tableName = tables[userInput - 1]
            displayTable(dbExecute, tableName)

            if tableName in ["Customers", "Employees", "Products"]:
                modifyTable(dbExecute, dbConnection, tableName)

        except (ValueError, IndexError):
            print("Invalid selection. Try again.")

    dbConnection.close()
    print("dbConnectionection closed.")

if __name__ == "__main__":
    main()
