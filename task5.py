const_hour = 40

class Employee:
    def __init__(self, name, pin, hour) -> None:
        self.name = name
        self.pin = pin
        self.hour = hour

    def calc_salary(self):
        pass

    def total_salary(self):
        pass

    def calc_perfomance(self):
        return (self.hour * 100) / const_hour

class Manager(Employee):
    def __init__(self, name, pin, hour, salary) -> None:
        super().__init__(name, pin, hour)
        self.salary = salary

    def calc_salary(self):
        return self.salary

class Secretary(Employee):
    def __init__(self, name, pin, hour, salary) -> None:
        super().__init__(name, pin, hour)
        self.salary = salary

    def calc_salary(self):
        return self.salary

class SalesPerson(Employee):
    def __init__(self, name, pin, hour, sell_count, salary) -> None:
        super().__init__(name, pin, hour)
        self.sell_count = sell_count
        self.salary = salary

    def calc_salary(self):
        return self.salary + (self.sell_count*50)

class CexEmployee(Employee):
    def __init__(self, name, pin, hour) -> None:
        super().__init__(name, pin, hour)

    def calc_salary(self):
        self.salary = self.hour * 100
        return self.salary

class SecretaryZamena(Employee):
    def __init__(self, name, pin, hour) -> None:
        super().__init__(name, pin, hour)

    def calc_salary(self):
        self.salary = self.hour * 100
        return self.salary

manager = Manager(
    "Barsbek Kanatkulov",
    1,
    18,
    45000
)
secretary = Secretary(
    "Alymkul",
    2, 
    38,
    20000
)
sales_person = SalesPerson(
    "Aypery",
    3,
    38,
    20,
    20000
)
cex = CexEmployee(
    "Bakyt",
    4,
    25
)
cex2 = CexEmployee(
    "Altynay",
    5,
    40
)
zamena = SecretaryZamena(
    "Janar",
    6, 
    33
)
personal = [
    manager,
    secretary,
    sales_person,
    cex,
    cex2,
    zamena
    ]

def spend_comp_money():
    total_money = sum([
        person.calc_salary() for person in personal
        ])
    return f"total salary - {total_money}"

def print_info():
    total = spend_comp_money()

    for person in personal:
        print(
            f"ID - {person.pin}, Name - {person.name} Salary - {person.salary} Perfomance - {person.calc_perfomance()}",
            end="\n"
        )
    return total

print_info()
