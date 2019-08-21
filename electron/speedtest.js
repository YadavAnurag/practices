var speedTest = require("speedtest-net");
var test = null;

setInterval(() => {
  test = speedTest({ maxTime: 100 });
  test.on("data", data => {
    console.log(
      `Download: ${data.speeds.download} , Upload: ${data.speeds.upload}`
    );
  });

  test.on("error", err => console.log(err));
}, 1000);
