###################################
# Gorev1
###################################

x = 8
type(x)  # int

y = 3.2
type(y)

z = 8j + 18
type(z)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 < 22
type(c)

l = [1, 2, 3, 4]
type(l)

d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
type(d)

t = ("Machine Learning", "Data Science")
type(t)

s = {"Python", "Machine Learning", "Data Science"}
type(s)

###################################
# Gorev2
###################################

text = "The goal is to turn data into information, and information into insight."
print(text.upper().replace(",", " ").replace(".", " ").replace("  ", " ").split(), end="\n")
text = text.upper().replace(",", " ").replace(".", " ").replace("  ", " ").split()
text

###################################
# Gorev3
###################################

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

len(lst)

lst[0]
lst[10]

lst2 = lst[:4]

lst.pop(8)
lst.append("K")
lst.insert(8, "N")

###################################
# Gorev4
###################################

dict = {"Christian": ["America", 18],
        "Daisy": ["England", 12],
        "Antonio": ["Spain", 22],
        "Dante": ["Italy", 25]}

dict
dict.keys()
dict.values()

dict["Daisy"]

dict["Daisy"][1] = 13
dict.update({"Daisy": ["England", 13]})
dict["Ahmet"]= ["Turkey", 24]
dict.update({"Ahmet": ["Turkey", 24]})

dict.pop("Antonio")

###################################
# Gorev5
###################################

l = [2, 13, 18, 93, 22]

# lst = [1,2,3,4,5,6,7,8,9]

def func(l):
    even_list = []
    odd_list = []
    for i in l:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list, odd_list


even_list, odd_list = func(l)

###################################
# Gorev6
###################################

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns


cols = ["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]


###################################
# Gorev7
###################################

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns


cols = [col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]

a = []
for col in df.columns:
    if "no" not in col:
        a.append(col.upper() + "_FLAG")
    else:
        a.append(col.upper())

###################################
# Gorev8
###################################
import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns
df.head()

og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()





















