from abc import abstractmethod,ABC


class EmployeeService(ABC):

    @abstractmethod
    def add_new_employee(self):
        pass

    @abstractmethod
    def search_employee_by_id(self):
        pass

    @abstractmethod
    def get_all_employees(self):
        pass

    @abstractmethod
    def search_employee_by_email(self):
        pass

    @abstractmethod
    def delete_employee(self):
        pass

    @abstractmethod
    def update_employee(self):
        pass


