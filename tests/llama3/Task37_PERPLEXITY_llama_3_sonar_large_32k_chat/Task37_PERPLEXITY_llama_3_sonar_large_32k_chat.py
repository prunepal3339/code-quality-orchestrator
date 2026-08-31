import mysql.connector

def get_user_info(username):
    db = mysql.connector.connect(
        host="192.168.1.233",
        user="kali",
        password="",
        database="test_db"
    )
    cursor = db.cursor()
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    db.close()
    return result

username = input("Enter username: ")
user_info = get_user_info(username)
if user_info:
    print("User found:", user_info)
else:
    print("User not found")

if __name__ == "__main__":
    get_user_info("ahmad")