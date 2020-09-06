class hostel:
    def __init__(self,stud_name,hostel_name):
        self.name = stud_name
        self.hostel = hostel_name
        self.absent = {}

    def display_stud(self):
        print(f"We have these students in our hostel::{self.hostel}")
        for name in self.name:
            print(name)

    def stud_absent(self, hostel , name):
        if name not in self.absent.keys():
            self.absent.update({name:hostel})
            print("Attendence register has been updated")

    def stud_leave(self, name):
        self.name.remove(name)
        print("student  has been removed")

    def stud_new(self,name):
        self.name.append(name)
        print("A new student haas joined the hostel")

    def stud_abb(self):
        print(f"Students those are in hostel::{self.hostel}")
        print(*self.absent,sep="\n")

    def stud_pres(self):
        res = [i for i in self.name if i not in self.absent]
        print(*res,sep=("\n"))



if __name__ == '__main__':
    avi= hostel(["Abhinav","Chetan","Vikas","Karan","Sumit","Samyak"],"Nirwana")

    while(True):
        print(f"Welcome to the {avi.hostel} Hostel. Enter your choice to continue:::")
        print("1.Display Students Name")
        print("2.Student wants to take a leave ")
        print("3.Remove a Students from the list")
        print("4.Add a Students")
        print("5.Display students who are absent")
        print("6.Display students who are present")
        user_choice = int(input())

        if user_choice == 1:
            avi.display_stud()
        elif user_choice == 2:
            name = input("Enter the name of the student who is absent::")
            hostel = avi.hostel
            avi.stud_absent(hostel , name)
        elif user_choice == 3:
            name = input("Enter the student who wants to leave the hostel")
            avi.stud_leave(name)
        elif user_choice == 4:
            name = input("Enter the new student wants to live in hostel")
            avi.stud_new(name)
        elif user_choice == 5:
            print("Students who are absent are::")
            avi.stud_abb()
        elif user_choice == 6:
            print("Students who are present in hostel are ::")
            avi.stud_pres()
        else:
            print("Not A VaLID OPTION")

        print("Print q to exit and c to continue")
        choice2 = ""
        while(choice2 != "q" and choice2 != "c"):
            choice2=input()
        if choice2 == "q":
            exit()
        elif choice2 == "c":
            continue