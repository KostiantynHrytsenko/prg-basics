class Phone:
    def __init__(self, battery, company, model):
        self.battery = battery
        self.company = company
        self.model = model

    def display_model(self):
        print(self.model)

    def display_battery(self):
        print(self.battery)

    def change_battery(self, decrease):
        self.battery = self.battery - decrease

    def display_company(self):
        print(self.company)

def main():
    phone1 = Phone(100, "Samsung", "S24")
    phone1.display_company()
    phone1.display_model()
    phone1.change_battery(10)
    phone1.display_battery()

if __name__ =="__main__":
    main()