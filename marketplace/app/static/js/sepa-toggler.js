// sepa-toggler.js
document.addEventListener('DOMContentLoaded', function() {
    const regionSelect = document.getElementById('region');
    const sepaBankDetails = document.getElementById('sepa-bank-details');
    const swiftBankDetails = document.getElementById('swift-bank-details');

    regionSelect.addEventListener('change', function() {
        // Hide both SEPA and SWIFT details by default
        sepaBankDetails.style.display = 'none';
        swiftBankDetails.style.display = 'none';

        // Show SEPA details if 'EU' region is selected
        if (regionSelect.value === 'eu') {
            sepaBankDetails.style.display = 'block';
        } 
        // Show SWIFT details if 'Other Regions' is selected
        else if (regionSelect.value === 'other') {
            swiftBankDetails.style.display = 'block';
        }
    });
});
