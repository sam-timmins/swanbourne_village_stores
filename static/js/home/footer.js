window.onload = function () {

    // Removes the social media links in the footer if they are
    // also present on the page

    const icons = document.querySelectorAll("i");
    let socialIcons = [];

    for (let icon of icons) {
        if (icon.classList.contains('fa-facebook-square') || icon.classList.contains('fa-twitter-square') || icon.classList.contains('fa-instagram')) {
                
                socialIcons.push(icon);
        }
    }

    if (socialIcons.length == 6) {
        let sliceDuplicates = socialIcons.slice(3,6);
        
        for (let duplicate of sliceDuplicates) {
            duplicate.parentNode.style.display = "none";
        }
    }
    
};