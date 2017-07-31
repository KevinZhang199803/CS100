from Matrix import Matrix
from Matrix import MatrixSyntaxError
from copy import deepcopy

def pt(s:str, m:Matrix):
    print(s+str(m))
    return None


def a():
    c1 = 2
    c2 = 2.4
    c3 = (1+3j)
    A = Matrix(' [ 6,      0,      -6,     4.5,    0.0,     -4.5;     4.5,    -4.5,   -0,     6,      -6,      -0;   2+2j,   2-2j,   2+0j,   2-0j,   0+2 j ,    0 - 2 j;     0j,     0 - 0  j,    2  +  2  j,   j,      -  4.5  +  j ,  0.0 - 4.5 j ]')
    #A = [6,      0,      -6,     4.5,    0.0,     -4.5;
    #     4.5,    -4.5,   -0,     6,      -6,      -0;
    #     2+2j,   2-2j,   2+0j,   2-0j,   0+2j,    0-2j;
    #     0j,     0-0j,   2+2j,   j,      -4.5+j,  0.0-4.5j]
    B = Matrix(' [ 1,     1.5,   1+1j,  1+0j, 0+1j,    -j;     1,     1.5,   1+1j,  1+0j, 0+1j,    -j;     1,     1.5,   1+1j,  1+0j, 0+1j,    -j;     1,     1.5,   1+1j,  1+0j, 0+1j,    -j]')
    #B = [1,     1.5,   1+1j,  1+0j, 0+1j,    -j;
    #     1,     1.5,   1+1j,  1+0j, 0+1j,    -j;
    #     1,     1.5,   1+1j,  1+0j, 0+1j,    -j;
    #     1,     1.5,   1+1j,  1+0j, 0+1j,    -j]
    C = Matrix('[1.1,2.2,3.3;j,0j,-0+0j;3-5j,0+3j,0.34]')
    #C = [1.5, 2.5, 3.5;
    #     j,   0j,  -0+0j;
    #     3-5j,0+3j,0.25]
    D = Matrix('[1,0,0,0,0;0,1,0,0,0;     0,0,1,0,0;     0,0,0,1,0;     0,0,0,0,1]')
    #D = [1,0,0,0,0;
    #     0,1,0,0,0;
    #     0,0,1,0,0;
    #     0,0,0,1,0;
    #     0,0,0,0,1]
    E = Matrix('[1,2,3;     4,5,6]')
    #E = [1,2,3;
    #     4,5,6]
    F = Matrix('[1,4;     2,5;     3,6]')
    #F = [1,4;
    #     2,5;
    #     3,6]
    G = Matrix('[]')
    H = Matrix('[1,2,3;     4,5,6;     7,8,9]')
    #H = [1,2,3;
    #     4,5,6;
    #     7,8,9]
    I = Matrix('[j,j,j,j,j,j;     j,j,j,j,j,j;     j,j,j,j,j,j;     j,j,j,j,j,j]')
    #I = [j,j,j,j,j,j;
    #     j,j,j,j,j,j;
    #     j,j,j,j,j,j;
    #     j,j,j,j,j,j]
    J = Matrix('[1, 2, 3, 4, 5;     6, 7, 8, 9, 10;     11,12,13,14,15;     16,17,18,19,20;     21,22,23,24,25]')
    #J = [1, 2, 3, 4, 5;
    #     6, 7, 8, 9, 10;
    #     11,12,13,14,15;
    #     16,17,18,19,20;
    #     21,22,23,24,25]
    K = Matrix('[1j, 2j, 3j, 4j, 5j;     6j, 7j, 8j, 9j, 10j;     11j,12j,13j,14j,15j;   16j,17j,18j,19j,20j;     21j,22j,23j,24j,25j]')
    #K = [1j, 2j, 3j, 4j, 5j;
    #     6j, 7j, 8j, 9j, 10j;
    #     11j,12j,13j,14j,15j;
    #     16j,17j,18j,19j,20j;
    #     21j,22j,23j,24j,25j]
    L = Matrix('[4,7;     2,6]')
    #L = [4,7;
    #     2,6]
    M = Matrix('[1,0,0,0;     1,1,0,0;     1,2,1,0;     1,3,3,1]')
    #M = [1,0,0,0;
    #     1,1,0,0;
    #     1,2,1,0;
    #     1,3,3,1]
    N = Matrix('[1,0,0,0;-1,1,0,0;1,-2,1,0;-1,3,-3,1]')
    #N = [1,  0,  0,  0;
    #     -1, 1,  0,  0;
    #     1,  -2, 1,  0;
    #     -1, 3,  -3, 1]
    pt('A->', A)
    pt('B->', B)
    pt('C->', C)
    pt('D->', D)
    pt('E->', E)
    pt('F->', F)
    pt('G->', G)
    pt('H->', H)
    print('-----------------------------A+B------------------------------')
    pt('A+B->',A + B)
    pt('A+I->',A + I)
    pt('B+I->',B + I)
    print('-----------------------------A-B------------------------------')
    pt('A-B->',A - B)
    print('-----------------------------A*B------------------------------')
    pt("Matrix('[4,7;2,6]') * Matrix('[0.6,-0.7;-0.2,0.4]') ->",Matrix('[4,7;2,6]') * Matrix('[0.6,-0.7;-0.2,0.4]'))
    #pt('A*B->',A * B)
    pt('A->', A)
    pt('A*2->',A * 2)
    pt('A->', A)
    pt('A*2.5->',A * 2.5)
    pt('A->', A)
    pt('A*1+1j->',A * (1+1j))
    print('------------------------------A/c-----------------------------')
    pt('A->',A)
    pt('A/2->',A / 2)
    pt('A->', A)
    pt('A/0.8->',A / 0.8)
    pt('A->', A)
    pt('A/1+1j->',A / (1+1j))
    print('-----------------------------A**c-----------------------------')
    #pt('A**2->',A**2)
    #pt('B**2->',B**2)
    pt('C**3->',C**3)
    pt('D**3->',D**3)
    #pt('E**3->',E**3)
    #pt('F**3->',F**3)
    pt('G**3->',G**3)
    print('-----------------------------==-------------------------------')
    pt('A == A ->',A == A)
    pt('G == F ->',G == F)
    pt('B == F ->',B == F)
    pt('E == C ->',E == C)
    pt('F == F ->',F == F)
    print('-----------------------------isIdentity-----------------------')
    pt('A.isIdentity()->',A.isIdentity())
    pt('B.isIdentity()->',B.isIdentity())
    pt('C.isIdentity()->',C.isIdentity())
    pt('D.isIdentity()->',D.isIdentity())
    pt('E.isIdentity()->',E.isIdentity())
    pt('F.isIdentity()->',F.isIdentity())
    pt('G.isIdentity()->',G.isIdentity())
    print('-----------------------------isSquare-----------------------')
    pt('A.isSquare()->',A.isSquare())
    pt('B.isSquare()->',B.isSquare())
    pt('C.isSquare()->',C.isSquare())
    pt('D.isSquare()->',D.isSquare())
    pt('E.isSquare()->',E.isSquare())
    pt('F.isSquare()->',F.isSquare())
    pt('G.isSquare()->',G.isSquare())
    pt('H.isSquare()->',H.isSquare())
    print('----------------------------transposition-------------------')
    pt('E.transposition()->',E.transposition())
    pt('F == E.transposition() ->',F == E.transposition())
    print('----------------------------index---------------------------')
    pt('A[2]->',A[2])
    pt('B[3,1]->',B[3,1])
    #pt('G[2.2]->',G[2.2])
    x = deepcopy(A)
    pt('x ->',x)
    x[2,2] = 1234567
    pt('x[2,2] = 1234567 x[2,2]->',x[2,2])
    #x[0] = H
    #pt('x[0] = H  x->',x)
    print('---------------------------slice----------------------------')
    pt('A[1:3:2,1:6:2]->',A[1:3:2,1:6:2])
    pt('A[0:4:2,1:6:2]->',A[0:4:2,1:6:2])
    pt('A[:] ->',A[:])
    x = deepcopy(J)
    x[1:6:2,1:6:2] = K
    pt('x copy K x[1:6:2,1:6:2] = K x ->',x)
    print('--------------------------Error-----------------------------')
    try:
        x = Matrix('[dfxcgvb;sd345fb,vsd7j7jfgse,vsdfv;sdvrer]')
    except MatrixSyntaxError:
        print("x = Matrix('[dfxcgvb;sd345fb,vsd7j7jfgse,vsdfv;sdvrer]')  -> correct error")
    try:
        x = A**0
        pt('x = A**0 x->',x)
    except MatrixSyntaxError:
        print("x = A**0 -> correct error")
    try:
        pt('H.determinant() ->',H.determinant()) 
        pt('H.inverse() ->',H.inverse())
    except MatrixSyntaxError:
        print("pt('H.inverse() ->',H.inverse()) ->correct error")
    print('---------------------------2*2inverse-----------------------')
    pt('L ->', L)
    pt('L.determinant() ->',L.determinant())
    pt('L.inverse() ->',L.inverse())
    pt('L.inverse().inverse() ->',L.inverse().inverse())
    pt('D.inverse() ->',D.inverse())
    print('--------------------------n*n inverse-----------------------')
    pt('the inverse of M shoule be N  M.inverse() ->',M.inverse())
    

