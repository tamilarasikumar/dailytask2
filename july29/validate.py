import re
mblno=input("Enter the mblno.:")
val=re.search("^91[6-9]\d{9}$",mblno) 
if val:
    print("Accepted")
else:
    print("Rejected")

# import re
# pincode=input("Enter the pincode:")
# val=re.search("^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$",pincode) 
# if val:
#     print("Accepted")
# else:
#     print("Rejected")

# import re
# email=input("Enter the Email:")
# val=re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",email) 
# if val:
#     print("Accepted")
# else:
#     print("Rejected")



# import re
# FirstName=input("Enter the Full Name:")
# val=re.search("^(Mr\.|Mrs\.|Ms\.)[A-Za-z]{2,25}\s[A-Za-z]{2,25}",FirstName) 
# if val: print("Accepted")
# else: print("Rejected")