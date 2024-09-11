let myPromise = new Promise((myResolve, myReject) => {
  myReject();
});
myPromise
  .then(() => {
    console.log("success");
  })
  .catch(() => {
    console.log("fail");
  });
