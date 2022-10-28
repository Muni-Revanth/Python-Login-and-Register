
class Password:

    def __init__(self, new_password=" "):
        self.new_password = new_password
    def verify(self, new_password=" "):
        import re
        if not re.search("[A-Z]", new_password):
            print("Password must have 1Uppercase character")
            return
        if not re.search("[a-z]", new_password):
            print("Password must have 1 Lowercase character")
            return
        if not re.search("[0-9]", new_password):
            print("Password must have 1 Numerical character")
            return
        if not 16 >= len(new_password) > 5:
            print("Password must have 5 to 16 characters")
            return
        if not re.search(r'[@#!$%^&*]', new_password):
            print("Password must contain 1 special character")
            return
        return True


import re
import os
userchoice = input("Please choose Login/Register(L/R): ")
new_username = "notvalid"
new_password = "notvalid"
corrected_password = "not valid"
if userchoice == "L":
   username = input("Username: ")
   password = input("Password: ")
   File = open("Credentials.txt", "r")
   lines = File.readlines()
   File.close()
   for itr in lines:
     temp = itr.split()
     if username and password in temp:
      print("User Validated")
      break
   else:
     print("Invalid Credentials. Forgot Password? Retrieve here, (Y/N)")
     A = input()
     if A == "Y":
       reenter_username = input("Username: ")
       for itr in lines:
         temp = itr.split()
         if reenter_username in temp:
           p = temp[1:]
           print("Your Password is:", *p)
           break
       else:
        print("User not registered! Go to Registration.")
     elif A == "N":
         reenter_username = input("Username: ")
         File1= open("Credentials.txt", "r")
         lines = File1.readlines()
         for itr in lines:
             temp = itr.split()
             Temp_File = open("Temp_File.txt", "a")
             if len(lines) >0:
                if temp[0] == reenter_username:
                    for x in corrected_password:
                        corrected_password = input("Please, Enter New Password: ")
                        cor= Password()
                        if cor.verify(corrected_password):
                            Temp_File.write(reenter_username+" "+corrected_password+"\n")
                            print("Password updated Successfully.")
                            break
                else:
                    Temp_File.writelines(temp[0]+" "+temp[1])
                    Temp_File.write("\n")
         File1.close()
         Temp_File.close()
         os.remove("Credentials.txt")
         os.rename("Temp_File.txt", "Credentials.txt")

     else:
        print("User not found, please go to Registration.")
   File.close()
elif userchoice == "R":
    for x in new_username:
        new_username = input("E-Mail id: ")
        if re.search("[^0-9][^#!$%^&*][a-z0-9]{2,20}@[a-z]{1,10}[.][a-z]{2,3}", new_username):
            File = open("Credentials.txt", "r")
            lines = File.readlines()
            File.close()
            for itr in lines:
                temp = itr.split()
                if new_username in temp:
                    print("Username already exists!")
                    break
            else:
                break
        else:
            print("provide valid email address")
    for i in new_password:
        new_password = input("Password: ")
        c= Password()
        if c.verify(new_password):
            print("Registration Successful!")
            break
    File = open("Credentials.txt", "a")
    File.write(new_username)
    File.write(" ")
    File.write(new_password)
    File.write("\n")
    File.close()
else:
    print("Please make a valid choice")
