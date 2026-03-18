transactions = [100, 2000, 3000, -50, 700, 1500, 2500]
X = 4  
categories = {
    "normal":[],
    "large":[],
    "high_risk":[],
    "invalid":[]
}
for t in transactions:
    if t<=0:
        categories["invalid"].append(t)
    elif 1<=t<=500:
        categories["normal"].append(t)
    elif 501<=t<=2000:
        categories["large"].append(t)
    else:
        categories["high_risk"].append(t)
valid_transaction = [t for t in transactions if t>0]
total_amount =  sum(valid_transaction)
total_transactions = len(valid_transaction)
large_spending  = total_amount >(5000+ X*100)
high_risk_condition =  len(categories["high_risk"])>=(2+X)

frequent = total_transactions >5

if high_risk_condition:
    risk = "High Risk"
elif frequent or large_spending:
    risk = "Moderate Risk"
else:
    risk = "Low Risk"

print("Categorized Transactions:",categories)
print("Total Transaction Value:", total_amount)
print("Number of Transactions:",total_transactions)
print("Final Risk Classification:", risk)
