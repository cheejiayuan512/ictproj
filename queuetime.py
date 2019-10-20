def waitingtime(headcount):
    while True:
        try:
            print("You will have to wait", round(1.5 * int(headcount)), "minutes!")
            break
        except ValueError:
            print("Give me an integer!")

waitingtime(23)