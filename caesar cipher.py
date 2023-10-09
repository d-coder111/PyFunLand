#creating a def for an ecryption
def encrypt(string, shift):
 
  cip = ''
  for char in string: 
    if char == ' ':
      cip = cip + char
    elif  char.isupper(): #creating alphabet for message
        #creating an equation for finding letter placement and then shifting that according to request by user
      cip = cip + chr((ord(char) + shift - 65) % 26 + 65) #65 stands for Capital A and is the starting point for formula and 26 for number of letters
    else:
      cip = cip + chr((ord(char) + shift - 97) % 26 + 97) #97 stand for small A with ASCII keys
  
  return cip
 
request = input("Enter something you wanted encrypted: ")
#Giving user the option to shift the numbers.  This could be set to one number only.
s = int(input("Enter the places you would like to shift.\nPostive number for a right shift\nNegative number for a left shift:   "))
print("Your original message: ", request)
a=(encrypt(request, s))  #a is the encrypt def which the request and the place shift number input
print("Your Encryption: ", a)

#creating a write file for the encrypted message above
def main():
    f= open("mymessage.txt", "w")
    f.write(a)
    f.close()

main()

#the def main with message.txt should show up in file.

 
