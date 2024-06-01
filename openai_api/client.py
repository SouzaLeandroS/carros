from openai import OpenAI

client = OpenAI(
    api_key='sk-proj-GTb246pJ5nfrYo0Fa0MDT3BlbkFJQ0h7QdEGcrhbVIIgQY4K'
)

def get_car_ai_bio(model, brand, year):
    message = ''''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
    '''
    
    message = message.format(brand, model, year)
    response = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': message
            }
        ],
        max_tokens=1000,
        model='gpt-3.5-turbo',
    )
    return response.choices[0].message.content