
# we start by importing the needed packages
# and declaring the needed variables

# the ast package is a package that converts a dictionary string to a dictionary that can be used by the programmer and vice versa  
import ast 

# the datetime package is a package that enables the programmer to record the date and time for registration for an example 
from datetime import datetime


registeredVehiclesDictionary = "registeredVehiclesDictionaryFile.txt"
parkedVehiclesDictionary = "parkedVehiclesDictionary.txt"
buildingsDictionary = "buildingsDictionaryFile.txt"
registeredVehiclesFile = "regidteredVehicles.txt"
parkedVehiclesFile = "parkedVehicles.txt"
buildingsFile = "buildings.txt"


NumberOfParkedVehicles = 0
dectionary = {}
dectionary1 = {}
validInputs = [1,2,3,4,5,6,7,8,9,10]
informationList = []
informationList1 = []

def main():
    
# inside main i called displayMenu to display the menu to the user on the screen
# i also called validateMenuInput, which is a function that has a while loop 
# that enables the user to choose what option from the menu that he want 
# until he choose option 10 then the program will terminate

    displayMenu()
    userInput = validateMenuInput (validInputs)

    while userInput != 10 :
        
        if userInput == 1 :

            print()
            registerVehicle (dectionary,informationList,registeredVehiclesDictionary)
            print()
            manageRegisteredVehiclesFile(registeredVehiclesDictionary,registeredVehiclesFile)
            displayMenu()
            userInput = validateMenuInput (validInputs)

        elif userInput == 2 :

            print()
            viewRegisteredVehicles (registeredVehiclesDictionary)
            print()
            displayMenu()
            userInput = validateMenuInput (validInputs)
            

        elif userInput == 3 :
            
            print()
            viewParkingBuildings(buildingsDictionary)
            print()
            displayMenu()
            userInput = validateMenuInput (validInputs)

        elif userInput == 4 :
            
            print()
            checkInForParking(dectionary1,informationList1,registeredVehiclesDictionary,parkedVehiclesDictionary)
            print()
            manageParkedVehiclesFile(parkedVehiclesDictionary,parkedVehiclesFile)
            displayMenu()
            userInput = validateMenuInput (validInputs)

        elif userInput == 5 :

            print()
            viewParkedVehicles(parkedVehiclesDictionary,buildingsDictionary)
            print()
            displayMenu()
            userInput = validateMenuInput (validInputs)

        elif userInput == 6 :

            print()
            searchVehicle(registeredVehiclesDictionary,parkedVehiclesDictionary)
            print()
            displayMenu()
            userInput = validateMenuInput (validInputs)

        elif userInput == 7 :

            print()
            checkOutParking(registeredVehiclesDictionary,parkedVehiclesDictionary,buildingsDictionary)
            print()
            displayMenu()
            userInput = validateMenuInput (validInputs)

        elif userInput == 8 :

            print()
            updateAParkingBuilding(buildingsDictionary)
            print()
            manageBuildingsFile(buildingsDictionary,buildingsFile)
            displayMenu()
            userInput = validateMenuInput (validInputs)

        elif userInput == 9 :

            print()
            printParkingStatistics(buildingsDictionary,parkedVehiclesDictionary)
            print()
            displayMenu()
            userInput = validateMenuInput (validInputs)


def displayMenu() :

# the the display menu function is the one, which will display the menu for the use

    print("KFUPM Parking Management System\n"
        "==============================\n"
        "1. Register a Vehicle\n"
        "2. View Registered Vehicles\n"
        "3. View Parking Buildings\n"
        "4. Check-in for Parking\n"
        "5. View Parked Vehicles\n"
        "6. Search a Vehicle\n"
        "7. Check-out Parking\n"
        "8. Update a Parking Building\n"
        "9. Print Parking Statistics\n"
        "10. Exit\n"
        "===============================")


def validateMenuInput (validInputs):

# the validate menu input function is a function that validates the user input for choosing an option from the menu
# and returns the user input

    found = False
    while not found :

        validInputs = [1,2,3,4,5,6,7,8,9,10]

        try:
            userInput = int(input("Enter your choice index (?): "))

            for i in validInputs:
                if i == userInput:
                    found = True

            if not found:
                print ("input should be between 1 to 10")
            
        except ValueError:
            print("input should be a digit between 1 to 10")
    return (userInput)


