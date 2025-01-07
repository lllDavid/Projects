function populateTable() {
    fetch(walletValuesUrl)
        .then(response => response.json())
        .then(data => {
            const tbody = document.getElementById("coin-data");
            tbody.innerHTML = '';

            if (data.coins && Object.keys(data.coins).length > 0) {
                Object.keys(data.coins).forEach(coin => {
                    const row = document.createElement("tr");

                    row.innerHTML = `
                        <td>${coin}</td>
                        <td>${data.coins[coin]}</td>
                        <td>--</td>
                        <td>--</td>
                    `;
                    tbody.appendChild(row);
                });
            } else {
                tbody.innerHTML = '<tr><td colspan="4">No coins in wallet.</td></tr>';
            }
        })
        .catch(error => {
            console.error("Error fetching wallet data:", error);
            document.getElementById("coin-data").innerHTML = '<tr><td colspan="4">Error loading data</td></tr>';
        });
}

document.addEventListener("DOMContentLoaded", function () {
    populateTable();
});
