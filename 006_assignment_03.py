t1=int(input("Give me the start time(hour): "))
t2=int(input("Give me the start time (minute): "))
t3=int(input("Give me the duration in minutes: "))
r=(t1*60)+t2+t3
print("The finish time is: ",end="")
print(r//60,r%60,sep=":")
