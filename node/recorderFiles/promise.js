const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    const num = Math.ceil(Math.random() * 19);
    if (num % 2 == 0) {
      resolve(`Successfully Got even number ${num}`);
    }
    reject(new Error("whoops"));
  }, 2000);
});

promise
  .then(
    result => {
      console.log(result);
    },
    error => {
      alert(error);
    }
  )
  .catch(() => {
    console.log("got rejected");
  })
  .finally(() => {
    console.log("finally got it");
  });
