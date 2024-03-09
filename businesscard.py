from faker import Faker
fake = Faker()

class BaseContact:
    def __init__(self, name, surname, telephone, email):
        self.name = name
        self.surname = surname
        self.telephone = telephone
        self.email = email
    def __repr__(self):
        return self.name
    def contact(self):
        print(f"I am dialing {self.telephone} and calling {self.name} {self.surname}")
    @property
    def label_length(self):
        return len(self.name + self.surname)    

class BusinessContact(BaseContact):
    def __init__(self, name, surname, telephone, email, position, compname, workphone):
        super().__init__(name, surname, telephone, email)
        self.position = position
        self.compname = compname
        self.workphone = workphone
    def __repr__(self):
        return self.compname
    def contact(self):
        print(f"I am dialing {self.workphone} and calling {self.compname} ({self.position})")
    @property
    def label_length(self):
        return len(self.compname)

def create_contacts(type, number):
    if type == "Base":
        for i in range(number):
            i = BaseContact(name=fake.first_name(), surname=fake.last_name(), telephone=fake.phone_number(), email=fake.email())
            print(f"Base card for {i.name} {i.surname}: {i.telephone}, {i.email}")
    if type == "Business":
        for i in range(number):
            i = BusinessContact(name=fake.first_name(), surname=fake.last_name(), telephone=fake.phone_number(), email=fake.email(), position=fake.job(), compname=fake.name(), workphone=fake.phone_number())
            print(f"Business card for {i.compname} ({i.position}): {i.workphone}, {i.email}")

Jim = BaseContact(name="Jim", surname="Jimmons", telephone=3, email="jim@jim.com")
Harry = BusinessContact(name="Harry", surname="Harrison", telephone=4, email="harry@gmail.com", compname="Dr. Harry H Harrison", position="CEO", workphone=45)

print(Jim.label_length)
print(Harry.label_length)

create_contacts("Base", 2)
create_contacts("Business", 3)