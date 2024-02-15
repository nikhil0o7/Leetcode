/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let min_prices = prices[0];
    let max_profit = 0;
    for(let i in prices){
        let temp = prices[i];
        if(max_profit < temp - min_prices){
            max_profit = temp - min_prices;
        }else if(temp < min_prices){
            min_prices = temp;
        }
    }
    
    return max_profit;
    
};

// var maxProfit = function(prices) {
//     let min_price = prices[0]
//     let max_profit = 0
//     for(let i=0; i<prices.length;i++){
//         let temp_price = prices[i];
//         if (max_profit < temp_price- min_price){
//             max_profit = temp_price - min_price;
//         } else if (temp_price < min_price){
//             min_price = temp_price
//         }
//     }
    
//     return max_profit;
    
// };