import google.generativeai as genai
import os # os 모듈 임포트 추가

# 1. Gemini API 키 불러오기 (환경 변수에서 Gemini API 키 불러오기)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")  # 환경변수 호출

# API 키가 설정되지 않은 경우 예외 처리 (선택 사항)
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY 환경 변수가 설정되지 않았습니다.")

genai.configure(api_key=GEMINI_API_KEY)

# 2. Gemini 모델 선택 (gemini-pro 모델 사용)
model = genai.GenerativeModel('gemini-2.0-flash')

# 3. LLM 호출 함수 (동기 방식)
def llm_call(prompt: str, model_name: str = "ggemini-2.0-flash") -> str:
    """
    Gemini Pro 모델을 호출하여 텍스트를 생성하는 동기 함수입니다.

    Args:
        prompt (str): 사용자 프롬프트 텍스트
        model_name (str, optional): 사용할 Gemini 모델 이름 (기본값: "gemini-pro").

    Returns:
        str: 모델이 생성한 텍스트 응답
    """
    response = model.generate_content(prompt) # Gemini API는 메시지 구조 없이 텍스트 프롬프트 직접 사용
    return response.text # 텍스트 응답 반환


# 4. LLM 호출 함수 (비동기 방식)
async def llm_call_async(prompt: str, model_name: str = "gemini-2.0-flash") -> str:
    """
    Gemini Pro 모델을 호출하여 텍스트를 생성하는 비동기 함수입니다.

    Args:
        prompt (str): 사용자 프롬프트 텍스트
        model_name (str, optional): 사용할 Gemini 모델 이름 (기본값: "gemini-pro").

    Returns:
        str: 모델이 생성한 텍스트 응답
    """
    response = await model.generate_content_async(prompt) # 비동기 호출
    print(model_name,"모델 비동기 완료") # 모델 이름 출력 (비동기 완료 확인용)
    return response.text # 텍스트 응답 반환


# 5. main 함수 (코드 실행 테스트)
if __name__ == "__main__":
    test = llm_call("안녕") # 동기 호출 테스트
    print("동기 답변:", test)

    import asyncio # 비동기 함수 실행을 위한 asyncio 라이브러리 임포트
    async def main_async(): # 비동기 main 함수 정의
        test_async = await llm_call_async("안녕하세요!") # 비동기 호출 테스트
        print("비동기 답변:", test_async)

    asyncio.run(main_async()) # 비동기 main 함수 실행




# import re
# from openai import AsyncOpenAI, OpenAI

# OPENAI_API_KEY = ""

# client = AsyncOpenAI(
#     api_key=OPENAI_API_KEY,  
# )
# sync_client = OpenAI(
#     api_key=OPENAI_API_KEY,
# )

# def llm_call(prompt: str,  model: str = "gpt-4o-mini") -> str:
#     messages = []
#     messages.append({"role": "user", "content": prompt})
#     chat_completion = sync_client.chat.completions.create(
#         model=model,
#         messages=messages,
#     )
#     return chat_completion.choices[0].message.content


# async def llm_call_async(prompt: str,  model: str = "gpt-4o-mini") -> str:
#     messages = []
#     messages.append({"role": "user", "content": prompt})
#     chat_completion = await client.chat.completions.create(
#         model=model,
#         messages=messages,
#     )
#     print(model,"완료")
    
#     return chat_completion.choices[0].message.content


# if __name__ == "__main__":
#     test = llm_call("안녕")
#     print(test)

