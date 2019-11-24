command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            
            print(" car already started ")
        else:
            started = True
            print("Car started  ")
    elif command == "stop":
        if not started:
            print('car already stopped ')
        else:
            started = False
            print('Car stop')
    elif command == "help":
        print(""" 
 start - to starting the car
 stop -  to stop the car
 help - gives help command
        """)
    elif command == "quit":
        break
    elif command == "":
        print('try to type in  th following command' +
               """ 
                start - to starting the car
                stop -  to stop the car
                help - gives help command
                       """
               )
    else:

        print(" I don'nt understand that command ")