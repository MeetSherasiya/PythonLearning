SECURE = (('s','$'),('and','&'),('a','@'),('i','|'))

def securepassword(password):
    for a,b in SECURE:
        password = password.replace(a,b)
    return password

if __name__ == "__main__":
    password = input("Enter a password : ")
    password = securepassword(password) 
    print(f"Your Secure Password is {password}")