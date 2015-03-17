/**
 * Created by Matt on 3/9/2015.
 */


coins = {
    1 : 6,
    5 : 4,
    10: 2,
    25: 1
};

function total(coins) {
    var total = 0;
    for (var key in coins) {
        var qty = coins[key];
        total += qty * key;
    }
    return total;
}

console.log(total(coins));