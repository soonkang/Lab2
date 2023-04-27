def calculate_bmi(height, weight):
  print("Height = " + str(height))
  print("Weight = " + str(weight))
weight =float(input("Weight : "))
height =float(input("Height : "))

bmi = weight/ height ** 2
print("BMI = " + str(bmi))

if bmi < 18.5 :
  print("Under weight")
elif (bmi <= 25):
  print("Normal weight")
else:
  print("Over weight")

