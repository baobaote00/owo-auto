var asciify = require('asciify-image');
 
var options = {
  fit:    'box',
  width:  100,
  height: 100
}
 
asciify('https://octodex.github.com/images/privateinvestocat.jpg', options, function (err, asciified) {
  if (err) throw err;
 
  // Print to console
  console.log(asciified);
});