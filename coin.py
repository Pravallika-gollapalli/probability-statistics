import random
coin=['H','T']
given_amount_amount=0
n=10
entry_fee=51
gain_amount=n*entry_fee
for i in range(1,n+1):
    flip=random.choice(coin)
    if flip=='h':
        given_amount=40+given_amount
    else:
        given_amount=60+ given_amount
print("the gain amount is",gain_amount)
print("the given amoun t is",given_amount)
if gain_amount>given_amount:
    print("the profit is",gain_amount-given_amount)
else:
    print("the loss is ",gain_amount-given_amount)
