users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234"),
]

user_mapping = {user[1]: user for user in users}
user_id = {user[1]: user for user in users}

# print(user_mapping['Bob'])

# print(username_mapping["Bob"])  # (0, "Bob", "password")

# -- Can be useful to log in for example --

# username_input = input("Enter your username: ")
# password_input = input("Enter your password: ")

# user_input = input("Enter your username: ")
# password_input = input("Enter your password: ")

# x,username,password = user_mapping[user_input]

# if password_input == password:
#     print("Your details are correct!")
# else:
#     print("Your details are incorrect.")


userid_input = input("Enter your user id: ")
username_input = input("Enter your username: ")

user_id1, username, password = user_mapping[username_input]



if str(userid_input) == str(user_id1):
    print("Your details are correct!")
else:
    print("Your details are incorrect.")

# if userid_input == user_id1:
#     print("Your details are correct!")
# else:
#     print("Your details are incorrect.")

# _, username, password = username_mapping[username_input]

# if password_input == password:
#     print("Your details are correct!")
# else:
#     print("Your details are incorrect.")

# If we didn't use the mapping, the code would require us to loop over all users.
# Shown on the side, pause the video if you want to read it thoroughly.
