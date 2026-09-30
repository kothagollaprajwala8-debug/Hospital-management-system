# Hospital Management System Main Hub

while True:
    print("\n========================================")
    print("      HOSPITAL MANAGEMENT SYSTEM        ")
    print("========================================")
    print("1. Patient Portal")
    print("2. Doctor Section")
    print("3. Receptionist Desk")
    print("4. Book Appointment")
    print("5. Medical Records")
    print("6. Laboratory")
    print("7. Pharmacy")
    print("8. Billing Counter")
    print("9. Room Allotment")
    print("10. Staff Directory")
    print("11. Hospital Summary Report")
    print("12. Exit Program")
    
    m_choice = input("Select Option (1-12): ")

    if m_choice == '1':
        exec(open("patient.py").read())
    elif m_choice == '2':
        exec(open("doctor.py").read())
    elif m_choice == '3':
        exec(open("receptionist.py").read())
    elif m_choice == '4':
        exec(open("appointment.py").read())
    elif m_choice == '5':
        exec(open("medical_records.py").read())
    elif m_choice == '6':
        exec(open("laboratory.py").read())
    elif m_choice == '7':
        exec(open("pharmacy.py").read())
    elif m_choice == '8':
        exec(open("billing.py").read())
    elif m_choice == '9':
        exec(open("room.py").read())
    elif m_choice == '10':
        exec(open("staff.py").read())
    elif m_choice == '11':
        exec(open("reports.py").read())
    elif m_choice == '12':
        print("Exiting application. Have a good day!")
        break
    else:
        print("Invalid selection, please enter 1 to 12.")