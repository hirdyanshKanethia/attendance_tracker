import csv

def subjects():
    global subj_list
    subj_list = []
    print("\nEnter the subject names one by one. Enter 0 when you are done.")
    i=1
    while True:
        subj = input(f"Enter subject {i}: ")
        if subj.strip() ==  "0":
            choice = input("\nEnter y to confirm your subject list: ")
            if  choice.lower().strip() == "y":
                return
            else:
                print("\nConfirmation denied. Enter your subject list again")
                subjects()
        else:
            subj_list.append([subj.title().strip(), 0, 0, 0])
            i+=1


with open("attendance.csv", "w+", newline = '') as file:
    csv_writer = csv.writer(file)
    subjects()
    for row in subj_list:
        csv_writer.writerow(row)
    print("Subject list has been saved. You are ready to use the main program now")

