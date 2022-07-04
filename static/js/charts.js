let nums = document.querySelectorAll('.myChart');
// let bums = document.querySelector('.chart')


nums.forEach((num)=>{

    const ctx = document.getElementById('myChart-'+ num.attributes.value.value);
    
    const totalX = document.getElementById('amount-don-'+ num.attributes.value.value)

    const remainderX = document.getElementById('cost-' + num.attributes.value.value)

    let remainder = remainderX.attributes.value.value - totalX.attributes.value.value

    let total = totalX.attributes.value.value
    
    console.log(remainderX.attributes.value.value)
    console.log(total)
    console.log(remainder)
    
    // console.log(totalX.attributes.value)
    
    
    

    const myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Donated', 'Remaining'],
        datasets: [{
            // label: '# of Votes',
            data: [total, remainder],
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

})


