# Ballistic Calculator for 308 Winchester

# 308 Cal.
# Zero at 200 yards
# ranges from 300 - 500

def zero_range_308():
    x = False
    while not x:

        while True:
            try:
                range = float(input("Enter the range in yards: "))
            except ValueError:
                print("You must enter a float, try again: ")
                continue
            else:
                break

        oneMoa = range / 100.0

        if oneMoa == 3.0:
            drop = 7.56
            moa = drop / oneMoa
            mil = moa / 3.5
            clicks = moa * 4

            print(" ")
            print("Drop in inches: ", drop)
            print("________________________")
            print("Moa: ", moa)
            print("________________________")
            print("Mils: ", mil)
            print("________________________________________")
            print('Turns on 1/4" scope: ', clicks)
            print("_____________________________________________")

        elif oneMoa == 3.5:
            drop = 14.05
            moa = drop / oneMoa
            mil = moa / 3.5
            clicks = moa * 4

            print(" ")
            print("Drop in inches: ", drop)
            print("________________________")
            print("Moa: ", moa)
            print("________________________")
            print("Mils: ", mil)
            print("________________________________________")
            print('Turns on 1/4" scope: ', clicks)
            print("_____________________________________________")

        elif oneMoa == 4.0:
            drop = 22.58
            moa = drop / oneMoa
            mil = moa / 3.5
            clicks = moa * 4

            print(" ")
            print("Drop in inches: ", drop)
            print("________________________")
            print("Moa: ", moa)
            print("________________________")
            print("Mils: ", mil)
            print("________________________________________")
            print('Turns on 1/4" scope: ', clicks)
            print("_____________________________________________")

        elif oneMoa == 4.5:
            drop = 33.37
            moa = drop / oneMoa
            mil = moa / 3.5
            clicks = moa * 4

            print(" ")
            print("Drop in inches: ", drop)
            print("________________________")
            print("Moa: ", moa)
            print("________________________")
            print("Mils: ", mil)
            print("________________________________________")
            print('Turns on 1/4" scope: ', clicks)
            print("_____________________________________________")

        elif oneMoa == 5.0:
            drop = 46.64
            moa = drop / oneMoa
            mil = moa / 3.5
            clicks = moa * 4

            print(" ")
            print("Drop in inches: ", drop)
            print("________________________")
            print("Moa: ", moa)
            print("________________________")
            print("Mils: ", mil)
            print("________________________________________")
            print('Turns on 1/4" scope: ', clicks)
            print("_____________________________________________")

        else:
            print("You must enter a range in increments of 50 starting at 300!")

        again = input("Would you like to enter another range? [y/n]: ").lower()
        if again == 'y':
            x = False
        else:
            x = True



if __name__ == '__main__':
    zero_range_308()
