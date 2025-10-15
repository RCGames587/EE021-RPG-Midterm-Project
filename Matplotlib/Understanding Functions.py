def print_student (name, course ="EE021"):
    print (f"My name is {name}")
    print (f"I am in {course}")
    print("I go to UC Merced")

print_student("Jose")
print_student ("Mira", "ENGR 065")
######
def is_ohms_law_verified(current,voltage,resistance):
    if (current*resistance == voltage):
        return 1
    else:
        return 0
    
print(is_ohms_law_verified(0.01,10,1000))
print(is_ohms_law_verified(69,69,67))

def is_ohms_law_verified(current=0.05,voltage=5,resistance=100):
    if (current*resistance == voltage):
        return 1
    else:
        return 0

print(is_ohms_law_verified())

score = 0
running = True
while running == True:
    current = input("Enter the Current in Amps")
    voltage = input("Enter the Voltage in Volts")
    resistance = input("Enter the Resistance in Ohms")
    if is_ohms_law_verified() == 1:
        score += 1
        print(f"Correct! Your score is {score}")
        continue
    else: 
        print ("Womp Womp Wrong!")
        print(f"Your final score is {score}")
        break