# LLM-PaperSearcher

## 1. 개요
최근에는 매일 엄청난 양의 논문이 쏟아져 나오고 있다. 연구에 필요한 논문을 찾고, 이 논문이 연구 주제에 적합한지 읽어보고 선별하는 과정은 연구 과정에 있어서 비효율을 가져온다. 이에 사용자가 자유롭게 질문을 하면, 해당 질문에 부합하는 검색어를 만들어내 검색하고, 논문 내용의 제목과 저자, 요약과 링크 등을 제공하는 챗봇을 기획하게 되었다. 이 챗봇으로 논문에 대한 접근성을 향상시키고, 논문을 이용한 연구에 효율성을 더할 것을 기대한다.

## 2. 서비스 구조 
- main.py: 메인 실행 파일. 
- LLM.py: generateST(검색어 생성), SummarizePP(논문 요약) 등의 openAl API를 사용하는 함수가 들어있는 파일. 
- parser.py: searchPaper(논문 검색 및 스크롤) 등 웹 파싱에 관련된 파일. 
- prompts.py: CoT, Few shot, Role playing 등 Prompting 기법들을 모아놓은 파일. 

### 위 서비스는 다음과 같이 크게 3단계 구조로 나눌 수 있다. 
- (1) 사용자의 prompt를 입력 받아 arxiv 검색어를 생성해내는 부분(LLM 사용) 
    - prompt를 입력받고, pydantic의 BaseModel을 상속받는 클래스를 만들어 structured Outputs을 적용했다
    -  Terms: List[str] 형식으로 검색어를 3개 생성하게 했다.
    -  CoT prompt와 Few shot prompt를 이용하여 검색의 정확도를 높이고자 했다.
- (2) 생성한 검색어로 arxiv.com의 검색 링크를 생성하여 논문 제목, 저자, 링크, abstract을 스크롤하는 부분. 
    - 생성된 검색어를 이용해 링크를 생성한다.
    -  request와 beautifulSoup을 이용하여 링크에서 필요한 부분, 즉 논문 제목, 저자, 링크, abstract를 스크롤해온다.검색어 생성은 arxiv의 검색 링크 형식이 일정함을 이용하여 생성했다.
    -  크롤한 정보들은 Paper = dict{"Title", "Author”, “Link","Abstract”}의 형식으로 저장한다. 또한, 검색어 하나당 일정 개수(사용자 입력)의 논문 링크를 추출하여 같은 작업을 반복한다.
    -  결과적으로 List[Paper] 형식으로 정보를 저장한다. 
- (3) 사용자의 prompt와 논문 제목, abstract를 이용하여 논문의 요약을 생성하고, 올바르게 추천했는지 타당성 검사(LLM 사용) 
    - (1)에서 입력받은 prompt와 논문 Title, Abstract를 이용하여 논문에 대한 설명과 prompt와의 연관성, 그리고 추천의 적합도를 생성해낸다.
    - (1)과 동일하게 BaseModel을 상속받는 클래스를 만들어 structured Outputs을 적용했고 다음과 같은 형식으로 답변이 나오도록 했다: **{description: str; Relevance: float}**
    -  또한, 여기서는 abstract가 너무 많은 토큰을 차지하고, 방대해서 Cot prompt나 Few shot prompt로 처리하기에는 무리가 있었다. 그리고 Transformer 구조를 기반으로 하는 GPT 모델의 특성상 요약 작업에 있어서 이미 좋은 성능을 보이기 때문에 요약 성능을 위한 prompting 기법은 따로 필요하지 않다고 판단했다. 따라서 Role playing prompt 기법만 LLM-PaperSearcher

## 1. 개요
최근에는 매일 엄청난 양의 논문이 쏟아져 나오고 있다. 연구에 필요한 논문을 찾고, 이 논문이 연구 주제에 적합한지 읽어보고 선별하는 과정은 연구 과정에 있어서 비효율을 가져온다. 이에 사용자가 자유롭게 질문을 하면, 해당 질문에 부합하는 검색어를 만들어내 검색하고, 논문 내용의 제목과 저자, 요약과 링크 등을 제공하는 챗봇을 기획하게 되었다. 이 챗봇으로 논문에 대한 접근성을 향상시키고, 논문을 이용한 연구에 효율성을 더할 것을 기대한다.

## 2. 서비스 구조 
- main.py: 메인 실행 파일. 
- LLM.py: generateST(검색어 생성), SummarizePP(논문 요약) 등의 openAl API를 사용하는 함수가 들어있는 파일. 
- parser.py: searchPaper(논문 검색 및 스크롤) 등 웹 파싱에 관련된 파일. 
- prompts.py: CoT, Few shot, Role playing 등 Prompting 기법들을 모아놓은 파일. 

### 위 서비스는 다음과 같이 크게 3단계 구조로 나눌 수 있다. 
- (1) 사용자의 prompt를 입력 받아 arxiv 검색어를 생성해내는 부분(LLM 사용) 
    - prompt를 입력받고, pydantic의 BaseModel을 상속받는 클래스를 만들어 structured Outputs을 적용했다
    -  Terms: List[str] 형식으로 검색어를 3개 생성하게 했다.
    -  CoT prompt와 Few shot prompt를 이용하여 검색의 정확도를 높이고자 했다.
- (2) 생성한 검색어로 arxiv.com의 검색 링크를 생성하여 논문 제목, 저자, 링크, abstract을 스크롤하는 부분. 
    - 생성된 검색어를 이용해 링크를 생성한다.
    -  request와 beautifulSoup을 이용하여 링크에서 필요한 부분, 즉 논문 제목, 저자, 링크, abstract를 스크롤해온다.검색어 생성은 arxiv의 검색 링크 형식이 일정함을 이용하여 생성했다.
    -  크롤한 정보들은 Paper = dict{"Title", "Author”, “Link","Abstract”}의 형식으로 저장한다. 또한, 검색어 하나당 일정 개수(사용자 입력)의 논문 링크를 추출하여 같은 작업을 반복한다.
    -  결과적으로 List[Paper] 형식으로 정보를 저장한다. 
- (3) 사용자의 prompt와 논문 제목, abstract를 이용하여 논문의 요약을 생성하고, 올바르게 추천했는지 타당성 검사(LLM 사용) 
    - (1)에서 입력받은 prompt와 논문 Title, Abstract를 이용하여 논문에 대한 설명과 prompt와의 연관성, 그리고 추천의 적합도를 생성해낸다.
    - (1)과 동일하게 BaseModel을 상속받는 클래스를 만들어 structured Outputs을 적용했고 다음과 같은 형식으로 답변이 나오도록 했다: **{description: str; Relevance: float}**
    -  또한, 여기서는 abstract가 너무 많은 토큰을 차지하고, 방대해서 Cot prompt나 Few shot prompt로 처리하기에는 무리가 있었다. 그리고 Transformer 구조를 기반으로 하는 GPT 모델의 특성상 요약 작업에 있어서 이미 좋은 성능을 보이기 때문에 요약 성능을 위한 prompting 기법은 따로 필요하지 않다고 판단했다. 따라서 Role playing prompt 기법만 적용하여 상황에 더 적절한 논문 해석을 제공하도록 했다.
    -  
(1)~(3) 과정을 마친 뒤에는 논문 제목, 저자, 링크, 요약, 적합성 등을 정리해서 유저에게 제공한다.
