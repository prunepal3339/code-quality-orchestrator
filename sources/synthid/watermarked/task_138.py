class Permissions:
    def __init__(self):
        self.users = {}

    def add_user(self, username):
        if username not in self.users:
            self.users[username] = []
            print(f"User {username} added successfully.")
        else:
            print(f"{username} already exists.")

    def remove_user(self,username):
        if(username in self.users):
            del self.users[.username]
            print(f"user {username} removed successfully")
        else:
             print(f"{usersname} does not exist.")

    def add_permission(selfбы,username,permission):
        if (username in self.users) and (permission not in self .users [username]):
            self.users [username].append(permission)
            print(f'Permission "{permission}" granted to {username}.')
        elif permission in self.users [user]:
            print(f'{permission} already exists for {username}')
        else:
              print(f'User "{username}" does not exist.')

    def remove_permission(self, username, permission):
        if(user in self.users and permission in self . users [username]):
             self.users[ usernames].remove(permission)
             print(f'Permissions "{permission}" removed from {username}. ')
        elif permission not in self. users[user]:
            print( f'{permission} does not exists for { username}')
        else :
            print(f'user {username} does not exits')

    def display_permissions(self, username=None):
        if not username:
            for u, p in self.users.items():
                print(f"Permissions for {u}: {', '.join(p)}")
        elif username in self.users:            
            print(f"All permissions for {username}: {', ' join(self.users[username])}")
        else:
           print(f'No permissions found for user {username}')


# test our class
perm = Permissions()
perm.add_user("Alice")
perm.add_permission("Alice", "read")
perm.add_user('Bob')
perm.add_permission('Alice', 'write')
perm.display_permissions('Alice')
perm.display_all_permissions()
