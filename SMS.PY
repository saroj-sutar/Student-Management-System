# Student Management System

# Features:

# Add student (code done)
# Search student by ID (code done)
# Update marks (code done)
# Delete student (code done)

# Concepts used:
# Classes, objects, lists, loops

std_data = []
std_unique = []

class SMS :
    
    def __init__ (self, name, id, marks):
        self.name = name
        self.marks = marks
        self.id = id

        data = {
            "name" : self.name,
            "id" : self.id,
            "Marks" : self.marks
        }

        std_data.append(data)
        print("Student add sucessfull.......!")

    
    def search_std (self):
        ent_id = int(input("Enter you id "))
        i = 0
        found = "no"
        for serid in std_data:
            while i < len(std_data):
                if serid["id"] == ent_id:
                    found = "yes"
                    print(std_data[i])
                    break
                else:
                    break
            i = i+1
        
        if found == "no":
            print("Enter valid id......!")


    def delete_std (self):
        ent_id = int(input("Enter you id "))
        i = 0
        found = "no"
        for del_id in std_data:
            while i < len(std_data):
                if del_id["id"] == ent_id:
                    found = "yes"
                    del std_data[i]
                    break
                else:
                    break
            i = i+1
        
        if found == "no":
            print("Enter valid id......!")


    def update_mark(self):
        ent_id = int(input("Enter you id "))
        i = 0
        found = "no"
        for upd_id in std_data:
            while i < len(std_data):
                if upd_id["id"] == ent_id:
                    found = "yes"
                    upd_id["Marks"] = [{'hindi': int(input("Hindi : ")), 'english': int(input("English : ")), 'odia': int(input("Odia : ")), 'science': int(input("Science : ")), 'math': int(input("Math : ")), 'physics': int(input("Physics : "))}]
                    break
                else:
                    break
            i = i+1
        
        if found == "no":
            print("Enter valid id......!")




def add_student():
    SMS(input("Enter you full Name : "), int(input("Enter you ID : ")), [{"hindi": int(input("Enter hindi mark : ")), "english": int(input("Enter english mark : ")), "odia": int(input("Enter odia mark : ")), "science": int(input("Enter science mark : ")), "math": int(input("Enter math mark : ")), "physics": int(input("Enter physics mark : "))}])


# Main function
def ad_student ():
    obj = SMS("temp", 0, []) #dummy for acces function in the class
    while True:
        print("Press 1 for add student ")
        print("Press 2 for delet student ")
        print("Press 3 for add update mark ")
        print("Press 4 for add view student details ")
        print("Press 5 for exit ")

        choose = int(input("Enter service code : "))

        if choose == 1:
            add_student ()
        elif choose == 2:
            obj.delete_std()
        elif choose == 3:
            obj.update_mark()
        elif choose == 4:
            obj.search_std()
        elif choose == 5:
            print("exit")
            break
        else:
            "invalid input"

ad_student()


    













