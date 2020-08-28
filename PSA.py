import operator
from prettytable import PrettyTable

def hasArrived(currentTime,arrivalTime) :
    if(arrivalTime <= currentTime) :
        return True
    else :
        return False
    
#start here    
#input
n = int(input("Enter no. of processes : "))
P = [] #list of tupless
for i in range(0,n) :
    print("\nP"+str(i+1)+" :")
    P.append((("P"+str(i+1)),int(input("Arrival time : ")),int(input("Burst time : ")),int(input("Enter priority : "))))

#split processes into zero and non-zero AT categories
ZAT,NZAT = [],[]
for process in P :
    if(process[1] == 0) :
        ZAT.append(process)
    else :
        NZAT.append(process)
ZAT.sort(key = operator.itemgetter(3)) #sorting zero AT processes by their priority
NZAT.sort(key = operator.itemgetter(3)) #sorting non-zero AT by thier priority value respectively
newP = ZAT + NZAT #creating the newP list by appending ZAT and NZAT since the processes are sorted according to Ghant Chart

#calculation of gantt chart
GC = []
startTime = 0
for ele in ZAT :
    GC.append((ele[0],startTime,startTime+ele[2]))
    startTime = startTime + ele[2] #updating start time of new process to end time of old process in the GC
    
for ele in NZAT :
    if(hasArrived(startTime,ele[1])) :
        GC.append((ele[0],startTime,startTime+ele[2]))
        startTime = startTime + ele[2]

#calculation of waiting and turnaround times in order of GC        
zip_lists = zip(GC,newP)
print("Gant Chart ",GC)
WT,TT = [],[]
for (i,j) in zip_lists :
    print("WT :",i[1]-j[1])
    WT.append(i[1]-j[1])
    print("TT :",i[1]-j[1]+j[2])
    TT.append(i[1]-j[1]+j[2])

#output

print("\nImplementation of Priority Scheduling :")

table = PrettyTable()
table.add_column("Process",[ele[0] for ele in GC])
table.add_column("Waiting Time",WT)
table.add_column("Turnaround Time",TT)
print("\n")
print(table)

#avg WT and avg TT       
avg_wt = sum(WT)/n
avg_tt = sum(TT)/n
print("\nAverage Waiting Time =",avg_wt)
print("\nAverage Turnaround Time =",avg_tt)
