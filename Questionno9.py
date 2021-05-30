# Courses
# Login/Signup
# Question 9

# Harshad numbers aise number hote hain jo apni digits ke sum se dhang se divide hote hain. Dhang se 
# divide hone ka matlab ki remainder 0 aata hai. Jaise 42 ek Harshad number hai kyunki 4 + 2 = 6 aur
#  42 ko 6 se vidie kar ke remainder aata hai Aise hi 18, 21 aur 24 bhi harshad number hai kyunki
#   1 + 8 = 9 aur 18 ko 9 se divide kar ke remainder 0 hai. Aise hi 1, 2, 3, 4, 5, 6, 7, 8, 9 saare 
#   harshad number hain kyunki inki digits ka sum khud yeh number hain aur yeh apne aap se divide ho 
#   jate hain. Ek number ke digits nikalne ka code yeh h


def is_harshad_number(num):
    n=1
    sum=0
    while n>0:
        k=1%10
        sum=sum+k
        n=n//10
    if num%sum==0:
        print("is harshad number",num)
    else:
        print("it is not a harshad number",num)
num=int(input("enter the no"))
is_harshad_number(num)