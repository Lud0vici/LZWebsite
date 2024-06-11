// Add click event listener to all radio buttons
const radioButtons = document.querySelectorAll('.input');
radioButtons.forEach(button => {
    button.addEventListener('click', function() {
        const target = this.getAttribute('data-target');
        window.location.href = target; // Redirect to the specified target URL
    });
});