import openai
import os
openai.api_key = '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'


def get_completion(prompt,
                   model="gpt-4"):  # Andrew mentioned that the prompt/ completion paradigm is preferable for this class
    messages = [{"role": "assistant", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


prompt = f"""
Your task is to generate a list of possible affirmation for me,
the outcome must be bullet text format
"""

response = get_completion(prompt)
print(response)