

while True: 
    print("\nMENU") 
    print("1. Sum of two values") 
    print("2. Product of two values") 
    print("3. Division result") 
    print("4. Difference between two values") 
    print("5. Exit") 
    choice = int(input("\nMake your choice, please: ")) 
 

    if choice == 1: 
        print( "\nSUM\n") 
        x = int(input("First value: ")) 
        y = int( input("Second value: ")) 
        sum(x, y) 
 
    elif choice == 2: 
        print( "\nMULTIPLY\n") 
        x = int(input("First value: ")) 
        y = int(input("Second value: ")) 
        mult(x, y)

    elif choice == 3: 
        print( "\nDIVISION\n") 
        x = int( input("First value: ")) 
        y = int( input("Second value: ")) 
        div(x, y) 

    elif choice == 4: 
        print( "\nSUBTRACTION\n") 
        x = int( input("First value: ")) 
        y = int( input("Second value: ")) 
        sub(x - y) 
 
    elif choice == 5: 
        break 
     
    else: 
        print( "Try again!")
