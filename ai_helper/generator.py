from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def generate_code(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
