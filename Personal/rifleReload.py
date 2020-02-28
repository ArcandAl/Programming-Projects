# Program to calculate price of reloading a certain handloaded rifle round

def reload_price():
    x = False
    while not x:
        while True:
            try:
                powderPrice = float(input("Enter the price of the powder: "))
            except ValueError:
                print("You must enter a float, try again: ")
                continue
            else:
                break

        while True:
            try:
                TotalPowder = float(input("Enter the amount of powder in the bag in pounds: ")) * 7000
            except ValueError:
                print("You must enter a float, try again: ")
                continue
            else:
                break

        while True:
            try:
                powderAmount = float(input("Enter the amount of powder in the load in grains: "))
            except ValueError:
                print("You must enter a float, try again: ")
                continue
            else:
                break




        while True:
            try:
                primerPrice = float(input("Enter the price of the primer: "))
            except ValueError:
                print("You must enter a float, try again: ")
                continue
            else:
                break


        while True:
            try:
                primers = float(input("Enter the amount of primers in the box: "))
            except ValueError:
                print("You must enter a float, try again: ")
                continue
            else:
                break




        while True:
            try:
                bulletPrice = float(input("Enter the price of the bullets: "))
            except ValueError:
                print("You must enter a float, try again: ")
                continue
            else:
                break


        while True:
            try:
                bullets = float(input("Enter the amount of bullets in the package: "))
            except ValueError:
                print("You must enter a float, try again: ")
                continue
            else:
                break



        powder = ( (powderPrice / TotalPowder ) * powderAmount )
        primer = (primerPrice / primers )
        bullet = (bulletPrice / bullets )

        single = powder + primer + bullet
        box = single * 20

        print("The price per round is: ", single)
        print("The price per box is: ", box)

        ag = input("Enter exact amount of rounds reloaded or 'x' to continue: ").lower()
        if ag.isdigit():
            new = float(ag) * single
            print("The price for ", ag , "is ", new)

        again = input("Would you like to enter another load? [y/n]: ").lower()
        if again == 'y':
            x = False
        else:
            x = True

if __name__ == '__main__':
    reload_price()
