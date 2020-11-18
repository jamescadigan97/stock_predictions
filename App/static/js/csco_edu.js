// Trace1 for the Greek Data
d3.csv("../static/js/edu_csco.csv",function(stock_data) {
  console.log(stock_data)

  dates = []
  Edu = []
  Csco = []
 
  for (var i = 0; i < stock_data.length; i++){
    dates.push(stock_data[i].Date)
    Edu.push(stock_data[i].edu)
    Csco.push(stock_data[i].csco)
  }

  var trace1 = {
    x: dates,
    y: Edu,
    type: "line",
    name: "EDU",
  };
  
  var trace2 = {
    x: dates,
    y: Csco,
    type: "line",
    name: "CSCO",
  };

  var data = [trace1, trace2];
  
  var layout = {
    title: "EDU and CSCO Stock Prices",
  };
  
  // Render the plot to the div tag with id "plot"
  Plotly.newPlot("plot", data, layout);
  
});

