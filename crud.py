#  initial list/array store userData / Update userData / Delete userData

users = []

print("\n ============= create userData ============")

user1 = {'id':1 , 'name':'John', 'age':30 , 'email':'john@gmail.com'}
user2 = {'id':2 , 'name':'alice', 'age':25 , 'email':'alice@gmail.com'}

users.append(user1)
users.append(user2)

print(users)

print("\n ============= read userData ============")

print("Read All Users;")

print("\n============= update userData ============")

found = False
for user in users:
    if user['id'] == 3:
        user['email'] = 'alice8225@gmail.com'
        print(user)
        found = True

if not found:
    print("User not valid!!")

print("\n ============= delete userData ============")

for user in users:
    if user['id'] == 2:
        users.remove(user)

        print(user)

    print("\nupdates user\n")
    for user in users:
        print(users)


       

