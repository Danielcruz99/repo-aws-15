// Add an event listener to validate the form on submit
document.querySelector('form').addEventListener('submit', function(event) {
    const amount = document.querySelector('input[name="amount"]').value;

    // Check if the amount is greater than 0
    if (amount <= 0) {
        alert("El monto debe ser mayor a 0.");
        event.preventDefault();  // Prevent form submission
    }

    const date = document.querySelector('input[name="purchase_date"]').value;

    // Check if the date is filled
    if (!date) {
        alert("Por favor, seleccione una fecha válida.");
        event.preventDefault();  // Prevent form submission
    }
});
