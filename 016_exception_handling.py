while True:
    #if u expect the code would fail
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("You didn't enter a number")
    except:
        print("An unknown error occured")

print("Thank you")

