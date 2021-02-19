function calculateTotalScore(scores) {
	console.log(scores);
	let total = 0; 
	for (let score of scores) {
		total += score;
	}
	return total;
}
let res = calculateTotalScore([1,2,3,4]);
console.log(res);