class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // keep track of lowest price and max profit
        int lowest_price = prices[0];
        int max_profit = 0;
        for (int i = 1; i < prices.size(); i++) {
            if (prices[i] < lowest_price) {
                lowest_price = prices[i];
            } else if (prices[i] - lowest_price > max_profit) {
                max_profit = prices[i] - lowest_price;
            }
        }
        return max_profit;
    }
};
