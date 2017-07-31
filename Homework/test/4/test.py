from program import *

s="""
    bool cs_blablax = True;
    bool y = False;
    bool z = True;
    bool a = True;
    main()
    {
    1:  cs_blablax= !y;
    2:  z= !cs_blablax;
    3:  if ( (cs_blablax & y) | (! z) )
    4:  pass;
        fi
    6:  cs_blablax=!y;
    7:  z=!z;
    8:  while ( ( cs_blablax | y) & (a | z) )
    9:  pass;
        done
    asd: while(True)
    bla:pass;
                  done
    conf:if(True)
    dada:pass;
     fi
    11: return cs_blablax;
    } 
"""

p=program(s)
try:
	A1 = p.evaluate()

	C1 = 'infinite'
	if A1 == C1:
		print('succeeded')
	else:
		print('Your answer EVA:')
		print(A1)
		print('failed')
		print('The answer should be:')
		print(C1)
except:
	print('Cannot be compiled')

try:
	B1 = p.getCFG()

	D1 = '[0,0,1,1,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,1,0,0,0,0,0,0;0,0,0,0,1,0,0,0,0,0;0,0,0,0,0,1,1,0,0,0;0,0,0,0,1,0,0,0,0,0;0,0,0,0,0,0,0,1,1,0;0,0,0,0,0,0,1,0,0,0;0,1,0,0,0,0,0,0,0,1;0,1,0,0,0,0,0,0,0,0]'
	if B1 == D1:
		print('succeeded')
	else:
		print('Your answer CFG:')
		print(B1)
		print('failed')
		print('The answer should be:')
		print(D1)
except:
	print('Cannot be compiled')
print('--------1---------')

s="""
    bool x = True;
    bool y = False;
    bool z = True;
    bool a = True;
    main()
    {
    1:  x= True;
    2:  z= !x;
    3:  if ( (x & y) | (! z) )
    4:      y= !y;
    5:      pass;
        fi
    8:  if (True)
    6:  x=!y;
    7:  z=!z;
    11: return x;
    12: x=True;
        fi
    } 
""" 

p=program(s)
try:
	A1 = p.evaluate()

	C1 = False
	if A1 == C1:
		print('succeeded')
	elif A1 == 'False':
		print('TypeError: should return a boolean value')
	else:
		print('Your answer EVA:')
		print(A1)
		print('failed')
		print('The answer should be:')
		print(C1)
except:
	print('Cannot be compiled')

try:
	B1 = p.getCFG()

	D1 = '[0,1,0,1;0,0,0,1;0,0,0,0;0,0,1,0]'
	if B1 == D1:
		print('succeeded')
	else:
		print('Your answer CFG:')
		print(B1)
		print('failed')
		print('The answer should be:')
		print(D1)
except:
	print('Cannot be compiled')
print('--------2---------')

s = '''
bool x = True;
bool y = False;
bool z = False;
main()
{
	1: x=False;
	2: y=!z;
	3: while (y)
	4: y=!y;
	5: z=!z;
	  done
	6:return y;
}
'''

p=program(s)
try:
	A1 = p.evaluate()
	C1 = False
	if A1 == C1:
		print('succeeded')
	elif A1 == 'False':
		print('TypeError: should return a boolean value')
	else:
		print('failed')
		print('Your answer EVA:')
		print(A1)
		print('The answer should be:')
		print(C1)
except:
	print('Cannot be compiled')

try:
	B1 = p.getCFG()
	D1 = '[0,1,0,0;0,0,1,1;0,1,0,0;0,0,0,0]'
	if B1 == D1:
		print('succeeded')
	else:
		print('Your answer CFG:')
		print(B1)
		print('failed')
		print('The answer should be:')
		print(D1)
except:
	print('Cannot be compiled')
print('--------3---------')

s="""
bool x = True;
bool y = False;
bool z = True;
bool a = True;
main()
{
1:  x= !y;
2:  z= !x;
3:  if ( (x & y) | (! z) )


4:      y= !y;
5:      pass;
    fi
6:  x=!y;


7:  z=!z;
8:  while ( ( x | y) & (a | z) )
9:      a=!y;
10:     y=z;

        done
11: return x;
} 
""" 

p=program(s)
try:
	A1 = p.evaluate()
	C1 = 'infinite'
	if A1 == C1:
		print('succeeded')
	else:
		print('Your answer EVA:')
		print(A1)
		print('failed')
		print('The answer should be:')
		print(C1)
except:
	print('Cannot be compiled')

