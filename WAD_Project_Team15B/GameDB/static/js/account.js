document.getElementById('update-profile-button').addEventListener('click', function() {
    document.getElementById('update-profile-form').style.display = 'block';
    document.getElementById('change-password-form').style.display = 'none';
});

document.getElementById('change-password-button').addEventListener('click', function() {
    document.getElementById('change-password-form').style.display = 'block';
    document.getElementById('update-profile-form').style.display = 'none';
});

document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the form from submitting normally

    var username = document.getElementById('id_username').value;
    var email = document.getElementById('id_email').value;
    var password = document.getElementById('id_password').value;

    // Get CSRF token
    var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    axios.post('/register/', {
        username: username,
        email: email,
        password: password
    }, {
        // Include the CSRF token in the headers
        headers: {
            'X-CSRFToken': csrftoken
        }
    })
    .then(function(response) {
        alert('Account created successfully.');
        window.location.href = '/login/';  // Redirect to the login page
    })
    .catch(function(error) {
        alert('An error occurred while creating the account.');
    });
});
