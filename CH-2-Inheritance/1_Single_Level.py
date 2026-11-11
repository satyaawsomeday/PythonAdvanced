class company:

    company_name = "consutancy"

    def __init__(self, company_name):
        self.company_name = company_name
     

    def display_info(self):
        return f"works at Company Name: {self.company_name}"
# obj=company("Tech Solutions")
# obj.display_info()

class employee(company):
    def __init__(self,employee_name, company_name):
        self.employee_name=employee_name
        self.company_name=company_name

    def employee_info(self):
        response = company.display_info(self)
        print(f"The employee :{self.employee_name} , {response}")

obj=employee("Satya","Claude")
obj.employee_info()
