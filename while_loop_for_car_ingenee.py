command = ""
while True:
    command = input(">").lower()
    if command == "start":
        print("Car started  ")
    elif command == "stop":
        print('Car stop')
    elif command == "help":
        print(""" 
 start - to starting the car
 stop -  to stop the car
 help - gives help command
        """)
    elif command == "quit":
        break
    else:
        print(" I don'nt understand that command ")