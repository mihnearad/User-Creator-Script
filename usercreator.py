import secrets
import string
import subprocess
import session_key

char_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+-/:;<=>?@^{|"
alphabet = string.ascii_letters + string.digits + string.punctuation    
PasswordVPN = ''.join(secrets.choice(char_seq) for i in range(20))
PasswordAD = ''.join(secrets.choice(char_seq) for i in range(10))
PasswordBW = ''.join(secrets.choice(char_seq) for i in range(5))

Firstname = input("Please add Employee First Name: ")
Lastname = input("Please add Employee Last Name: ")
Email = input("Please add email: ")
Department = input("Please add department: ")
CopyTemplate = input("Whose permissions to copy: ")
Username = Firstname[0]+Lastname

print("\n")
print("Hi VIjay,\n")
print( "Please create AD/VPN credentials for the following user: " + "\n")
print("Username: " + Username)
print("Full Name: " + Firstname + " " + Lastname)
print("Email: " + Email)
print("Department: " + Department)
print("Copy template of: " + CopyTemplate + "\n")
print("VPN Password: " + PasswordVPN)
print("AD Password: " + PasswordAD)
print("BW Link PW: " +PasswordBW)
print("\n")

BothPasswords="VPN: "+PasswordVPN+"   AD: "+PasswordAD

JQName="jq \'.name=\""+Username+"\""

JQText= ".text.text=\""+BothPasswords+"\"'"

password="\""+PasswordBW+"\""

bashcommand1 = subprocess.run('bw send template send.text |' +JQName+' | '+JQText+' |  bw encode | bw send create --session ' + session_key.sesskey + ' --pretty --password '+ password  ,
    shell=True  , text=True, check=True)

