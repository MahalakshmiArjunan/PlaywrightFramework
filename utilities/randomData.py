from faker import Faker
import random
import string

class RandomData:
    def __init__(self):
        self.fake = Faker()

    def get_first_name(self):
        return self.fake.first_name()

    def get_last_name(self):
        return self.fake.last_name()

    def get_full_name(self):
        return self.fake.first_name() + " " + self.fake.last_name()

    def get_email(self):
        return self.fake.email()

    def get_phone_number(self):
        return self.fake.phone_number()

    def get_address(self):
        return self.fake.address()

    def get_city(self):
        return self.fake.city()

    def get_state(self):
        return self.fake.state()

    def get_zipcode(self):
        return self.fake.zipcode()

    def get_country(self):
        return self.fake.country()

    def get_company_name(self):
        return self.fake.company()

    def get_random_string(self, length = 10):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

    def get_random_number(self, start=0, end=100):
        return random.randint(start, end)



