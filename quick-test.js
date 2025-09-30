const { Eko } = require("@eko-ai/eko");
const { BrowserAgent } = require("@eko-ai/eko-nodejs");

async function run() {
  const llms = {
    default: {
      provider: "anthropic",
      model: "claude-sonnet-4-20250514",
      apiKey: "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",
      config: {
        baseURL: "https://api.anthropic.com/v1",
      },
    },
  };

  const agents = [new BrowserAgent()];
  const eko = new Eko({ llms, agents });

  console.log("Starting test...");
  
  const result = await eko.run("Go to google.com");
  console.log("Result:", result);
}

run().catch(console.error);