def manageParkedVehiclesFile(parkedVehiclesDictionary,parkedVehiclesFile):  

# Manage parked vehicles file is a function that will writing the information that is in the parked vehicles dictionary file
# in the parked vehicles file in a formatted way  

    f1 = open (parkedVehiclesDictionary,"r")
    f2 = open (parkedVehiclesFile,"w")

    f2.write("   vehicle plate number       KFUPM ID       building number       check in date and time \n")
    f2.write("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n")
    for string in f1:
        dectionary = ast.literal_eval(string.strip())
        for key in dectionary:
            plateNumber = key
            kfupmID = dectionary[key][0]
            buildingNumber = dectionary[key][1]
            checkInTime = dectionary[key][2]
            
            f2.write("          %-19s%-22s%-16s%-s\n" % (plateNumber,kfupmID,buildingNumber,checkInTime))
            f2.write("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n")
    f1.close()
    f2.close()


def manageBuildingsFile(buildingsDictionary,buildingsFile):

# Manage buildings  file is a function that will writing the information that is in the buildings dictionary file
# in the buildings file in a formatted way

    f1 = open(buildingsDictionary,"r")
    f2 = open(buildingsFile,"w")

    for string in f1:
        dectionary = ast.literal_eval(string.strip())

    f2.write("   building number    department name    parking capacity    number of parked vehicles    \n")
    f2.write("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n")

    for key in dectionary :
        
        buildingNumber = key
        departmentName = dectionary[key][0]
        parkingCapacity = dectionary[key][1]
        numberOfParkedVehicles = dectionary[key][2]

        f2.write("         %-13s%-26s%-25s%-s\n" % (buildingNumber,departmentName,parkingCapacity,numberOfParkedVehicles))
        f2.write("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n")

    f1.close()
    f2.close()


def manageRegisteredVehiclesFile(registeredVehiclesDictionary,registeredVehiclesFile) :

# Manage registered vehicles file is a function that will writing the information that is in the regidtered vehicles dectionary file
# in the registered vehicles file in a formatted way

    f1 = open (registeredVehiclesDictionary,"r")
    f2 = open (registeredVehiclesFile,"w")

    f2.write("   vehicle plate number        KFUPM ID        Iqama        vehicle model        manufacture year        vehicle color   \n")
    f2.write("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n")
    for string in f1:
        dectionary = ast.literal_eval(string.strip())
        for key in dectionary:
            plateNumber = key
            kfupmID = dectionary[key][0]
            iqama = dectionary[key][1]
            model = dectionary[key][2]
            manufactureYear = dectionary[key][3]
            carColor = dectionary[key][4]
            
            f2.write("          %-20s%-15s%-18d%-24s%-18d%-s\n" % (plateNumber,kfupmID,iqama,model,manufactureYear,carColor))
            f2.write("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n")
    f1.close()
    f2.close()


