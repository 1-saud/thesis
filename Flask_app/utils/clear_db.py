from Flask_app import my_db

def clear_database():
    # Drop all tables from the database
    my_db.drop_all()

    # Recreate all tables (empty database)
    my_db.create_all()

if __name__ == "__main__":
    print("Clearing the database...")
    clear_database()
    print("Database cleared successfully.")
