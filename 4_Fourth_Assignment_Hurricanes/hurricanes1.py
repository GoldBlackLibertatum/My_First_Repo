#Assignment/Problem A Solution, Using Law of Sines to Solve and Assignment
import numpy as np
starting_position_miles = float (input("How far (in miles) was the eye from Orlando when it was directly east of Orlando? (Numeric Form, Min is 10, Max is 1000) \n"))
angle_input = float (input("What angle (in degrees), north of east is the hurricane moving? (Numeric Form, More than 1 and Less than 90) \n"))
radians_conversion = np.sin (angle_input * np.pi / 180)
eye_distance_miles = radians_conversion * starting_position_miles
eye_distance_miles_round = round(eye_distance_miles, 5)                              

#Math Equation To Get Remainder As A Iterative and Boolean Tool Tool For Solving Problem. 
#refuel_no_remainder = int((distance_miles-total_fuel)/ total_fuel) + (((distance_miles - total_fuel) % total_fuel > 0))
#print(refuel_no_remainder)

    
print("The closest distance the eye will get to Orlando is " + str(eye_distance_miles_round) + " miles.")

# Tested, 155.5, 45, Output = 109.9551
# Tested, 300, 30, Output = 150
# Tested, 200.5, 61.2, Output = 175.69949 [Wonder why it added another significant digit?]