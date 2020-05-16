bn, nbn, smn = 1e+15, -1e+15, 1e-15
print(bn + nbn + smn == smn + bn + nbn)

print(format(bn,'0.20f'))
print(format(nbn,'0.20f'))
print(format(smn,'0.20f'))


#calculate left to right
print(format(bn+nbn,'0.20f'))
print(format(smn+(bn+nbn),'0.20f'))
print(format(smn+bn,'0.20f'))
print(format((smn+bn)+nbn,'0.20f'))

'''
python add number left to right
first it add bn + nbn
they have no floting point value then it normally add (computer wht ever number he convert it ieee)
if we have floting number with decimal we have to consider about ieee stands

bn=1000000000000000.00000000000000000000
nbn=-1000000000000000.00000000000000000000
total=0.0

then we add that nnumber to smn
total=0.0
smn=0.00000000000000100000

so it is floting foint number then we have to convert then ieee stand and add them

sum=0.000000000000001  ---------- (1)


ok now conside other part

smn+bn=1000000000000000.0 

now we add nbn to it

it become 0

then first part we get 0.000000000000001
second part we get 0.0

not equal

'''