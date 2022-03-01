import datetime
import time
import math
now=datetime.datetime.now()
print("----------------------------------------------------------------------------------------")
print("                                      ",chr(int('231B',16)),chr(int('231B',16)),chr(int('231B',16)))
print(now.strftime("Date :%d/%m/%y                                              Time:%H:%M:%S"))
print("                             ESTIMATION OF TIME OF DEATH")
print("                               (For Forensic Purpose)")
print("                                 (Fahrenheit Only)")
print("                                                                                 -Saran")
print("----------------------------------------------------------------------------------------")
Body_Temperature=float(input("Enter the body temperature (in fahrenheit)  :"))
Normal_Temperature=98.6
Surface_Temperature=int(input("Enter the surface temperature of the room   :"))
After=float(input("How many hours after you see the body       :"))
After_Temperature=float(input("Enter the body temperature after {} hours  ?".format(After)))
C=(Body_Temperature-Surface_Temperature)
e=(After_Temperature-Surface_Temperature)/C
Upp=((Normal_Temperature-Surface_Temperature)/C)
l1=math.log(e)
ll=After*(math.log(Upp))
lll=(ll/l1)
print("The hours =",lll)#4.57
x=((int(lll))*-1)#4
xx=x+lll#0.57
xxx=((round(xx*100))*-1)#57
Sec=round(1)
yn=input("If you want to know exact time of the death(Y/N)?")
if (yn=="Y" or yn=="y"):
    Year=int(input("Enter the  Current Year        :"))
    Month=int(input("Enter the Current Month        :"))
    Day=int(input("Enter the Current Day          :"))
    now2=datetime.datetime(Year,Month,Day,x,xxx,Sec)
    Exact_Time=now-now2
    print("THE EXACT TIME OF THE DEATH IS ",Exact_Time)
else:
    print("Note")
    print("Ex: If the hours = -5.75 means subtract the hours with time now")
    print("Thank you")
    
print("----------------------------------------------------------------------------------------")
