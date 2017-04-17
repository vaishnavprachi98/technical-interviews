def  findPotentialInsiderTraders(datafeed):
    # datafeed = array of strings, without leading number of lines?
    days = {}
    trades = {}  # mapping for int (day) to list of trades (trader, type, $)
    for line in datafeed:
        data = line.split('|')
        if len(data) == 2:  # reached a day.
            day, price = [int(x) for x in data]
            days[day] = price
        else:          # processing trader information.
            day = int(data[0])
            trader = data[1]
            trade_type = data[2]
            amount = int(data[3])
            tup = (trader, trade_type, amount)
            if day in trades:
                trades[day].append(tup)
            else:
                trades[day] = [tup]
    # do checks whenever stock price changes in a 3 day window.
    suspicious_traders = {}
    days_prices = list(days.items())
    days_prices.sort(key=lambda t:t[0]) # sort by day.
    first_day = days_prices[0][0]
    current_price = days_prices[0][1]
    for i in range(1, len(days_prices)):  # skip first entry.
        price_change_day = days_prices[i][0]
        new_price = days_prices[i][1]
        # loop backwards and check
        loop_until = price_change_day - 3 if price_change_day - 3 >= 0 else 0
        # no negative days.
        price_difference = new_price - current_price
        # loop through all days to check.
        for day in range(price_change_day, loop_until-1, -1):
            if day in trades:
                trades_on_that_day = trades[day]
                for a_trade in trades_on_that_day:
                    amount = a_trade[2]
                    trade_type = a_trade[1]
                    trader = a_trade[0]
                    s = str(day) + '|' + trader
                    if s in suspicious_traders:
                        continue
                    # check trade_type.
                    if trade_type == "BUY":
                        if amount * price_difference >= 500000:
                            # is sus.
                            suspicious_traders[s] = (day, trader)
                    else: # trade_tye == "SELL"
                        if amount * price_difference * -1 >= 500000:
                            # is sus.
                            suspicious_traders[s] = (day, trader)
            # else no trades, pass.
        current_price = new_price
    ans = list(suspicious_traders.values())
    ans.sort(key=lambda t: (t[0], t[1]))  # sort by day then name
    to_string_ans = []
    for a in ans:
        s = str(a[0]) + '|' + a[1]
        to_string_ans.append(s)
    print(to_string_ans)
    return to_string_ans



d = ['0|20',
'0|Kristi|SELL|300',
'0|Will|BUY|500',
'0|Tom|BUY|5000',
'0|Shilpa|BUY|150',
'1|Tom|BUY|150000',
'3|25',
'5|Shilpa|SELL|150',
'8|Kristi|SELL|60000',
'9|Shilpa|BUY|50',
'10|15',
'11|5',
'14|Will|BUY|10000',
'15|Will|BUY|10000',
'16|Will|BUY|10000',
'17|25']



feed1 = """0|1000
0|Shilpa|BUY|30000
0|Will|BUY|50000
0|Tom|BUY|40000
0|Kristi|BUY|15000
1|Kristi|BUY|11000
1|Tom|BUY|1000
1|Will|BUY|19000
1|Shilpa|BUY|25000
2|1500
2|Will|SELL|7000
2|Shilpa|SELL|8000
2|Kristi|SELL|6000
2|Tom|SELL|9000
3|500
38|1000
78|Shilpa|BUY|30000
79|Kristi|BUY|60000
80|1100
81|1200"""

datafeed1 = feed1.split("\n")

feed2 = """0|20
0|Kristi|SELL|3000
0|Will|BUY|5000
0|Tom|BUY|50000
0|Shilpa|BUY|1500
1|Tom|BUY|1500000
3|25
5|Shilpa|SELL|1500
8|Kristi|SELL|600000
9|Shilpa|BUY|500
10|15
11|5
14|Will|BUY|100000
15|Will|BUY|100000
16|Will|BUY|100000
17|25"""

datafeed2 = feed2.split("\n")

def findFraudolentTraders(datafeed):
    flagged_trades = set()
    trades = dict()
    current_price = None
    for feed in datafeed:
        vals = feed.split("|")
        day = int(vals[0])
        if len(vals) == 2:
            current_price = int(vals[1])
            for x in range(day - 3, day):
                if x in trades:
                    for (trader_name, isBuy, price, amount) in trades[x]:
                        if (x, trader_name) in flagged_trades:
                            continue
                        if isBuy:
                            fraudolent = (current_price - price) * amount >= 500000
                        else:
                            fraudolent = (price - current_price) * amount >= 500000
                        if fraudolent:
                            flagged_trades.add((x, trader_name))
        else:
            trader_name = vals[1]
            isBuy = len(vals[2]) == 3
            amount = int(vals[3])
            if day not in trades:
                trades[day] = []
            trades[day].append((trader_name, isBuy, current_price, amount))
    flagged_trades = sorted(list(flagged_trades))
    return list(map(lambda x: str(x[0]) + "|" + str(x[1]), flagged_trades))

a = findFraudolentTraders(datafeed1)

print('mine')
b = findPotentialInsiderTraders(datafeed1)

print(a==b)