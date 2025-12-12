from openai import OpenAI
from dotenv import dotenv_values

config = dotenv_values(".env")

client = OpenAI(api_key=config["API_KEY"])

def generate_blog(paragraph_topic):
    response = client.completions.create(
        model= 'gpt-3.5-turbo-instruct',
        prompt=f"Create a blog on this topic: {paragraph_topic}",
        max_tokens= 400,
        temperature= 0.3
    )

    retrieve_blog =  response.choices[0].text
    return retrieve_blog

keep_writing = True

while keep_writing: 
    answer = input('Want to create blog? Y for yes and anything else for no ')

    if (answer == 'Y'):
        paragraph_topic = input('What should this blog be about? ')
        print(generate_blog(paragraph_topic))

    else:
        keep_writing = False

        

