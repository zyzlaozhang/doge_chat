import openai
openai.api_key = "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"
response = openai.Completion.create(
model="text-davinci-003",
prompt="markdown",
temperature=0.7,
max_tokens=256,
top_p=1,
frequency_penalty=0,
presence_penalty=0
)
print(response["choices"][0]["text"])