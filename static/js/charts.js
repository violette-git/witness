let nums = document.querySelectorAll('.myChart');


nums.forEach((num)=>{

    const ctx = document.getElementById('myChart-'+ num.attributes.value.value);
    
    // const totalX = document.getElementById('amount-don-'+ num.attributes.value.value)
    
    // console.log(totalX.attributes.value)

    const percentageX = document.getElementById('perc-don-'+ num.attributes.value.value)

    let percentage = percentageX.attributes.value.value

    // console.log(parseInt(percentage))

    let percentageTotal = 100
    
    let percentage_total = (percentageTotal - percentage)
    console.log(percentage_total)
    console.log(percentage)
    

const myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        // labels: ['percent donated', 'remaining amount'],
        datasets: [{
            // label: '# of Votes',
            data: [percentage, percentage_total],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                
            ],
            borderWidth: 1,
            hoverOffset: 20
        }]
    },
    
});

})





