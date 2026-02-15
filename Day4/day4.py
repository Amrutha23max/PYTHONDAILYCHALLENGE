D = int(input("ENTER THE LAST DIGIT OF REGISTRATION NUMBER(NOT 0):"))
print("Register Digit (D):",D)
N= int(input("number of scores :"))
activity_scores = [0]*N;
Invalid_count =0;
Valid_count =0
low_risk =[]
medium_risk=[]
high_risk=[]
critical_risk=[]
for i in range(N):
    score = int(input("ENTER THE SCORE:"))
    activity_scores[i] = score
   
for i in range(N):
     if activity_scores[i]<0:
        Invalid_count +=1
     else:
         Valid_count+=1
         if activity_scores[i]>=0 and activity_scores[i]<=30:
           low_risk =low_risk + [activity_scores[i]]
         elif activity_scores[i]>=31 and activity_scores[i]<=60:
           medium_risk=medium_risk+ [activity_scores[i]]
         elif activity_scores[i]>=61 and activity_scores[i]<=100:
           high_risk=high_risk+[activity_scores[i]]
         else:
           critical_risk=critical_risk+[activity_scores[i]]
print("\n BEFORE PERSONALISATION LOGIC:\n")

print("low_risk :",low_risk)
print("medium_risk:",medium_risk)
print("high_risk:",high_risk)
print("critical_risk:",critical_risk)

new_low =[]
new_medium =[]
new_high =[]
new_critical =[]
removed_entries = 0

for i in range(len(low_risk)):
    if low_risk[i]%D!=0:
        new_low = new_low+[low_risk[i]]
    else:
        removed_entries +=1
low_risk = new_low
for i in range(len(medium_risk)):
    if medium_risk[i]%D!=0:
        new_medium = new_medium+[medium_risk[i]]
    else:
        removed_entries +=1
medium_risk = new_medium
for i in range(len(high_risk)):
    if high_risk[i]%D!=0:
        new_high = new_high+[high_risk[i]]
    else:
        removed_entries +=1
high_risk = new_high
for i in range(len(critical_risk)):
    if critical_risk[i]%D!=0:
        new_critical = new_critical+[critical_risk[i]]
    else:
        removed_entries +=1

critical_risk = new_critical      





print("\nAFTER PERSONALISATION LOGIC:\n")

print("low_risk :",low_risk)
print("medium_risk:",medium_risk)
print("high_risk:",high_risk)
print("critical_risk:",critical_risk)

print("\nTotal Valid Entries:",Valid_count)
print("Ignored Entries:", Invalid_count)
print("Removed Due to Personalization:",removed_entries)





    

