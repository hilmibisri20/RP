def toFixed(value, digits):
    return "%.*f" % (digits, value)

while True:    #This simulates a Do Loop
    print("Masukan Pilihan Anda" + chr(13) + "1.Celcius ke Fahrenheit" + chr(13) + "2.Celcius ke Reamur" + chr(13) + "3.Celcius ke Kelvin" + chr(13) + "4. Exit", end='', flush=True)
    n = int(input())
    if n == 3:
        print("Masukan Suhu Celcius yang ingin di konversikan ke Kelvin:= ")
        c = float(input())
        k = c + 273.15
        print(toFixed(c,3) + "° Celcius = " + toFixed(k,3) + "° Kelvin")
    else:
        if n == 2:
            print("Masukan Suhu Celcius yang ingin di konversikan ke Reamur:= ")
            c = float(input())
            r = c * 9 / 5
            print(toFixed(c,3) + "° Celcius = " + toFixed(r,3) + "° Reamur")
        else:
            if n == 1:
                print("Masukan Suhu Celcius yang ingin di konversikan ke Fahrenheit:= ")
                c = float(input())
                f = (c + 32) * 9 / 5
                print(toFixed(c,3) + "° Celcius = " + toFixed(f,3) + "° Fahrenheit")
    if n == 4:
        n = 4
    if not(n > 4 or n < 4): break   #Exit loop
print("Progam ini akan Berhenti")
