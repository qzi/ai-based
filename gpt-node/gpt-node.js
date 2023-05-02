import { Configuration, OpenAIApi } from "openai";

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);

const completion = await openai.createCompletion({
  model: "text-davinci-003",
  prompt: "能帮我详细解读阿德勒的课题分离吗?",
  max_tokens: 1024,
  n: 1,
  stop: "None",
  temperature: 0.5,
});
console.log(completion.data.choices[0].text);