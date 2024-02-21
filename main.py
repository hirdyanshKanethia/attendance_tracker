# content composition
# subjecy   classes attended    classes occured     attendance %age

import csv
import pandas as pd
from tabulate import tabulate 




# ********************** FUNCTIONS ******************************

def create_data():
    # 'data' variable to store data for the table 
    global data, content
    data = {
        "S.No": [i for i in range(1,len(content)+1)],
        "Subjects": [row[0] for row in content], 
        "Classes attended": [row[1] for row in content],
        "Classes occured": [row[2] for row in content],
        "Attendance rate (%)": ["NA" if (int(row[2]) == 0) else (str((int(row[1])/int(row[2]))*100) + "%") for row in content]
    }




def print_data_table():
    global data
    df = pd.DataFrame(data)
    table = tabulate(df, headers = 'keys', tablefmt = 'pretty', showindex = False)
    print(table)




def raw_data_entry(index_subj):
    global content
    data_row = content[index_subj-1]

    while True:
        class_attended = input(f"\nEnter the total number of classes of {data_row[0]} that you have attended: ")
        class_occured = input(f"\nEnter the total number of classes of {data_row[0]} that have taken place till now: ")

        if class_attended.isdigit() and class_occured.isdigit():
            if int(class_attended) >= 0 and int(class_occured) >= int(class_attended):
                break
            else:
                print("\nThe combination of these inputs is not valid. Please enter a valid input")
        else:
            print("\nInvalid Input! Please enter valid positive integers only")

    # while True:
    #     class_attended = input(f"\nEnter the total number of classes you have attended of {data_row[0]}: ")
    #     if int(class_attended) >= 0:
    #         break
    #     else:
    #         print("\nInvalid Input! Please enter a valid number")

    # while True:
    #     class_occured = input(f"\nEnter the total number of classes that have occured till now of the subject {data_row[0]}: ")
    #     if int(class_occured) >= int(class_attended):
    #         break
    #     else:
    #         print("\nInvalid Input! Please enter a valid number")
    
    while True:
        confirmation = input(f'''\nThis is the data you entered
\nClasses attended of {data_row[0]}: {class_attended}
Classes occured of {data_row[0]}: {class_occured}
\nDo you want to finalize these changes?
Enter y for yes 
Enter n to enter the numbers again
Enter b to go back to the subject selection: ''')
        if confirmation.strip().lower() == "y":
            data_row[1] = str(class_attended)
            data_row[2] = str(class_occured)
            create_data()
            break

        elif confirmation.strip().lower() == "n":
            raw_data_entry(index_subj)
        
        elif confirmation.strip().lower() == "b":
            print("\nNow going back to the subject selection")
            break

        else:
            print("\nIncorrect Input! Please enter a valid input")

        
def previous_data_entry(index_subj):
    global content
    data_row = content[index_subj-1]

    while True:
        class_occured = input(f"\nEnter the number of classes of {data_row[0]} that have taken place today: ")
        if class_occured.isdigit():
            if int(class_occured) >= 1:
                break
            else:
                print("Invalid Input. Please enter a +ve value greater than 1")
        else:
            print("Invalid Input. Please enter an integer value")

    while True:
        class_attended = input(f'''\nDid you attend the class/classes
Enter y for yes
Enter n for no: ''')
        if  class_attended.strip().lower() == 'y':
            data_row[1] = str(int(data_row[1])+int(class_occured))
            data_row[2] = str(int(data_row[2])+int(class_occured))
            create_data()
            break
        elif class_attended.strip().lower() == 'n':
            data_row[2] = str(int(data_row[2])+int(class_occured))
            create_data()
            break
        else:
            print("\nInvalid Input! Please enter a valid input")


def save_data():
    with open('attendance.csv', 'w+', newline='') as file:
        csv_writer = csv.writer(file)
        for row in content:
            csv_writer.writerow(row)
        print("\nYOUR DATA HAS BEEN SAVED. THANK YOU, MEET YOU TOMORROW\n")





# ******************************** MAIN ************************************

with open("attendance.csv", "a+") as file:
    file.seek(0)
    # 'csv_reader' and 'content' variables to store the contents of the csv file
    global csv_reader, content
    csv_reader = csv.reader(file) 
    content = []
    for row in csv_reader:
        row
        content.append(row)

# Welcome interface for the start of the program
print(     "\n\n********************************************************")
print("********    WELCOME TO THE ATTENDANCE TRACKER    ********")
print(     "********************************************************")
print("\nThis is your previous data->\n")
create_data()
print_data_table()
print("NOTE - PLEASE INCREASE YOUR WINDOW SIZE IF THE TABLE IS DISTORTED")

while True:
    subj_choice = input('''\nEnter the subject number from the table
Enter p to print the table with the currently made changes
Enter s if you want to save the changes and end the session: ''')
    
    # if block to handle the case of selection of a subject
    if subj_choice.lower().strip() in [str(i) for i in range(1, len(content)+1)]:
        print(f"\nYou have selected the subject: {content[int(subj_choice)-1][0]}")
        while True:
            data_entry_choice = input('''\nEnter u to update previous data in the table
Enter r to put raw data in the table
Enter 0 if you want to go to the previous step: ''')
            if data_entry_choice.lower().strip() == 'r':
                print()
                raw_data_entry(int(subj_choice))
                break

            elif data_entry_choice.lower().strip() == 'u':
                print()
                previous_data_entry(int(subj_choice))
                break

            elif data_entry_choice.lower().strip() == '0':
                print("\nNow going back to the previous step")
                break

            else:
                print('\nInvalid Input! Please try again')

    elif subj_choice.lower().strip() == 'p':
        print_data_table()
    
    elif subj_choice.lower().strip() == 's':
        print()
        save_data()
        break
    
    else:
        print('\nInvalid Input! Please try again')
