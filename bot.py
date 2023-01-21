import openai
openai.api_key = "your api-key"

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

while True:
    user_input = input("User: ")
    if user_input == "exit":
        break
    response = generate_response(user_input)
    print("ChatGPT: " + response)