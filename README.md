# book_tracking
## 예스24와 알라딘의 판매지수는 믿을 수 있을까?

### 현재까지 찾은 사실: 대중서는 확실하게 맞다.
* 예1: <빈곤의 연대기> 박선미 외, 사실 지도교수님의 저서라 얼마난 팔렸는지 알 수 있었습니다. 지수는 0.8:1 로 보입니다. (알라딘:실판매권수)
* 예2: 윤구병 선생님의 저서들(천년의 상상) 소위 '저자'빨이 먹히는 듯 합니다.
* 예3: <평행 우주 속의 소녀>, <하트마크> (도서출판 이새) 제가 관계된 회사 입니다. 얼추 맞아 떨어집니다.

### 현재까지 찾은 안맞는 사실: 출판사의 판매 전략
* 출판사는 2쇄, 3쇄를 털어내고 안찍을 수도 있습니다. <1960을 묻다> 와 <1970 박정희와 모더니즘>은 앞의 책이 세일즈 포인트가 낮지만 오히려 수익을 봤다고 합니다. 이유는 앞책이 대중서라고 하기에는 난이도가 높은데다 중요한 자료들이 많아서 대학원에서 많이 교재로 썼다는 군요.
* 출판사는 도서 정가제 이후 가격에 엄청 민감해졌습니다. 예전처럼 책을 철판하지 않겠다고 하는 출판사도 많이 줄어들었구요. 이런 면들을 보면 세일즈 포인트라는 일면은 참 믿기 힘들어지기도 합니다.

### 그래도 믿을 구석은 세일즈 포인트
* 현재 그래도 독자, 소비자의 입장에서 책이 얼마나 팔렸냐를 예측, 분석해 보려면 쓰일 자료가 예스24와 알라딘에서 제공하는 판매지수 뿐인 듯 합니다. 

### 분석 방법은
* 캐낼 수 있는 판매 자료를 입수할 수 있다면 세일즈 포인트를 꾸준히 기록해서 판매량, 가격 등을 이용해서 기계학습을 시켜야 분석이 가능해 보입니다.
* 안타깝게 제가 입수 할 수 있는 정확한 판매 부수 자료는 Training Set으로 쓰기에 너무 역부족이네요.

### 자료 입수는
* 신규 도서가 나오고 매일매일 체크 되어야 합니다. 출판사 측에서는 매일 주문량을 보고 해줘야 하는데 초도 물량은 확인이 어려울 듯 합니다.
* 출판사로 들어오는 신규 주문과 판매지수의 변화를 측정해야 하는데 까딱하다 책이 안팔리게 되면 모델이 데이터를 학습하기 어렵습니다. 쉽지 않은 작업 같군요.
