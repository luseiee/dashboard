$(function() {

    $.getJSON('/traffic-data.json', function(json) {

            var dataget = [];
            for(var key in json){
                dataget.push({
                    label: key,
                    value: json[key]
                });
            }
            Morris.Donut({
                element: 'morris-donut-chart',
                data: dataget,
                formatter: function (y, data) { return y + '%' },
                resize: true
            });
            // Morris.Donut({
            //     element: 'morris-donut-chart',
            //     data: [{
            //         label: "POD1",
            //         value: 50
            //     }, {
            //         label: "POD2",
            //         value: 20
            //     }, {
            //         label: "POD31",
            //         value: 30
            //     }],
            //     resize: true
            // });

    });

    
});