def registerVehicle (dectionary,informationList,registeredVehiclesDictionary):

    # register vehicle is a function that enables the user to register a vehicle 
    # for each input i used a while loop that will break if the sentinel found set to True
    # the sentinel will be set to True if a valid input is provided by the user
    # after that, the information will be written in the registered vehicles file

    informationList = []

    found = False
    while not found :

        vehiclePlate = input ("Eentr vehicle plate number: ")

        if len(vehiclePlate) > 7 :
            print ("vehicle plate should be a string of length 7 ")
        else:
            plateNumber = vehiclePlate[0:4]
            plateLetters = vehiclePlate[4:]

            if not plateNumber.isdigit() :
                print ("plate number should contain 4 digits and 3 letters respectively")
            elif not plateLetters.isalpha() :
                print ("plate number should contain 4 digits and 3 letters respectively")
            else:

                status = False

                with open (registeredVehiclesDictionary,"r") as f :

                    for string in f:
                        dectionary = ast.literal_eval(string.strip())
                        for key in dectionary:
                            if key == vehiclePlate :
                                status = True
                f.close()

                if status :
                    print ("plate number is already exists please try another one ")
                else:
                    found = True

    informationList.append(vehiclePlate)

    found = False
    while not found :
        kfupmID = input("Enter ID number: ")

        if len(kfupmID) != 10 :
            print("ID number should be 10 digits only")
        else:

            status = False

            with open (registeredVehiclesDictionary,"r") as f :

                for string in f:
                    dectionary = ast.literal_eval(string.strip())
                    for key in dectionary:
                        if dectionary[key][0] == kfupmID :
                            status = True
            f.close()
            
            if status :
                print ("ID number is already exists please try another one ")
            else:
                found = True

    informationList.append(kfupmID)

    found = False
    while not found :
        try:
            iqama = input("Enter iqama number: ")

            if len(iqama) != 10 :
                print("iqama number should be 10 digits")
            else:
                iqama = int(iqama)
                found = True

        except ValueError :
            print("iqama number should be in digits ")

    informationList.append(iqama)

    found = False
    while not found :
        model = input("Enter vehicle model name: ")

        if model == "":
            print ("vehicle model name cannot be empty")
        else :
            found = True

    informationList.append(model)


    found = False
    while not found :
        try:
            manufactureYear = input("Enter car manufacture Year: ")

            if len(manufactureYear) != 4 :
                print ("car manufacture Year should be 4 digits ")
            else:
                manufactureYear = int(manufactureYear)
                found = True

        except ValueError :
            print ("car manufacture Year should be in digits")
    informationList.append(manufactureYear)


    found = False
    while not found :

        carColor = input("Enter car color: ")

        carColor = carColor.strip()

        if carColor == "":
            print("car color cannot ba an empty string ")
        else:
            found = True

    informationList.append(carColor)

    dectionary[informationList.pop(0)] = informationList

    with open (registeredVehiclesDictionary,"w") as f :
        f.write(str(dectionary))
        f.close()
    
    return(registeredVehiclesDictionary)


def viewRegisteredVehicles (registeredVehiclesDictionary):

# view registered vehicles is a function that takes registered vehicles dictionary file as a parameter then it will read it 
# then it will display the registered vehicles in a properly formatted way to the user

    print("   vehicle plate number    KFUPM ID    vehicle model    manufacture year    vehicle color     ")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")

    with open( registeredVehiclesDictionary , "r") as f:



        for string in f:

                dectionary = ast.literal_eval(string.strip())
                for key in dectionary:
                    
                    plateNumber = key
                    kfupmID = dectionary[key][0]
                    model = dectionary[key][2]
                    manufactureYear = dectionary[key][3]
                    carColor = dectionary[key][4]
                    print("          %-16s%-16s%-20s%-15d%-12s" % (plateNumber,kfupmID,model,manufactureYear,carColor))
                    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        f.close()


def viewParkingBuildings(buildingsDictionary):

# view parking buildings is a function that takes the parking buildings dictionary file as a parameter then it will read it 
# then it will display the parking buildings in a properly formatted way to the user

    with open(buildingsDictionary,"r") as f :

        for string in f:
            dectionary = ast.literal_eval(string.strip())

        print ("   building number    department name    parking capacity    number of parked vehicles    ")
        print ("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")

        for key in dectionary :
            
            buildingNumber = key
            departmentName = dectionary[key][0]
            parkingCapacity = dectionary[key][1]
            numberOfParkedVehicles = dectionary[key][2]

            print ("         %-13s%-26s%-25s%-s" % (buildingNumber,departmentName,parkingCapacity,numberOfParkedVehicles))
            print ("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")

        f.close()


def checkInForParking(dectionary1,informationList1,registeredVehiclesDictionary,parkedVehiclesDictionary) :

