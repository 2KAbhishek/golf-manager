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
    for i in range(3):
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
    for index, teeTime in enumerate(golfClub.getEmptyTeeTimes()):
        print("{}. {}".format(index, teeTime))

    print("Enter option: ")
    selection = int(input())
    if selection in golfClub.teeTimes:
        golfClub.addBooking(selection, flight)
        print("Tee time {} booked for flight with golfers {}".format(
            selection, golfers))
    else:
        print("Invalid option")
        submitBooking(golfClub)

    if golfClub.searchBooking(flight.teeTime) != None:
        raise GolfingException("Tee time is already booked")
    for memberID, golfer in golfClub.golfers.items():
        if golfer.booking != None:
            raise GolfingException(
                "Booking has failed as one member already has another booking")
    if golfClub.golfingDate.weekday() == 5 or golfClub.golfingDate.weekday() == 6:
        if not flight.getWeekendEligibility():
            raise GolfingException(
                "Booking has failed as flight is not eligible to play on weekend")
    golfClub.bookings[flight.teeTime] = flight


def display_menu(golfClub):
    print("""
Golf Booking for {} Sunday
======================================
1. Submit Booking
2. Cancel Booking
3. Edit Booking
4. Print Play Schedule
5. Overview of Tee Schedule
0. Exit
Enter option: """.format(golfClub.golfingDate.strftime("%A")))

    selection = int(input())
    if selection == 1:
        submitBooking(golfClub)
    elif selection == 2:
        cancel_booking()
    elif selection == 3:
        edit_booking()
    elif selection == 4:
        print_play_schedule()
    elif selection == 5:
        overview_tee_schedule()
    elif selection == 0:
        exit()
    else:
        print("Invalid option")
        display_menu()


if __name__ == "__main__":
    fileName = "../data/" + input("Enter course file name: ")
    course = Course(fileName)

    golfingDate = input("Enter golfing date in dd/mm/yyyy: ")
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

    display_menu(golfClub)
