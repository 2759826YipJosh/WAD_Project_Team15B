document.getElementById('update-profile-button').addEventListener('click', function() {
    document.getElementById('update-profile-form').style.display = 'block';
    document.getElementById('change-password-form').style.display = 'none';
});

document.getElementById('change-password-button').addEventListener('click', function() {
    document.getElementById('change-password-form').style.display = 'block';
    document.getElementById('update-profile-form').style.display = 'none';
});
