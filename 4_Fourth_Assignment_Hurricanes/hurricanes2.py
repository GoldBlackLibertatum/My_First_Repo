import numpy as np
starting_position_miles = float (input("How far (in miles) was the eye from Orlando when it was directly east of Orlando? (Numeric Form, Min is 10, Max is 1000) \n"))
angle_input = float (input("What angle (in degrees), north of east is the hurricane moving? (Numeric Form, More than 1 and Less than 90) \n"))
speed = float (input("How fast is the hurricane moving in miles per hour?\n"))
radians_conversion = np.sin (angle_input * np.pi / 180)
eye_distance_miles = radians_conversion * starting_position_miles
eye_distance_miles_round = round(eye_distance_miles, 5)                              
time = round(eye_distance_miles_round / speed, 5)
#Math Equation To Get Remainder As A Iterative and Boolean Tool Tool For Solving Problem. 
#refuel_no_remainder = int((distance_miles-total_fuel)/ total_fuel) + (((distance_miles - total_fuel) % total_fuel > 0))
#print(refuel_no_remainder)

    
print("The closest distance the eye will get to Orlando is " + str(eye_distance_miles_round) + " miles.")
print("This will occur " + str(time) +" hours after the eye was east of Orlando.")

#Tested, 155.5, 45, 5.5, Output = 109.9551044, 19.99184
#Tested, 300, 30, 5, Output = 150.0 miles, 30.0 hours
#Tested, 100, 70, 5, Output = 93.96926, 18.79385 hours
#Tested, 200.3, 58.3, 7.1 = 170.41747 miles, 24.00246 hours