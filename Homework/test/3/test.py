from Matrix import *
x = Matrix("[2,3]*(1+j)", "infix")
print(x)
x = Matrix("*[2,3](1+j)", "prefix")
print(x)
x = Matrix("[1,2]+[2,3]+[3,4]", "infix")
print(x)
# x = Matrix("/[2][2](2)", "prefix")#Error
# print(x)
x = Matrix("[2,3](1+j)*", "postfix")
print(x)
x = Matrix("**T[1,2,3; 4,5,6](0.0j)(5.0)", "prefix")
print(x)
x = Matrix("**[1,2,3; 4,5,6](0+j)(5)")
print(x)
x = Matrix("[1,  2  ,3   ;   4, 5, 6]*(0 +   j  )   ", "infix")
print(x)
# x = Matrix("[5]*(4*(2+1j))", "infix")#Error
# print(x)
# one more (3) raise Error
# c = Matrix('[0]    T(3)/(3)*', 'postfix')#Error
# print (c)
c = Matrix('[]T*[3,4,5;1,2,3;2,3,4;6,7,8]T/(3)', 'infix')
print(c)
# c = Matrix('[0]', 'infix')
# print (c)
# x = Matrix("([5]+[1])*5 ", "infix")
# print(x)
# x = Matrix('+T[1;2][2,1]', 'prefix')
# print (x)
# x= Matrix('[0,1]    T', 'infix')
# print (x)
# x = Matrix("*[1+j,2+j](5)", "prefix")
# print(x)
# x = Matrix("+T[1,2;3,4]T[1,3;2,4]")
# print(x)
# x = Matrix('-*[1,2,3; 3,4,5] [1,2; 3,4; 5, 6][1,2;3,4]')
# print(x)
# y = Matrix("** [1,2,3; 3,4,5] [1,2; 3,4; 5, 6][1,2;3,4]", "prefix")
# print(y)
# z = Matrix("[1,2,3; 3,4,5] * [1,2; 3,4; 5, 6]*[1,2;3,4]", "infix")
# print(z)
# z = Matrix("[1,2,3; 3,4,5] /(-5)* [1,2; 3,4; 5, 6]*(5)*([1,2;3,4]*(5)*(6))", "infix")
# print(z)
# x = Matrix("[1,2,3; 3,4j,5][1,2; 3,4; 5, 6] *[1,2;3,4]*", "postfix")
# print(x)
# x = Matrix('[0*1j]T[0*2j]*', 'postfix')
# print(x)

#x = Matrix('([0.1j]+[0.2j])-[0+3j]', 'infix')
#print(x)
#y = Matrix('[0.1j][0.2j]+[0+3j]-', 'postfix')
#print(y)  # bug1
#z = Matrix('-+[0.1j][0.2j][0+3j]', 'prefix')
#print(z)
#a = Matrix('-+[0.1j][0.2j][0+3j]')
#print(a)

# z = Matrix('**[1,2;3,4][1,2;4,5][8j,0;1j,0+j]', 'prefix')
# print(z)

# x = Matrix('*[1;2+j;3;4][1,2,3,4]')
# print(x)

#x = Matrix('*[1,2,3,4][1;2;3;4]')
#x = Matrix('TT[4+j]', 'prefix')
# print(x)

#x = Matrix('[4+j]TT', 'infix')
# print(x)
'''
y = Matrix('[8.0+0.000000j]+[0j]', 'infix')
print(y)

print(y / 6)

print(x + y)

'''
