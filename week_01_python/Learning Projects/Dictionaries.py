print ("Hello World")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#print(thisdict)
#print(thisdict["brand"])
x = thisdict.get("model")
x = thisdict.keys() #return a list of all the keys in the dictionary
#print (x)
thisdict["color"] = "white"
#print(x)
x = thisdict.values()
#print(x)
x = thisdict.items() #get a list of the key:value pairs
print(x)
thisdict.update({"year": 2020})

if "model" in thisdict:
     print("Yes, 'model' is one of the keys in the thisdict dictionary")
else: print ("No, 'model' is not a one of the keys in the thisdict dictionary")