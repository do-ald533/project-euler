function sum_of_squares(n) {
    sumOfSquares = 0;
    for (let i = 0; i <= n; i++) {
        sumOfSquares += i ** 2;
    }
    return sumOfSquares;
}


function square_of_sum(n) {
    squareOfSum = 0;
    for (let i = 0; i <= n; i++) {
        squareOfSum += i
    }
    return squareOfSum ** 2;
}


num = 100
console.log(square_of_sum(num) - sum_of_squares(num));