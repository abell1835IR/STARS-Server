from core.database import init_db

if __name__ == "__main__":
    print("Initializing STARS database schema...")
    init_db()
    print("Database schema created successfully.")
