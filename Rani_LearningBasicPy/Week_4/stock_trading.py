# coding: utf-8
## COMP1730/6730 S2 2022 - Homework 4
# Submission is due 09:00am, Monday the 19th of September, 2022.

## YOUR ANU ID: uxxxxxxx
## YOUR NAME: XXX YYY

## You should implement one function stock_trade; you may define
## more functions if this will help you to achieve the functional
## correctness, and to improve the code quality of you program

import math

def stock_trade(stock_price, capital, p):

    starting_capital = capital
    portofolio = 0
    
    for count, price in enumerate(stock_price):

        quantity = round(capital * (1-p) / price)

        if count == 0:
            if math.floor(capital * (1-p)) <= price * quantity:
                portofolio += quantity
                capital -= price * quantity
            else:
                continue
        else:
            # make a comparison with previous loop
            if stock_price[count - 1] > price:

                if math.floor(capital * (1-p)) <= price * quantity:
                    portofolio += quantity
                    capital -= price * quantity
                else:
                    continue
            elif stock_price[count - 1] < price:                
                total_shares_to_be_sell = round((1-p)*portofolio)
                
                if total_shares_to_be_sell != 0 and total_shares_to_be_sell <= portofolio:
                    capital += price*total_shares_to_be_sell
                    portofolio -= total_shares_to_be_sell
    
    # calculation profit or loss
    if stock_price:
        end_capital = capital + portofolio*stock_price[-1]
    else:
        return 0

    return end_capital - starting_capital
    

def test_stock_trade():
    ''' some typical trading situations but by no means exhaustive
    '''
    assert math.isclose( stock_trade([1,1,1,1,1], 100, 0.5), 0.0 ) 
    assert math.isclose( stock_trade([100, 50, 50], 10, 0.01), 0.0 ) 
    assert math.isclose( stock_trade([50, 100, 50], 10, 0.01), 0.0 ) 
    assert math.isclose( stock_trade([1,2,3,4,5], 2, 0.5), 5-1 )
    assert math.isclose( stock_trade(tuple(), 100, 0.5), 0.0 )
    assert math.isclose( stock_trade([1, 10, 2.0, 5.0], 50, 0.5), 268.0 )
    assert math.isclose( stock_trade([1, 10, 2.0, 2.0, 5.0, 5], 50, 0.5), 268.0 )


def test_stock_trade_more():
    ''' some typical trading situations but by no means exhaustive
    '''
    assert math.isclose( stock_trade([1, 100, 10, 10], 10, 0.9), 10-1 )
    assert math.isclose( stock_trade([], 100, 0.5), 0.0 )
    assert math.isclose( stock_trade(tuple(), 100, 0.5), 0.0 )
    print('all tests passed')

test_stock_trade()
test_stock_trade_more()