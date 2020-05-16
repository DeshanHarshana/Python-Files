'''
Exercise: Write the output of the following code:
for i in range(1, 5):
    print(i, end='->')
    for j in range(11, 20):
        print(j, end=' ')
# end for j
print()
# end for i
'''
#output
'''
1->11 12 13 14 15 16 17 18 19
2->11 12 13 14 15 16 17 18 19
3->11 12 13 14 15 16 17 18 19
4->11 12 13 14 15 16 17 18 19
'''
#----------------------------------------------------------------------------------------------------------

'''
Exercise: Write the output of the following code:
product = [(i, j) for i in range(1, 4) for j in range(2, 10, 2)]
print(product)
'''
#output
'''
[(1, 2), (1, 4), (1, 6), (1, 8), (2, 2), (2, 4), (2, 6), (2, 8), (3, 2), (3, 4), (3, 6), (3, 8)]
'''