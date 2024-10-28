
$(function () {

  'use strict';
  
   var basicpieChart = echarts.init(document.getElementById('basic-pie'));
        var option = {
           

                // Add tooltip
                tooltip: {
                    trigger: 'item',
                    formatter: "{a} <br/>{b}: {c} ({d}%)"
                },

                // Add legend
                legend: {
                    orient: 'vertical',
                    x: 'left',
                    data: ['HVAC', 'Lightnings', 'Machineries', 'Pumps']
                },

                // Add custom colors
                color: ['#51ce8a', '#38649f', '#ff9920', '#fc696a'],

                // Display toolbox
                toolbox: {
                    show: true,
                    orient: 'vertical',
                    feature: {
                        mark: {
                            show: true,
                            title: {
                                mark: 'Markline switch',
                                markUndo: 'Undo markline',
                                markClear: 'Clear markline'
                            }
                        },
                        dataView: {
                            show: true,
                            readOnly: false,
                            title: 'View data',
                            lang: ['View chart data', 'Close', 'Update']
                        },
                        magicType: {
                            show: true,
                            title: {
                                pie: 'Switch to pies',
                                funnel: 'Switch to funnel',
                            },
                            type: ['pie', 'funnel'],
                            option: {
                                funnel: {
                                    x: '25%',
                                    y: '20%',
                                    width: '50%',
                                    height: '70%',
                                    funnelAlign: 'left',
                                    max: 1548
                                }
                            }
                        },
                        restore: {
                            show: true,
                            title: 'Restore'
                        },
                        saveAsImage: {
                            show: true,
                            title: 'Same as image',
                            lang: ['Save']
                        }
                    }
                },

                // Enable drag recalculate
                calculable: true,

                // Add series
                series: [{
                    name: 'Usage',
                    type: 'pie',
                    radius: '70%',
                    center: ['50%', '57.5%'],
                    data: [
                        {value: 335, name: 'HVAC'},
                        {value: 310, name: 'Lightnings'},
                        {value: 234, name: 'Machineries'},
                        {value: 135, name: 'Pumps'},
                        
                    ]
                }]
        };
    
        basicpieChart.setOption(option);



        var options = {
          series: [{
          name: 'Panels',
          data: [44, 55, 41, 67, 22, 43, 44, 23, 46, 56, 32, 30, 15, 54]
        }, {
          name: 'Investors',
          data: [13, 23, 20, 8, 13, 27, 13, 12, 43, 56, 32, 48, 32, 10]
        }, {
          name: 'Batteries',
          data: [23, 17, 12, 9, 15, 24, 18, 16, 29, 43, 54, 65, 78, 11]
        }],
          chart: {
      foreColor:"#bac0c7",
          type: 'bar',
          height: 311,
          stacked: true,
          toolbar: {
            show: false
          },
          zoom: {
            enabled: true
          }
        },
        responsive: [{
          breakpoint: 480,
          options: {
            legend: {
              position: 'bottom',
              offsetX: -10,
              offsetY: 0
            }
          }
        }],   
    grid: {
      show: true,
      borderColor: '#f7f7f7',      
    },
    colors:['#0052cc', '#04a08b', '#00baff'],
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: '15%',
        colors: {
        backgroundBarColors: ['#f0f0f0'],
        backgroundBarOpacity: 1,
      },
          },
        },
        dataLabels: {
          enabled: false
        },
 
        xaxis: {
          categories: ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7', 'Day 8', 'Day 9', 'Day 10', 'Day 11', 'Day 12', 'Day 13', 'Day 14'],
        },
        legend: {
          show: true,
      position: 'top',
          horizontalAlign: 'center',
        },
        fill: {
          opacity: 1
        }
        };

        var chart = new ApexCharts(document.querySelector("#charts_widget_1_chart"), options);
        chart.render();



}); // End of use strict


var options = {
          series: [
          {
            name: "Production",
            data: [28, 29, 33, 36, 32, 12, 33]
          },
          {
            name: "Consumption",
            data: [12, 11, 22, 36, 17, 13, 13]
          }
        ],
          chart: {
          height: 285,
          type: 'line',
          dropShadow: {
            enabled: true,
            color: '#000',
            top: 18,
            left: 7,
            blur: 10,
            opacity: 0.2
          },
          zoom: {
            enabled: false
          },
          toolbar: {
            show: false
          }
        },
        colors: ['#77B6EA', '#545454'],
        dataLabels: {
          enabled: true,
        },
        stroke: {
          curve: 'smooth'
        },
        
        
        grid: {
          borderColor: '#e7e7e7',
          row: {
            colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
            opacity: 0.5
          },
        },
        markers: {
          size: 1
        },
        xaxis: {
          categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
          
        },
        yaxis: {
          title: {
            text: 'Values in kwh'
          },
          min: 5,
          max: 40
        },
        legend: {
          position: 'top',
          horizontalAlign: 'right',
          floating: true,
          offsetY: -3,
          offsetX: -10
        }
        };

        var chart = new ApexCharts(document.querySelector("#chart"), options);
        chart.render();


        var options = {
          series: [{
          name: 'Inverter Power',
          data: [101, 40, 28, 81, 42, 109]
        }, {
          name: 'Feeding Power',
          data: [-11, 132, -45, 32, 34, -52]
        },{
          name: 'Load Power',
          data: [11, 32, 145, 32, 154, 52]

        }],
          chart: {
          height: 254,
           toolbar: {
            show: false
          },
          type: 'area'
          
        },
        dataLabels: {
          enabled: false
        },
        legend:
        {
          show:false
        },
        stroke: {
          curve: 'straight'
        },
        xaxis: {
          categories: ['1 pm', '5 pm', '9 pm', '1 am', '5 am', '9 am',]
        },
        tooltip: {
          x: {
            format: 'dd/MM/yy HH:mm'
          },
        },
        };

        var chart = new ApexCharts(document.querySelector("#chart2"), options);
        chart.render();