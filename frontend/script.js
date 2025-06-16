document.addEventListener("DOMContentLoaded", function () {
    const movies = [
        { title: "joker", image: "stranger-things.jpg" },
        { title: "intestellar", image: "witcher.jpg" },
        { title: "batman", image: "money-heist.jpg" },
        { title: "inception", image: "inception.jpg" },
        { title: "avengers", image: "../images/avengers.jpg" }
    ];

    const movieGrid = document.getElementById("movies-list");

    movies.forEach(movie => {
        const movieItem = document.createElement("div");
        movieItem.classList.add("movie-item");

        const img = document.createElement("img");
        img.src = movie.image;
        img.alt = movie.title;

        movieItem.appendChild(img);
        movieGrid.appendChild(movieItem);
    });
});
