from abc import ABCMeta, abstractmethod, abstractstaticmethod


class IDepartment(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, employees):
        """ implement in child class """

    @abstractstaticmethod
    def print_department(self):
        """ implement in child class """


class Accounting(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Accounting: {self.employees}")


class Development(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Development: {self.employees}")


class ParentDepartment(IDepartment):

    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add(self, dept):
        self.sub_depts.append(dept)
        self.employees += dept.employees

    def print_department(self):
        print(f"ParentDepartment: {self.base_employees}")

        for depth in self.sesub_depts:
            depth.print_department()

        print(f"Total number of employees: {self.employees}")


dept1 = Accounting(100)
dept2 = Development(200)

parent_dept = ParentDepartment(30)
parent_dept.add(dept1)
parent_dept.add(dept2)

parent_dept.print_department()
