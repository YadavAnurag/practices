const recordAudio = () => {
  return new Promise((resolve, reject) => {
    navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
      const mediaRecorder = new MediaRecorder(stream);
      const audioChunks = [];

      mediaRecorder.addEventListener("dataavailable", event => {
        audioChunks.push(event.data);
      });

      const start = () => {
        mediaRecorder.start();
      };

      const stop = () => {
        return new Promise((resolve, reject) => {
          mediaRecorder.addEventListener("stop", () => {
            const audioBlob = new Blob(audioChunks);
            const audioURL = URL.createObjectURL(audioBlob);
            const audio = new Audio(audioURL);
            const play = () => {
              audio.play();
            };
            resolve({ audioBlob, audioURL, play });
          });
          mediaRecorder.stop();
        });
      };

      resolve({ start, stop });
    });
  });
};

const sleep = time =>
  new Promise((resolve, reject) => {
    setTimeout(resolve, time);
  });
