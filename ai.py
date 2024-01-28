import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "make a story"}])
print(completion.choices[0].message.content)