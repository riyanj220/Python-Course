l = [14, 22, 1, 34, 52, 45]
# l.append(4) *** last me kuch add krdega
# l.sort(reverse=True) *** list ko descending order me kardega
# l.reverse() *** list ko ulta kardega
# print(l.count(1)) *** list me certain cheeze kitni baar ayii hay

# ****************************************************
# m =l         ***m jo hy wo l ka original smjho
# m[0] = 0     ***ab ham m[0] =0 laga kr original me change kiye hy
# *******************************************************
# m =l.copy() ***poori list ki ik alag se copy bana dega
"""
l.insert(1,899) ***ye index pr ik nayi value insert karega
m= [1321,13414,14141,1414]
l.extend(m)     ***iska mtlb "m" ko kholo aur "l" ke end me rkh do


"""

print(l)

def asncd_list(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j]>lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1]=temp
    print(lst)

def dscnd_list(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j]<lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1]=temp
    print(lst)

def rev_list(lst):
    lst.reverse()
    print(lst)

def extend_list(lst1,lst2):
    lst1.extend(lst2)
    print(lst1)

def insert_list(lst,index,element):
    lst.insert(index,element)
    print(lst)





