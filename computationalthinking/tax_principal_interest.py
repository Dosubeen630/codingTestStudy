savings_principal = 15000000
interest = savings_principal * 0.0325 * 3
tax = interest * 0.154
principal_interest = savings_principal + interest - tax

print("원금:", savings_principal)
print("이자:", interest)
print("세금:", tax)
print("원리금:", principal_interest)