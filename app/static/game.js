document.addEventListener('DOMContentLoaded', () => {
	const board = document.getElementById('board');
	const size = 11;

	for (let row = 0; row < size; row++) {
		const rowDiv = document.createElement('div');
		if (row === 0) {
			rowDiv.classList.add('hex-row-first');
		} else {
			rowDiv.classList.add('hex-row');
		}
		// else if (row === 2) {
		// 	rowDiv.classList.add('hex-rowff');
		// }

		rowDiv.style.setProperty('--row', row);

		for (let col = 0; col < size; col++) {
			const hex = document.createElement('div');
			hex.classList.add('hex');
			rowDiv.appendChild(hex);
		}

		board.appendChild(rowDiv);
	}
});
