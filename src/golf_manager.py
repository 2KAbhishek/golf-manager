from course import Course
from flight import Flight
from golf_club import GolfClub


def display_menu(golfingDate):
    print("""
Golf Booking for {} Sunday
======================================
1. Submit Booking
2. Cancel Booking
3. Edit Booking
4. Print Play Schedule
5. Overview of Tee Schedule
0. Exit
Enter option: """.format(golfingDate.strftime("%A")))

    selection = int(input())
    if selection == 1:
        submit_booking()
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

    display_menu(golfingDate)
