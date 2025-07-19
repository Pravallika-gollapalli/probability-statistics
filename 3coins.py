# import random
# coin=['H','T']
# n=100
# c=0
# p=0
# for i in range(1,n+1):
#     choice=random.choice(coin)
#     if choice=='h':
#         c=c+1
#     else:
#         p=p+1
# print("head count",c)



# half percentile code
import random
dice=[1,2,3,4,5,6]
s=0
c=0
n=100
for i in range(1,n+1):

    outcome=random.choice(dice)
    if outcome%2==0:
        s=s+1
    else:
        c=c+1
print("even count",s)
