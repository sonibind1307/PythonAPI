from core.database import get_connection

class DoctorRepository:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor(dictionary=True)

    def create_doctor(self, doctor_data):
        self.cursor.execute(
            "INSERT INTO doctors (name, designation, degree, mobile) VALUES (%s, %s, %s, %s)",
            doctor_data
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def get_all_doctors(self):
        self.cursor.execute("SELECT * FROM doctors")
        return self.cursor.fetchall()

    def get_doctor_by_id(self, doctor_id):
        self.cursor.execute("SELECT * FROM doctors WHERE id = %s", (doctor_id,))
        return self.cursor.fetchone()

    def update_doctor(self, doctor_id, update_data):
        self.cursor.execute("""
            UPDATE doctors SET name=%s, designation=%s, degree=%s, mobile=%s WHERE id=%s
        """, (*update_data, doctor_id))
        self.conn.commit()

    def delete_doctor(self, doctor_id):
        self.cursor.execute("DELETE FROM doctors WHERE id = %s", (doctor_id,))
        self.conn.commit()
