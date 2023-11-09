#declare variables
choice=0.0
action=0.0
led_on=0.0
start_time=0.0

import sys
import time
import random

# select options for Drive LED Servo Random and Exit
def main():
    print("Robot Dance Program by Adesina Osibodu")
    while True:
        print("\nOptions:")
        print("1. Drive Mode")
        print("2. LEDs Mode")
        print("3. Servo Mode")
        print("4. Random Mode")
        print("5. Exit Program")
        
        choice = input("Please select your option (1/2/3/4/5): ")
      
        if choice == '1':
            drive_robot()
        elif choice == '2':
            led_control()
        elif choice == '3':
            servo_control()
        elif choice == '4':
            random_control()
        elif choice == '5':
            print("Thank you for using Robot Dance. You have successfully exited the program")
            sys.exit()
        else:
            print("Invalid choice. Please enter a valid option.")
            
# Robot control Drive mode
def drive_robot():
    print("\nRobot control: Drive Mode")
    while True:
# Ask user to enter movement command
        action = input("Enter a movement command (w/a/d/s/x/g/t/z): ")
        
        if action == 'w':
            print(" forward")
        elif action == 'a':
            print("turn left")
        elif action == 'd':
            print("turn right")
        elif action == 's':
            print("move back")
        elif action == 'x':
            print("stop")
        elif action == 'g':
            print("decrease speed")
        elif action == 't':
            print("increase speed")
        elif action == 'z':
            print("Exit using sys module.")
            break
        else:
            print("Invalid selection. Please enter a valid command.")
            
# Robot control Led mode
def led_control():
    print("\nRobot control: LEDs Mode")
    led_on = False
    while True:
        if led_on:
            action = input("LEDs powered ON. Power OFF? (y/n): ")
        else:
            action = input("LEDs powered OFF. Power ON? (y/n): ")
        
        if action == 'y':
            led_on = not led_on
            if led_on:
                print("LEDs Activated.")
            else:
                print("LEDs Deactivated.")
        elif action == 'n':
            print("Now exiting LED control mode.")
            break
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")
            
# Robot Control Servo mode
def servo_control():
    print("\nRobot control: Servo Mode")
    Permited_servo_commands = ['left', 'right', 'home', 'z']
    while True:
        action = input("Enter  servo movement command (left/right/home/z): ")
        
        if action == 'left':
            print("servo left")
        elif action == 'right':
            print("servo right")
        elif action == 'home':
            print("Servo home")
        elif action == 'z':
            print("Now exiting servo control mode.")
            break
        else:
            print("Invalid action. Please use a valid command.")
            
# Robot control random mode
def random_control():
    print("\nRobot control: Random (Dancing Mode)")
    start_time = time.time()
    
    while time.time() - start_time < random.randint(20, 30):
        action = random.choice(['w', 'a', 'd', 's', 'x', 'g', 't'])
        
        if action == 'w':
            print("forward")
        elif action == 'a':
            print("left")
        elif action == 'd':
            print("right")
        elif action == 's':
            print("back")
        elif action == 'x':
            print("stop")
        elif action == 'g':
            print("decrease speed")
        elif action == 't':
            print("increase speed")
# Delay sequence
        time.sleep(random.uniform(0.5, 1.5))  

    print("Dance finished. Now exiting dance mode.")

if __name__ == "__main__":
    main()
