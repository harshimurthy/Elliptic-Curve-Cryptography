#using python for Shank's algorithm

#S Table
print "Shank's algorithm!\n"
print "\n\n S table \n"
for x in range(0,46):
    val = (5**(45*x))%2017;
    print x," ",val,"\n";
 
#T table 
print "\n\n T table \n"
for y in range(0,46):
    val = (1736*(5**y))% 2017;
    print y,"  ",val,"\n";

#Finding values from S and T table to compute x
for x in range(0,46):
    x_val = (5**(45*x))%2017;
    for y in range(0,46):
        y_val = (1736*(5**y))% 2017;
        if x_val==y_val:
            print x," ",y,"\n"
