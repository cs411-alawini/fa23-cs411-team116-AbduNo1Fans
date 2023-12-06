function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('message').innerText = data.message;
    })
    .catch(error => console.error('Error:', error));
}


function initializeMap(crimeSpots) {
    var map = L.map('map').setView([34.050, -118.250], 13); // Default view

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Adding crime spots to the map
    crimeSpots.forEach(function(spot) {
        L.marker([spot.lat, spot.lon])
            .addTo(map)
            .bindPopup(spot.info); // Popup text can be any detail about the crime
    });
}