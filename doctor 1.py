# Doctor details section
print("\n*** DOCTOR MODULE ***")
print("1. Add New Doctor")
print("2. Display Doctors")
opt = input("Choice: ")

if opt == '1':
    dname = input("Doctor Name: ")
    spec = input("Specialization: ")
    fee = input("Consultation Fee: ")
    
    fp = open("doctors.txt", "a")
    fp.write(dname + "|" + spec + "|" + fee + "\n")
    fp.close()
    print("Doctor details saved.")

elif opt == '2':
    print("\nNAME | SPECIALIZATION | FEE")
    print("====================================")
    try:
        fp = open("doctors.txt", "r")
        for line in fp:
            item = line.strip().split("|")
            if len(item) == 3:
                print(item[0] + " | " + item[1] + " | Rs." + item[2])
        fp.close()
    except:
        print("No doctor data available.")