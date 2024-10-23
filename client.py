from dotenv import load_dotenv
import os
import json
from openai import OpenAI

load_dotenv()
key = os.getenv('OPENAI_API_KEY')

party_animals = [
    {"type":"capybara", "clothing": "party hat", "description" : "friendly, chill", "price": "150$" },
    {"type":"cat", "clothing": "nothing", "description" : "diabolical, aggressive and fat", "price": "0$" },
    {"type":"giraffe", "clothing": "tie", "description" : "he's pretty cool", "price": "3000$" }
]

print(key)

animals_string = json.dumps(party_animals)

prompt = ("we are a party agency. we rent out party animals. you're supposed to answer questions about these animals:" + animals_string  +
          "if you dont know, dont make assumptions (instead, tell them to contact us at 054123456 for additional info). also dont elaborate too much unless asked. be freindly");


client = OpenAI(
    api_key=key
)

print("Hi! welcome to our party agency. we rent party animals. do you have any questions?")

message_history = [{ "role": "system", "content": prompt}]

while True:
    user_input = input("user: ");

    if user_input == "exit":
        break

    message_history.append({"role": "user", "content": user_input})

    chat_completion = client.chat.completions.create(
        messages=message_history,
        model="gpt-3.5-turbo",
    )

    message_history.append(chat_completion.choices[0].message)
    print(chat_completion.choices[0].message.content)

print("thanks for your time!")