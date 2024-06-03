from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

# 환경 변수에서 API 키 가져오기
api_key = os.getenv('OPENAI_API_KEY')


# ChatOpenAI 객체 생성
llm = ChatOpenAI(
    temperature=0.1,  # 창의성 (0.0 ~ 2.0)
    max_tokens=2048,  # 최대 토큰수
    model_name="gpt-3.5-turbo",  # 모델명
)



#----------------------------------------------------------#
from langchain.schema import HumanMessage

# 질의내용
question = "대한민국의 수도는 어디인가요?"

# 질의
response = llm([HumanMessage(content=question)])

print(f"[답변]: response: {response.content}")

#----------------------------------------------------------#
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# 질문 템플릿 형식 정의
template = "{country}의 수도는 뭐야?"

# 템플릿
prompt = PromptTemplate.from_template(template=template)


# 연결된 체인(Chain)객체 생성
input_list = [{"country": "호주"}, {"country": "중국"}, {"country": "네덜란드"}]
llm_chain = LLMChain(prompt=prompt, llm=llm)
result = llm_chain.apply(input_list)

for res in result:
 print(res["text"].strip())
