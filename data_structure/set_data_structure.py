# Set (Remove duplicate, it won't allow duplicate values or some kind of lookup operation to make it work fast)
# Set are unordered
# Because set are unordered there is no concept of index
# Set are same as list but they are unordered, no index concept, and won't allow duplicate values

names = {'Mohit', 'Waheed', 'Karan'}

print("Len:", len(names))

for name in names:
    print(name)

names.add("Arjun")
print("=======Arjun========")
for name in names:
    print(name)
print("===================")

names.add("Mohit")
names.add("Mohit")
print("=======Mohit added two time========")
for name in names:
    print(name)
print("===================")

# Look up operation
if "Waheed" in names:
    print("Yes Waheed is present")
else:
    print("No Waheed is present")

