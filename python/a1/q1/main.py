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
    
    name = input("Input name:")
    length_of_stay = int(input("Number of days staying:"))
    if length_of_stay <=14:
        breakfast_plan = input("Would they like to purchase the breakfast plan? (Y/N)").lower()
        renter = ShortTermRenter(name, length_of_stay, breakfast_plan)
    else:
        package = input("Would they like to purchase an insurance package?\n0: No Package\n1: Basic Package\n2: Premium Package")
        renter = LongTermRenter(name, length_of_stay, package)
    
    renter_dict[room_num] = renter
    print("Cost of stay: "+ str(renter.calculate_cost()))

def check_out():
    out = input("Input the room number checking out:")
    if renter_dict.pop(out, -1) == -1:
        print("Room does not exist or is vacant")
    else:
        print("Successful removal") 

def print_system():
    for i in range(8):
        if i in renter_dict:
            renter = renter_dict[i]
            room_num = str((i+1))
            print(renter.name+" ("+room_num+"):\t"+renter.get_info_string())

while True:
    print("Make a Selection:")
    selection = input("Rent a Room (R), Check Out (C), Print Motel Details (P), Exit Program (X)")
    selection = selection.lower()
    if selection == "x":
         break
    elif selection == "c":
         check_out()
    elif selection == "p":
         print_system()
    elif selection == "r":
        rent_room()
    else:
        print("Invalid Input")