try:
	B1 = p.getCFG()

	D1 = '[0,0,1,1,0,0;0,0,0,0,0,0;0,0,0,1,0,0;0,0,0,0,1,0;0,1,0,0,0,1;0,0,0,0,1,0]'
	if B1 == D1:
		print('succeeded')
	else:
		print('Your answer CFG:')
		print(B1)
		print('failed')
		print('The answer should be:')
		print(D1)
except:
	print('Cannot be compiled')
print('--------4---------')

s="""
    bool x = True;
    bool y = False;
    bool z = True;
    bool a = True;
    main()
    {
    1:  x= !y;
    2:  z= !x;
    3:  if ( (x & y) | (! z) )
    4:  pass;
        fi
    6:  x=!y;
    7:  z=!z;
    8:  while ( ( x | y) & (a | z) )
    9:  pass;
        done
    asd: while(False)
    bla:pass;
                  done
    conf:if(True)
    dada:pass;
     fi
    11: return x;
    } 
"""

p=program(s)
try:
	A1 = p.evaluate()

	C1 = 'infinite'
	if A1 == C1:
		print('succeeded')
	else:
		print('Your answer EVA:')
		print(A1)
		print('failed')
		print('The answer should be:')
		print(C1)
except:
	print('Cannot be compiled')

try:
	B1 = p.getCFG()

	D1 = '[0,0,1,1,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,1,0,0,0,0,0,0;0,0,0,0,1,0,0,0,0,0;0,0,0,0,0,1,1,0,0,0;0,0,0,0,1,0,0,0,0,0;0,0,0,0,0,0,0,1,1,0;0,0,0,0,0,0,1,0,0,0;0,1,0,0,0,0,0,0,0,1;0,1,0,0,0,0,0,0,0,0]'
	if B1 == D1:
		print('succeeded')
	else:
		print('Your answer CFG:')
		print(B1)
		print('failed')
		print('The answer should be:')
		print(D1)
except:
	print('Cannot be compiled')
print('--------5---------')

# 2-time-loop
s='''
bool x = True;
bool y = True;
main()
{
	1: while (x | y)
	2: y=x;
	3: x=False;
	   done
	4:return y;
}
'''

p=program(s)
try:
	A1 = p.evaluate()

	C1 = False
	if A1 == C1:
		print('succeeded')
	elif A1 == 'False':
		print('TypeError: should return a boolean value')
	else:
		print('Your answer EVA:')
		print(A1)
		print('failed')
		print('The answer should be:')
		print(C1)
except:
	print('Cannot be compiled')

try:
	B1 = p.getCFG()

	D1 = '[0,1,1;1,0,0;0,0,0]'
	if B1 == D1:
		print('succeeded')
	else:
		print('Your answer CFG:')
		print(B1)
		print('failed')
		print('The answer should be:')
		print(D1)
except:
	print('Cannot be compiled')
print('--------6---------')

s='''
bool x = True;
bool y = True;
main()
{
	1: while (True)
	2: y=x;
	3: x=False;
	   done
	4:return y;
}
'''
p=program(s)
try:
	A1 = p.evaluate()

	C1 = 'infinite'
	if A1 == C1:
		print('succeeded')
	else:
		print('Your answer EVA:')
		print(A1)
		print('failed')
		print('The answer should be:')
		print(C1)
except:
	print('Cannot be compiled')

try:
	B1 = p.getCFG()

	D1 = '[0,1,1;1,0,0;0,0,0]'
	if B1 == D1:
		print('succeeded')
	else:
		print('Your answer CFG:')
		print(B1)
		print('failed')
		print('The answer should be:')
		print(D1)
except:
	print('Cannot be compiled')
print('--------7---------')

s='''
bool x = True;
bool y = True;
bool z = False;
bool a = True;
main()
{
	1: x=False;
	2: if (x)
	3: z = True;
	   fi
	4: if (True)
	5: a = False;
	6: pass;
	   fi
	7: y = z|a;
	8: return y;
}
'''

p=program(s)
try:
	A1 = p.evaluate()

	C1 = False
	if A1 == C1:
		print('succeeded')
	elif A1 == 'False':
		print('TypeError: should return a boolean value')
	else:
		print('Your answer EVA:')
		print(A1)
		print('failed')
		print('The answer should be:')
		print(C1)
except:
	print('Cannot be compiled')

try:
	B1 = p.getCFG()

	D1 = '[0,1,1,0,0;0,0,1,0,0;0,0,0,1,1;0,0,0,0,1;0,0,0,0,0]'
	if B1 == D1:
		print('succeeded')
	else:
		print('Your answer CFG:')
		print(B1)
		print('failed')
		print('The answer should be:')
		print(D1)
except:
	print('Cannot be compiled')
print('--------8---------')