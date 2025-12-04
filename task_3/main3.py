day = int(input("введите день месяца - "))
month = int(input("введите месяц года цифрой - "))

if month == 1 or month == 2 or month == 12:
    print("сезон - зима")
elif month == 3 or month == 4 or month == 5:
    print("сезон - весна")
elif month == 6 or month == 7 or month == 8:
    print("сезон - лето")
else:
    print("сезон - осень")
