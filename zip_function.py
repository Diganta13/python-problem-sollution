def merge_the_tools(s, k):
    # your code goes here

    for part in zip(*[iter(s)] * k):
        d = dict()
        
        print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
