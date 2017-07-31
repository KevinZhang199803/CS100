class program(object):
    def __init__(self,string):
        self.string=string
        s=string
        s=s.replace(' ','').replace('bool','').replace('\t','').replace('\r','')
        s=s.replace('&',' and ').replace('!','not ').replace('|',' or ')
        strstore=s.split('\n')
        if '' in strstore and '{' in strstore and '}' in strstore and 'main()' in strstore:
            strstore.remove('{')
            strstore.remove('}')
            strstore.remove('main()')
            for i in range(strstore.count('')):
                strstore.remove('')
        for i in range(len(strstore)): 
            if ':' in strstore[i]:
                strstore[i]=strstore[i][strstore[i].find(':')+1:]
            if 'while'in strstore[i] or 'if' in strstore[i]:
                strstore[i]=strstore[i]+':'
            elif 'return'in strstore[i]:
                strstore[i]=strstore[i].replace('return','arg=')
        for i in range(len(strstore)):
            strstore[i]+='\n'
        for i in range(len(strstore)):
                if 'if' in strstore[i]:
                        a=i
                if 'fi' in strstore[i]:
                        b=i
                        ifls=strstore[a+1:b]
                        for i in range(len(ifls)):
                                ifls[i]='\t'+ifls[i]
                        strstore[a+1:b]=ifls
        for i in range(len(strstore)):
                if 'while' in strstore[i]:
                        m=i
                if 'done' in strstore[i]:
                        n=i
                        whilels=strstore[m+1:n]
                        for j in range(len(whilels)):
                                whilels[j]='\t'+whilels[j]
                        strstore[m+1:n]=whilels                             
        comb=''.join(strstore)
        self.strstore=strstore
        self.comb=comb
        
    def evaluate(self):
        biglist=self.strstore
        for i in range(len(biglist)):
                if 'if' in biglist[i]:
                        a=i
                if 'fi' in biglist[i]:
                        b=i
                        ifls=biglist[a+1:b]
                        for i in range(len(ifls)):
                                ifls[i]='\t'+ifls[i]
                        biglist[a+1:b]=ifls
        for i in range(len(biglist)):
                if 'while' in biglist[i]:
                        m=i
                if 'done' in biglist[i]:
                        n=i
                        whilels=biglist[m+1:n]
                        for j in range(len(whilels)):
                                whilels[j]='\t'+whilels[j]
                        biglist[m+1:n]=whilels
        for i in range(len(biglist)):
                if 'while'in biglist[i]:
                        m=i
                if 'done'in biglist[i]:
                        n=i
                        biglist.insert(n+1,'\t\tk=k+1;\n\t\tif k>100:\n\t\t\tbreak;\n\t\telse:\n\t\t\tpass;\n')        
        if 'while' in ''.join(biglist):
                biglist.insert(1,'global k\nk=0\n')
        biglist.insert(0,'arg=0\n')
        for i in biglist:
                if 'fi' in i or 'done' in i:
                        biglist.remove(i)
        con=''.join(biglist)
        print(con)
        #print(eval(big
        exec(con)
        if 'while' in con:
                if k<=100:
                        return eval('arg')
                else:
                        return 'infinite'
        else:
                return eval('arg')
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
p = program(s)