def b():
    x = Matrix("[1,2,3; 4,5,6; 7,8,9]")
    y = Matrix("[0,1,2; 3,4,5; 6,7,8]")
    z = x + y
    print(z) #[1,3,5;7,9,11;13,15,17]
    z = x-y
    print(z) #[1,1,1;1,1,1;1,1,1]
    z = x * 2
    print(z) #[2,4,6;8,10,12;14,16,18]
    z = x * y
    print(z) #[24,30,36;51,66,81;78,102,126]
    print(z/2) #[12,15,18;25.5,33,40.5;39,51,63]
    z = x**3 #e.g., x**3 = xxx
    print(z) #[468,576,684;1062,1305,1548;1656,2034,2412]
    print(x == y) #False
    print(x == Matrix("[1,2,3; 4,5,6;7,8,9]")) #Ture
    print(x.isIdentity()) #False
    print(Matrix("[1,0,0,0; 0,1,0,0; 0,0,1,0; 0,0,0,1]").isIdentity()) #True
    print(x.isSquare()) #False
    print(Matrix("[1,2,3,4; 0,1,4,0; 0,0,1,0; 0,0,0,1]").isSquare()) #True
    z = x[2]
    print(z) #[7,8,9]
    print(x[2,1]) #8
    z = x[1:3:1,0:3:2]
    print(z) #[4,6;7,9]
    x[2] = Matrix("[17,18,19]")
    print(x) #[1,2,3;4,5,6;17,18,19]
    x[1,2] = 0
    print(x) #[1,2,3;4,5,0;17,18,19]
    x[1:3:1,0:3:2] = Matrix("[14,16;7,9]")
    print(x) #[1,2,3;14,5,16;7,18,9]
    x = Matrix("[2,-2;-1,5]")
    print(x.determinant()) #8
    x = Matrix("[2,4;1,0]")
    z= x.inverse()
    print(z) #[0,1;0.25,-0.5]

i = True
while i:
    ty = input('type 1 for test written by myself, 2 for test from Example:')   
    if ty == '1':
        a()
        i = False
        input('press enter to quit')
    elif ty == '2':
        b()
        i = False
        input('press enter to quit')
    else:
        get = input('please choose again or type q to quit:')
        if get == 'q':
            break
        i = True

    









