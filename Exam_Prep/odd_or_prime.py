list1 = [1,2,3,4,5,6,7,8,9]

print(list1)

def div2():
    new_list = []

    for x in list1:
        print(f"{x}")

    for i in list1:
        if i%2 != 0:
            new_list.append(i)
            print(f"\n{i}")

    #print(f"\n{i}")        
    print(f"\n{new_list}")

div2()


