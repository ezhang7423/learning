dataSet = [1, 5,3, 4, 5]


d3.select('body')
    .selectAll('p')
    .data(dataSet)
    .enter()
    .append('p')
    .text(function(d){return d;})