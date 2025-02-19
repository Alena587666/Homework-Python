from address import Address
from mailing import Mailing


to_address = Address("353821", "Уфа", "ул.Ленина", "78", "5")
from_address = Address("356377", "Самара", " ул.Коммунаров", "32", "7")


mailing = Mailing("s987256473h9090", to_address, from_address, 3400)

print(mailing)
