from address import Address
from mailing import Mailing

to_address = Address("656 666", "Белый", "Сад", "12", "1")
from_address = Address("566 887", "Нильф", "Императорская", "1", "576")

mailing = Mailing(to_address, from_address, 776, "4567fh245v55")

print(mailing)
