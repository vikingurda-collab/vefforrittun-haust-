function calculatetotal(price, count, smt) {
    return price * count + smt;
}

const total = calculatetotal(1800, 4, 20);
console.log("heildarverð: " + total + " kr");