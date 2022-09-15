def toFixed(value, digits):
    return "%.*f" % (digits, value)
def menu():
    print ('Menu Utama')
    print ('=========')
    print ('1. Celcius ke Fahrenheit')
    print ('2. Celcius ke Reamur')
    print ('3. Celcius ke Kelvin')
    print ('4. Exit')
def fahrenheit():
    print("Masukan Suhu Celcius yang ingin di konversikan ke Fahrenheit:= ")
    c = float(input())
    f = (c + 32) * 9 / 5
    print(toFixed(c,3) + "° Celcius = " + toFixed(f,3) + "° Fahrenheit")
def reamur():
    print("Masukan Suhu Celcius yang ingin di konversikan ke Reamur:= ")
    c = float(input())
    r = c * 9 / 5
    print(toFixed(c,3) + "° Celcius = " + toFixed(r,3) + "° Reamur")
def kelvin():
    print("Masukan Suhu Celcius yang ingin di konversikan ke Kelvin:= ")
    c = float(input())
    k = c + 273.15
    print(toFixed(c,3) + "° Celcius = " + toFixed(k,3) + "° Kelvin")
print ('Menu')
print ('=========')
menu()
while True:
    n = input('Masukan Pilihan ')
    print ('=========')
    if n == ('1'):
            fahrenheit()
            menu()
    elif n == ('2'):
            reamur()
            menu()
    elif n == ('3'):
            kelvin()
            menu()
    if n == ('4'):
        break

print("Progam ini akan Berhenti")
