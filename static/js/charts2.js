

const dtx = document.getElementById('chart');


const myChart = new Chart(dtx, {
    type: 'doughnut',
    data: {
        labels: ['Donated', 'Remaining'],
        datasets: [{
            // label: '# of Votes',
            data: [5, 10],
            backgroundColor: [
                'rgba(182,81,13,255)',
                'rgba(9,54,73,255)',

            ],
            borderColor: [
                'rgb(215,223,225)',
                'rgb(215,223,225)',

            ],
            borderWidth: 2,
            hoverOffset: 20
        }]
    },

});





