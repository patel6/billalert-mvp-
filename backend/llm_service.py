import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize the Async client
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def summarize_bill(bill_title: str, bill_text: str) -> str:
    """
    Generates a 3-4 sentence plain-language summary using GPT-4o-mini.
    """
    prompt = f"""Summarize the following Arizona legislative bill in 3-4 sentences. 
    Use plain language that a high school student would understand.
    
    Bill Title: {bill_title}
    Bill Content: {bill_text[:5000]}
    """

    try:
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes complex legislation into simple terms."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=250
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI Error: {e}")
        return "Summary currently unavailable via OpenAI."