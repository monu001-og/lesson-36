lst =['apple','Guava','Mango','Banana','kiwi']
print("Length of list:",len(lst))
print(" First Element:",lst[0])
print("Lasrt Element:",lst[-1])

lst.append('papaya')
print('updated list:',lst)

lst.remove('Guava')
print('updated list:',lst)

lst.sort()
print('sorted list:',lst)

lst.pop(1)
print('updated list:',lst)

lst.reverse()
print('reversed list:',lst)

print("Multiplication on list:",lst)

lst=lst[:4]
print('sliced list:',lst)

lst.clear()
print('updated list:',lst)