# check-in for parking is a function that validates the information that is needed from the user to check-in
# by matching the user input with the information from the registered vehicles dictionary file and the parking buildings dictionary file
# it also records the check-in time and writes the parked vehicles' information in the parked vehicles file through manageParkedVehiclesFile

    informationList1 = []

    found = False
    while not found :

        vehiclePlate = input ("Eentr vehicle plate number: ")

        plateNumber = vehiclePlate[0:4]
        plateLetters = vehiclePlate[4:]

        if not plateNumber.isdigit() :
            print ("plate number should contain 4 digits and 3 letters respectively")
        elif not plateLetters.isalpha() :
            print ("plate number should contain 4 digits and 3 letters respectively")  
        else:

            status1 = False
            status2 = False

            with open( registeredVehiclesDictionary , "r") as f:

                for string in f:
                    dectionary = ast.literal_eval(string.strip())
                    for key in dectionary:
                        if key == vehiclePlate :
                            status1 = True
            f.close()

            with open( parkedVehiclesDictionary , "r") as f:

                for string in f:
                    dectionary = ast.literal_eval(string.strip())
                    for key in dectionary:
                        if key == vehiclePlate :
                            status2 = True

            if status1 and not status2 :
                found = True
            elif status1:
                print("vehicle has already check in for parking please try another one ")
            else:
                print ("plate number does not exist please try another one ")
    informationList1.append(vehiclePlate)

    found = False
    while not found :

        kfupmID = input("Enter ID number: ")

        if len(kfupmID) != 10 :
            print("ID number should be 10 digits only")
        else:

            status = False

            with open( registeredVehiclesDictionary , "r") as f:

                for string in f:

                    dectionary = ast.literal_eval(string.strip())

                    for key in dectionary:

                        if key == vehiclePlate :

                            validateID = list(dectionary[key])

                            if validateID[0] == kfupmID :
                                status = True
                        
            f.close()
            
            if status :
                found = True
            else:
                print ("vehicle plate does not match ID number")
    informationList1.append(kfupmID)

    status1 = False
    status2 = False
    found = False
    while not found :
        buildingNumber = input("Enter building number: ")

        if len(buildingNumber) != 3 :
            print("building number should be 3 digits")
        else:

            status1 = False
            status2 = False


            with open (buildingsDictionary,"r") as f1 :

                for string in f1:
                    dectionary = ast.literal_eval(string.strip())
                    for key in dectionary:
                        if key == buildingNumber:
                            status1 = True                          
                            parkingCapacity = dectionary[buildingNumber][1]
                            numberOfParkedVehicles = dectionary[buildingNumber][2]
                            numberOfParkedVehicles = numberOfParkedVehicles + 1
                            updatedNumberOfParkedVehicles = numberOfParkedVehicles

                            if parkingCapacity < updatedNumberOfParkedVehicles :
                                status2 = True
                            else:
                                dectionary[buildingNumber][2] = updatedNumberOfParkedVehicles
            f1.close()
            with open (buildingsDictionary,"w") as f2 :
                f2.write(str(dectionary))
                f2.close()

        if status1 and status2:
            print ("building is already filled please try another one")
        elif status1 and not status2:

            found = True
        else :
            print ("building number does not exist")
    informationList1.append(buildingNumber)    

    ts = datetime.timestamp(datetime.now()) 
    checkInTime = datetime.fromtimestamp(ts)

    date = str(checkInTime.date())
    hours = str(checkInTime.hour)
    minutes = str(checkInTime.minute)

    checkInTime = ("%s, Time(%s, %s)" % (date,hours,minutes))

    informationList1.append(checkInTime)

    with open (parkedVehiclesDictionary,"r") as f :

        for string in f:
            dectionary1 = ast.literal_eval(string.strip())
    f.close()

    dectionary1[informationList1.pop(0)] = informationList1

    with open (parkedVehiclesDictionary,"w") as f :
        f.write(str(dectionary1))
    f.close()
    
    manageBuildingsFile(buildingsDictionary,buildingsFile)
    manageParkedVehiclesFile(parkedVehiclesDictionary,parkedVehiclesFile)
    manageRegisteredVehiclesFile(registeredVehiclesDictionary,registeredVehiclesFile)

    return(parkedVehiclesDictionary)


def viewParkedVehicles(parkedVehiclesDictionary,buildingsDictionary):

