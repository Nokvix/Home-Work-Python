import re

licence_plates = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

private_cars_pattern = r"[АВЕКМНОРСТУХ][1234567890]{3}[АВЕКМНОРСТУХ]{2}[1234567890]{2,3}"
taxi_pattern = r"[АВЕКМНОРСТУХ]{2}[1234567890]{3}[1234567890]{2,3}"

private_cars = re.findall(private_cars_pattern, licence_plates)
taxi = re.findall(taxi_pattern, licence_plates)

print(private_cars)
print(taxi)
