from smartphone import Smartphone


catalog = [
   Smartphone("Samsung", "Galaxy S25", "+79888564738"), 
   Smartphone("Honor", "300 Ultra", "+79283648392"),
   Smartphone("Nokia", "220 4G", "+79784320108"),
   Smartphone("LG", "K92 5G", "+79950937249"),
   Smartphone("POCO", "C61", "+79997540204")
]


for smartphone in catalog:
    print(f'{smartphone.brand} - {smartphone.model},' 
          f'{smartphone.phone_number}')
