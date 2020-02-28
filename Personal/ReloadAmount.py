# Program to calculate amount of shotgun shell able to reload with remaining supplies

def reload_amount():
    x = False
    while not x:
        while True:
            try:
                Allpowder = float(input("Enter the amount powder you have in pounds: ")) * 7000
            except ValueError:
                print("You must enter a float, try again: ")
                continue
            else:
                break

        while True:
            try:
                powder = float(input("Enter the amount powder in the load in grains: "))
            except ValueError:
                print("You must enter a float, try again: ")
                continue
            else:
                break

        while True:
            try:
                Allshot = float(input("Enter the amount shot you have in pounds: ")) * 16
            except ValueError:
                print("You must enter a float, try again: ")
                continue
            else:
                break

        while True:
            try:
                shot = float(input("Enter the amount of shot in the load in oz: "))
            except ValueError:
                print("You must enter a float, try again: ")
                continue
            else:
                break

        while True:
            try:
                primers = float(input("Enter the amount of primers you have: "))
            except ValueError:
                print("You must enter a float, try again: ")
                continue
            else:
                break

        while True:
            try:
                wads = float(input("Enter the amount of wads you have: "))
            except ValueError:
                print("You must enter a float, try again: ")
                continue
            else:
                break

        new_list = []
        end_powder = Allpowder/powder
        end_shot = Allshot/shot
        new_list.append(end_powder)
        new_list.append(end_shot)
        new_list.append(wads)
        new_list.append(primers)

        print("You can reload ", min(new_list), " shells with your remaining materials")

        again = input("Would you like to enter another amount of materials? [y/n]: ").lower()
        if again == 'y':
            x = False
        else:
            x = True

if __name__ == '__main__':
    reload_amount()
