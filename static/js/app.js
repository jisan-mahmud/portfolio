let x = 0;
function menu_ber(event){
    let menu_items = document.getElementById('menu_items');
    let menu_icon = document.querySelector('.menu_icon')
    console.log(menu_icon)
    if(x == 0){
        menu_items.classList.remove('hidden')
        menu_icon.classList.remove('fa-bars')
        menu_icon.classList.add('fa-xmark')
        x = 1
    }else{
        menu_items.classList.add('hidden')
        menu_icon.classList.add('fa-bars')
        menu_icon.classList.remove('fa-xmark')
        x = 0
    }
}

let github_profile_load = () => {
    fetch('https://api.github.com/users/jisan-mahmud')
    .then(res => {
        return res.json();
    })
    .then(json => {
        github_profile_display(json)
    })
    
}

let github_profile_display = (json) =>{
    
}

github_profile_load()