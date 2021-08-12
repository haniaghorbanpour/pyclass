def BMI(height , weight):
    denominator=height**2
    numerator=weight
    ourBMI=numerator/denominator
    return ourBMI

BMI=BMI(float(input("enter your height plz (m)")),float(input("enter your weight plz (kg)")))

print("your BMI is {}".format(BMI))
