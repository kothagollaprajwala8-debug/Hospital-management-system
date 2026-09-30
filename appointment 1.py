# Appointment booking
print("\n[ APPOINTMENT BOOKING ]")
print("1. Book Slot")
print("2. View Scheduled Appointments")
sel = input("Option: ")

if sel == '1':
    p_name = input("Patient Name: ")
    d_name = input("Doctor Name: ")
    app_date = input("Date (DD-MM-YYYY): ")
    
    f = open("appointments.txt", "a")
    f.write(p_name + "," + d_name + "," + app_date + "\n")
    f.close()
    print("Appointment fixed!")

elif sel == '2':
    print("\nPATIENT | DOCTOR | DATE")
    print("-----------------------------------")
    try:
        f = open("appointments.txt", "r")
        for line in f:
            data = line.strip().split(",")
            if len(data) == 3:
                print(data[0] + " | " + data[1] + " | " + data[2])
        f.close()
    except:
        print("No appointments booked yet.")