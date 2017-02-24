#using python to find the suitable value of alpha
for i in range (1,110):
    smooth = (5**i)%2017
    if smooth%2==0 and smooth%3==0 and smooth%5==0:
        print i," ",smooth,"\n"
