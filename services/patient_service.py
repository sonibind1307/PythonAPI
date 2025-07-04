from repository.patient_repository import PatientRepository

class PatientService:
    def __init__(self):
        self.repo = PatientRepository()

    def create_patient(self, patient):
        balance = (patient.total_amount or 0) - (patient.paid_amount or 0)
        patient_data = (
            patient.name, patient.last_name, patient.dob, patient.age, patient.gender,
            patient.mobile, patient.email, patient.refere_by_doctor, patient.consultant,
            patient.total_amount, patient.paid_amount, balance,
            patient.discount, patient.other_amount, patient.remark
        )
        return self.repo.create_patient(patient_data, patient.test_list)
    
    def get_all_patients(self):
        return self.repo.get_all_patients()
    
    def get_all_patients(self):
        return self.repo.get_all_patients()

    def get_patient_by_id(self, patient_id):
        return self.repo.get_patient_by_id(patient_id)

    def update_patient(self, patient_id, patient):
        current = self.repo.get_patient_by_id(patient_id)
        if not current:
            return None
        updated = (
            patient.name or current['name'],
            patient.last_name or current['last_name'],
            patient.dob or current['dob'],
            patient.age or current['age'],
            patient.gender or current['gender'],
            patient.mobile or current['mobile'],
            patient.email or current['email'],
            patient.refere_by_doctor or current['refere_by_doctor'],
            patient.consultant or current['consultant'],
            patient.total_amount or current['total_amount'],
            patient.paid_amount or current['paid_amount'],
            patient.balance_amount or current['balance_amount'],
            patient.discount or current['discount'],
            patient.other_amount or current['other_amount'],
            patient.remark or current['remark']
        )
        self.repo.update_patient(patient_id, updated, patient.test_list or current['test_list'])
        return self.repo.get_patient_by_id(patient_id)

    def delete_patient(self, patient_id):
        self.repo.delete_patient(patient_id)

        