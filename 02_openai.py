from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="Your OpenAI API Key",
)

command = '''[9:25 AM, 8/18/2024] Thy_Professor: Bhai sun
[9:25 AM, 8/18/2024] Thy_Professor: Smo main chalna hai na
[9:25 AM, 8/18/2024] Haroon: Han chalte hr
[9:25 AM, 8/18/2024] Thy_Professor: 10 ka bola hai lakin apan 10:15 per chalty Hain
[9:26 AM, 8/18/2024] Thy_Professor: 10:30 pohch jaingy
[9:26 AM, 8/18/2024] Haroon: Ok
[10:16 AM, 8/18/2024] Haroon: Bhai
[10:16 AM, 8/18/2024] Haroon: Me nikal gya
[10:16 AM, 8/18/2024] Haroon: Tu bahar aa
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named Raimal who speaks hindi as well as english. He is from Pakistan and is a coder. You analyze chat history and respond like Raimal"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)