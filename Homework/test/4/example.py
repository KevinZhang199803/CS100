#s=False
#s=[0,0,1,1,0,0;0,0,0,0,0,0;0,0,0,1,0,0;0,0,0,0,1,0;0,1,0,0,0,1;0,0,0,0,1,0]
s="""
    bool x = True;
    bool y = False;
    bool z = True;
    bool a = True;
    main()
    {
    1:  x = !y;
    2:  z = !x;
    3:  if ( (x & y) | (! z) )
    4:      y= !y;
    5:      pass;
        fi
    6:  x=!y;
    7:  z=!z;
    8:  while ( ( x | y) & (a | z) )
    9:      a=!y;
    10:     y=!z;
        done
    11: return x;
    } 
""" 

#s1=True
#s1=[0,0,1,1,0;0,0,0,0,0;0,0,0,1,0;0,1,0,0,1;0,0,0,1,0]
s1='''
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
    8:  while ( ( x | y) & (a | z) )
    9:      a=!y;
    10:     y=!z;
        done
    11: return x;
    } 
''' 

#s2=infinite
#s2=[0,0,1,1,0,0;0,0,0,0,0,0;0,0,0,1,0,0;0,0,0,0,1,0;0,1,0,0,0,1;0,0,0,0,1,0]
s2="""
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

#s3=infinite
#s3=[0,0,1,1,0,0,0,0;0,0,0,0,0,0,0,0;0,0,0,1,0,0,0,0;0,0,0,0,1,0,0,0;0,1,0,0,1,0,1,0;0,0,0,0,0,0,0,0;0,0,0,0,1,0,0,0;0,0,0,0,0,0,0,0]
s3="""
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
    a:  while ( ( x | y) & (a | z) )
    b:      a=!y;
    c:     y=!z;
        done
    11: return x;
    } 
""" 
#s4=infinite
#s4=
s4="""
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
    a:  if ( (x & y) | (! z) )
    b:      y= !y;
    c:      pass;
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

#s5=
s5="""
    bool x = True;
    bool y = False;
    bool z = True;
    bool a = True;
    main()
    {
    8:  while ( ( x | y) & (a | z) )
    9:      a=!y;
    10:     y=z;
        done
    3:  if ( (x & y) | (! z) )
    4:      y= !y;
    5:      pass;
        fi
    11: return x;
    } 
""" 

#s=False
#s6=[0,0,1,1,0,0;0,0,0,0,0,0;0,0,0,1,0,0;0,0,0,0,1,0;0,1,0,0,0,1;0,0,0,0,1,0]
s6="""
    bool x = True;
    bool y = False;
    bool z = True;
    bool a = True;
    main()
    {
    1:  x = !y;
    2:  z = !x;
    6:  x=!y;
    7:  z=!z;
    11: return x;
    } 
""" 

#s7
s7="""
    bool x = True;
    main()
    {
    ac1:  x= !y;
    bd2:  z= !x;
    qw3:  if ( (x & y) | (! z) )
    re4:      y= !y;
    ty5:      pass;
        fi
    i6u6:  if ( ( x | y) & (a | z) )
    o0i7:      a=!y;
    e9r8:     y=!z;
        fi
    wrr8:   x!=y
    w6rr9:   x!=y
    wrr10:   x!=y
    q4w3:  if ( (x & y) | (! z) )
    r2e4:      y= !y;
    ty5:      aaaaaa;
        fi
    yu9:  while ( ( x | y) & (a | z) )
    nb10:      a=!y;
    mn11:     y=!z;





        done
    ret12:  if ( ( x | y) & (a | z) )
    iu13:      a=!y;
    uy14:     y=!z;
        fi
    po15:  while ( ( x | y) & (a | z) )
    zx16:      a=!y;
    vc17:     y=!z;
        done
    wrqcr8:   x!=y
    w6r9:   x!=y
    wruyr10:   x!=y
    mn18:  while ( ( x | y) & (a | z) )
    gf19:      a=!y;
    mn20:     y=!z;
        done
    mn5466208:  while ( ( x | y) & (a | z) )
    gf9:      a=!y;
    mn31:     y=!z;
        done
    po21: return x;
    }
    bool y = False;
    bool z = True;
    bool a = True;
"""

s8="""
    bool x = True;
    bool y = False;
    bool z = True;
    bool a = True;
    main()
    {
    1:  x = !y;
    2:  z = !x;
    3:  if ( (x & y) | (! z) )
    4:      y= !y;
    5:      pass;
        fi
    6:  x=!y;
    7:  z=!z;
    11: return x;
    } 
""" 
from program import *

p =  program(s6)
print(p.getCFG())
print(p.getCFG()=='[0,0,1,1,0,0;0,0,0,0,0,0;0,0,0,1,0,0;0,0,0,0,1,0;0,1,0,0,0,1;0,0,0,0,1,0]')
    
