var fs = require('fs');
var json2csv = require('json2csv');
var request = require('request');

request('http://algorest.carzacc.info', { json: true }, function(err, res, body){
  if (err) { return console.log(err); }
  try {
  var csvgenerato = json2csv({ data: body});
  console.log(csvgenerato);
  fs.writeFile('csvs/dati.csv', csvgenerato, function (err) {
  if (err) return console.log(err);
  console.log('Creati CSV');
});

} catch (err) {
  console.error(err);
}
});
