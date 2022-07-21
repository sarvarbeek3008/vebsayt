# # # a = int(input())
# # # c=[]
# # # c.append(map(int, input().split()))
# # # d=sorted(c)
# # # if c==d:
# # #   print("YES")
# # # else:
# # #   print("NO")
# # # print(d)
# # # w = []
# # # c = map(int,input().split())
# # # print((map(int,input().split())))
# # # # print(c)
# # # a = int(input())
# # # print(int(a%10))
 
# # a = int(input())
# # s = []
# # h = []
# # s.append(str(a))
# # for i in s:
# #   for g in i:
# #         if g=="1":
# #               h.append(g)
# # print(ord('a'))


# n = int(input())

# l = list(map(int,input().strip().split()))[:n]

# print(l)

t = int(input())
for x in range(1, t+1):
      l = []
      n = int(input())
      for y in range(1, n+1):
            T = y*y - (y-1)*(y-1)
            l.append(T)
      print(sum(l))