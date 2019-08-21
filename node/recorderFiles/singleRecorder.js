navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
  const mediaRecorder = new MediaRecorder(stream);
  mediaRecorder.start(1000);

  const audioChunks = [];

  mediaRecorder.addEventListener("dataavailable", event => {
    audioChunks.push(event.data);
  });

  // creating URL
  mediaRecorder.addEventListener("stop", () => {
    const audioBlob = new Blob(audioChunks);
    const audioURL = URL.createObjectURL(audioBlob);

    const audio = new Audio(audioURL);
    audio.play();
  });

  setTimeout(() => {
    mediaRecorder.stop();
    console.log(audioChunks);
  }, 4000);
});
