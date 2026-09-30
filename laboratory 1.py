# Lab reports module
print("\n=== LABORATORY PORTAL ===")
print("1. New Test Request")
print("2. View Lab Results")
opt = input("Selection: ")

if opt == '1':
    p_name = input("Patient Name: ")
    t_type = input("Test Required (Blood/X-Ray/MRI): ")
    res = input("Result Summary: ")
    
    fp = open("lab.txt", "a")
    fp.write(p_name + "," + t_type + "," + res + "\n")
    fp.close()
    print("Lab report saved.")

elif opt == '2':
    print("\nPATIENT | TEST | RESULT")
    print("----------------------------------")
    try:
        fp = open("lab.txt", "r")
        for line in fp:
            row = line.strip().split(",")
            if len(row) == 3:
                print(row[0] + " | " + row[1] + " | " + row[2])
        fp.close()
    except:
        print("No lab data found.")