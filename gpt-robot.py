import openai

# Set up the OpenAI API client
openai.api_key = "you-gpt-api-token"

# Set up the model and prompt
model_engine = "text-davinci-003"


def generate_response(input_text):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=input_text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text
    return message.strip()

while True:
    user_input = input("您的问题： ")
    if user_input.lower() == "退出":
        break
    response = generate_response(user_input)
    print("ChatGPT: " + response)
