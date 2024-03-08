document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the form from submitting normally

    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirm_password').value;

    if (password !== confirmPassword) {
        alert('Passwords do not match.');
        return;
    }

    axios.post('/register/', {
        username: username,
        password: password
    })
    .then(function(response) {
        alert('Account created successfully.');
        window.location.href = '/login/';  // Redirect to the login page
    })
    .catch(function(error) {
        alert('An error occurred while creating the account.');
    });
});
