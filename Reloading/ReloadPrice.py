# Program to calculate price of reloading a certain handloaded shotgun shell

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
                shotPrice = float(input("Enter the price of the shot: "))
            except ValueError:
                print("You must enter a float, try again: ")
                continue
            else:
                break


        while True:
            try:
                Totalshot = float(input("Enter the amount of shot in the bag in pounds: ")) * 16
            except ValueError:
                print("You must enter a float, try again: ")
                continue
            else:
                break

        while True:
            try:
                shotAmount = float(input("Enter the amount of shot in the load in oz: "))
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
                wadPrice = float(input("Enter the price of the wads: "))
            except ValueError:
                print("You must enter a float, try again: ")
                continue
            else:
                break

        while True:
            try:
                wads = float(input("Enter the amount of wads in the bag: "))
            except ValueError:
                print("You must enter a float, try again: ")
                continue
            else:
                break

        powder = ( (powderPrice / TotalPowder ) * powderAmount )
        shot = ( (shotPrice / Totalshot ) * shotAmount )
        primer = (primerPrice / primers )
        wad = ( wadPrice / wads )

        single = powder + shot + primer + wad
        box = single * 25
        pack = box * 4
        print("The price per round is: ", single)
        print("The price per box is: ", box)
        print("The price per four pack is: ", pack)

        ag = input("Enter exact amount of shells reloaded or 'x' to continue: ").lower()
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
