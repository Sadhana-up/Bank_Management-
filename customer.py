class Customer:
    def __init__(self, customer_id, name, email, age=None, phone=None):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.age = age
        self.phone = phone

    def get_customer_info(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "age": self.age,
            "phone": self.phone
        }
    def update_email(self, new_email):
        self.email = new_email
    def update_phone(self, new_phone):
        self.phone = new_phone
    def update_age(self, new_age):
        self.age = new_age
    def get_contact_info(self):
        return {
            "email": self.email,
            "phone": self.phone
        }
    def is_adult(self):
        return self.age is not None and self.age >= 18  