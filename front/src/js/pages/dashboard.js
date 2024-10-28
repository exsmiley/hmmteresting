
$(function () {

  'use strict';
  
  
 var dom = document.getElementById('chart-container');
var myChart = echarts.init(dom, null, {
  renderer: 'canvas',
  useDirtyRect: false
});
var app = {};

var option;

option = {
  series: [
    {
      type: 'gauge',
      axisLine: {
        lineStyle: {
          width: 10,
          color: [
            [0.3, '#ff9920'],
            [0.7, '#51ce8a'],
            [1, '#fc696a']
          ]
        }
      },
      pointer: {
        itemStyle: {
          color: 'auto'
        }
      },
      
      splitLine: {
        distance: -75,
        length: 20,
        lineStyle: {
          color: '#fff',
          width: 0
        }
      },
      axisLabel: {
        color: 'inherit',
        distance: 40,
        fontSize: 10
      },
      detail: {
        valueAnimation: true,
        formatter: '{value} %',
        fontSize: 10,
        color: 'inherit',
        offsetCenter: [0, '75%']
      },
      data: [
        {
          value: 10,
          fontSize:2
        }
      ]
    }
  ]
};
setInterval(function () {
  myChart.setOption({
    series: [
      {
        data: [
          {
            value: +(Math.random() * 100).toFixed(2)
          }
        ]
      }
    ]
  });
}, 2000);

if (option && typeof option === 'object') {
  myChart.setOption(option);
}

window.addEventListener('resize', myChart.resize);




  var dom = document.getElementById('chart-conta');
var myChart = echarts.init(dom, null, {
  renderer: 'canvas',
  useDirtyRect: false
});
var app = {};

var option;

option = {
  series: [
    {
      type: 'gauge',
      axisLine: {
        lineStyle: {
          width: 10,
          color: [
            [0.3, '#ff9920'],
            [0.7, '#51ce8a'],
            [1, '#fc696a']
          ]
        }
      },
      pointer: {
        itemStyle: {
          color: 'auto'
        }
      },
      
      splitLine: {
        distance: -75,
        length: 20,
        lineStyle: {
          color: '#fff',
          width: 0
        }
      },
      axisLabel: {
        color: 'inherit',
        distance: 40,
        fontSize: 10
      },
      detail: {
        valueAnimation: true,
        formatter: '{value} ',
        fontSize: 10,
        color: 'inherit',
        offsetCenter: [0, '75%']
      },
      data: [
        {
          value: 70,
          fontSize:2
        }
      ]
    }
  ]
};
setInterval(function () {
  myChart.setOption({
    series: [
      {
        data: [
          {
            value: +(Math.random() * 100).toFixed(2)
          }
        ]
      }
    ]
  });
}, 2000);

if (option && typeof option === 'object') {
  myChart.setOption(option);
}

window.addEventListener('resize', myChart.resize);


var dom = document.getElementById('chart-contain');
var myChart = echarts.init(dom, null, {
  renderer: 'canvas',
  useDirtyRect: false
});
var app = {};

var option;

option = {
  series: [
    {
      type: 'gauge',
      axisLine: {
        lineStyle: {
          width: 10,
          color: [
            [0.3, '#ff9920'],
            [0.7, '#51ce8a'],
            [1, '#fc696a']
          ]
        }
      },
      pointer: {
        itemStyle: {
          color: 'auto'
        }
      },
      
      splitLine: {
        distance: -75,
        length: 20,
        lineStyle: {
          color: '#fff',
          width: 0
        }
      },
      axisLabel: {
        color: 'inherit',
        distance: 40,
        fontSize: 10
      },
      detail: {
        valueAnimation: true,
        formatter: '{value} %',
        fontSize: 10,
        color: 'inherit',
        offsetCenter: [0, '75%']
      },
      data: [
        {
          value: 80,
          fontSize:2
        }
      ]
    }
  ]
};
setInterval(function () {
  myChart.setOption({
    series: [
      {
        data: [
          {
            value: +(Math.random() * 100).toFixed(2)
          }
        ]
      }
    ]
  });
}, 2000);

if (option && typeof option === 'object') {
  myChart.setOption(option);
}

window.addEventListener('resize', myChart.resize);



Morris.Area({
        element: 'area-chart',
        data: [{
            period: '2018',
            data1: 525,
            data2: 852,
            data3: 225
        }, {
            period: '2019',
            data1: 635,
            data2: 505,
            data3: 185
        }, {
            period: '2020',
            data1: 385,
            data2: 465,
            data3: 375
        }, {
            period: '2021',
            data1: 575,
            data2: 205,
            data3: 545
        }, {
            period: '2022',
            data1: 785,
            data2: 355,
            data3: 545
        }, {
            period: '2023',
            data1: 810,
            data2: 405,
            data3: 285
        },
         {
            period: '2024',
            data1: 855,
            data2: 555,
            data3: 305
        }],
        xkey: 'period',
        ykeys: ['data1', 'data2', 'data3'],
        labels: ['Energy Produced', 'Energy Consumption', 'Energy Sold to grid'],
        pointSize: 3,
        fillOpacity: 0,
        pointStrokeColors:['#4d7cff', '#51ce8a', '#733aeb'],
        behaveLikeLine: true,
        gridLineColor: '#e0e0e0',
        lineWidth: 3,
        hideHover: 'auto',
        lineColors: ['#4d7cff', '#51ce8a', '#733aeb'],
        resize: true
        
    });


}); // End of use strict


var options = {
          series: [{
          name: 'Yield Energy',
          data: [44, 55, 57, 56, 61, 58]
        }, {
          name: 'Exported Energy',
          data: [76, 85, 101, 98, 87, 105]
        }, {
          name: 'Selfuse Energy',
          data: [35, 41, 36, 26, 45, 48]
        }],
          chart: {
          type: 'bar',
          height: 300
        },
        legend:
        {
          show:false,
        },
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: '55%',
            endingShape: 'rounded'
          },
        },
        dataLabels: {
          enabled: false
        },

        stroke: {
          show: true,
          width: 2,
          colors: ['transparent']
        },
        xaxis: {
          categories: ['1 pm', '5 pm', '9 pm', '1 am', '5 am', '9 am'],
        },
        // yaxis: {
        //   title: {
        //     text: '$ (thousands)'
        //   }
        // },
        fill: {
          opacity: 1
        },
        tooltip: {
          y: {
            formatter: function (val) {
              return "kw " + val + " thousands"
            }
          }
        }
        };

        var chart = new ApexCharts(document.querySelector("#chart"), options);
        chart.render();