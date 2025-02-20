def calcAge(age):
    days = age * 365
    return days

yas = int(input("Yaş gir: "))  # input fonksiyonu ile kullanıcıdan yaş alıyoruz
print(calcAge(yas))
