def celciusToFheraniteConverter(c):
    f=(9/5)*int(c)+32
    print("Temperature in Fharenite is: "+str(f))

def hourToMinuteCoverter(m,s=0):
    h=int(m)*60+ int(s)*3600
    print("Time in Minutes is: "+str(h))

celcius=int(input("Enter temperature in celcius: "))
min=int(input("Enter Hours: "))
celciusToFheraniteConverter(celcius)
hourToMinuteCoverter(min)