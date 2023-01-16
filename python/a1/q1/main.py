from renter import LongTermRenter, ShortTermRenter
renter_dict = {}


def has_vacancy():
    for i in range(8):
        if i not in renter_dict:
            return i
    return -1


def rent_room():
    room_num = has_vacancy()
    if room_num == -1:
        print("No Vacancy")
        return
    
    name = input("Input name:\n")
    length_of_stay = int(input("Number of days staying:\n"))
    if length_of_stay <=14:
        breakfast_plan = input("Would they like to purchase the breakfast plan? (Y/N)\n").lower()
        renter = ShortTermRenter(name, length_of_stay, room_num, breakfast_plan)
    else:
        print("Would they like to purchase an insurance package?")
        print("\t0: No Package")
        print("\t1: Basic Package")
        package = input("\t2: Premium Package\n")

        renter = LongTermRenter(name, length_of_stay, room_num, package)
    
    renter_dict[room_num] = renter
    print("Cost of stay: " + str(round(renter.calculate_cost(), 2)))


def check_out():
    out = input("Input the room number checking out:\n")
    if renter_dict.pop(int(out)-1, -1) == -1:
        print("Room does not exist or is vacant")
    else:
        print("Successful removal") 


def print_system():
    printed = False
    for i in range(8):
        if i in renter_dict:
            printed = True
            renter = renter_dict[i]
            room_num = str((i+1))
            print(renter.name+" ("+room_num+"):\t"+renter.get_info_string())
    if not printed:
        print("No current renters")


if __name__ == "__main__":
    while True:
        print("\nMake a Selection:")
        selection = input("Rent a Room (R), Check Out (C), Print Motel Details (P), Exit Program (X)\n")
        selection = selection.lower()
        if selection == "x":
            print("Thank you for using the program!")
            break
        elif selection == "c":
            check_out()
        elif selection == "p":
            print_system()
        elif selection == "r":
            rent_room()
        else:
            print("Invalid Input")
