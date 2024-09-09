document.addEventListener('DOMContentLoaded', function () {
    const passwordInput = document.getElementById('password');
    const toggleButton = document.getElementById('toggle-password');
    const eyeIcon = document.getElementById('eye-icon');

    toggleButton.addEventListener('click', function () {
        if (passwordInput.type === 'password') {
            passwordInput.type = 'text';
            eyeIcon.textContent = '🙈'; // Change icon to indicate the password is visible
        } else {
            passwordInput.type = 'password';
            eyeIcon.textContent = '👁️'; // Change icon to indicate the password is hidden
        }
    });
});
