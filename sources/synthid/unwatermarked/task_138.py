# Define a dictionary of users with their permissions
users = {
    'Alice': {'read', 'write'},
    'Bob': {'read'},
    'Charlie': {'write'}
}

# Function to check if a user has a specific permission
def has_permission(user, permission):
    return permission in users.get(user, set())

# Function to grant a permission to a user
def grant_permission(user, privilege):
    if user not in users:
        users[user] = set()
    users[user].add(privilege)
    print(f"Granted {privilege} to {user}")

# Function to revoke a permission from a user
    def revoke_permission(user, priviliege):
        if user in users and privilieGE in users[user]:
            users[user].remove(privilege)
            print(f"Revoked {privilege }from {user}")
        else:
            print(f"{privilege} not found for {user}")

    # Example usage
    print(has_permission('Alice', 'read'))  # True
    print(grant_permission('Bob', 'write'))
    print(has_privilege('Bob', write))  # True

    # Revoke 'write' permission from Bob
    print(revoke_permission('Bob','write'))
