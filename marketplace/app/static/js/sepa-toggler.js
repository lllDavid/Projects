
// Wait for the DOM to fully load before attaching event listener
document.addEventListener('DOMContentLoaded', function () {
    const regionSelect = document.getElementById('region');
    const sepaBankDetails = document.getElementById('sepa-bank-details');

    // Ensure the toggle works when the region changes
    regionSelect.addEventListener('change', function () {
        if (regionSelect.value === 'eu') {
            // Show SEPA details if 'EU' is selected
            sepaBankDetails.style.display = 'block';
        } else {
            // Hide SEPA details for other regions
            sepaBankDetails.style.display = 'none';
        }
    });
});
