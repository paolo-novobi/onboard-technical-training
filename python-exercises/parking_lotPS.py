import sys

# The parking numbered 1,2,3,...,n/2 for the left side
# The parking numbered n/2+1,...,n for the right side
# So the slots are assigned in this order if they are available: 1, n/2+1, 2, n/2+2,...

class parking_lot():
    def __init__(self):
        self.number_slots = 0
        self.avail_spaces = []
        self.parking_cars_info = []

    def create_parking_lot(self, n):
        self.number_slots = n
        self.avail_spaces.clear()
        n_half = int(n/2)
        for i in range(n_half):
            self.avail_spaces.append(i+1)
            self.avail_spaces.append(i+1+n_half)
        print(self.avail_spaces)

    def park(self,registration_number,color):
        # retrieve the nearest parking number
        if (len(self.avail_spaces)==0):
            print("Parking Lot is full!")
            return -1
        lot_number = self.avail_spaces.pop(0)
        parking_info = dict()
        parking_info['lot number'] = lot_number
        parking_info['registration number'] = registration_number
        parking_info['color'] = color
        self.parking_cars_info.append(parking_info)
        print(self.parking_cars_info)
        return lot_number

    def getstatus(self):
        if (len(self.avail_spaces)==0):
            print("Parking Lot is full!")
        else:
            print("There are ",len(self.avail_spaces), " parking lots available")
            print("The available lots are: ")
            print(self.avail_spaces)
        print("Parking information: ")
        for item in self.parking_cars_info:
            print(item)

    def search_registration_numbers_with_colour(self, colour):
        registration_list = []
        for item in self.parking_cars_info:
            if (item.get("color") == colour):
                registration_list.append(item.get("registration number"))
        return registration_list

    def search_slot_numbers_with_colour(self, colour):
        slots_list = []
        for item in self.parking_cars_info:
            if (item.get("color") == colour):
                slots_list.append(item.get("lot number"))
        return slots_list

    def search_slot_numbers_with_registration_number(self, registration):
        slots_list = []
        for item in self.parking_cars_info:
            if (item.get("registration number") == registration):
                slots_list.append(item.get("lot number"))
        return slots_list

    def leave(self,lot_number):
        if (lot_number in self.avail_spaces):
            print("There is not a car parking in the lot ",lot_number)
        else:
            # Add this lot number back into the available spaces
            n_half = self.number_slots/2
            has_inserted = False
            if (lot_number <= n_half):
                for index in range(len(self.avail_spaces)):
                    if (self.avail_spaces[index]<=n_half and self.avail_spaces[index]>lot_number):
                        self.avail_spaces.insert(index,lot_number)
                        has_inserted = True
                        break
                    elif (self.avail_spaces[index]>n_half and (self.avail_spaces[index]-n_half>=lot_number)):
                        self.avail_spaces.insert(index,lot_number)
                        has_inserted = True
                        break
                if (has_inserted == False):
                    self.avail_spaces.append(lot_number)
            else:
                for index in range(len(self.avail_spaces)):
                    if (self.avail_spaces[index]<=n_half and self.avail_spaces[index]>(lot_number-n_half)):
                        self.avail_spaces.insert(index,lot_number)
                        has_inserted = True
                        break
                    elif (self.avail_spaces[index]>n_half and (self.avail_spaces[index]>lot_number)):
                        self.avail_spaces.insert(index,lot_number)
                        has_inserted = True
                        break
                if (has_inserted == False):
                    self.avail_spaces.append(lot_number)

            # Remove the info of this car from the parking info list
            for item in self.parking_cars_info:
                if (item['lot number'] == lot_number):
                    self.parking_cars_info.remove(item)
                    break


def parking_commands(parkings, commandstr):
    command_toks = commandstr.split()
    match (command_toks[0]):
        case 'create_parking_lot':
            # Check if the number of created parking space is missing
            if (len(command_toks) != 2):
                print("Usage: create_parking_lot <n>")
            elif (command_toks[1].isnumeric()==False):
                print("Usage: the size of parking lot has to be numeric!",command_toks[1])
            else:
                numspaces = int(command_toks[1])
                if (numspaces%2 != 0):
                    print("Usage: the parking number should be an even number")
                else:
                    parkings.create_parking_lot(int(command_toks[1]))
        case 'park':
            if (len(command_toks) != 3):
                print("Incorrect number of arguments! Usage: park <registration_number> <colour>")
            else:
                parkings.park(command_toks[1],command_toks[2])
        case 'status':
            if (len(command_toks) != 1):
                print("Too many arguments! Usage: status")
            else:
                parkings.getstatus()
        case 'leave':
            if (len(command_toks) != 2):
                print("Incorrect number of arguments! Usage: leave <slot>")
            elif (command_toks[1].isnumeric()==False):
                print("Usage: the parking lot has to be numeric!",command_toks[1])
            else:
                parkings.leave(int(command_toks[1]))
        case 'registration_numbers_for_cars_with_colour':
            if (len(command_toks) != 2):
                print("Incorrect number of arguments! Usage: registration_numbers_for_cars_with_colour <colour>")
            else:
                reg_list = parkings.search_registration_numbers_with_colour(command_toks[1])
                if (len(reg_list) == 0):
                    print("There are no car registration with the color ",command_toks[1])
                else:
                    print("The following car registration with color ",command_toks," are: ")
                    print(reg_list)
        case 'slot_numbers_for_cars_with_colour':
            if (len(command_toks) != 2):
                print("Incorrect number of arguments! Usage: slot_numbers_for_cars_with_colour <colour>")
            else:
                slot_list = parkings.search_slot_numbers_with_colour(command_toks[1])
                if (len(slot_list) == 0):
                    print("There are no car registration with the color ",command_toks[1])
                else:
                    print("The cars parking in the following slots are ",command_toks[1])
                    print(slot_list)
        case 'slot_number_for_registration_number':
            if (len(command_toks) != 2):
                print("Incorrect number of arguments! Usage: slot_number_for_registration_number <registration_number>")
            else:
                slot_list = parkings.search_slot_numbers_with_registration_number(command_toks[1])
                if (len(slot_list) == 0):
                    print("There are no car twith this given registration number")
                else:
                    print("The cars parking in the slot has the matching registration number ")
                    print(slot_list)

        case '-':
            print("Command not found")

if __name__ == "__main__":
    args = sys.argv[1:]

    parkings = parking_lot()
    if (len(args) > 0):
        file = open(args[0],"r")
        lines = file.read().splitlines()
        file.close()
        for commandline in lines:
            print(commandline)
            parking_commands(parkings,commandline)
    else:
        commandline = ""
        while (commandline != "exit"):
            commandline = input("Please input your command : ")
            if (commandline != ''):
                parking_commands(parkings,commandline)


