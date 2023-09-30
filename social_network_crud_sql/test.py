# Test CRUD operations
from user_crud import create_user, read_user, update_user, delete_user

# Create demo user
create_user('john_doe', 'john@example.com', 'I love coding!')
create_user('jane_doe', 'jane@example.com')

all_users = read_user()
print("All Users:", all_users)

user_john = read_user(1)
print("Before Update:", user_john)

update_user(1, new_username='john_smith', new_bio='Passionate coder')
user_john = read_user(1)
print("After Update:", user_john)

delete_user(2)
all_users = read_user()
print("After Delete id 2 All users: ", all_users)

