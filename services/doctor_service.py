from repository.doctor_repository import DoctorRepository

class DoctorService:
    def __init__(self):
        self.repo = DoctorRepository()

    def create_doctor(self, doctor):
        doctor_data = (
            doctor.name,
            doctor.designation,
            doctor.degree,
            doctor.mobile
        )
        return self.repo.create_doctor(doctor_data)

    def get_all_doctors(self):
        return self.repo.get_all_doctors()

    def get_doctor_by_id(self, doctor_id):
        return self.repo.get_doctor_by_id(doctor_id)

    def update_doctor(self, doctor_id, doctor):
        # Get current doctor to fill missing fields
        current = self.repo.get_doctor_by_id(doctor_id)
        if not current:
            return None
        updated = (
            doctor.name or current['name'],
            doctor.designation or current['designation'],
            doctor.degree or current['degree'],
            doctor.mobile or current['mobile'],
        )
        self.repo.update_doctor(doctor_id, updated)
        return self.repo.get_doctor_by_id(doctor_id)

    def delete_doctor(self, doctor_id):
        self.repo.delete_doctor(doctor_id)
