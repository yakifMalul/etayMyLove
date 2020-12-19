uname = input("Entter your usermane: ")
crohit = ("@" in uname)
nekoda = ("." in uname)
if crohit == 1 and nekoda == 1:
    pword = input("Enter your password: ")
    solamit = ("#" in pword)
    pwordLen = len(pword)

    if solamit > 0 and pwordLen >= 8:
        print ("Congratulations! you entered your account successfully!")
    else:
        print("Invalid Password")
else:
    print ("Invalid Username")