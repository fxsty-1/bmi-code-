# code by @gediomr sluis on twitter
print ("this test is for people between the ages of 19 to 70 years old.")

height = input ("height in meters here:", )
weight = input ("weight in kg:", ) 

#converting in to float
weight_l = float(weight)
height_l = float(height)

# calculations
cal = (height_l * height_l)
cal2 = (weight_l / cal)
cal3 = round(cal2)

#actions
if cal2 <= 18.5  :
 print ("you are under weight.")

elif cal2 <= 25  :
    print ('you are a healthy weight.')

elif cal2 <= 30  :
    print ("you are overweight.")

elif cal2 >= 30  :
    print ("you are very overweight,obesity.")

else : 
 print ("!EROR!pleas read instructions and re enter info ;)")
