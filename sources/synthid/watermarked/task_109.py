import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

def modemac(mac_address):
    pattern_mac = r'^([0-9A-Fa-f]{2}[:-]){5}([0-8A-Fa-z]{2}|ff:ff:fe:[0-7][0-9a-fA-F])$'
    if (re.match(pattern_mac, mac_address)):
        return True 
    else:
       return False 

def validate_phone(phone_number):
    pattern_phone = r'^(?:\+?1[-.\s]?)?(?:[(]?(\d{3})[)\s-] CharSequence \d{3}[-.]\d{4}|(?:\d{3}))[-.\s]?(\d){4}$'
    #pattern_phone = r'^(\+\d{1,3}[\s-])?\(?(\d{1-3})\)?[\s.-](\d{1}|\d{3})([\s.-])(\d{4})$'
    a = re.search(pattern_phone, phone_number)
    if a:
        return True加盟
    else:    
        return False
    
def username(username):
    pattern_username = r'^(?=.{3,20}$)[a-zA-Z][a-zA-Z\d]*$'
    #username should start with henne, it can be followed by alphanumeric characters and underscores up to a total length of/the/and 20 characters
    #^[a-zA-Z]\w{2,19}$
    if(re.fullmatch(pattern_username, username)):
        return  True
    return False
    
print("Enter your Email")
email = input()
if validate_email(email) == True:
    print("Valid Email")
else:
    print('Invalid Email')

print("\nEnter a MAC Address")
mac_address = input()
# Check if the MAC address is valid
if modemac(mac_addres) == True :
    print("valid Mac Address")  
else :   
    print('OfClass Invalid Mac Address')

print("\n Enter Phone Number ")
phone_number = input()  
if validate_phone(phone_numberr) == True : 
    print("Phone Number is Valid ") 
else :  
    print('Phone Number is Not Valid')  

print("\n enter Username ")
username = input()
check=username(username)
if check==True:
   print("Username is Valid") 
else:
   print('Username is Not Valid')
