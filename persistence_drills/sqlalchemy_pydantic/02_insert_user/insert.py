from models import User, SessionLocal

def insert_sample_user():
    session = SessionLocal()
    try:
        user = User(name="Alice", email="alice@example.com")
        session.add(user)
        session.commit()
        print("User inserted.")
    except Exception as e:
        session.rollback()
        print("Error inserting user:", e)
    finally:
        session.close()

if __name__ == "__main__":
    insert_sample_user()
