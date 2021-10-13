#string cancatenation
name = "Marina"
print("Hello, " + name) #1st way
print ("Hello, {}".format(name)) #2nd way
print (f"Hello, {name}") #3rd way


adj1 = input("Adjective1: ")
adj2 = input("Adjective2: ")
verb1 = input("Verb1: ")
verb2 = input("Verb2: ")

madlib = f"{adj1} and {adj2} were going on a road trip. Ted {verb1}. Fred {verb2}. They drove away."
print(madlib)