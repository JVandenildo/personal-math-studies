function factorial(number) {
	let i = 1;
	let result = 1;

	while (number >= i) {
		result = result * i;
		i += 1;
	}

	return result;
}

var number = 5; // just for testing, 5! is 120

console.log(`${number}! is ${factorial(number)}.`);
