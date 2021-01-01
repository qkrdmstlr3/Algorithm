// Run by Node.js
const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  const input = [];
  for await (const line of rl) {
    input.push(line);
    rl.close();
  }
  const [k, n] = input[0].split(" ");
  const result = Math.ceil((k - 1) / (n - 1));
  console.log(result);

  process.exit();
})();
