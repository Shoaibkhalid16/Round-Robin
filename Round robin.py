print("                                    This Is Round Robin Process")
size = int(raw_input("Enter How many Process you want to Enter ??"))

process = [0] * size
arrival = [0] * size
burst = [0] * size
totaltime = 0
for i in range(size):
    process[i] = (raw_input("Enter process name"))
    arrival[i] = int(raw_input("Enter Arrival Time for the process"))
    burst[i] = int(raw_input("Enter Burst time for the Process"))
    totaltime += burst[i]
qt = int(raw_input("ENter quantum time"))
print(" ")
print("                             your Enter Pocess Information")
for i in range(size):
    print(process[i], "     ", arrival[i], "      ", burst[i])
print('Quantum time is: ', qt)
turn = [0] * size
wt = [0] * size
rt = [0] * size
waitingtime = [0] * size
turntime = [0] * size
for i in range(size):
    rt[i] = burst[i]
time = 0
while True:
    done = True
    for i in range(size):
        if rt[i] > 0:
            done = False
            if rt[i] > qt:
                time += qt
                rt[i] -= qt
            else:
                time = time + rt[i]
                wt[i] = time - burst[i]
                rt[i] = 0

    if done == True:
        break

for i in range(size):
    turn[i] = burst[i] + wt[i]

for j in range(size):
    turntime[j] = turn[j] - arrival[j]
    waitingtime[j] = turn[j] - arrival[j] - burst[j]

sum1 = 0
sum2 = 0

for k in range(size):
    sum1 += waitingtime[k]
    sum2 += turntime[k]
awt = sum1 / size
atat = sum2 / size

for j in range(size):
    first1 = min(burst)
    runn = burst.index(first1)
    print(process[j], 'arrival time is', arrival[j], 'and ends at ', turn[j])

print('average waiting time is', awt)
print('average turn around time is', atat)