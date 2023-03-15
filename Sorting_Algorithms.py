import random


def BubSort(lst):
    notSorted = True
    swaps = 0
    passes = 1
    checks = 1

    while notSorted:

        for i in range(1,len(lst)):
            if lst[i-1] > lst[i]:
                lst[i], lst[i-1] = lst[i-1], lst[i]
                swaps += 1

        tally = 1
        for j in range(1,len(lst)):
            if lst[j-1] <= lst[j]:
                tally += 1
            checks += 1
        if tally == len(lst):
            notSorted = False
            break

        passes += 1


    print(f"""\n\n\tBubble Sorted
Number of Item Swaps: {swaps}
Number of Passes: {passes}
Number of Checks: {checks}\n""") #type: ignore


def InSort(lst):
    
    swaps = 0
    passes = 1
    checks = 0
    while True:

        for i in range(1,len(lst)):
            if lst[i-1] > lst[i]:
                for j in range(i,0,-1):
                    if lst[j-1] > lst[j]:
                        lst[j], lst[j-1] = lst[j-1], lst[j]
                        swaps += 1
                    passes += 1

        tally = 1
        for j in range(1,len(lst)):
            if lst[j-1] <= lst[j]:
                tally += 1
            checks += 1
        if tally == len(lst):
            break
    
    print(f"""\n\n\tInsertion Sort
Number of Item Swaps: {swaps}
Number of Passes: {passes}
Number of Checks: {checks}\n""") #type: ignore

def fmt_list(lst):
    out = "["
    for i in range(len(lst)):
        if i%10 == 0 and i != 0:
            out += '\n'
        elif i == len(lst)-1:
            out += f"{lst[i]}]"
        else:
            out += f"{lst[i]}, "
            
    return out


lset = []

for i in range(100):
    num = random.randint(1,1001)
    if num not in lset:
        lset.append(num)

dataset = (tuple(lset))
    


control = sorted(dataset)

print(f"\t\tOriginal List: \n{fmt_list(lset)}\n\n\t\tSorted List: \n{fmt_list(control)}\n\n\n")

BubSort(list(dataset))
InSort(list(dataset))
input()
