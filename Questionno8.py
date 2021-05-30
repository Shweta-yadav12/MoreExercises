# Courses
# Login/Signup
# Question 8

# Socho aapke paas do lists hain. Ab aapko nayi list banani hai jisme dono lists ke elements hone 
# chaiye. Lekin yeh dhyan mein rakhna hai ki dono lists ke saare elements sirf ek-ek baar hi hone 
# chaiye. Agar humare paas yeh do lists hain:

 
list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
i=0
while i<len(list2):
    if list2[i] not in list1:
        list1.append((list2[i]))
    i=i+1
list1.sort()
print(list1)