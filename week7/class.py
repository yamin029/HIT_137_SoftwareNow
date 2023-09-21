class User:
    pass

user1 = User()
user1.first_name = "Yamin"
user1.last_name = "Hossain"
print(user1.first_name, user1.last_name)

user2 = User()
user2.first_name = "Tamanna"
user2.last_name = "Prova"
print(user2.first_name, user2.last_name)

user1.age = 25
user2.favourite_book = "ABC Book"
print(user1.first_name, user1.last_name, user1.age)
print(user2.first_name, user2.last_name, user2.favourite_book)