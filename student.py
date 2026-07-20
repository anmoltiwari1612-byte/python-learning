class employee:
    def __init__(self, name, age, department, salary):
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary
    def display_info(self):
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")
            print(f"Department: {self.department}")
            print(f"Salary: {self.salary}")

emp = employee("Anmol", 25, "IT", 50000)
                           
emp.display_info()