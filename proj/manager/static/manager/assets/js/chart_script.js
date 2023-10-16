document.addEventListener('DOMContentLoaded', function() {
    var ctx = document.getElementById('chart').getContext('2d');

    var data = {
        labels: ['Leftover Capacity', 'Product Capacity', 'Warehouse Capacity'],
        datasets: [{
            data: [
                leftover_capacity,
                total_products_quantity,
                total_warehouse_capacity,
            ],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)'
            ],
            borderWidth: 1
        }]
    };

    var myPieChart = new Chart(ctx, {
        type: 'pie',
        data: data
    });
});
