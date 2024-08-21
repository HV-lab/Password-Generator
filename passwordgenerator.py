import random

def generatePassword(pl):
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    passwords = []
    
    for i in pl:
        password = ""
        
        for j in range(i):
            n_l = random.randrange(len(alphabet))
            password += alphabet[n_l]
            
        password = replaceWithNumber(password)
        password = replaceWithUppercaseLetter(password)
        
        passwords.append(password)
        
    return passwords
    
def replaceWithNumber(pwd):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pwd)//2)
        pwd = pwd[0:replace_index] + str(random.randrange(10)) + pwd[replace_index+1:]
        return pwd
    
def replaceWithUppercaseLetter(pwd):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pwd)//2, len(pwd))
        pwd = pwd[0:replace_index] + pwd[replace_index].upper() + pwd[replace_index+1:]
        return pwd
     
def main():
    num_Password = int(input("How many password do you want to generate? "))
    
    print(f"Generating {str(num_Password)} passwords")
    
    pass_Lengths = []
    
    print("Minimum Length of password should be 3")
    
    for i in range(num_Password):
        length = int(input(f"Enter the Length of the Password # {str(i+1)}  "))
        if length<3:
            length = 3
        pass_Lengths.append(length)
        
    Password = generatePassword(pass_Lengths)
    
    for i in range(num_Password):
        print(f"password # {str(i+1)} = {Password[i]} ")
        
main()