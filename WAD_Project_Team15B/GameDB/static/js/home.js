const search_inupt = document.getElementById('search_input');
const search_button = document.getElementById('search_button');

search_button.addEventListener('click', () => {
    const search_query = search_inupt.value;
    window.location.href = `/search/?kw=${search_query}`;
});


document.addEventListener('keypress', (e)=>{
    const search_query = search_inupt.value;
    // console.log(search_query);
    if (search_query!='' && e.key=='Enter') {
        e.preventDefault();
        window.location.href = `/search/?kw=${search_query}`;
    }
});

const pc1 = document.getElementById('pc1');
pc1.addEventListener('click', ()=>{
    console.log(123);
});

