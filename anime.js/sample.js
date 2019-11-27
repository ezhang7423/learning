anime.speed = .38;
var timeline = anime.timeline({ autoplay: true, direction: 'linear', loop: true });


var temp = document.querySelector('.temp');
var pH = document.querySelector('.pH');
var salinity = document.querySelector('.Salinity');
var dataCotainer = {
  Temperature: 3001,
  pH: 800,
  Salinity: 3700,
}


function makeDecimal(prop){
  prop = JSON.stringify(prop)
  return (prop.substr(0, 2)+'.'+prop.substr(2, 4))
}
timeline.add({
  targets: dataCotainer,
  Temperature: 3010,
  pH: 809,
  Salinity: 3710,
  easing: 'linear',
  round: 1,
  update: function() {
    temp.innerHTML = makeDecimal(dataCotainer.Temperature);
    pH.innerHTML =makeDecimal( dataCotainer.pH);
    salinity.innerHTML =makeDecimal(dataCotainer.Salinity);
  },
  duration: 10000,
})
timeline.add({
  targets: dataCotainer,
  Temperature: 3001,
  pH: 809,
  Salinity: 3700,
  easing: 'linear',
  round: 1,
  update: function() {
    temp.innerHTML = makeDecimal(dataCotainer.Temperature);
    pH.innerHTML =makeDecimal( dataCotainer.pH);
    salinity.innerHTML =makeDecimal(dataCotainer.Salinity);
  },
  duration: 10000,
})
