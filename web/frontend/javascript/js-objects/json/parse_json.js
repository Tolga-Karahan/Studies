async function populate() {
    const requestURL = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json";
    const request = new Request(requestURL);

    // To make a network request
    const response = await fetch(request);
    const superHeroes = await response.json();

    populateHeader(superHeroes);
    populateHeroes(superHeroes);
}

function populateHeader(data) {
    const header = document.querySelector("header");
    const h1 = document.createElement("h1");
    h1.textContent = data["squadName"];
    header.appendChild(h1);

    const p1 = document.createElement("p");
    p1.textContent = `Hometown: ${data["homeTown"]} // Formed: ${data["formed"]}`;
    header.appendChild(p1);
}

function populateHeroes(data) {
    const section = document.querySelector("section");
    const heroes = data["members"];

    for (const hero of heroes) {
        const article = document.createElement("article");
        const h2 = document.createElement("h2");
        const p1 = document.createElement("p");
        const p2 = document.createElement("p");
        const p3 = document.createElementNS("p");
        const list = document.createElement("ul");

        h2.textContent = hero["name"];
        p1.textContent = `Secret identity: ${hero["secretIdentity"]}`;
        p2.textContent = `Age: ${hero["age"]}`;
        p3.textContent = "Superpowers:";

        const superPowers = hero["powers"];
        for (const power of superPowers) {
            const listItem = document.createElement("li");
            listItem.textContent = power;
            list.appendChild(listItem);
        }

        article.appendChild(h2);
        article.appendChild(p1);
        article.appendChild(p2);
        article.appendChild(p3);
        article.appendChild(list);

        section.appendChild(article);
    }
}

populate();