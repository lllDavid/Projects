// Mock random values for home crypto market data table

function getRandomPriceChange(currentPrice) {
    let priceChange = (Math.random() > 0.5 ? 1 : -1) * Math.floor(Math.random() * 1000);
    return Math.max(10, Math.min(1000000, currentPrice + priceChange));
}

function getRandomPercentage(previousValue) {
    return (previousValue + (Math.random() * 5 - 2.5)).toFixed(2);
}

function updateCell(cell, value) {
    cell.textContent = value;
    if (value.includes('%')) {
        const change = parseFloat(value);
        cell.classList.toggle('text-success', change > 0);
        cell.classList.toggle('text-danger', change <= 0);
    }
}

function updateTable() {
    document.querySelectorAll('#coinTable tbody tr').forEach(row => {
        let previousValues = [...row.querySelectorAll('td')].slice(3, 6).map(cell => parseFloat(cell.textContent.replace(/[^0-9.-]+/g, "")));
        row.querySelectorAll('td').forEach((cell, i) => {
            if (i === 2) {
                updateCell(cell, `$${getRandomPriceChange(parseFloat(cell.textContent.replace(/[^0-9.-]+/g, ""))).toFixed(2)}`);
            } else if (i >= 3 && i <= 5) {
                updateCell(cell, `${getRandomPercentage(previousValues[i - 3])}%`);
            }
        });
    });
}

setInterval(updateTable, 1500);
