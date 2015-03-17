/**
 * Created by Matt on 3/10/2015.
 */

coins = [
    {'Name' : 'Pennies',
     'Value' : 1,
     'Qty' : 6 },
    {'Name' : 'Nickels',
     'Value': 5,
     'Qty' : 4 },
    {'Name' : 'Dimes',
     'Value': 10,
     'Qty' : 2 },
    {'Name' : 'Quarters',
     'Value': 25,
     'Qty' : 1 }
];

function getDollars(coins) {
    var total = 0;
    for(var key in coins) {
        var value = coins[key].Value;
        var qty = coins[key].Qty;
        total += value * qty;
    }
    total = total / 100;
    return "$" + total;
}

console.log(getDollars(coins));