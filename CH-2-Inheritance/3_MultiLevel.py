class comapany:

    title:str = "Consultancy"

    def __init__(self, company_name:str):
        self.company_name = company_name

    def info(self):
        return f"works at Company Name: {self.company_name}"
# obj=comapany("Tech Solutions")
# obj.info()

class employee(comapany):
    def __init__(self, employee_name:str, company_name:str):
        self.employee_name = employee_name
        self.company_name = company_name

    def info(self):
        response = comapany.info(self)
        return f"The employee: {self.employee_name}, {response}"

# obj = employee("Satya", "Claude")
# obj.info()

class contractor(employee):
    def __init__(self, contractor_name:str, company_name:str, employee_name:str):
        self.contractor_name = contractor_name
        self.company_name = company_name
    def info(self):
        response = employee.info(self)
        print(f"The contractor: {self.contractor_name}, {response}")

obj = contractor("John","langchain")
obj.info()