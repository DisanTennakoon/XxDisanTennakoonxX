driver = input("What is your name?: ")
def enterFine():
    global totalFines
    
    validInput = False
    while validInput == False:
        try:
            speed_limit = 100
            speed = int(input("How fast were you driving?: "))
            difference = speed - speed_limit
            if speed <= 100:
                print("Good job {}, you are not speeding.".format(driver))
            elif difference > 0 and difference <50:
                charge = 10 * (difference)
                from datetime import date
                today = date.today()      
                print("{}, you are charged ${} for speeding {}km/h over the limit.".format(driver, charge, difference))
                print("Here is your receipt.")
                print("{}. {} has sped {}km/h over the limit and is charged ${:.2f}".format(today, driver, difference, charge)):
                    
            elif speed >= 150 and speed <=180:
                print("{}, you have sped {}km/h over the limit. May I see your license? Sike, it's mine now! Go back to driving school nigga!".format(driver, difference))
            elif speed > 180 and speed <=200:
                print("{}, you have sped {}km/h over the limit. You are under arrest and sentenced to 6 months in jail. Have fun talking to Jake Paul!".format(driver, difference))
                list = [driver]
                print("Current list of offenders:{}".format(list))
                
            else:
                print("{} has been shot by the police for speeding {}km/h over the limit.".format(driver, difference))            

    
moreInput = "Y"