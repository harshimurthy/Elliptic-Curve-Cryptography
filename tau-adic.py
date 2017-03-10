def taunaf(d,mu):
    c0=d
    c1=0
    s=[]
    u=0
    while(c0!=0 or c1!=0):
        if(c0%2==1):
            u=2-(c0-2*c1)%4
            c0=c0-u
        else:
            u=0
        s.append(u)
        nc0=c1+mu*c0//2
        nc1=-c0//2
        c0=nc0
        c1=nc1
    s.reverse()
    print(len(s)-1,s)
    
taunaf(15,1)
