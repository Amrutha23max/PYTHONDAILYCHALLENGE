# Smart Transaction Risk Detector

## Problem
This program analyzes a list of daily transaction amounts.  
Each transaction is classified into categories, and patterns are checked to identify suspicious activity and determine the overall risk level.

## Approach
- Used a dictionary to store categorized transactions (normal, large, high risk, invalid)  
- Iterated through the list using a loop and applied conditions for classification  
- Used list comprehension to extract valid transactions  
- Calculated total transaction amount and number of transactions  
- Applied pattern detection rules like frequent transactions and large spending  
- Final risk level is determined based on these conditions  

## Personalization
- High Risk if number of high-risk transactions ≥ (2 + X)  
- Large Spending if total amount > (5000 + X × 100)  

This makes the system dynamic instead of using fixed thresholds.

## Examples

### Example 1
Input:  
[100,200,300]  

Output:  
Low Risk  


### Example 2
Input:  
[100, 2000, 3000, -50, 700, 1500, 2500]  

Output:  
Moderate Risk  

## Learning
This task helped me understand how to use loops, conditions, dictionaries, and list comprehension effectively.  
It also improved my ability to solve real-world problems using Python.
