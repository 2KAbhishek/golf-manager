from datetime import datetime
from course import Course
from flight import Flight
from golf_club import GolfClub
from golfing_exception import GolfingException


def submitBooking(golfClub):

    print("""
Enter 3 or 4 golfers to form a flight
=====================================
""")
    golfers = []
    for i in range(4):
        print("Enter ID for golfer {} or -1 to stop: ".format(i+1))
        id = int(input())
        if id == -1:
            break
        golfers.append(golfClub.searchGolfer(id))
    flight = Flight(golfers)
    print("""
List of available tee times
=========================
""")
    availableTimes = golfClub.getEmptyTeeTimes()
    for index, teeTime in enumerate(availableTimes):
        print("{}. {}".format(index, teeTime))

    print("Enter option: ")
    selection = availableTimes[int(input())]
    try:
        for golfer in flight.getGolfersID():
            if golfClub.searchMemberBooking(golfer) != None:
                raise GolfingException(
                    "Booking has failed as one member already has another booking")
        if golfClub.golfingDate.weekday() == 5 or golfClub.golfingDate.weekday() == 6:
            if not flight.getWeekendEligibility():
                raise GolfingException(
                    "Booking has failed as flight is not eligible to play on weekend")
        golfClub.addBooking(selection, flight)
        print("Tee time {} booked for flight with golfers {}".format(
            selection, flight.getGolfersID()))
        displayMenu(golfClub)
    except GolfingException as e:
        print(e)
        print("Invalid option")
        submitBooking(golfClub)


def cancelBooking(golfClub):
    print("Enter member ID to cancel booking: ")
    memberID = int(input())
    try:
        cancelTime = golfClub.searchMemberBooking(memberID)
        golfClub.cancelBooking(cancelTime)
        print("Tee Time {} cancelled successfully".format(cancelTime))
        displayMenu(golfClub)
    except GolfingException as e:
        print(e)
        print("Invalid member ID")
        cancelBooking(golfClub)


def editBooking(golfClub):
    print("Enter tee time (HH:MM) to edit booking: ")
    teeTime = input()
    try:
        flight = golfClub.searchBooking(teeTime)
        print("""
Current flight of golfers {} will be replaced by a new flight
Confirm to replace? (Y/N): """.format(flight.getGolfersID()))
        selection = input()
        if selection == 'y':
            print("Enter 3 or 4 golfers to form a flight")
            golfers = []
            for i in range(4):
                print("Enter ID for golfer {} or -1 to stop: ".format(i+1))
                id = int(input())
                if id == -1:
                    break
                golfers.append(golfClub.searchGolfer(id))
            flight = Flight(golfers)
            golfClub.cancelBooking(teeTime)
            golfClub.addBooking(teeTime, flight)
            print("Flight with golfers {} updated successfully".format(
                flight.getGolfersID()))
            displayMenu(golfClub)
    except GolfingException as e:
        print(e)
        print("Invalid tee time")
        editBooking(golfClub)


def printPlaySchedule(golfClub):
    print("Enter member ID to print play schedule: ")
    memberID = int(input())
    try:
        teeTime = golfClub.searchMemberBooking(memberID)
        print(golfClub.course.getPlaySchedule(teeTime))
        displayMenu(golfClub)
    except GolfingException as e:
        print(e)
        print("Invalid member ID")
        printPlaySchedule(golfClub)


def overviewTeeSchedule(golfClub):
    print("""
Overview of Tee Schedule
===========================
""")
    print(golfClub.getBookings())
    displayMenu(golfClub)


def displayMenu(golfClub):
    print("""
Golf Booking for {}
======================================
1. Submit Booking
2. Cancel Booking
3. Edit Booking
4. Print Play Schedule
5. Overview of Tee Schedule
0. Exit
Enter option: """.format(golfClub.golfingDate.strftime("%d/%m/%Y %A")))

    selection = int(input())
    if selection == 1:
        submitBooking(golfClub)
    elif selection == 2:
        cancelBooking(golfClub)
    elif selection == 3:
        editBooking(golfClub)
    elif selection == 4:
        printPlaySchedule(golfClub)
    elif selection == 5:
        overviewTeeSchedule(golfClub)
    elif selection == 0:
        exit()
    else:
        print("Invalid option")
        displayMenu(golfClub)


if __name__ == "__main__":
    fileName = "../data/" + input("Enter course file name: ")
    course = Course(fileName)

    golfingDate = datetime.strptime(
        input("Enter golfing date in dd/mm/yyyy: "), "%d/%m/%Y")
    golfClub = GolfClub("Fantasy Golf", course, golfingDate)

    golfClub.setupGolfers("../data/Golfers.txt")

    flight1 = Flight([golfClub.searchGolfer(21), golfClub.searchGolfer(
        57), golfClub.searchGolfer(58), golfClub.searchGolfer(5)])
    golfClub.addBooking("07:28", flight1)

    flight2 = Flight([golfClub.searchGolfer(
        8), golfClub.searchGolfer(18), golfClub.searchGolfer(17)])
    golfClub.addBooking("07:48", flight2)

    flight3 = Flight([golfClub.searchGolfer(
        9), golfClub.searchGolfer(27), golfClub.searchGolfer(24)])
    golfClub.addBooking("07:58", flight3)

    displayMenu(golfClub)
