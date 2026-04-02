print("========================================================================================================")
title = "ACT"
motto = "YOUR REVISION HUB"
print( title.center(100))
print( motto.center(100))
print("========================================================================================================")
print ("Manage your course materials and track your revision progress.\n")
print(f"Welcome aboard, sir/madam\n\n")

name = input("Enter your name: ")
user_name = input("Enter your user_name: ")
if not user_name:
    user_name = "student"
email = input("Enter email: ")
password = input("Enter password: ")
course = input("\nEnter course: ")
number_of_course_units = int(input(f"Number of vourse untis had in {course}: "))

course_units = []
for i in range (number_of_course_units):
    course_units.append(input(f"Enter course unit {i + 1}: "))
    
while(True):
    print("\n\nOptions\n")
    print("1. Upload a paper into storage.")
    print("2. Upload a presentation or revision material.")
    print("3. Upload a video about a course unit.")
    print("4. Delete a document from storage.")
    print("5. View the documments stored in memory ")
    print("6. Exit.")
    choice = input("Option chosen: ")
    if(choice == '1'):
        paper = input("Enter the paper path you want to upload: ")
    elif(choice == '2'):
        file = input("Enter the document path you want to upload: ")
    elif(choice == '3'):
        video = input("Enter the video path you want to upload: ")
    elif(choice == '4'):
        doc = input("Enter the name of the document you want to delete: ")
    elif(choice == '5'):
        dfile = input("Enter the document you want to view: ")
    elif(choice == '6'):
        print("Exiting from ACT. Thank you")
        exit(0)
    else:
        print("Invalid option inserted, please try again")