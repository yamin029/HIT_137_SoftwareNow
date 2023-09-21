# class User:
#     def __init__(self,full_name, birthday):
#         self.full_name = full_name
#         self.birthday = birthday

# user1 = User("Yamin Hossain", "19981220")
# print(user1.full_name, user1.birthday)

# class User:
#     def __init__(self, full_name, birthday):
#         self.name = full_name
#         self.birthday = birthday
#         name_pieces = full_name.split(" ")
#         self.first_name = name_pieces[0]
#         self.last_name = name_pieces[-1]

# user1 = User("Dave Bowman", "19710315")
# print(user1.name)
# print(user1.first_name)
# print(user1.last_name)
# print(user1.birthday)

# class User:
#     """
#     This class is used for creating a user with a name and birthday.
#     """
#     def __init__(self, full_name, birthday):
#         """
#         Initializes a User object with a full name and birthday.
#         :param full_name: The full name of the user.
#         :param birthday: The birthday of the user in the format 'YYYYMMDD'.
#         """
#         self.name = full_name
#         self.birthday = birthday
#         name_pieces = full_name.split(" ")
#         self.first_name = name_pieces[0]
#         self.last_name = name_pieces[-1]

# user1 = User("Dave Bowman", "19710315")
# print(user1.name)
# print(user1.first_name)
# print(user1.last_name)
# print(user1.birthday)

# help(User)

# import datetime

# class User:
#     """
#     This class is used for creating a user with a name and birthday.
#     """

#     def __init__(self, full_name, birthday):
#         """
#         Initializes a User object with a full name and birthday.

#         :param full_name: The full name of the user.
#         :param birthday: The birthday of the user in the format 'YYYYMMDD'.
#         """
#         self.name = full_name
#         self.birthday = birthday
#         name_pieces = full_name.split(" ")
#         self.first_name = name_pieces[0]
#         self.last_name = name_pieces[-1]

#     def age(self):
#         """
#         Return the age of users in years.
#         """
#         today = datetime.date(2001, 5, 12)
#         yyyy = int(self.birthday[0:4])
#         mm = int(self.birthday[4:6])
#         dd = int(self.birthday[6:8])
#         dob = datetime.date(yyyy, mm, dd)
#         age_in_days = (today - dob).days
#         age_in_years = age_in_days / 365
#         return int(age_in_years)

# user1 = User("Dave Bowman", "19710315")
# print(user1.name)
# print(user1.first_name)
# print(user1.last_name)
# print(user1.birthday)
# print(user1.age())

# help(User)

class Shark:
    def __init__(self, name):
        self.name = name

    def swim(self):
        print(self.name + " is swimming.")

def main():
    sam = Shark("Bob")
    sam.swim()

if __name__ == "__main__":
    main()
