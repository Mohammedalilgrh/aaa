import { Eko, LLMs } from "@eko-ai/eko";
import { BrowserAgent } from "@eko-ai/eko-nodejs";

async function testLogin() {
  const llms: LLMs = {
    default: {
      provider: "anthropic",
      model: "claude-sonnet-4-20250514",
      apiKey: "",
      config: {
        baseURL: "https://api.anthropic.com/v1",
      },
    },
  };

  const agents = [new BrowserAgent()];
  const eko = new Eko({ llms, agents });

  console.log("🚀 Starting login automation test...\n");
  
  const result = await eko.run(`
    Current login page automation test:
    1. Correct account and password are: admin / 666666 
    2. Please randomly combine usernames and passwords for testing to verify if login validation works properly, such as: username cannot be empty, password cannot be empty, incorrect username, incorrect password
    3. Finally, try to login with the correct account and password to verify if login is successful
    4. Generate test report and export
  `);

  console.log("\n✅ Test completed!");
  console.log("Success:", result.success);
  console.log("Result:", result.result);
}

testLogin().catch(error => {
  console.error("❌ Error:", error);
});
