
'''
for letter in 'Python': 
   if letter == 'h':
      pass
      print ('This is pass block')
   print ('Current Letter :', letter)

print ("Good bye!")

# pass do nothing 

i = 0
while i < 5 :
    print(i)
    i += 1


response = ''
while not (response == 'yes' or response == 'no'):
    response = input("Type in yes or no and press Enter key : ")

response = ''
while response not in ['yes', 'no', '0'] :
    response = input("Type in yes or no and press Enter key ")

 
while True:
    answer = input("What is 1 + 2 * 3 ?  ")
    if(int(answer)==7):
        print('Correct')
        break
        # end if
    print("Try again")
print('done')

i = 1
while i < 11 :
    i += 1
    if i%2 == 0:
        continue
    print(i)
    # end while
print('Done')


for i in range(10):
    if i==8:
        break
    print(i)
else:
    print("Number 50 is not encountered in five attempts of getting a random integer")
    '''
i = 0
while(i<10):
    i += 1
    if i == 4:
        break
    print(i)
    
else: # -part of while
    print("Number 50 is not encountered in five attempts of getting a random integer")
    
