def ways(stairs):
    if stairs<0:
        return 0
    #if no stair left u will reach the top in one step
    if stairs==0:
        return 1
    onestep=0
    twostep=0
    if stairs>=2:
        twostep=ways(stairs-2)
        #jump 1 if 1 or more steps remain
    onestep=ways(stairs-1)
    return twostep+onestep
stairs=int(input("Enter the number of stairs u want to climb:"))
print("Number of ways to climb are:",ways(stairs))