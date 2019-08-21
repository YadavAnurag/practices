var recorder = null;
var audio = null;

const record = async () => {
  document.querySelector("#record").innerHTML = "Recording...";
  recorder = await recordAudio();
  recorder.start();
};

const stop = async () => {
  document.querySelector("#record").innerHTML = "Record";
  audio = await recorder.stop();
};

const play = async () => {
  audio.play();
};

var socket = io.connect("localhost:3000");
socket.on("connect", () => {
  console.log("Client got connected to server");
});

socket.on("helloMessage", data => {
  console.log(`Server: ${data.msg}`);
});
