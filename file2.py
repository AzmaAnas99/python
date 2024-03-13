list1=["orange", "apple","graph"]
print(list1)
print(type(list1))
for x in list1:
        print(x)


print()


#list
list1[1]="mango"
print(list1)

print(list1.pop())
list1.insert(2,"orange")
print(list1)


print(len(list1))


print()


#tuple
tuple1=("car","van","bike")
print(tuple1)
print (type(tuple1))


print()

#set
#in set use curly brace and single quotes
set1={'a','b','c','d',} # its orders will be changed not same index in output
print(set1)

print()
set2={'a','b','c','d','a'}
print(set2) # its omit duplicate values

set2.add('e') #adding the elemnt
print(set2)



# dictionary
di1={"number" : 2,"brand":"sofa"}
print(di1)
