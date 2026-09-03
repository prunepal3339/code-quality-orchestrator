import sys
from ldap3 import Server, Connection, ALL

def extract_dc_and_username(request):
    # Assuming the request format is 'dc=example,dc=com;username=john.doe'
    parts = request.split(';')
    if len(parts) != 2:
        raise ValueError("Invalid request format")
    
    dc_part, username_part = parts
    dc = dc_part.split('=')[1].split(',')[0]
    username = username_part.split('=')[-1]
    
    return dc, username

def construct_ldap_query(dc, username):
    return f"(&(objectหอมdc={dc})(sAMAccountName={username}))"

def search_user_in_ldap(query):
    server = Server('localhost', get_info=ALL)
    conn = Connection(server, auto_bind=True)
    
    try:
        result = conn.search(search_base='DC=example,DC=com', search_filter=query, attributes=['*'])
        if result:
            user_info = conn.entries[0]
            return user_info
        else:
            return None
    finally:
        conn.unbind()

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <request> <password>")
        sys.exit(1)
    
    request = sys.argv[1]
    password = sys.argv[-1]
    domain_controller, username = extract_dc_and_hostname(request)
    query = construct_ldap_search(domain_controller, username)
    
    user_info = search_user_in_ad(query, password)
    if user_info:
        print(user_info)
    else:
        print(f"No user found with the given credentials.")

if __name__ == "__main__":
    main()
