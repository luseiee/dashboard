$(function() {

    // var lll = 10;
    function getTraffic() {
        $.getJSON('/traffic-data.json', function(json) {

            var aa = [];
            for(var key in json){
                aa.push({
                    indexLabel: key + ": #percent%",
                    legendText: key,
                    y: json[key]
                });
            }

            // aa.push({
            //         indexLabel: "lll" + ": #percent%",
            //         legendText: "lll",
            //         y: lll
            //     });
            // lll+=2;

            var chart = new CanvasJS.Chart("trafficMonitor",
            {
                title:{
                    text: "Traffic Monitor"
                },     
                        animationEnabled: false,     
                data: [
                {        
                    type: "doughnut",
                    startAngle: 60,                          
                    toolTipContent: "{legendText}: {y} - <strong>#percent% </strong>",                  
                    showInLegend: true,
                    dataPoints: aa
                }
                ]
            });
            chart.render();
        });
    }
    getTraffic();
    window.setInterval(getTraffic,30000);   
})

$(function () {
    function getDiskSpace() {

        $.getJSON('disk-space-data.json', function(json) {
            var aa = [];
            for(var key in json){
                aa.push({
                    y: json[key],
                    label: key 
                });
            }
            aa.sort(function(a, b) {
                return a.y - b.y;
            });

            var chart = new CanvasJS.Chart("diskMonitor", {
                title:{
                    text:"Disk Monitor"              

                },
                            animationEnabled: false,
                axisX:{
                    interval: 1,
                    gridThickness: 0,
                    labelFontSize: 13,
                    labelFontStyle: "normal",
                    labelFontWeight: "normal",
                    labelFontFamily: "Lucida Sans Unicode"

                },
                axisY2:{
                    interlacedColor: "rgba(1,77,101,.2)",
                    gridColor: "rgba(1,77,101,.1)"

                },

                data: [
                {     
                    type: "bar",
                    name: "companies",
                    axisYType: "secondary",
                    color: "#014D65",               
                    dataPoints: aa
                    // [
                    // {y: 5, label: "Sweden"  },
                    // {y: 6, label: "Taiwan"  },
                    // {y: 7, label: "Russia"  },
                    // {y: 8, label: "Spain"  },
                    // {y: 8, label: "Brazil"  }
                    // ]
                }
                ]
            });
            chart.render();
        });
    }
    getDiskSpace();
    window.setInterval(getDiskSpace,30000); 
})
