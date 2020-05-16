def count_substring(string,sub_string):
    len1 = len(string)
    len2 = len(sub_string)
    j =0
    counter = 0
    for j in range(len1):
        if(string[j] == sub_string[0]):#this step get conclution there should be a substring
            if(string[j:j+len2] == sub_string):#check sub string lenth
                counter += 1
        

    return counter

print(count_substring('ABCDCDC','CDC'))

'''
The Difference Between Unicode and UTF-8
Unicode is a character set. UTF-8 is encoding.

Unicode is a list of characters with unique decimal numbers (code points). A = 65, B = 66, C = 67, ....

This list of decimal numbers represent the string "hello": 104 101 108 108 111

Encoding is how these numbers are translated into binary numbers to be stored in a computer:

UTF-8 encoding will store "hello" like this (binary): 01101000 01100101 01101100 01101100  01101111

'''