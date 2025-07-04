from core.database import get_connection

class PatientRepository:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor(dictionary=True)

    def create_patient(self, patient_data, test_list):
        insert_query = """
            INSERT INTO patients (name, last_name, dob, age, gender, mobile, email, refere_by_doctor, consultant,
                                  total_amount, paid_amount, balance_amount, discount, other_amount, remark)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(insert_query, patient_data)
        patient_id = self.cursor.lastrowid

        for test_id in test_list:
            self.cursor.execute(
                "INSERT INTO patient_tests (patient_id, test_id) VALUES (%s, %s)",
                (patient_id, test_id)
            )
        self.conn.commit()
        return patient_id
    
    def get_all_patients(self):
        self.cursor.execute("SELECT p.*, GROUP_CONCAT(pt.test_id) AS test_list FROM patients p LEFT JOIN patient_tests pt ON p.id = pt.patient_id GROUP BY p.id")
        rows = self.cursor.fetchall()
        for row in rows:
            if row['test_list']:
                [int(x) for x in row['test_list'].split(',')]
            else:
                row['test_list'] = []    
        return rows
    
    def get_patient_by_id(self, patient_id):
        self.cursor.execute("""
            SELECT p.*,
                GROUP_CONCAT(pt.test_id) AS test_list
            FROM patients p
            LEFT JOIN patient_tests pt ON p.id = pt.patient_id
            WHERE p.id = %s
            GROUP BY p.id
        """, (patient_id,))
        row = self.cursor.fetchone()
        if row:
            row['test_list'] = [int(x) for x in row['test_list'].split(',')] if row['test_list'] else []
        return row
    
    def update_patient(self, patient_id, update_data, test_list):
        self.cursor.execute("""
            UPDATE patients SET name=%s, last_name=%s, dob=%s, age=%s, gender=%s, 
                mobile=%s, email=%s, refere_by_doctor=%s, consultant=%s, total_amount=%s,
                paid_amount=%s, balance_amount=%s, discount=%s, other_amount=%s, remark=%s
            WHERE id=%s
        """, (*update_data, patient_id))

        # Update patient tests: remove old, insert new
        self.cursor.execute("DELETE FROM patient_tests WHERE patient_id = %s", (patient_id,))
        for test_id in test_list:
            self.cursor.execute("""
                INSERT INTO patient_tests (patient_id, test_id) VALUES (%s, %s)
            """, (patient_id, test_id))

        self.conn.commit()

    def delete_patient(self, patient_id):
        self.cursor.execute("DELETE FROM patient_tests WHERE patient_id = %s", (patient_id,))
        self.cursor.execute("DELETE FROM patients WHERE id = %s", (patient_id,))
        self.conn.commit()
