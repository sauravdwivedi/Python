"""The price of silver varies day-to-day. You are allowed to buy and 
sell silver only once. Condition is that you can't buy and sell the 
same day. The prices are given for a range of days. You have to write 
an algorithm to find out best days to buy and sell silver such that 
either profit is maximum or loss is minimum.

Input:

prices = [7, 12, 5, 3, 11, 6, 10, 2, 8]
prices = [15, 15]
prices = [15, 13, 5, 10]

days are counted from 0.

Output: 

Buy on day 3, sell on day 4 with profit 8
Buy on day 0, sell on day 1 with profit 0 
Buy on day 2, sell on day 3 with profit 5
"""

class Solution:
    def __init__(self, prices):
        self.day_min_price = 0
        self.prices = prices
        self.days = len(prices)
        self.dic_profit = {}

    def get_buy_day(self):
        self.day_min_price = self.prices.index(min(self.prices))
        for i in range(self.days-1):
            prices_rest = self.prices[i+1:]
            index_sell = prices_rest.index(max(prices_rest))
            self.dic_profit[i] = prices_rest[index_sell] - self.prices[i]
        self.day_min_price = max(self.dic_profit, key=self.dic_profit.get)
        return self.day_min_price

    def get_sell_day(self):
        prices_sell = self.prices[self.day_min_price+1:]
        day_max_price = prices_sell.index(max(prices_sell)) \
            + self.day_min_price + 1
        return day_max_price
        
if __name__ == '__main__':
    prices = input("Enter prices per day as space separated"\
        + f" values (e.g. '7 12 5 3')\n:").strip().split(" ")
    prices = [price for price in prices if price != '']
    prices = list(map(int, prices))
    obj = Solution(prices)
    res_buy = obj.get_buy_day()
    res_sell = obj.get_sell_day()
    print(f"Buy on day {res_buy}, sell on day {res_sell} with"\
        + f" profit {obj.dic_profit[res_buy]}")
