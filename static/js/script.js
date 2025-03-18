document.addEventListener("DOMContentLoaded", function () {
    alert("Welcome to our Interactive Multimedia Webpage!");
});
document.addEventListener("DOMContentLoaded", function () {
    const images = document.querySelectorAll(".media img");
    
    images.forEach((img, index) => {
        setTimeout(() => {
            img.style.opacity = "1";
            img.style.transform = "scale(1)";
        }, index * 500); // Delay each image animation
    });

    // Scroll event to animate text
    window.addEventListener("scroll", function () {
        let text = document.querySelector(".text-content p");
        let position = text.getBoundingClientRect().top;
        let screenHeight = window.innerHeight;

        if (position < screenHeight - 100) {
            text.style.opacity = "1";
            text.style.transform = "translateY(0)";
        }
    });
});
