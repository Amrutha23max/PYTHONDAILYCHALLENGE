full_name = input("enter full name:")
L = len(full_name.replace(" ",""))
        
no_of_requests = int(input("ENTER NUMBER OF INPUTS:"))
total_entries =[]
total_valid_count =0
for i in range(no_of_requests):
    request = int(input("ENTER NUMBER OF REQUESTS:"))
    total_entries.append(request)
low_demand = []
moderate_demand = []
high_demand = []
invalid_requests = []
no_demand = []

for request in total_entries:
    if request  <0:
        invalid_requests.append(request)
    elif request ==0:
        no_demand.append(request)
        total_valid_count +=1
    elif 1<= request <=20:
        low_demand.append(request)
        total_valid_count +=1
    elif 21<= request <=50:
        moderate_demand.append(request)
        total_valid_count +=1
    else:
        high_demand.append(request)
        total_valid_count +=1
        
print("=== Before PLI Filtering ===")
print("Low Demand:", low_demand)
print("Moderate Demand:", moderate_demand)
print("High Demand:", high_demand)
print("Invalid Requests:", invalid_requests)
print("No Demand Requests:", no_demand)
print()
# PLI
PLI = L%3

requests_removed =0
if PLI ==0:
    requests_removed = len(low_demand)
    low_demand = []
elif PLI ==1:
    requests_removed = len(high_demand)
    high_demand = []
elif PLI ==2:
    requests_removed = len(low_demand)+len(high_demand)
    low_demand =[]
    high_demand=[]
    
print("=== Emergency Dispatch Report (AFTER PLI FILTERING) ===")
print("Name Length (L):", L)
print("PLI Logic: L%3")
print("PLI Value:", PLI)
print()   
print("Total Valid Requests:", total_valid_count)
print("Requests Removed due to PLI:", requests_removed)
print()
print("Low Demand:", low_demand)
print("Moderate Demand:", moderate_demand)
print("High Demand:", high_demand)
print("Invalid Requests:", invalid_requests)
print("No Demand Requests:", no_demand)
