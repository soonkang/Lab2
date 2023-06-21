def calculate_bmi(height, weight):
  print("Height = " + str(height))
  print("Weight = " + str(weight))
  bmi = weight/ height ** 2
  print("BMI = " + str(bmi))

  if bmi < 18.5 :
    print("Under weight")
    return -1
  elif (bmi <= 25):
    print("Normal weight")
    return 0
  else:
    print("Over weight")
    return 1
x= calculate_bmi(weight=65.0, height=1.73)
print(x)


