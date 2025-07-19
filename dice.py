import random
dice=[1,2,3,4,5,6]
s=0
n=100000
entry_fee=4
gain_amount=n*entry_fee
for i in range(1,n+1):
    outcome=random.choice(dice)
    s=s+outcome
print("the given amount is ",s)
print("the gain amount is",gain_amount)
if gain_amount>s:
    print("the profit is",gain_amount-s)
else:
    print("the loss amount is ",s-gain_amount)
    