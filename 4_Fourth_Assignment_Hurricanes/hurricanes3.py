import numpy as np
#Input Section for Position and Time Using Speed and Starting Position 
starting_position_miles = float (input("How far (in miles) was the eye from Orlando when it was directly east of Orlando? (Numeric Form, Min is 10, Max is 1000) \n"))
angle_input = float (input("What angle (in degrees), north of east is the hurricane moving? (Numeric Form, More than 1 and Less than 90) \n"))
speed = float (input("How fast is the hurricane moving in miles per hour?\n"))

#Conversion Section for Radians Given Angle And Doing the Sine of Angle, Given Hypotenuse And Angle
radians_conversion = np.sin (angle_input * np.pi / 180)
#Multiplying by Starting Position (Hypotenuse) To Find Position Closest and Rounding 
eye_distance_miles = round(radians_conversion * starting_position_miles, 5)
#Finding Time and Rounding
time = round(eye_distance_miles / speed, 5)

#Inputs for If Conditionals
categoryh= int (input("What category is the hurricane? (Numeric Form)\n"))
if   categoryh > 5 or categoryh <= 0:
    print ("God isn't going to flood the world. Please pick a number between 0 to 5 to represent tropical to category 5 storms. \n")
elif categoryh == 0:
    tropical_dist = float(input("How far (in miles) from the eye do tropical storm winds extend? (Numeric Form)\n"))
    cat1_dist = 0
    cat2_dist = 0
    cat3_dist = 0
    cat4_dist = 0
    cat5_dist = 0
elif categoryh == 1:
    tropical_dist = float(input("How far (in miles) from the eye do tropical storm winds extend? (Numeric Form)\n"))
    cat1_dist = float(input("How far (in miles) from the eye do category 1 winds extend? (Numeric Form)\n"))
    cat2_dist = 0
    cat3_dist = 0
    cat4_dist = 0
    cat5_dist = 0
elif categoryh == 2:
    tropical_dist = float(input("How far (in miles) from the eye do tropical storm winds extend? (Numeric Form)\n"))
    cat1_dist = float(input("How far (in miles) from the eye do category 1 winds extend? (Numeric Form)\n"))
    cat2_dist = float(input("How far (in miles) from the eye do category 2 winds extend? (Numeric Form)\n"))
    cat3_dist = 0
    cat4_dist = 0
    cat5_dist = 0
elif categoryh == 3:
    tropical_dist = float(input("How far (in miles) from the eye do tropical storm winds extend? (Numeric Form)\n"))
    cat1_dist = float(input("How far (in miles) from the eye do category 1 winds extend? (Numeric Form)\n"))
    cat2_dist = float(input("How far (in miles) from the eye do category 2 winds extend? (Numeric Form)\n"))
    cat3_dist = float(input("How far (in miles) from the eye do category 3 winds extend? (Numeric Form)\n"))
    cat4_dist = 0
    cat5_dist = 0
elif categoryh == 4:
    tropical_dist = float(input("How far (in miles) from the eye do tropical storm winds extend? (Numeric Form)\n"))
    cat1_dist = float(input("How far (in miles) from the eye do category 1 winds extend? (Numeric Form)\n"))
    cat2_dist = float(input("How far (in miles) from the eye do category 2 winds extend? (Numeric Form)\n"))
    cat3_dist = float(input("How far (in miles) from the eye do category 3 winds extend? (Numeric Form)\n"))
    cat4_dist = float(input("How far (in miles) from the eye do category 4 winds extend? (Numeric Form)\n"))
    cat5_dist = 0
elif categoryh == 5:  
    tropical_dist = float(input("How far (in miles) from the eye do tropical storm winds extend? (Numeric Form)\n"))
    cat1_dist = float(input("How far (in miles) from the eye do category 1 winds extend? (Numeric Form)\n"))
    cat2_dist = float(input("How far (in miles) from the eye do category 2 winds extend? (Numeric Form)\n"))
    cat3_dist = float(input("How far (in miles) from the eye do category 3 winds extend? (Numeric Form)\n"))
    cat4_dist = float(input("How far (in miles) from the eye do category 4 winds extend? (Numeric Form)\n"))
    cat5_dist = float(input("How far (in miles) from the eye do category 5 winds extend? (Numeric Form)\n"))
#Part A and B 
print("The closest distance the eye will get to Orlando is " + str(eye_distance_miles) + " miles.")
print("This will occur " + str(time) +" hours after the eye was east of Orlando.")

#Part C
if eye_distance_miles <= cat5_dist:
    print ("The strongest winds experienced in Orlando will be category 5 winds.")
elif eye_distance_miles <= cat4_dist:
    print ("The strongest winds experienced in Orlando will be category 4 winds.")
elif eye_distance_miles <= cat3_dist:
    print ("The strongest winds experienced in Orlando will be category 3 winds.")
elif eye_distance_miles <= cat2_dist: 
    print ("The strongest winds experienced in Orlando will be category 2 winds.")
elif eye_distance_miles <= cat1_dist:
    print ("The strongest winds experienced in Orlando will be category 1 winds.")
elif eye_distance_miles <= tropical_dist:
    print ("The strongest winds experienced in Orlando will be tropical storm winds.")
else:
    print ("You are safe from all winds.")
#Tested, 155.5, 45, 5.5, cath = 5, Trop = 200, Cat1 = 90, Cat 2= 70, Cat 3= 55, Cat 4= 45, Cat 5 = 30, 
#Output(Test1) = 109.9551044, 19.99184,
#Output(Test1)(cont) = The strongest winds experienced in Orlando will be tropical storm winds.

#Tested, Input = 300, 30, 5, Cath = 3, Trop = 100, Cat1 = 75, Cat2 = 50, Cat3 = 25
#Ouput (Test2) = 150, 30, "You are safe from all winds."

#Tested, Input = 100, 7-, 5, Cath= 3, Trop = 100, Cat1 = 75, Cat2 = 50, Cat3 = 25
#Ouput (Test3) =  12.18693 miles, 2.43739 hours,"The strongest winds experienced in Orlando will be category 3 winds."