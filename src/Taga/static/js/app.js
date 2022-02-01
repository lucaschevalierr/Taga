let moyenne_productivity = document.getElementById("productivity").value
let moyenne_mood = document.getElementById("mood").value
let moyenne_sociability = document.getElementById("sociability").value
let moyenne_sleep = document.getElementById("sleep").value

moyenne_productivity = moyenne_productivity.replace(',', '.')
moyenne_mood = moyenne_mood.replace(',', '.')
moyenne_sociability = moyenne_sociability.replace(',', '.')
moyenne_sleep = moyenne_sleep.replace(',', '.')


//////////////////////////////////Graph////////////////////////////////////////
let ctxTemp = document.getElementById('chart').getContext('2d');
let chartTemp = new Chart(ctxTemp, {
    type: 'bar',
    data: {
        labels: ["Moyenne/Catégorie"],
        datasets: [{
            label: 'Productivité',
            data: [moyenne_productivity],
            backgroundColor: [
                'rgb(255,100,100)',
            ],
        },
        {
            label: 'Humeur',
            data: [moyenne_mood],
            backgroundColor: [
                'rgb(255,170,62)',
            ],
        },
        {
            label: 'Sociabilité',
            data: [moyenne_sociability],
            backgroundColor: [
                'rgb(104,221,123)',
            ],
        },
        {
            label: 'Sommeil',
            data: [moyenne_sleep],
            backgroundColor: [
                'rgb(104,116,221)',
            ],
        }]
    },

    options: {
        scales: {
            y: {
                beginAtZero: true,
                max: 10
            }
        },
    }
});