# view parked vehicles is a function that takes parked vehicles dectionary file and buildings dictionary file as parameters then it will take the user input
# which is the building number then it will disply the parked vehicles in that building in a properly formatted way to the user

    status = False
    found = False
    while not found :
        buildingNumber = input("Enter building number: ")

        if len(buildingNumber) != 3 :
            print("building number should be 3 digits")
        elif not buildingNumber.isdigit() :
            print("building number should be digits")
        else:
            with open(buildingsDictionary,"r") as f1 :
                
                for string in f1:
                    dectionary = ast.literal_eval(string.strip())

                for key in dectionary :
                    if key == buildingNumber :
                        status = True
            f1.close()

        if status:
            found = True
        else:
            print("building number does not exist")

    with open (parkedVehiclesDictionary,"r") as f2 :
        for string in f2:
            dectionary1 = ast.literal_eval(string.strip())
        
        print()
        print("   vehicle plate number       KFUPM ID       check in date and time ")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")


        if dectionary[buildingNumber][2] == 0 :
            print()
            print ("There are no vehicles in this building ")
            print()
        else:
            for key in dectionary1 :
                if dectionary1[key][1] == buildingNumber :
                    plateNumber = key
                    kfupmID = dectionary1[key][0]
                    checkInTime = dectionary1[key][2]
                    
                    print("          %-19s%-16s%-s" % (plateNumber,kfupmID,checkInTime))
                    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                    print()
    f2.close()


def searchVehicle(registeredVehiclesDictionary,parkedVehiclesDictionary):

# search vehicle function is a function that takes from the user the vehicle plate as input then it will display the registration information 
# and if it is parked inside the campus it will display the building that is parked inside it and the check-in time 

    found = False
    while not found :

        vehiclePlate = input ("Eentr vehicle plate number: ")

        plateNumber = vehiclePlate[0:4]
        plateLetters = vehiclePlate[4:]

        if not plateNumber.isdigit() :
            print ("plate number should contain 4 digits and 3 letters respectively")
        elif not plateLetters.isalpha() :
            print ("plate number should contain 4 digits and 3 letters respectively")
        else:

            status = False

            with open (registeredVehiclesDictionary,"r") as f1 :

                for string in f1:
                    dectionary = ast.literal_eval(string.strip())
                    for key in dectionary:
                        if key == vehiclePlate :
                            status = True
            f1.close()

            if status :
                found = True
            else:
                print ("plate number does not exists please try another one ")

    print()
    print("   vehicle plate number    KFUPM ID    vehicle model    manufacture year    vehicle color     ")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")

    with open( registeredVehiclesDictionary , "r") as f2:

        for string in f2:

                dectionary = ast.literal_eval(string.strip())
                for key in dectionary:
                    if key == vehiclePlate :
                        plateNumber = key
                        kfupmID = dectionary[key][0]
                        model = dectionary[key][2]
                        manufactureYear = dectionary[key][3]
                        carColor = dectionary[key][4]
                        print("          %-16s%-16s%-20s%-15d%-12s" % (plateNumber,kfupmID,model,manufactureYear,carColor))
                        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    f2.close()

    status = False
    with open (parkedVehiclesDictionary,"r") as f3 :

        for string in f3:
            dectionary = ast.literal_eval(string.strip())
            for key in dectionary:
                if key == vehiclePlate :
                    status = True
    

        if status :
            print("   Parking Status: parked inside the campus in building %s and the check-in time is %s" % (dectionary[key][1],dectionary[key][2]))
            print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        else:
            print("   Parking Status: not parked inside the campus")
            print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    f3.close()


def checkOutParking(registeredVehiclesDictionary,parkedVehiclesDictionary,buildingsDictionary):

