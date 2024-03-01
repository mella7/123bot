document.addEventListener('DOMContentLoaded', function() {
    const saveButton = document.getElementById('saveButton');
    const webhookUrlInput = document.getElementById('webhookUrl');
    const statusMessage = document.getElementById('statusMessage');

    saveButton.addEventListener('click', function() {
        const webhookUrl = webhookUrlInput.value.trim();
        if (webhookUrl === '') {
            statusMessage.textContent = 'Please enter a webhook URL.';
            return;
        }

        // Perform AJAX request to save the webhook URL (You'll need to implement this)
        // For demonstration purposes, we're just showing a success message
        statusMessage.textContent = 'Webhook URL saved successfully!';
    });
});
