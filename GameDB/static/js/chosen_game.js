const add_review_btn = document.getElementById('add-review-btn')
const alert_div_located = document.getElementById('alert-div-located')

add_review_btn.addEventListener('click', (e)=>{
    axios.get('/check_login/')
        .then(function(response) {
            console.log(response);
            if (!response.data.logged_in) {
                let alert_div = document.createElement('div');
                alert_div.className = "alert alert-warning alert-dismissible fade show"
                alert_div.innerHTML = `   
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                    <strong>Not logged in! </strong>Please log in first before posting your review.        
                `;
                alert_div_located.appendChild(alert_div);
            } else {
                alert('already log in')
                // do sth
            }
        })
        .catch(function(error) {
            console.error('Error:', error);
        });
});