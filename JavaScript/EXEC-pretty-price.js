const prettyPrice = (price, extension) => {
    const priceGross = Math.floor(price);
    if (extension % 1 === 0 && extension <= 100) {
        extension = extension / 100;
        extension = parseFloat(extension.toFixed(2));
        
    } else if (extension % 1 != 0){
        return (priceGross + extension).toFixed(2);
    }
    else {
        return (`Extension is ${extension} and must be between 1 and 99`);
    }
    return (priceGross + extension).toFixed(2);
};

console.log(prettyPrice(100.31, 0.99)); // Output: 100.32
console.log(prettyPrice(96.32, 99)); // Output: 96.99
console.log(prettyPrice(5.32, 102)); // Output: 5.99

