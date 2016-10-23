console.log('gsg')

var now = new Date();
var minutes = now.getMinutes();
var seconds = now.getSeconds();
console.log (minutes)

var clock = $('.your-clock').FlipClock({
	countdown: true,
    stop: function() {
	    // do something
	    // reset the counter and it will start again
	    this.setTime(900);
    }
  });

minutes_seconds = minutes * 60 +seconds; 
console.log (minutes_seconds)

timestuff = minutes_seconds;

while (timestuff >= 900){
	timestuff = timestuff - 900;
}

timestuff = (timestuff - 900)*(-1);

clock.setTime(timestuff);
clock.start();
console.log (timestuff);
