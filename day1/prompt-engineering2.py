import os

from openai import OpenAI

os.environ["OPENAI_API_KEY"] = "api_key"


client = OpenAI()


def generate_prompt(user_input):
    prompt = """
    너는 IT 회사의 프로젝트 리더야. 요구 사항이 생기면 너는 너의 부하직원에게 적절히 업무를 부여해야해. 입력으로 들어오는 요청(요구 사항)을 보고 이 일을 백앤드 개발자에게 전달해야 할지, 프런트 개발자에게 전달해야 할지, 기획자에게 전달해야 할지 판단해줘. 그리고 왜 그렇게 판단했는지도 설명해줘.
    답변(출력) 형식은 다음과 같아.
    {팀원의 역할}: {이 팀원을 선택한 이유. 1~2줄 분량}
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
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
user_input = "브라우저에 뜨는 팝업 중 일부의 버튼을 수정해야한다. '진행하기' 버튼의 색상을 더 눈에 띄게 개선하라."

# 프롬프트 생성
generated_prompt = generate_prompt(user_input)
print("Generated Prompt:\n", generated_prompt)
