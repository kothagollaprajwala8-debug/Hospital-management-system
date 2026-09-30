# Billing counter module
print("\n--- BILLING COUNTER ---")
print("1. Generate Patient Bill")
print("2. View Bill Records")
b_choice = input("Select choice: ")

if b_choice == '1':
    name = input("Patient Name: ")
    doc_charge = int(input("Doctor Fee: "))
    med_charge = int(input("Medicine Charges: "))
    grand_total = doc_charge + med_charge
    
    f = open("bills.txt", "a")
    f.write(name + "," + str(doc_charge) + "," + str(med_charge) + "," + str(grand_total) + "\n")
    f.close()
    print("Total Bill = Rs.", grand_total)

elif b_choice == '2':
    print("\nPATIENT | DOC FEE | MED FEE | TOTAL")
    print("------------------------------------------")
    try:
        f = open("bills.txt", "r")
        for line in f:
            b = line.strip().split(",")
            if len(b) == 4:
                print(b[0] + " | Rs." + b[1] + " | Rs." + b[2] + " | Rs." + b[3])
        f.close()
    except:
        print("No billing history.")