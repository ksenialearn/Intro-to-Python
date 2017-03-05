#Use bisection search to find the smallest monthly payment

monthlyInterestRate= annualInterestRate/12.0
balance1= balance

months =12

lowPayLow= balance/12
lowPayUp= (balance*(1+monthlyInterestRate)**12)/12.0

while round(balance,2) != 0:

    lowPay= (lowPayUp + lowPayLow)/2.0
 
    balance= balance1
    count= 0   
          
    while count < months:
        
        unpaidBalance= balance- lowPay
        balance= unpaidBalance + (monthlyInterestRate * unpaidBalance)
        count +=1
    
    if balance > 0:
        lowPayLow= lowPay
    else:
        lowPayUp= lowPay
    
print 'Lowest Payment:', round(lowPay,2)
