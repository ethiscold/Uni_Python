
degrees_F=70
def convert(degrees_F):
    degrees_K = ((degrees_F-32) * (5/9))+273.15
    return degrees_K
print (convert(70))

mpg=32
LITRES_PER_GALLON = 4.54609
KMS_PER_MILE = 1.60934
fuel_consumption = LITRES_PER_GALLON / (KMS_PER_MILE*mpg)
print (fuel_consumption*100)

principal = 1500
rate = 0.043
n = 4
time = 6
amount = principal * (1 + (rate/n)) ** (n*time)
print (amount)