# check out parking is a function that will delete the corresponding information for the vehicle plate that is provided by the user
#  from the registered vehicles file and the  parked vehicles file. It also updates the number of parked vehicles in the buildings file 

    found = False
    while not found :

        vehiclePlate = input ("Eentr vehicle plate number: ")

        print()

        plateNumber = vehiclePlate[0:4]
        plateLetters = vehiclePlate[4:]

        if not plateNumber.isdigit() :
            print ("plate number should contain 4 digits and 3 letters respectively")
        elif not plateLetters.isalpha() :
            print ("plate number should contain 4 digits and 3 letters respectively")
        else:

            status1 = False
            status2 = False

            with open (registeredVehiclesDictionary,"r") as f1 :

                for string in f1:
                    dectionary = ast.literal_eval(string.strip())
                    for key in dectionary:
                        if key == vehiclePlate :
                            status1 = True
            
            with open (parkedVehiclesDictionary,"r") as f2 :
                
                for string in f2:
                    dectionary = ast.literal_eval(string.strip())
                    for key in dectionary:
                        if key == vehiclePlate :
                            status2 = True

            if status1 and status2 :

                print("   vehicle plate number       KFUPM ID       building number       check in date and time ")
                print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")

                for key in dectionary:
                    if key == vehiclePlate :
                        plateNumber = key
                        kfupmID = dectionary[key][0]
                        buildingNumber = dectionary[key][1]
                        checkInTime = dectionary[key][2]
                        
                        print("          %-19s%-22s%-16s%-s" % (plateNumber,kfupmID,buildingNumber,checkInTime))
                        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                        found = True
            elif status1 :
                print("plate number is not checked in please try another one")            
            else:
                print("plate number does not exists please try another one ")
    
    f1.close()
    f2.close()

    status = False
    found = False
    
    print()

    while not found :

        confirmation = input ("Enter y for yes or n for no to confiarm check out Parking: ")

        print()

        if confirmation.lower() == "y" :

            with open (registeredVehiclesDictionary,"r") as f3 :

                for string in f3:
                    dectionary = ast.literal_eval(string.strip())
                    for key in dectionary:
                        if key == vehiclePlate :
                            status = True
                                                                      

                if status :
                    with open (parkedVehiclesDictionary,"r") as f4:

                        for string in f4:
                            dectionary1 = ast.literal_eval(string.strip())

                        with open (buildingsDictionary,"r") as f5 :
                            for string in f5 :
                                dectionary2 = ast.literal_eval(string.strip())
                            for key in dectionary2:
                                if dectionary1[vehiclePlate][1] == key:
                                    dectionary2[key][2] = int(dectionary2[key][2]) - 1
                            f5.close()

                        dectionary1.pop(vehiclePlate)
                        f4.close()
                        
                if status :
                    dectionary.pop(vehiclePlate)
                    f3.close()

                with open (registeredVehiclesDictionary,"w") as f6 :
                    f6.write(str(dectionary))
                    f6.close()

                with open (parkedVehiclesDictionary,"w") as f7 :
                    f7.write(str(dectionary1))
                    f7.close()

                with open (buildingsDictionary,"w") as f8 :
                    f8.write(str(dectionary2))
                    f8.close()

            manageBuildingsFile(buildingsDictionary,buildingsFile)
            manageParkedVehiclesFile(parkedVehiclesDictionary,parkedVehiclesFile)
            manageRegisteredVehiclesFile(registeredVehiclesDictionary,registeredVehiclesFile)
            found = True
        elif confirmation.lower() == "n" :
            manageBuildingsFile(buildingsDictionary,buildingsFile)
            manageParkedVehiclesFile(parkedVehiclesDictionary,parkedVehiclesFile)
            manageRegisteredVehiclesFile(registeredVehiclesDictionary,registeredVehiclesFile)
            found = True
        else:
            print("please enter valid letter")


def updateAParkingBuilding(buildingsDictionary):

