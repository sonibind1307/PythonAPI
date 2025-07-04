from repository.test_repository import TestRepository

class TestService:
    def __init__(self):
        self.repo = TestRepository()

    def create_test(self, test):
        test_data = (
            test.name,
            test.description,
            test.parameters
        )
        return self.repo.create_test(test_data)

    def get_all_tests(self):
        return self.repo.get_all_tests()

    def get_test_by_id(self, test_id):
        return self.repo.get_test_by_id(test_id)

    def update_test(self, test_id, test):
        current = self.repo.get_test_by_id(test_id)
        if not current:
            return None

        updated = (
            test.name or current['name'],
            test.description or current['description'],
            test.parameters or current['parameters']
        )
        self.repo.update_test(test_id, updated)
        return self.repo.get_test_by_id(test_id)

    def delete_test(self, test_id):
        self.repo.delete_test(test_id)
