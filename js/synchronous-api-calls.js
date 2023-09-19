
const urls = ["GET https://www.go.com", "GET https://www.now.com", "GET https://ksm.com"]

const main = async () => {
  for (const url of urls) {
    console.log(url)
    await wait(1000);
  }
}
const wait = (milliseconds) => {
  return new Promise(resolve => setTimeout(resolve, milliseconds));
}

main();