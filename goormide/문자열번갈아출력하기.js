const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", function (line) {
  const newText = [];
  line = line.split("");

  let flag = false;
  while (line.length) {
    flag = !flag;
    if (flag) {
      newText.push(line.shift());
      continue;
    }
    newText.push(line.pop());
  }
  console.log(newText.join(""));
  rl.close();
}).on("close", function () {
  process.exit();
});
