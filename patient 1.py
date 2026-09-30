# Patient registration module
print("\n=== PATIENT PORTAL ===")
print("1. Register Patient")
print("2. View Patient List")
ch = input("Enter choice (1-2): ")

if ch == '1':
    p_name = input("Patient Name: ")
    p_age = input("Age: ")
    p_phone = input("Phone Number: ")
    
    f = open("patients.txt", "a")
    f.write(p_name + "," + p_age + "," + p_phone + "\n")
    f.close()
    print("Patient added!")

elif ch == '2':
    print("\nNAME\t\tAGE\tPHONE")
    print("--------------------------------")
    try:
        f = open("patients.txt", "r")
        for line in f:
            rec = line.strip().split(",")
            if len(rec) == 3:
                print(rec[0] + "\t\t" + rec[1] + "\t" + rec[2])
        f.close()
    except:
        print("No patient records found.")