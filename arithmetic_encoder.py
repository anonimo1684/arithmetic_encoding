#Code made by: anonimo1684
#Data: March 23rd, 2023
#Descripció: This repository contains a file that implements arithmetic coding of character strings. Arithmetic coding is a data compression method that allows representing a string of characters as a single number.
#Download: 


def arithmetic_encoding(string):
    # Create an empty dictionary to store character frequencies
    dict = {}
    
    # Count the frequency of each character in the input string
    for i in string:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    # Calculate the relative frequency of each character
    freq = {}
    for i in dict:
        freq[i] = dict[i]/len(string)
    
    # Create a dictionary to store the intervals for each character
    intervals = {}
    l = 0
    for i in sorted(freq):
        intervals[i] = [l, l+freq[i]]
        l += freq[i]
    
    # Initialize variables for the final interval
    l = 0
    h = 1
    w = 1
    
    # Calculate the final interval for the input string
    for i in string:
        h = round(l + (w*intervals[i][1]), 4)
        l = round(l + (w*intervals[i][0]), 4)
        w = h-l
    
    # Calculate the final encoded value for the input string
    n = round(l+(w/2), 2)
    
    # Increase precision until the final encoded value is within the final interval
    i = 3
    while n < l or n > h:
        n = round(l+(w/2), i)
        i += 1
    
    print([l, h], n)

# Get user input and call arithmetic_encoding function with it as argument
string = input("Enter the string: ")
arithmetic_encoding(string)

input()