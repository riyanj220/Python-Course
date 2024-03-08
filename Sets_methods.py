s = {13, 12, 34, 5, 532, 6}
s1 = {23, 42, 514, 34, 155, 25, 214}

# print(s.union(s1))
# print(s.intersection(s1))
# _______________________________________________________________
# s3.intersection_update(s1)
# print(s3)
# ________________________________________________________________
# s.update(s1)  # iska matlb s me wo values b lee aao jo s1 me hy
# print(s)
# ________________________________________________________________
# s3 = s.symmetric_difference(s1) iska matlb wo values jo common nahi h
# print(s3)
# ________________________________________________________________
# s3 = s.difference(s1) iska matlb s ke unique element jo baaki sets me na hoo(A-B)
# print(s3)
# ________________________________________________________________

# print(s.isdisjoint(s1)) #mtlb ke ik set ke element ksii b dosre set me present hay ke nahi boolean return karega
# ________________________________________________________________
# s3 = {1, 2, 3, 4, 5, 6, 7}
# s4 = {1, 2, 3}
# print(s3.issuperset(s4)) #if s3 is a super set of s4 then true dega else false
# __________________________________________________________________
# s3 = {1, 2, 3, 4, 5, 6, 7}
# s4 = {1, 2, 3}
# print(s4.issubset(s3))  # check karega agr s4 subset hay s3 ka ya nahi
# __________________________________________________________________
# s9 = {"asdad", "adada", "dghdsss"}
# s9.add("riyan")
# print(s9) #end me add kardega kuch b yeh
# __________________________________________________________________
# s7 = {1, 321, 4, 45, 1, 5, 13}
# s7.remove(321)
# print(s7) #kuch b remove krskta hy yeh
# __________________________________________________________________
# s7 = {1, 321, 4, 45, 1, 5, 13}
# s7.discard(3211)
# print(
#     s7
# )  # discard b remove krta hy liken agr entity present na huyi to error ni dega yeh jab ke remove error deta hy
# __________________________________________________________________
# s54 = {1, 321, 31, 41, 414}
# del s54 #delete kardega yeh poore set koo
# __________________________________________________________________
# s11 = {13, 314, 142, 4, 252, 2}
# s11.clear()
# print(s11) #ye sirf entities clear kardega set baaki rahega jab ke delete entities sameet poore set ko ura deta hy
# __________________________________________________________________
# s45 = {"a", "b"}
# if "a" in s45:
#     print("yes") #koi value set me exist krti hy ke nahi
# __________________________________________________________________
