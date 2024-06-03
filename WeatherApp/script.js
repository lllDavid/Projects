function getWeather() {
    const stadt = document.getElementById("stadtname").value;
    const apiKey = "0e4194c846936b540bce21b6b2a47fb9";
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${stadt}&appid=${apiKey}&units=metric&lang=de`;

    fetch(url)
        .then(response => {
            if (response.ok) {                        // Fehlerüberprüfung API Aufruf
                console.log("API abgerufen")
                return response.json();
            } else {
                console.log("API konnte nicht abgerufen werden")
                throw new Error(`API request failed with status: ${response.status}`);
            }
        })
        .then(data => {
            const main = data.weather[0].main;
            const { temp, feels_like } = data.main;
            const beschreibung = data.weather[0].description;
            const stadtName = data.name;
            const land = data.sys.country;


            switch (main) {
                case "Snow":
                    document.getElementById("body").style.backgroundImage =
                        "url('https://media0.giphy.com/media/dAyD6PWoQRs40/giphy.gif?cid=ecf05e475ul323fts08b7jp701kex4spm485lyff99y96eoq&ep=v1_gifs_related&rid=giphy.gif&ct=g')";
                    break;
                case "Clouds":
                    document.getElementById("body").style.backgroundImage =
                        "url('https://media4.giphy.com/media/Cn46Wi1Fvh11S/giphy.gif?cid=ecf05e47oqa61bzz0ptx0g4fgnowttmij7o648emusmlzgd0&ep=v1_gifs_search&rid=giphy.gif&ct=g')";
                    break;
                case "Fog":
                    document.getElementById("body").style.backgroundImage =
                        "url('https://mdbgo.io/ascensus/mdb-advanced/img/fog.gif')";
                    break;
                case "Rain":
                    document.getElementById("body").style.backgroundImage =
                        "url('https://mdbgo.io/ascensus/mdb-advanced/img/rain.gif')";
                    break;
                case "Clear":
                    document.getElementById("body").style.backgroundImage =
                        "url('https://media2.giphy.com/media/26FmRqkLwliASGq8o/giphy.gif?cid=ecf05e47l9969i5tg4zull6nxwfipirn94s1b1h6xdx0cx4a&ep=v1_gifs_related&rid=giphy.gif&ct=g')";
                    break;
                case "Thunderstorm":
                    document.getElementById("body").style.backgroundImage =
                        "url('https://mdbgo.io/ascensus/mdb-advanced/img/thunderstorm.gif')";
                    break;

            }

            const wetterAnzeigen = `Das aktuelle Wetter in: ${stadtName}, ${land}: ${beschreibung}, ${temp}°C (gefühlte ${feels_like}°C)`;

            document.getElementById("ausgabe").textContent = '';

            const wetterElement = document.createElement("p");
            wetterElement.textContent = wetterAnzeigen;

            document.getElementById("ausgabe").appendChild(wetterElement);
            document.getElementById("ausgabe").style.display = "block";
            document.getElementById("ausgabe2").style.display = "none";

        })

        .catch(error => {
            if (document.getElementById('stadtname').value == "") {       // Fehlerüberprüfung Stadteingabe
                console.log(error);
                window.alert("Bitte geben sie einen Ort ein!");
            }
            else {
                window.alert("Bitte geben sie einen gültigen Ort ein!");
                document.getElementById('stadtname').value = "";
            }
        });

}
function getWeather5days() {
    const stadt = document.getElementById("stadtname").value;
    const apiKey = "0e4194c846936b540bce21b6b2a47fb9";
    const url = `https://api.openweathermap.org/data/2.5/forecast?q=${stadt}&appid=${apiKey}&units=metric&lang=de`;

    fetch(url)
        .then(response => {
            if (response.ok) {
                console.log("API abgerufen")
                return response.json();
            } else {
                console.log("API konnte nicht abgerufen werden")
                throw new Error(`API request failed with status: ${response.status}`);
            }
        })
        .then(data => {
            const forecasts = {};
            const currentDate = new Date();


            data.list.forEach(item => {                                  // Code Block mit ChatGPT erstellt
                const itemDate = new Date(item.dt * 1000);
                const date = itemDate.toDateString();

                if (itemDate >= currentDate && !forecasts[date]) {
                    forecasts[date] = item;
                }

            });

            document.getElementById("ausgabe2").textContent = '';

            for (const date in forecasts) {

                const item = forecasts[date];
                const { temp } = item.main;
                const beschreibung = item.weather[0].description;                       // Code Block mit ChatGPT erstellt
                const wetterAnzeigen = `${date}: ${beschreibung}, ${temp}°C `;

                const wetterElement = document.createElement("p");
                wetterElement.textContent = wetterAnzeigen;
                document.getElementById("ausgabe2").appendChild(wetterElement);

                document.getElementById("ausgabe").style.display = "none";
                document.getElementById("ausgabe2").style.display = "block";
            }

        })
        .catch(error => {
            if (document.getElementById('stadtname').value == "") {
                console.log(error);
                window.alert("Bitte geben sie einen Ort ein!");
            }
            else {
                window.alert("Bitte geben sie einen gültigen Ort ein!");
                document.getElementById('stadtname').value = "";
            }
        });
};


function resetBackground() {
    document.getElementById("body").style.backgroundImage = "url('https://images.pexels.com/photos/1525041/pexels-photo-1525041.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')";
}

