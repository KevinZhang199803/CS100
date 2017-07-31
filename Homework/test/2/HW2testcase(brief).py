x = Matrix("  [12j,-0.35+j,4j,3;0.000007,3,4,5;100j,4,5,6;1,2,3,4]")
print (x)
y = Matrix('[-10-j,-j-2,j-1,j+1;123,25.000000000000000000000000005,-9,2;8,13,3j,98;1,2,3,4]')
print (y)



print (x.determinant())
print (x.inverse())
x[1] = Matrix('[1,4,3,5]');print (x)

x[1,0] = 0j;print (x)

print (Matrix('[1,2,3]'))
print (Matrix('[]')**3)
print (x[2,0])
print (x[1:2:1,0:3:2])
print (x[1])




print (x[1,0])
print (MatAdd([],[]))
print (Matrix('[1,2,3]'))


b = Matrix('[2,1,2;-1,5,21;13,-1,-17]')
print (b.determinant())

c = Matrix('[1,2,3;2,2,3;4,1,4]')
print (c.determinant())


a = Matrix('[1,1,2;-1,2,0;1,1,3]')
print (a.inverse())  
