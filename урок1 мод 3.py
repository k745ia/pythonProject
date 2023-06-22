'''
acbd

a 1

b 1

d 1

c 1

aabc

a 2

b 1

c 1
'''






# def counter(s): # O(N**2)
#     for i in s:
#         count = 0
#         for j in s:
#             if i == j:
#                 count += 1
#         print(i,count)




# def counter(s): #(N * M)
#     for i in set(s):
#         count = 0
#         for j in s:
#             if i == j:
#                 count += 1
#         print(i,count)




def counter(s): # O(N)
    syms = {}
    for i in s:
        syms[i] = syms.get(i, 0) + 1
    for i, count in syms.items():
        print(i,count)


counter('aaaaadsfiyad')
print(len('aaaaadsfiyad'))
