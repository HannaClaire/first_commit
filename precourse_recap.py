

day_of_week = "monday"
current_week = 1
total_course_weeks = 16
print("today is " + (day_of_week) + " and week", str(current_week) + " of the course. We have " + str(total_course_weeks) + " altogether.") 

weeks_left_to_go = 15

def weeks_to_go():
    weeks_left = weeks_left_to_go - current_week
    days_left = total_course_weeks - current_week
    print(f"only {weeks_left} weeks and {days_left} days to go!")

def motivate_me():
    print("We got this, you're doing great!")

weeks_to_go()
motivate_me()











      
         
         
