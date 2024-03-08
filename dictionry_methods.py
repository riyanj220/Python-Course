ep1 = {122: 45, 123: 65, 124: 68, 125: 60}
ep2 = {222: 75, 454: 90}

ep1.update(ep2) #ep2 ki saari cheezen ep1 me agayi hy
print(ep1)
# -----------------------------------------------------------

ep1.clear() #ep1 khaali hojaaye gi ik dam
print(ep1)
# -----------------------------------------------------------

empt = {} #creates an empty dictionary
print(empt)
# -----------------------------------------------------------

ep1.pop(122) #key value pair ko remove kardeta hy
print(ep1)
# -----------------------------------------------------------

ep1.popitem() #last waaali entry hata deta hy yeh
print(ep1)
# -----------------------------------------------------------

del ep1  # poori dictionary uraa dega yeh
print(ep1) #ab del use krne k bad agr me print krun ga to error dega
# -----------------------------------------------------------

del ep1[122]  # agar koi particular entry delete krna chahty hy aap to value do del me
print(ep1)
# -----------------------------------------------------------

info = {"name": "riyan", "age": 18, "country": "pakistan"}
print(info["name"])
info["name"] = "ALi"
print(info["name"])
print(info.keys())

for key in info:
    print(key)

print(info.values())

for key in info.keys():
    print(f"{key} is {info[key]}")

#________________________________________________________________
    
def merge_dicts(dict1,dict2):
    merged_dicts={**dict1,**dict2}
    print(merged_dicts)

# merge_dicts(dict1, dict2)

def key_exists(dic,key):
    return key in dic


# a= key_exists({
#     1:10,
#     2:20,
#     3:30},2)
# print(a)


def get_keys_as_list(dic):
    print(list(dic.keys()))
# get_keys_as_list({1:10,2:20,3:30})

def update_dict(org_dic,upd_dict):
    org_dic.update(upd_dict)
    print(org_dic)

update_dict({"riyan":10,"ahmed":20},{"saleem":30,"saad":40})

def create_dic_from_list(keys, values):
    return dict(zip(keys,values))

# a= create_dic_from_list(("riyan","ahmed","saad"),(10,20,30))
# print(a)


