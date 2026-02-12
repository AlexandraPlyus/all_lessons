
class Address:

    def __init__(self, code, city, street, hous, apartment):
        self.code = code
        self.city = city
        self.street = street
        self.hous = hous
        self.apartment = apartment

    def __str__(self):
        return (f"{self.code}, {self.city}, {self.street}, "
                f"{self.hous} - {self.apartment}")
