7월 1일 mainpage 생성 및 flask 적용

7월 5일 카테고리 추천 페이지 생성(1차 설계) 및 메인 페이지 색상 수정
        사이트 이름 수정

7울 6일 크롤링 기능 추가(1차 설계) 및 mysql 연동

7월 7일 카테고리 추천 사이드 바 생성, 몇몇 요소 크기 조정 및 글씨 크기 수정, 레이아웃 변경
        메인과 카테고리 추천 페이지 홈 버튼 삭제(새일로 버튼과 유사한 기능을 가지고 있어서 삭제) 

7월 8일 crolling 리팩토링 & mysql내 데이터 삽입 완료, schedule 구현 완료

7월 9일 css 몇가지 복구, 사이드바 삭제, 위에 nav바로 이동, 맞춤 추천 -고용 형태 버튼 생성, 지역 추천 창 생성, 카테고리 추천 창 레이아웃 변경

7월 13일 def registration_date_check 함수 추가

7월 15일 def delete_db(마감날짜 지남 혹은 공고 올라온지 6개월 지난 데이터 삭제) 함수 추가

7월 15일 전체 일자리 창 추가

7월 15일 전체 일자리 페이지 DB 연동 완료

7월 16일 카테고리 창 수정, css 추가

7월 16일 지역창 지역 선택 버튼 구현, css 추가, 지역창 선택 js 작성

7월 16일 페이징 작업, full 성공, category 미완성

7월 16일 js 작성 및 아래 참고

        -카테고리 창-
        카테고리 미화 추가
        카테고리 > 유형별 일자리 추천으로 변경
        인덱스 삭제, 넓이 줄이기
        근무조건 삭제 => 근무일수 & 월급 (td, <p>{{row.job_employmentType}}</p>,<p>{{row.job_pay}}</p> 부분 수정)
        하이퍼 링크 nav bar 공지사항, 고용 도움 프로그램 소개 제외 모두 달았음. 새일로 포함
        지역, 근무조건, 마감일 간격 넓히기는 데이터 들어간거 보고 내일 조정 예정

        -메인 창 -
        하이퍼 링크 달았음(공지사항, 고용 도움 프로그램 소개 칸 제외, 맨 위 새일로 포함)
        카테고리 > 유형별 일자리 추천으로 변경
        각 칸 색상 변경

        -전체 창(full)-
        하이퍼 링크 nav bar 공지사항, 고용 도움 프로그램 소개 제외 모두 달았음. 새일로 포함
        지역, 근무조건, 마감일 간격 넓히기는 데이터 들어간거 보고 내일 조정 예정
        근무조건 삭제 => 근무일수 & 월급 (td, <p>{{row.job_employmentType}}</p>,<p>{{row.job_pay}}</p> 부분 수정)
        중복 아이디 삭제

        -맞춤 추천 창-
        자바 스크립트 링크 코드 작성
        중복 아이디 삭제
        하이퍼 링크 nav bar 공지사항, 고용 도움 프로그램 소개 제외 모두 달았음. 새일로 포함
        지역, 근무조건, 마감일 간격 넓히기는 데이터 들어간거 보고 내일 조정 예정
        고용 형태 체크박스 css 수정, 희망임금 체크 박스 생성 및 css 생성
        근무조건 삭제 => 근무일수 & 월급 (td부분)

        -지역 추천 창-
        중복 아이디 삭제
        하이퍼 링크 nav bar 공지사항, 고용 도움 프로그램 소개 제외 모두 달았음. 새일로 포함
        지역, 근무조건, 마감일 간격 넓히기는 데이터 들어간거 보고 내일 조정 예정
        근무조건 삭제 => 근무일수 & 월급 (td부분)
        지역 선택 박스 생성 완료, 시에 따라 구,군 체크박스 생성하는 자바 스크립트 작성 완료, 이에 대한 css 생성
        지역 선택 1개씩만 가능하게 하는 자바 스크립트 작성
        지역창 구,군 버튼 정렬 수정
        *****근데 자바 스크립트 연결이 안됨. 이는 추후 수정 예정

7월 17일 전체적인 색상 변경, 최소 크기 조정으로 깨지는 현상 수정, js 연동, 비율 수정
        main 화면 카드 위에 커서 올렸을 때 사용되는 커서 모양 수정
        지역 선택 창 밑에 밑줄 제거, 지역 선택 구,군 선택 박스 크기, 정렬 방법, 클릭했을 때 색상 수정
        맞춤 추천 창에 제출, 초기화 버튼 생성 (제출 버튼 기능 구현)

7월 18일 테두리 색 변경, 상세 페이지 구현
        상세 페이지 레이아웃 변경, 자세히 버튼 생성
        공지 페이지 추가, 공지 게시글 작성 페이지 생성

7월 19일 디테일 페이지 연결 및 공지 페이지 생성
        메인 최종 수정 완료
        카테고리 최종 수정 완료
