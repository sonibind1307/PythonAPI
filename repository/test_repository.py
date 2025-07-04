from core.database import get_connection

class TestRepository:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor(dictionary=True)

    def create_test(self, test_data):
        self.cursor.execute(
            "INSERT INTO tests (name, description, parameters) VALUES (%s, %s, %s)",
            test_data
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def get_all_tests(self):
        self.cursor.execute("SELECT * FROM tests")
        return self.cursor.fetchall()

    def get_test_by_id(self, test_id):
        self.cursor.execute("SELECT * FROM tests WHERE id = %s", (test_id,))
        return self.cursor.fetchone()

    def update_test(self, test_id, update_data):
        self.cursor.execute(
            """
            UPDATE tests SET name = %s, description = %s, parameters = %s
            WHERE id = %s
            """,
            (*update_data, test_id)
        )
        self.conn.commit()

    def delete_test(self, test_id):
        self.cursor.execute("DELETE FROM tests WHERE id = %s", (test_id,))
        self.conn.commit()
