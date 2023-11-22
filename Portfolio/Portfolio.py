# 1#
def sorting(string):
    print([*string])
    # unique method isn't working


sorting("Cheese")


def one_two(string1, string2):
    string1 = set(string1)
    string2 = set(string2)
    ans = (string1.intersection(string2))
    print(ans)


# 2#
def both(string1, string2):
    string1 = set(string1)
    string2 = set(string2)
    ans = string1 - string2
    print(ans)


def not_both(string1, string2):
    string1 = set(string1)
    string2 = set(string2)
    ans = string1 ^ string2
    print(ans)


one_two("hours", "powers")
both("hours", "powers")
not_both("hours", "powers")

# 3#

check = False
file = {"Brazil", "Asia"}
#print("#Enter nothing when you're done#")
#while not check:
    #country = (input("Enter a country"))
    #country = {country}
    #if country >= file:
        #print(country)
    #elif country - file:
        #print("country has been added to file")
        #file.update(country)
        #print(file)

# 4#
folder = {}
line = (input("Enter a string: "))
for i in range(len(line)):
    if line[i] in folder:
        folder[line[i]] += 1
    else:
        folder[line[i]] = 1
print(folder)
print(line)






