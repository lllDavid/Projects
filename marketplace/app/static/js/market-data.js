function getRandomPriceChange(currentPrice) {
    if (isNaN(currentPrice)) {
        return 10;
    }

    let priceChange = (Math.random() > 0.5 ? 1 : -1) * Math.floor(Math.random() * 1000);
    let newPrice = currentPrice + priceChange;

    return clampPrice(newPrice);
}

function clampPrice(price) {
    return Math.max(10, Math.min(1000000, price));
}

function getRandomPercentage(previousValue) {
    let randomChange = (Math.random() * 5 - 2.5);
    let newPercentage = previousValue + randomChange;
    return newPercentage.toFixed(2);
}

function updatePriceCell(priceCell) {
    const currentPrice = parseFloat(priceCell.textContent.replace(/[^0-9.-]+/g, ""));

    if (isNaN(currentPrice)) {
        priceCell.textContent = "$10.00";
        return;
    }

    const newPrice = getRandomPriceChange(currentPrice);
    priceCell.textContent = `$${newPrice.toFixed(2)}`;
}

function updatePercentageCell(percentageCell, previousValue, currentValue) {
    const change = ((currentValue - previousValue) / previousValue) * 100;
    percentageCell.textContent = `${change.toFixed(2)}%`;

    if (change > 0) {
        percentageCell.classList.remove('text-danger');
        percentageCell.classList.add('text-success');
    } else {
        percentageCell.classList.remove('text-success');
        percentageCell.classList.add('text-danger');
    }
}

function updatePercentageColumns(row, previousValues) {
    for (let i = 3; i <= 5; i++) {
        const percentageCell = row.querySelectorAll('td')[i];
        const currentValue = parseFloat(percentageCell.textContent.replace(/[^0-9.-]+/g, ""));
        const previousValue = previousValues[i];

        updatePercentageCell(percentageCell, previousValue, currentValue);
    }
}

function updateTable() {
    const rows = document.querySelectorAll('#coinTable tbody tr');
    rows.forEach(row => {
        const cells = row.querySelectorAll('td');
        let previousValues = {};

        cells.forEach((cell, index) => {
            if (index >= 3 && index <= 5) {
                previousValues[index] = parseFloat(cell.textContent.replace(/[^0-9.-]+/g, ""));
            }
            if (index > 1 && index < 6) {
                cell.textContent = `${getRandomPercentage(previousValues[index])}%`;
            }
        });

        const priceCell = row.querySelectorAll('td')[2];
        updatePriceCell(priceCell);

        updatePercentageColumns(row, previousValues);
    });
}

setInterval(updateTable, 1500);
