#!/usr/bin/python3

items = [["rice", 2.4, 8], ["flour", 1.9, 5], ["corn", 4.7, 6]]
for item in items:
    print("Product: %s Price: %.2f Quality: %i" % (item[0], item[1], item[2]))