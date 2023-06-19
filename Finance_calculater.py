'''This program allows the user to calculate their interest on an investment or 
Calculate the amount that should be repaid on a home loan each month.'''

import math

print('nvestment - to calculate the amount of interest you earn on your investment')
print('Bond       - to calculate the amount you will have to pay on a home loa per month')
user_choice = input('Enter either investment or bond from the menu above : ')
user_choice_lowercase = user_choice.lower() #This is to make the user input case insensive

if user_choice_lowercase == "investment":    #If the user choose investment the programe calculates the return 
                                                #on the amount of investment after simple and compound interest.
    principal = int(input('Please enter the deposit you like to invest: '))
    interest_rate = float(input('Please enter the interest rate: '))
    years = int(input('For how long you want to invest? '))
    print('Please choose the type of interest: either simple or compound')
    interest_type = input('Please type in simple or compound: ')
    interest_type = interest_type.lower()
    my_interest_rate = interest_rate/100
    if interest_type == 'simple':                    #
        total_return_simple = principal * (1 + my_interest_rate * years) # Given formula for simple interest
        print(f'The total amount of money you get after investing £{principal} for {years}  at the interest rate of {interest_rate}% is £{round(total_return_simple,2)}')
    
    elif interest_type == 'compound':                #If the user choose compound interest calculate total return on investment based on that.
        total_return_compound = principal * math.pow((1 + my_interest_rate),years)
        print(f'The total amount of return you get after investing £{principal} for {years} at compound interest{interest_rate}% is £{round(total_return_compound,2)} ')
    else:
        print(f'{interest_type} is not correct.')
elif user_choice_lowercase == 'bond':                #If the user choose bond instead of investment calculate the amount of money you pay per month.
    present_value_of_the_house = int(input('What is the pressent value of your house?'))
    interest_rate = float(input('Please enter the interest rate:'))
    num_of_months = int(input('How many months do you plan to pay you mortgage?'))
    my_interest_rate = interest_rate/100
    interest_rate_per_month = my_interest_rate/12
    repayment = interest_rate_per_month * present_value_of_the_house / (1 - math.pow((1 + interest_rate_per_month),-num_of_months))
    print(f'The present value of the house is, {present_value_of_the_house}')
    print(f' The nuber of months you agreed to repay your mortgage is{num_of_months} months') 
    print(f'The interest rate per month  is {round(interest_rate_per_month, 3)}% ')
    print(f'Total amount of mortgage you pay back per month is,  {round(repayment,2)}')
else:
    print(f'{user_choice_lowercase} is incorrect path.') #If the user didn't choose ether investment or bond the program retuns error message

    print('******************** End of finance calculator program  **********************')