// Generate a random value for updating the price
function getRandomPriceChange(currentPrice) {
    // If the price is not a valid number, return a default value of 10
    if (isNaN(currentPrice)) {
        return 10;
    }

    // Random price change within the range of -100,000 to +100,000
    let priceChange = (Math.random() > 0.5 ? 1 : -1) * Math.floor(Math.random() * 1000);
    let newPrice = currentPrice + priceChange;

    // Ensure the price stays between 10 and 1,000,000
    return clampPrice(newPrice);
}

// Clamp price to stay between 10 and 1,000,000
function clampPrice(price) {
    return Math.max(10, Math.min(1000000, price));
}

// Generate a random percentage for 1h, 24h, or 7d
function getRandomPercentage(previousValue) {
    // Generate a realistic percentage change based on the previous value
    let randomChange = (Math.random() * 5 - 2.5); // Random value between -2.5% and +2.5%
    let newPercentage = previousValue + randomChange; // Add the random change to the previous value
    return newPercentage.toFixed(2); // Return the updated percentage
}

// Update the price cell in the table
function updatePriceCell(priceCell) {
    // Get the current price from the price cell
    const currentPrice = parseFloat(priceCell.textContent.replace(/[^0-9.-]+/g, ""));

    // If the current price is NaN, set it to a default value
    if (isNaN(currentPrice)) {
        priceCell.textContent = "$10.00"; // Default price if NaN
        return;
    }

    // Get new price with random fluctuation
    const newPrice = getRandomPriceChange(currentPrice);
    priceCell.textContent = `$${newPrice.toFixed(2)}`;
}

// Update percentage cell based on previous and current values
function updatePercentageCell(percentageCell, previousValue, currentValue) {
    const change = ((currentValue - previousValue) / previousValue) * 100; // Calculate the percentage change
    percentageCell.textContent = `${change.toFixed(2)}%`; // Update the percentage text

    // Apply green for positive change, red for negative change
    if (change > 0) {
        percentageCell.classList.remove('text-danger');
        percentageCell.classList.add('text-success');
    } else {
        percentageCell.classList.remove('text-success');
        percentageCell.classList.add('text-danger');
    }
}

// Update percentage columns (1h, 24h, 7d) based on previous values
function updatePercentageColumns(row, previousValues) {
    for (let i = 3; i <= 5; i++) {
        const percentageCell = row.querySelectorAll('td')[i];
        const currentValue = parseFloat(percentageCell.textContent.replace(/[^0-9.-]+/g, ""));
        const previousValue = previousValues[i];

        updatePercentageCell(percentageCell, previousValue, currentValue);
    }
}

// Update all table rows with new data
function updateTable() {
    const rows = document.querySelectorAll('#coinTable tbody tr');
    rows.forEach(row => {
        const cells = row.querySelectorAll('td');
        let previousValues = {}; // Object to store previous percentage values

        // Store previous percentage values for comparison
        cells.forEach((cell, index) => {
            if (index >= 3 && index <= 5) {
                previousValues[index] = parseFloat(cell.textContent.replace(/[^0-9.-]+/g, ""));
            }
            // Randomly generate new percentage values for 1h, 24h, and 7d columns
            if (index > 1 && index < 6) {
                // Generate a new percentage based on previous value
                cell.textContent = `${getRandomPercentage(previousValues[index])}%`;
            }
        });

        // Update the price column
        const priceCell = row.querySelectorAll('td')[2];
        updatePriceCell(priceCell);

        // Update percentage columns based on previous values
        updatePercentageColumns(row, previousValues);
    });
}

// Update the table every 1.5 seconds
setInterval(updateTable, 1500);


