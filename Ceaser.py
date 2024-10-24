#Setting Up Program
import string
alp=string.ascii_uppercase
x=list(alp)*2
cipher=[]
plain=[]

#The Method
method=input("Encryption OR Decryption:\n").strip().lower()

if method=="encryption" or  method=="e":
    #Taking The plain Text
    plain_text=input("Enter Your Plain Text :\n").upper()
    #Taking The Key Value
    key=int(input("Enter The Key:\n"))
    list_p=list(plain_text)
    #Encryption
    for i in (list_p):
        if i==" ":
            #space Sequence
            cipher.append(" ")
            continue
        #New Index
        let=i
        index=x.index(let)
        new_index=index+key
        cipher.append(x[new_index])
    print("".join(cipher))

elif method=="decryption" or method=="d":
    #Taking The plain Text
    ciphered_text=input("Enter Your Cipher :\n").upper()
    #Taking The Key Value   
    key=int(input("Enter The Key:\n"))
    list_c=list(ciphered_text)
    #Decryption
    for i in (list_c):
        if i==" ":
            #space Sequence
            plain.append(" ")
            continue
        #New Index
        let=i
        index=x.index(let)
        new_index=index-key
        plain.append(x[new_index])
    print("".join(plain))

else:
    print("Invalid Choice")
