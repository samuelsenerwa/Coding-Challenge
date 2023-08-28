#!/usr/bin/python3
d = {'k1':1,'k2':2,'k3':3}

# Create a dictionary view object using .items() method

print(d.items())
for k,v in d.items():#iterating through dictionary view object
    print(k)#will print keys in a dictionary 
    print(v)#will print values in a dictionary

#If you want to obtain a true list of keys, values, or key/value tuples, you can cast the view as a list:
print(list(d.keys()))#Print a list of keys in the dictionary
print(list(d.values()))#Print a list of values in the dictionary
print(list(d.items()))# Print a list of (key, value) tuples in the dictionary

#Remember that dictionaries are unordered, and that keys and values come back in arbitrary order. You can obtain a sorted list using sorted():
print(sorted(d.values()))
