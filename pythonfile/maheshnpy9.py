st = "Python Programming Language"
st = st.replace('o', 'O')
print(st)
tpl = st.partition('On')
print(tpl)

'''
Partition the string into three parts using the given separator.

This will search for the separator in the string. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the original string and two empty strings.
'''

lst = st.split('P', 1)
print(lst)

'''
Return a list of the words in the string, using sep as the delimiter string.

sep The delimiter according which to split the string. None (the default value) means split according to any whitespace, and discard empty strings from the result. maxsplit Maximum number of splits to do. -1 (the default value) means no limit.

'''

lst = "mississippi".split('i')
print(lst)

print('1234'.center(5))
print('1234'.center(10, '*'))
'''
print(help(str.center))
print(help(str.partition))
print(help(str.maketrans))
print(help(str.translate))
'''

intab = "aeiou"
outtab = "12345"
stri = "The quick sly fox jumped over a lazy brown dog"
# we need transtable first then apply translate
trtable = str.maketrans(intab, outtab)


print(stri.translate(trtable))


trans_table = str.maketrans("aeiou", "AEIOU")
print(stri.translate(trans_table))

n = 14
offset = 10  # shift value

width = 2*n-1 + 2*offset  # updated

tile = '^'
for i in range(n):
    tile_width = 2*i + 1
    print((tile * tile_width).center(width))

def foo():
     print('This is a function, named, "foo"')

foo()

del foo



ls  = [1, 2, 3, 3, 3, 4]
print(ls[2], ls[3], ls[4])
del (ls[2], ls[3])
print(ls)
