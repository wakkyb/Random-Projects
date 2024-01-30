import time


# calculation function:
def infinite_cal():
    a = int(input('Tell me your first number: '))
    b = int(input('Tell me your second number: '))
    return a + b


# loop for single event of infinite invocations
def sssh():
    while True:
        x = int(input("""Do you want to do a calculation? 
            Press 1 for Yes
            Press 2 for No
            """))
        # call the calculator
        if x == 1:
            print(infinite_cal())
            continue
        # reset the program
        elif x == 2:
            print('Thank You for using our calculator. Take Care')
            break
        else:
            print('Input error')


# visual feedback to user
def countdown():
    print("""starting in:
3""")
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')


# loop to make the above loop infinite
while True:
    countdown()
    sssh()