# update a parking building is a function that enables the user to change the building name or capacity. 
# it also validates if the new parking capacity is less than the already parked vehicles if that is the case then an error message will be displayed 

    status = False
    found = False
    while not found :
        buildingNumber = input("Enter building number: ")

        with open(buildingsDictionary,"r") as f1 :
                
                for string in f1:
                    dectionary = ast.literal_eval(string.strip())

                for key in dectionary :
                    if key == buildingNumber :
                        status = True
        f1.close()


        if len(buildingNumber) != 3 :
            print("building number should be 3 digits")
        elif not buildingNumber.isdigit() :
            print("building number should be digits")
        else:

            if status :
                found = True

                with open(buildingsDictionary,"r") as f1 :

                    for string in f1:
                        dectionary = ast.literal_eval(string.strip())
                    for key in dectionary :
                        if key == buildingNumber :

                            print ("   building number    department name    parking capacity    number of parked vehicles    ")
                            print ("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")

                            
                                
                            buildingNumber = key
                            departmentName = dectionary[key][0]
                            parkingCapacity = dectionary[key][1]
                            numberOfParkedVehicles = dectionary[key][2]

                            print ("         %-13s%-26s%-25d%-d" % (buildingNumber,departmentName,parkingCapacity,numberOfParkedVehicles))
                            print ("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")

                            f1.close()
                            print()
                            print("Options menu\n" 
                                "=========================================================\n"
                                "1. Modify building name \n"
                                "2. Modify building parking capacity\n"
                                "3. Modify building name and parking capacity\n"
                                "4. continue without modifications \n"
                                "=========================================================\n")

                            found = False
                            while not found :
                                userInput = input ("Choose your option: ")

                                if userInput == "1" :

                                    newBuildingName = input("Enter the new building name: ")
                                    dectionary[buildingNumber][0] = newBuildingName

                                    with open(buildingsDictionary,"w") as f2 :
                                        f2.write(str(dectionary))
                                        f2.close()
                                    manageBuildingsFile(buildingsDictionary,buildingsFile)
                                    found = True

                                elif userInput == "2" :
                                    
                                    while not found :
                                        newPrkingCapacity = input ("Enter the new parking capacity: ")
                                        if int(newPrkingCapacity) < dectionary[buildingNumber][2] :
                                            print ("the new parking capacity cannot be less than the number of parked vehicles, which is %d " % dectionary[buildingNumber][2] )
                                        else:
                                            dectionary[buildingNumber][1] = int(newPrkingCapacity)

                                            with open(buildingsDictionary,"w") as f3 :
                                                f3.write(str(dectionary))
                                                f3.close()
                                            manageBuildingsFile(buildingsDictionary,buildingsFile)
                                            found = True

                                elif userInput == "3" :

                                    while not found :
                                        newPrkingCapacity = input ("Enter the new parking capacity: ")
                                        if int(newPrkingCapacity) < dectionary[buildingNumber][2] :
                                            print ("the new parking capacity cannot be less than the number of parked vehicles, which is %d " % dectionary[buildingNumber][2] )
                                        else:
                                            newBuildingName = input("Enter the new building name: ")
                                            dectionary[buildingNumber][0] = newBuildingName
                                            dectionary[buildingNumber][1] = int(newPrkingCapacity)

                                            with open(buildingsDictionary,"w") as f4 :
                                                f4.write(str(dectionary))
                                                f4.close()
                                            manageBuildingsFile(buildingsDictionary,buildingsFile)
                                            found = True

                                elif userInput == "4" :
                                    found = True

                                else:
                                    print ("please enter a valid input from the menu")
            else:
                print("building number does not exist please try again")


def printParkingStatistics(buildingsDictionary,parkedVehiclesDictionary):

# print parking statistics is a function that will display the building information and the parked vehicles inside it
# if the building has no parked vehicles inside it then the function displays a message that says that the building has no parked vehicles inside it 

    with open(buildingsDictionary,"r") as f1 :

        for string in f1:
            dectionary1 = ast.literal_eval(string.strip())
       
        for key in dectionary1 :
            print()
            print ("   building number    building name    total parking capacity    number of parked cars    space available   ")
            print ("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")

            buildingNumber = key
            departmentName = dectionary1[key][0]
            parkingCapacity = dectionary1[key][1]
            numberOfParkedVehicles = dectionary1[key][2]
            spaceAvailble = parkingCapacity - numberOfParkedVehicles

            print ("         %-13s%-26s%-25s%-24d%-d" % (buildingNumber,departmentName,parkingCapacity,numberOfParkedVehicles,spaceAvailble))
            print ("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print()
            print("List of all parked cars information")
            print()
            with open (parkedVehiclesDictionary,"r") as f2 :
                for string in f2:
                    dectionary2 = ast.literal_eval(string.strip())
                if dectionary1[key][2] == 0 :
                    print("There are no parked vehicles in this building ")
                    print()
                else:
                    print("   vehicle plate number       KFUPM ID       check in date and time ")
                    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")

                    for key in dectionary2 :
                        if dectionary2[key][1] == buildingNumber :
                            plateNumber = key
                            kfupmID = dectionary2[key][0]
                            checkInTime = dectionary2[key][2]
                            
                            print("          %-19s%-16s%-s" % (plateNumber,kfupmID,checkInTime))
                            print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")

        f1.close()
        f2.close()


main()