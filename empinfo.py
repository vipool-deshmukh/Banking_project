
class Employee:

    def __init__(self,eid,enm,eag,esal,email,erol):
        self.empId  = int(eid)
        self.empName = enm
        self.empAge = int(eag)
        self.empSalary = float(esal)
        self.empEmail = email
        self.empRole = erol

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''\n {self.__dict__}'''