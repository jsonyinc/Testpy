import os

def 환경변수_테스트():
    """
    'GEMINI_API_KEY' 환경변수가 제대로 설정되었는지 확인하고,
    값이 있다면 처음 몇 글자를 출력하여 사용자가 확인할 수 있도록 돕는 함수입니다.
    """
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key:
        print("축하합니다! GEMINI_API_KEY 환경변수가 성공적으로 로드되었습니다.")
        # API 키의 전체를 보여주는 것은 보안상 위험하므로, 처음 몇 글자만 보여줍니다.
        masked_api_key = api_key[:4] + "***"  # 처음 4글자만 보여주고 나머지는 "***"로 마스킹
        print(f"확인을 위해 처음 몇 글자를 보여드립니다: {masked_api_key}")
        print("이제 Gemini API를 사용하기 위한 준비가 완료되었습니다.")
    else:
        print("오류: GEMINI_API_KEY 환경변수를 찾을 수 없습니다.")
        print("환경변수가 제대로 설정되었는지 다시 한번 확인해 주세요.")
        print("macOS 환경에서 환경변수 설정 방법은 다음과 같습니다:")
        print("1. 터미널을 열고, `~/.zshrc` 또는 `~/.bash_profile` 파일을 편집기로 여세요 (예: `nano ~/.zshrc`).")
        print("2. 파일 내용 맨 아래에 `export GEMINI_API_KEY='YOUR_API_KEY'` 를 추가하고 'YOUR_API_KEY' 부분에 실제 API 키로 대체하세요.")
        print("3. 변경 사항을 저장하고 편집기를 닫으세요.")
        print("4. 터미널에서 `source ~/.zshrc` 또는 `source ~/.bash_profile` 를 실행하여 변경된 환경변수를 적용하세요.")
        print("5. 또는, 새로운 터미널 세션을 열면 환경변수가 자동으로 적용됩니다.")

if __name__ == "__main__":
    환경변수_테스트()