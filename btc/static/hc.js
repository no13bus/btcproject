$(function () {
        Highcharts.setOptions({
            global: {
                useUTC: false //开启UTC
            }
        });

        var chart = new Highcharts.Chart({
            chart: {
                type: 'line',
                renderTo: 'mychart'
            },
            title: {
                text: 'btc价格变动情况'
            },
            subtitle: {
                text: '副标题不知道写啥了:)'
            },
            xAxis: {
                type: 'datetime',
                title: {
                    text: '时间轴'
                }
            },
            yAxis: {
                title: {
                    text: '价格 (美元)'
                },
                
            },
            tooltip: {
                headerFormat: '<b>{series.name}</b><br>',

                pointFormat: '{point.x:%Y-%m-%e %H:%M : %S}: {point.y} 美元 <br>{point.extra}'
            },

            series: [{
                name: 'okcoin买价',
                // Define the data points. All series have a dummy year
                // of 1970/71 in order to be compared on the same x axis. Note
                // that in JavaScript, months start at 0 for January, 1 for February etc.
                
            }, 
            {
                name: 'huobi买价',
                // Define the data points. All series have a dummy year
                // of 1970/71 in order to be compared on the same x axis. Note
                // that in JavaScript, months start at 0 for January, 1 for February etc.
                
            }, 
            {
                name: 'btcchina买价',
                // Define the data points. All series have a dummy year
                // of 1970/71 in order to be compared on the same x axis. Note
                // that in JavaScript, months start at 0 for January, 1 for February etc.
                
            }, 
            {
                name: 'bitfinex买价',
                // Define the data points. All series have a dummy year
                // of 1970/71 in order to be compared on the same x axis. Note
                // that in JavaScript, months start at 0 for January, 1 for February etc.
                
            }, 


            ]
        });
        
        var chart_ltc = new Highcharts.Chart({
            chart: {
                type: 'line',
                renderTo: 'mychart_ltc'
            },
            title: {
                text: 'ltc价格变动情况'
            },
            subtitle: {
                text: 'test'
            },
            xAxis: {
                type: 'datetime',
                title: {
                    text: '时间轴'
                }
            },
            yAxis: {
                title: {
                    text: '价格 (美元)'
                },
                
            },
            tooltip: {
                headerFormat: '<b>{series.name}</b><br>',

                pointFormat: '{point.x:%Y-%m-%e %H:%M : %S}: {point.y} 美元 <br>{point.extra}'
            },

            series: [{
                name: 'okcoin_ltc买价',
                // Define the data points. All series have a dummy year
                // of 1970/71 in order to be compared on the same x axis. Note
                // that in JavaScript, months start at 0 for January, 1 for February etc.
                
            }, 
            {
                name: 'huobi_ltc买价',
                // Define the data points. All series have a dummy year
                // of 1970/71 in order to be compared on the same x axis. Note
                // that in JavaScript, months start at 0 for January, 1 for February etc.
                
            }, 
            {
                name: 'btcchina_ltc买价',
                // Define the data points. All series have a dummy year
                // of 1970/71 in order to be compared on the same x axis. Note
                // that in JavaScript, months start at 0 for January, 1 for February etc.
                
            }, 
            {
                name: 'bitfinex_ltc买价',
                // Define the data points. All series have a dummy year
                // of 1970/71 in order to be compared on the same x axis. Note
                // that in JavaScript, months start at 0 for January, 1 for February etc.
                
            }, 


            ]
        });
        


        function getForm(){  

            var mydata0=[];
            var mydata1=[];
            var mydata2=[];
            var mydata3=[];
            var mydata4=[];
            var mydata5=[];
            var mydata6=[];
            var mydata7=[];
            $.ajax({  
                url: 'http://127.0.0.1:8002/getprice/',  
                dataType:"json", 
                async:false,
                success:function(point){
              var obj=eval(point);

              for (var i=0; i<obj[0].length; i++){
        
                mydata0.push({x:Date.parse(obj[0][i].created),y:parseFloat(obj[0][i].okcoin_buyprice),extra:obj[0][i].diff});                 
              };


              for (var i=0; i<obj[1].length; i++){
                mydata1.push({x:Date.parse(obj[1][i].created),y:parseFloat(obj[1][i].huobi_buyprice),extra:obj[1][i].diff});
              };

              for (var i=0; i<obj[2].length; i++){
               mydata2.push({x:Date.parse(obj[2][i].created),y:parseFloat(obj[2][i].btcchina_buyprice),extra:obj[2][i].diff});
              };

              for (var i=0; i<obj[3].length; i++){
               mydata3.push({x:Date.parse(obj[3][i].created),y:parseFloat(obj[3][i].bitfinex_buyprice),extra:obj[3][i].diff});
              };
              for (var i=0; i<obj[4].length; i++){
               mydata4.push({x:Date.parse(obj[4][i].created),y:parseFloat(obj[4][i].okcoin_buyprice_ltc),extra:obj[4][i].diff});
              };
              for (var i=0; i<obj[5].length; i++){
               mydata5.push({x:Date.parse(obj[5][i].created),y:parseFloat(obj[5][i].huobi_buyprice_ltc),extra:obj[5][i].diff});
              };
              for (var i=0; i<obj[6].length; i++){
               mydata6.push({x:Date.parse(obj[6][i].created),y:parseFloat(obj[6][i].btcchina_buyprice_ltc),extra:obj[6][i].diff});
              };
              for (var i=0; i<obj[7].length; i++){
               mydata7.push({x:Date.parse(obj[7][i].created),y:parseFloat(obj[7][i].bitfinex_buyprice_ltc),extra:obj[7][i].diff});
              };

            },  
                error: function(){alert('error!')},  
            });

            // chart.series[0].setData(mydata0);
            // chart.series[1].setData(mydata1);
            // chart.series[2].setData(mydata2);
            // chart.series[3].setData(mydata3);
            // chart_ltc.series[0].setData(mydata4);
            // chart_ltc.series[1].setData(mydata5);
            // chart_ltc.series[2].setData(mydata6);
            // chart_ltc.series[3].setData(mydata7);
            chart.series[0].setData(mydata0);
            chart.series[1].setData(mydata1);
            chart.series[2].setData(mydata2);
            chart.series[3].setData(mydata3);

            chart_ltc.series[0].setData(mydata4);
            chart_ltc.series[1].setData(mydata5);
            chart_ltc.series[2].setData(mydata6);
            chart_ltc.series[3].setData(mydata7);
        }  
  
        getForm();
        $(document).ready(function() {  
            //每隔3秒自动调用方法，实现图表的实时更新  
            window.setInterval(getForm,3000);   
              
        });  





    });