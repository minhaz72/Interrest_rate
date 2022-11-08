from colorama import Fore  
import database 
from database  import * 
print(Fore.CYAN , '---------Bangla Link Bank Limited -----------------')
print(Fore.BLACK , 'which you want to try Take loan From Bank : , Give Loan to Bank   ')
a= str(input('enter your response between 1. Take Loan \n 2. Give Loan '))
if a == 'Take Loan ' or a== 'take loan ' or a==  'take Loan ' or a== 'teke loan ': 
    amm = int(input('enter the ammount you want : '))
    tim= int(input('enter the time you want  :'))
    a= Database.take_loan(amm, tim )

else : 
    
    amm = int(input('enter the ammount you want : '))
    tim= int(input('enter the time you want  :'))
    a= Database.give_loan(amm, tim )

    