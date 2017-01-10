const Si7021 = require('si7021-sensor');
var parseJson = require('parse-json');
var json;
 
// Si7021 constructor options object is optional, i2cBusNo defaults to 1
//
const si7021 = new Si7021({ i2cBusNo : 1 });
 
const readSensorData = () => {
  si7021.readSensorData()
    .then((data) => {
//      console.log(`data = ${JSON.stringify(data, null, 2)}`);
      json = JSON.stringify(data, null, 2);
      hum = JSON.parse(json).humidity;
      tmp = JSON.parse(json).temperature_C;
      console.log("Humidity      = ", hum);
      console.log("Temperature C = ", tmp);
      console.log("Temperature F = ", tmp * 9 / 5 + 32);
      setTimeout(readSensorData, 2000);
    })
    .catch((err) => {
      console.log(`Si7021 read error: ${err}`);
      setTimeout(readSensorData, 20000);
    });
};

 
si7021.reset()
  .then((result) => readSensorData())
  .catch((err) => console.error(`Si7021 reset failed: ${err} `));

