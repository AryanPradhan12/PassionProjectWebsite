

// Function to toggle active class on buttons
document.querySelectorAll('.toggle-btn').forEach(button => {
    button.addEventListener('click', function() {
        // Toggle the 'active' class for button color change
        this.classList.toggle('active');
        
        // Set the hidden input value based on which button was clicked
        if (this.name === 'passion') {
            document.getElementById('selected-passion').value = this.value;
        } else if (this.name === 'activity') {
            document.getElementById('selected-activity').value = this.value;
        } else if (this.name === 'hours') {
            document.getElementById('selected-hours').value = this.value;
        }

        // Remove active class from sibling buttons
        let siblings = document.querySelectorAll(`button[name="${this.name}"]`);
        siblings.forEach(sibling => {
            if (sibling !== this) {
                sibling.classList.remove('active');
            }
        });
    });
});
