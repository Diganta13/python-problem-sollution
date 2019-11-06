if __name__ == '__main__':

    n = int(input())
    d = {}
    l2 = []

for i in range(n):
    name = input() # here i have taken keys as strings
    marks = float(input()) # here i have taken values as integers
    d[name] = marks



values = (list(set(d.values())))
values = sorted(values)

for i in d.keys():
    if(d[i] == values[1]):
        l2.append(i)
l2=sorted(l2)        
for i in l2:
    print(i)
