function redirectToPage1() {
    // Array of URLs for the two HTML pages
    var pages = [
        "weather positive.html",
        "weather negative.html"
    ];

    // Generate a random index to choose between the two pages
    var randomIndex = 0;

    // Get the randomly chosen page URL
    var randomPage = pages[randomIndex];

    // Redirect the user to the randomly chosen page
    window.location.href = randomPage;
}

function redirectToPage2() {
    // Array of URLs for the two HTML pages
    var pages = [
        "weather positive.html",
        "weather negative.html"
    ];

    // Generate a random index to choose between the two pages
    var randomIndex = 1;

    // Get the randomly chosen page URL
    var randomPage = pages[randomIndex];

    // Redirect the user to the randomly chosen page
    window.location.href = randomPage;
}