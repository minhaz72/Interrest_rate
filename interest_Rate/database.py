class Database : 
    def take_loan(amm : int ,   tim : int  ) : # amm : ammount , tim : time : 
        total_ammount = amm * tim * (5/ 100 )
        print( ' your total ammount to pay is ' , total_ammount )
        print( f' and this sould be payed in {tim}  years  and every mounth you shold pay {total_ammount / (tim* 12 )} ')
    def give_loan(amm: int, tim: int ):
        total_ammount= amm * (1+ (5/100 ))**tim 
        print( f'your total ammount is {total_ammount }')
         
        