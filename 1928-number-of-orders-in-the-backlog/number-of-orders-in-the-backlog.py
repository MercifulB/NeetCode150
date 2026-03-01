
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:

        MOD = 10**9 + 7
        
        # buy: max-heap by price (store as negative price)
        buy = [] # elements: (-price, amount)
        # sell: min-heap by price
        sell = [] # elements: (price, amount)

        for price, amount, orderType in orders:
            if orderType == 0: # buy
                while amount > 0 and sell and sell[0][0] <= price:
                    sp, sa = heappop(sell)
                    matched = min(amount, sa)
                    amount -= matched
                    sa -= matched
                    if sa > 0:
                        heappush(sell, (sp, sa))
                if amount > 0:
                    heappush(buy, (-price, amount))
            else:  # sell
                # Match with most expensive buys while buy price >= sell price
                while amount > 0 and buy and -buy[0][0] >= price:
                    bp, ba = heappop(buy)
                    bp = -bp
                    matched = min(amount, ba)
                    amount -= matched
                    ba -= matched
                    if ba > 0:
                        heappush(buy, (-bp, ba))
                if amount > 0:
                    heappush(sell, (price, amount))
        
        total = 0
        for _, amt in buy:
            total = (total + amt) % MOD
        for _, amt in sell:
            total = (total + amt) % MOD
        return total

        