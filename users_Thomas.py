print("\033[0;32m:.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.")
class Students:
    def __init__(self, fname, lname, age, grade):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.grade = grade

    def describe_students(self):
        print(f"{self.fname} {self.lname} is {self.age} years old and in {self.grade}th grade.")

    def greet_user(self):
        print(f"Greetings, {self.fname} {self.lname}. Have a good day!\n________")


#Instances
SchoolUser = Students("Seth","Thomas",16,11)
SchoolUser2 = Students("Billy","Bob",25,10)
SchoolUser3 = Students("Lebron","James",39,9)
#--
SchoolUser.describe_students()
SchoolUser.greet_user()

SchoolUser2.describe_students()
SchoolUser2.greet_user()

SchoolUser3.describe_students()
SchoolUser3.greet_user()

