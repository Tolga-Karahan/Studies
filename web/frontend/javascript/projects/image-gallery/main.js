const displayedImage = document.querySelector('.displayed-img');
const thumbBar = document.querySelector('.thumb-bar');

const btn = document.querySelector('button');
const overlay = document.querySelector('.overlay');

const imageArray = ["pic1.jpg", "pic2.jpg", "pic3.jpg", "pic4.jpg", "pic5.jpg"];

const altTexts = ["pic1.jpg", "pic2.jpg", "pic3.jpg", "pic4.jpg", "pic5.jpg"];

for (let i=0; i < imageArray.length; i++) {
    const newImg = document.createElement("img");
    newImg.src = "images/" + imageArray[i];
    newImg.alt = altTexts[i];
    thumbBar.appendChild(newImg);

    newImg.addEventListener("click", (event) => {
        displayedImage.src = event.target.src;
        displayedImage.alt = event.target.alt;
    });
}

btn.addEventListener("click", (event) => {
    const classValue = event.target.getAttribute("class");

    if (classValue === "dark") {
        event.target.setAttribute("class", "light");
        overlay.style.backgroundColor = "rgba(0, 0, 0, 0.5)";
    } else {
        event.target.setAttribute("class", "dark");
        overlay.style.backgroundColor = "rgba(0, 0, 0, 0)";
    }
});

