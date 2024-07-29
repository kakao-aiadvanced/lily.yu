import os

from openai import OpenAI

os.environ["OPENAI_API_KEY"] = "api_key"


client = OpenAI()


def generate_prompt(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "당신은 유용한 조력자입니다."},
            {
                "role": "user",
                "content": user_input,
            },
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].message.content


# 사용자 입력 받기
user_input = "What are the tourist attractions in Korea?."

# 프롬프트 생성
generated_prompt = generate_prompt(user_input)
print("Generated Prompt:", generated_prompt)
