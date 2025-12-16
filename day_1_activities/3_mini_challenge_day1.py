# Project Prompt:

# You are hired to build a Student Lookup Tool for a school front office. The secretary must be able to:

    # Enter a student’s full name

    # Instantly see:

            # CPS ID

            # Homeroom

            # Grade Level

            # Primary Email

            # Students must:

            # Describe the search process

## be able to add new data
# Your program must allow the secretary to ADD a brand new student
# into the system while the program is running.

# Your job is to let the secretary type in a new student just like filling out a registration form.
# Once the form is complete, your program must turn that information into a dictionary and add it to the main list of students.
# If the student already exists (same CPS ID), your program must block the entry to prevent duplicates.

# The program should:
    # 1. Ask the user for the following information:
    #    - CPS ID
    #    - First Name
    #    - Last Name
    #    - Middle Name
    #    - Homeroom
    #    - Grade Level
    #    - Primary Email
    #    - Secondary Email

# 2. Combine the First and Last name into this format:
    #    "Last, First"  

# 3. Store all of the new information into ONE dictionary
    #    that matches the structure of the existing student data.

# 4. Add (append) that new dictionary into the main students list.

# 5. After adding the student, the program must:
    #    - Print a confirmation message
    #    - Print the total number of students in the system
    #    - Print the newly added student record

# 6. The program must NOT delete or overwrite any existing students.

# 7. If the CPS ID already exists in the system:
        #    - Do NOT add the student
        #    - Display an error message saying the CPS ID is already taken


import student_data2 #imports our data from our other set

student_data = student_data2.students # reference to our dictionary set

create_response = False # Boolean
Start_New_Response = input("Would you like to add a new response? (Yes or No): ")

if Start_New_Response == "Yes": #this part works
    create_response = True
else:
    print("Response Declined, Rerun program to add a response")

while create_response: # if create_reponse == true then we are taking responses 
    for response in student_data: # Creates a loop to iterate through our data
        student_ID = int(input("CPS ID?: "))

        if student_ID == response.items():
            print("ID is already in the system, Please Retry")
            break

        student_data[0].update({"CPSID":student_ID}) #Add student ID to dictionary

        student_data[0].update(["LName"]) == input("Last Name?: ")
        student_data[0].update(["FName"]) == input("First Name?: ")
        student_data[0].update(["MName"]) == input("Middle Name?: ")
        student_data[0].update(["Combo,Name"]) == (["FName" + "LName"])

        student_data[0].update(["HR"]) == input("Home Room?: ")
        student_data[0].update(["GL"]) == int(input("Grade Level?: "))

        student_data[0].update(["Email"]) == input("Primary Email?: ") + input("Secondary Email")


        print(student_data) #for testing
        
        # for key, value in student_data.items():
        #     if value == "":


        

        # student_data.update() == input("Last Name?: ") # we need .update, .append is for adding the student to the dictionary
        

        # student_data.update(["FName"]) == input("First Name?: ") 
        # student_data.update(["HR"]) == input("Homeroom?: ")
        # print(student_data) # To see if it adds it to the dictionary
        # Grade_Level = int(input("Grade Level?: "))
        # Primary_Email = input("Primary Email?:")
        # Secondary_Email = input("Secondary Email?: ")
