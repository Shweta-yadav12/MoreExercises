# Question 4

# input ka use kar ke 3 alag variables mein 3 integers ka input lein. Input lene ke baad inn 3 mein se 
# sabse bade number ko print karo Note: Isme aap loops ka use nahi kar sakte.

a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b and a>c:
    print(a,"is grinter")
elif b>a and b>c:
    print(b,"is grinter")
else:
    print(c,"is grinter")
