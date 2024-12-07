# Dictionary-Manipulations
Dictionary Manipulations showing in 15 programs


#Basic dict creation, len finding
d={}
n=int(input())
for i in range(n):
  k=input()
  v=int(input())
  d[k]=v
print(d)
print(len(d))



#Square of values as value for a key
d={}
n=int(input())
for i in range(n):
  k=int(input())
  v=k*k
  d[k]=v
print(d)




#MERGE of DICT
d1={'a':1,'b':2}
d2={'c':3,'d':4}
d3=d1.copy()
for k,v in d2.items():
  d3[k]=v
print(d3)



#checking key is in dict or not
d={'name': 'Alice','age':30}
key=input()
for i in range(len(d)):
  if key in list(d.keys()):
    print(True)
    break
else:
  print(False)



#Accesing value // printing value associated with key
d={'name': 'Alice','age':30}
k=input()



#print(f"Value of k is : {d.get(k)}")
if k in d:
  print(f"The value of key is: {d.get(k)}")
else:
  print(f"The key is not in {d}")



#Update the value of key
d={'name':'akki','age':30,'roll':890}
k=input()
d[k]=31
print(d)



#Remove key value pair
d={'name':'akki','age':30,'roll':890}
m=d.pop('name')
print(d)
print(f"The popped element is: {m}")


#checking dict is empty or not
d={}
#d={'name':'akki','age':30,'roll':890}
if len(d)==0:
  print("Empty")
else:
  print(f"The dict is {d}")


#Get all the keys, values, items
d={'name':'akki','age':30,'roll':890}
print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))



#create 2 keys vowels and consonants
#append all the charcters of word "codewala flask" to 2 keys
d={}
s=input()
s=s.replace(" ","")
v=[]
c=[]
for i in range(len(s)):
  if s[i] in "aeiou":
    v.append(s[i])
  else:
    c.append(s[i])
d['vowel']=v
d['consonants']=c
print(d)


#create dict with key as string, value as a dict
d = {'name': 'akki', 'age': 30, 'roll': 890} 
db = {}  
name = d['name']
db[name] = {}  
print(db)
for key in d:
    if key != 'name': 
        db[name][key] = d[key]
print(db)



#create dict with key as int and value as list
d = {'name': 'akki', 'age': 30, 'roll': 890} 
db = {}  
age = d['age']
print(type(age))
db[age] = {}  
print(db)
for key in d:
    if key != 'age': 
        db[age][key] = d[key]
print(db)



#create even and odd list append 1-100 numbers (inclusive)
d={'even':[],'odd':[]}
ev_count=0
odd_count=0
for i in range(1,101):
  if i%2 == 0:
    d['even'].append(i)
    ev_count+=1
  else:
    d['odd'].append(i)
    odd_count+=1
print(d)
print()
for k,v in d.items():
  print(f'{k} : {v}')
print(f"even-count:{ev_count} odd-count:{odd_count}")




#count frequency of each letter in a string
d={}
n=int(input())
for i in range(n):
  key=input()
  l=list(key)
  m={}
  for i in range(len(l)):
    if l[i] not in m:
      m[l[i]]=1
    else:
      m[l[i]]+=1
  value=m
  d[key]=value
print(d)

