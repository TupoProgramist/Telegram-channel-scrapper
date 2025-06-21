import sqlite3

#+ Retrieve the first row with parsed = 0 and return only the username
def get_unparsed_parent_username(conn):
    # Set row_factory to sqlite3.Row to access the result as a dictionary
    cursor = conn.cursor()
    
    # Select only the username where parsed = 0
    cursor.execute('''
        SELECT username FROM Chats
        WHERE is_parced = 0 AND is_newborn = 0
        LIMIT 1
    ''')
    
    result = cursor.fetchone()  # Fetch the first result
    
    if result:
        return result['username']  # Return the username by dictionary-like reference
    else:
        return None  # Return None if no unparsed child is found

#+ completely resets the Chats table  
def reset_database(conn):
    cursor = conn.cursor()

    # Step 1: Get a list of all table names in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Step 2: For each table, delete all rows
    for table_name in tables:
        table_name = table_name[0]  # Get the table name from the tuple
        if table_name == 'sqlite_sequence':  # Skip the internal sequence table used for AUTOINCREMENT
            continue
        cursor.execute(f"DELETE FROM {table_name};")
    
    # Commit the changes
    conn.commit()

#+ insert found children into the database !parent_username
def insert_child(conn, parent_username, child):
    cursor = conn.cursor()
    #if the child with the same username already exists 
    cursor.execute('SELECT 1 FROM Chats WHERE username = ?', (child.username,))
    if cursor.fetchone():
        return  

    # Insert the child into the Chats table
    cursor.execute('''
        INSERT INTO Chats (id, title, username, participants_count, access_hash, is_megagroup, is_broadcast, is_parced, is_newborn, is_verified)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        child.id,
        child.title,
        child.username,
        getattr(child, 'participants_count', 0),  # Default to 0 if not available
        child.access_hash,
        getattr(child, 'megagroup', False),  # Whether it's a supergroup (megagroup)
        getattr(child, 'broadcast', False),  # Whether it's a broadcast channel
        0,  # is_parced default value
        1,  # is_newborn because it's new
        0   # is_verified default value
    ))

    # Insert the parent-child pair into the recommendations table
    cursor.execute('''
        INSERT INTO recommendations (parent, child)
        VALUES (?, ?)
    ''', (parent_username, child.username))
    # Commit the changes
    conn.commit()

#+ for initial upload of the parents
def initial_parent_upload(conn, parent):
    cursor = conn.cursor()

    # Prepare the SQL insert statement
    insert_query = '''
        INSERT OR IGNORE INTO Chats (id, title, username, participants_count, access_hash, is_megagroup, is_broadcast, is_parced, is_newborn, is_verified)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    
    # Extract relevant fields from the parent Chat object
    chat_data = (
        parent.id,
        parent.title,
        parent.username,
        getattr(parent, 'participants_count', 0),  # Use 0 if participants_count is not available
        parent.access_hash,
        getattr(parent, 'megagroup', False),  # Default to False if not a megagroup
        getattr(parent, 'broadcast', False),  # Default to False if not a broadcast
        0,  # Default value for is_parced
        0,  # Default value for is_newborn
        1   # Default value for is_verified
    )
    
    # Execute the SQL insert
    cursor.execute(insert_query, chat_data)

def update_is_verified(conn, channel_username, is_verified):
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE Chats
        SET is_verified = ?
        WHERE username = ?
    ''', (1 if is_verified else 0, channel_username))
    
    conn.commit()

def get_unvalidated_channel_username(conn):
    # Set row_factory to sqlite3.Row to access the result as a dictionary
    cursor = conn.cursor()

    # Select the first username where is_verified = 0 (unvalidated channel)
    cursor.execute('''
        SELECT username FROM Chats
        WHERE is_verified = 0
        LIMIT 1
    ''')

    result = cursor.fetchone()  # Fetch the first result

    if result:
        return result['username']  # Return the username of the unvalidated channel
    else:
        return None

def get_deleted_channel_username(conn):
    # Set row_factory to sqlite3.Row to access the result as a dictionary
    cursor = conn.cursor()

    # Select the first username where is_verified = 0 (unvalidated channel)
    cursor.execute('''
        SELECT username FROM deleted
        LIMIT 1
    ''')
    result = cursor.fetchone()  # Fetch the first result

    if result:
        return result['username']  # Return the username of the unvalidated channel
    else:
        return None
    
def config_database(conn):
    """
    Rebuilds the Chats table with the `username` column set to NOT NULL.
    """
    cursor = conn.cursor()
    # Step 1: Create a new table with `username` as NOT NULL and PRIMARY KEY
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Chats_new (
            id INTEGER,
            title TEXT,
            username TEXT NOT NULL PRIMARY KEY,
            participants_count INTEGER,
            access_hash INTEGER,
            is_megagroup BOOLEAN,
            is_broadcast BOOLEAN,
            is_parced BOOLEAN DEFAULT 0,
            is_newborn BOOLEAN DEFAULT 1,
            is_verified BOOLEAN DEFAULT 0
        )
    ''')

    # Step 2: Copy data from the old `Chats` table to the new table
    cursor.execute('''
        INSERT OR IGNORE INTO Chats_new (id, title, username, participants_count, access_hash, is_megagroup, is_broadcast, is_parced, is_newborn, is_verified)
        SELECT id, title, username, participants_count, access_hash, is_megagroup, is_broadcast, is_parced, is_newborn, is_verified
        FROM Chats
    ''')

    # Step 3: Drop the old `Chats` table
    cursor.execute('DROP TABLE Chats')

    # Step 4: Rename the new table to `Chats`
    cursor.execute('ALTER TABLE Chats_new RENAME TO Chats')

    # Commit the changes and close the connection
    conn.commit()