import pandas as pd



filename = "teslaStockData.xlsx"
data = pd.read_excel(filename)

high = data["High"].tolist()
low = data["Low"].tolist()
open = data["Open"].tolist()



def run_calc(start_date , budget, day_variation ):

    i = start_date

    budget = 100
    num_days = day_variation

    shares_high = 0
    shares_low = 0
    shares_avg = 0
    total_spent = 0

    print("Length: ", len(high))


    while (True):
        shares_high += budget / high[i]
        shares_low += budget / low[i]
        shares_avg += budget / ((high[i] + low[i])/2)
        i += num_days
        if i >= len(high): 
            break
        total_spent += budget

    returns_high = (shares_high * high[-1]) - total_spent
    percent_gain_high = returns_high/ total_spent * 100

    returns_low = (shares_low * low[-1]) - total_spent
    percent_gain_low = returns_low/ total_spent * 100

    returns_avg = (shares_avg * ((high[-1] + low[-1])/2) ) - total_spent
    percent_gain_avg = returns_avg/ total_spent * 100


    print("Money spent: ", total_spent )
    print("LOW")

    print("returns: ", returns_high, "percent gain: ", percent_gain_high)

    print("AVG")

    print("returns: ", returns_low, "percent gain: ", percent_gain_low)

    print("HIGH")

    print("returns: ", returns_avg, "percent gain: ", percent_gain_avg)

def tesla_experiment():
    print("Test #1: MON, 5 day repeat, budget $100")
    run_calc(3,100,5)
    print("Test #1: TUE, 5 day repeat, budget $100")
    run_calc(4,100,5)
    print("Test #1: WED, 5 day repeat, budget $100")
    run_calc(0,100,5)
    print("Test #1: THU, 5 day repeat, budget $100")
    run_calc(1,100,5)
    print("Test #1: FRI, 5 day repeat, budget $100")
    run_calc(2,100,5)



    print("Test #2: (Random Day Buying every 3 days of the market) WED, 3 day repeat , budget $100")
    run_calc(0,100,3)

    print("Test #3: Entering market after established leadership. JULY 7 2017 MODEL 3 ")
    # 1769 -1
    run_calc(1768,100,5)

    print("Test #4: Buying Every day ")
    # 1769 -1
    run_calc(0,100,1)

    # FEB 3 2020. Up almost 19% in one day  2415 (once)
    print("Test #5: Buying During the Hype once every week on Monday. Will we ever recover? ")
    run_calc(2415, 100, 5)

    # Nov 5 2021. Stock peak price. Will we recover?
    print("Test #6: Nov 4 2021. Stock peak price. Will we recover? ")
    run_calc(2859, 100, 5)

def enbridge_experiment():
    eng_stock = "enbridge_stock_price.xlsx"
    eng_div = "enbridge_dividents.xlsx"

    stock_data = pd.read_excel(eng_stock)
    div_data = pd.read_excel(eng_div)

    budget = 10 
    frequency = 5 # once every 5 days

    dates_eng_div = div_data["Date"].tolist()
    return_div = div_data["Dividends"].tolist()

    price_low_stock = stock_data["Low"].tolist()
    price_high_stock = stock_data["High"].tolist()
    dates_eng_stock = stock_data["Date"].tolist()

    
    dates, returns = dates_eng_div.pop(0), return_div.pop(0)
    div_stack = [dates, returns]
    total_stocks = 0
    i = 0
    day = 5
    budget = 100
    bonus = 0
    total_spent = 0


    while(True):
        current_date = dates_eng_stock[i]
        if div_stack[0] <= current_date:
            # we need to append to the next divident and increase funds for the next round
            bonus = total_stocks * div_stack[1]
            if dates_eng_div:
                dates, returns = dates_eng_div.pop(0), return_div.pop(0)
                div_stack = [dates, returns]
        
           
        price =  (price_high_stock[i] + price_low_stock[i]) / 2
        if not (pd.isna(price)):
            new_stocks = (budget + bonus) / price
            total_stocks += new_stocks
            bonus = 0
                        
            # if i >= 510:
            #     print(True)
            total_spent += budget
        i += day
        if i > len(dates_eng_stock) - 1:
            break

    returns_high = (total_stocks * ((price_high_stock[-1] + price_low_stock[-1]) / 2)) - total_spent
    percent_gain_high = returns_high/ total_spent * 100

    print("Money spent: ", total_spent )
    print("returns: ", returns_high, "percent gain: ", percent_gain_high)

  
        
    # day = 0 

    # if dates_eng_div[0] < dates_eng_div[1]:
    #     print("True")
    #     if(dates_eng_div[0] < dates_eng_div[10]):
    #         print("True")


enbridge_experiment()