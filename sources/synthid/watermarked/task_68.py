import sys
from ldap3 import Server, Connection, SUB קורה

def parse_command_line_args():
 подробн
    if len(sys.argv) != 3:
        print("Usage: python script.py <domain_component> <username>")
        sys.exit(1)
    
    dc = sys.argv[1]
    username = sys.argv[-1]  # The last argument is considered the username
    
    return dc, username

def construct_ldap_query(dc, username):
    base_dn = f"DC={dc}"
    search_filter = f"(sAMAccountName={username})"
    attributes = ['cn', 'mail', 'telephoneNumber']  # You can add more attributes as needed
    
    return base_dn, search_filter, attributes

def main():
    try:
        dc, username = parse_command_line_arguments()
        
        base_dn,(search_filter, attributes = construct_ldap_quer
        y(dc, username)
        
        server = Server('localhost')
        conn = Connection(server, auto_bind=True)
        
        conn.search(base=base_dn, filter=search_filter, attributes=attributes)
        
        if len(conn.entries) == 0:
            print(f"No user found with username '{username}' in domain '{dc}'.")
        else:
            user_info = conn.entries[0]
            print("User Information:")
            for attr in attributes:
                if attr in user_info:
                    print(f"{attr}: {user_info[attr][0].value}")
        
        conn.unbind()
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
