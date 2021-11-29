import re


def find_name(line):
    pattern = r"(M[r|s|rs|iss]\.? [A-Z][a-z]*)"
    #Salutation plus Last Name
    #((M[r|s|rs|s][.])(\s)([A-Z][a-z]*))|((([A-Z][a-z]*)(\s|-))[A-Z][a-z]*)"
    result = re.findall(pattern,line)
   
    pattern = r"((?!((T|t)he))[A-Z][a-z]* [A-Z][a-z]*)"
    #First Name plus Last Name, exlude words "The" and "the"
    result = result + re.findall(pattern,line)

    pattern = r"((?!((T|t)he))[A-Z][a-z]* [A-Z][a-z]*(\s|-)[A-Z][a-z]*)"
    #First Name plus Double Last Name, exclude "The" and "the"
    result = result + re.findall(pattern,line)
    return result

f = open("dancersnames.dat")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)