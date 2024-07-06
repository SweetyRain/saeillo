import requests
from bs4 import BeautifulSoup

url_list = ['https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?careerTo=&keywordJobCd=&occupation=&templateInfo=&shsyWorkSecd=&rot2WorkYn=&payGbn=&resultCnt=30&keywordJobCont=N&cert=&cloDateStdt=&moreCon=&minPay=&codeDepth2Info=11000&isChkLocCall=&sortFieldInfo=DATE&major=&resrDutyExcYn=&eodwYn=&sortField=DATE&staArea=&sortOrderBy=DESC&keyword=&termSearchGbn=all&carrEssYns=&benefitSrchAndOr=O&disableEmpHopeGbn=&webIsOut=&actServExcYn=&maxPay=&keywordStaAreaNm=N&emailApplyYn=&listCookieInfo=DTL&pageCode=&codeDepth1Info=11000&keywordEtcYn=&publDutyExcYn=&keywordJobCdSeqNo=&exJobsCd=&templateDepthNmInfo=&computerPreferential=&regDateStdt=&employGbn=&empTpGbcd=&region=&infaYn=&resultCntInfo=30&siteClcd=all&cloDateEndt=&sortOrderByInfo=DESC&currntPageNo=2&indArea=&careerTypes=&searchOn=Y&tlmgYn=&subEmpHopeYn=&academicGbn=&templateDepthNoInfo=&foriegn=&mealOfferClcd=&station=&moerButtonYn=Y&holidayGbn=&srcKeyword=&enterPriseGbn=all&academicGbnoEdu=noEdu&cloTermSearchGbn=all&keywordWantedTitle=N&stationNm=&benefitGbn=&keywordFlag=&notSrcKeyword=&essCertChk=&isEmptyHeader=&depth2SelCode=&_csrf=3d5649ca-a311-49e1-8aba-6ae9e9acbe85&keywordBusiNm=N&preferentialGbn=&rot3WorkYn=&pfMatterPreferential=B&regDateEndt=&staAreaLineInfo1=11000&staAreaLineInfo2=1&pageIndex=1&termContractMmcnt=&careerFrom=&laborHrShortYn=#viewSPL',
            'https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?careerTo=&keywordJobCd=&occupation=&templateInfo=&shsyWorkSecd=&rot2WorkYn=&payGbn=&resultCnt=30&keywordJobCont=N&cert=&cloDateStdt=&moreCon=&minPay=&codeDepth2Info=11000&isChkLocCall=&sortFieldInfo=DATE&major=&resrDutyExcYn=&eodwYn=&sortField=DATE&staArea=&sortOrderBy=DESC&keyword=&termSearchGbn=all&carrEssYns=&benefitSrchAndOr=O&disableEmpHopeGbn=&webIsOut=&actServExcYn=&maxPay=&keywordStaAreaNm=N&emailApplyYn=&listCookieInfo=DTL&pageCode=&codeDepth1Info=11000&keywordEtcYn=&publDutyExcYn=&keywordJobCdSeqNo=&exJobsCd=&templateDepthNmInfo=&computerPreferential=&regDateStdt=&employGbn=&empTpGbcd=&region=&infaYn=&resultCntInfo=30&siteClcd=all&cloDateEndt=&sortOrderByInfo=DESC&currntPageNo=1&indArea=&careerTypes=&searchOn=Y&tlmgYn=&subEmpHopeYn=&academicGbn=&templateDepthNoInfo=&foriegn=&mealOfferClcd=&station=&moerButtonYn=Y&holidayGbn=&srcKeyword=&enterPriseGbn=all&academicGbnoEdu=noEdu&cloTermSearchGbn=all&keywordWantedTitle=N&stationNm=&benefitGbn=&keywordFlag=&notSrcKeyword=&essCertChk=&isEmptyHeader=&depth2SelCode=&_csrf=3d5649ca-a311-49e1-8aba-6ae9e9acbe85&keywordBusiNm=N&preferentialGbn=&rot3WorkYn=&pfMatterPreferential=B&regDateEndt=&staAreaLineInfo1=11000&staAreaLineInfo2=1&pageIndex=2&termContractMmcnt=&careerFrom=&laborHrShortYn=#viewSPL',
            'https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?careerTo=&keywordJobCd=&occupation=&templateInfo=&shsyWorkSecd=&rot2WorkYn=&payGbn=&resultCnt=30&keywordJobCont=N&cert=&cloDateStdt=&moreCon=&minPay=&codeDepth2Info=11000&isChkLocCall=&sortFieldInfo=DATE&major=&resrDutyExcYn=&eodwYn=&sortField=DATE&staArea=&sortOrderBy=DESC&keyword=&termSearchGbn=all&carrEssYns=&benefitSrchAndOr=O&disableEmpHopeGbn=&webIsOut=&actServExcYn=&maxPay=&keywordStaAreaNm=N&emailApplyYn=&listCookieInfo=DTL&pageCode=&codeDepth1Info=11000&keywordEtcYn=&publDutyExcYn=&keywordJobCdSeqNo=&exJobsCd=&templateDepthNmInfo=&computerPreferential=&regDateStdt=&employGbn=&empTpGbcd=&region=&infaYn=&resultCntInfo=30&siteClcd=all&cloDateEndt=&sortOrderByInfo=DESC&currntPageNo=2&indArea=&careerTypes=&searchOn=Y&tlmgYn=&subEmpHopeYn=&academicGbn=&templateDepthNoInfo=&foriegn=&mealOfferClcd=&station=&moerButtonYn=Y&holidayGbn=&srcKeyword=&enterPriseGbn=all&academicGbnoEdu=noEdu&cloTermSearchGbn=all&keywordWantedTitle=N&stationNm=&benefitGbn=&keywordFlag=&notSrcKeyword=&essCertChk=&isEmptyHeader=&depth2SelCode=&_csrf=3d5649ca-a311-49e1-8aba-6ae9e9acbe85&keywordBusiNm=N&preferentialGbn=&rot3WorkYn=&pfMatterPreferential=B&regDateEndt=&staAreaLineInfo1=11000&staAreaLineInfo2=1&pageIndex=3&termContractMmcnt=&careerFrom=&laborHrShortYn=#viewSPL']

db = []

for url in url_list:
  response = requests.get(url)
  response.raise_for_status()

  soup = BeautifulSoup(response.text, "html.parser")

  divs = soup.find_all('div', class_='cp-info-in')
  deadlines = soup.select('tr> td:nth-child(5) > div > p:nth-child(2)')


  # 각 div 안에 있는 a 태그의 href와 텍스트 추출
  for i, (div, deadline) in enumerate(zip(divs, deadlines)):

    # 공고명, 카테고리, href 분류
    a_tag = div.find('a')

    if a_tag:
      # href를 워크넷 상세페이지에 맞는 형식으로 변경
      href = 'https://www.work.go.kr/' + a_tag.get('href')
      name = a_tag.get_text(strip=True)

      #카테고리 분류
      if "조리" in name:
        categorie = "조리"
      elif "요양" in name:
        categorie = "요양"
      elif "경비" in name or "보안" in name:
        categorie = "경비"
      else:
        categorie = "기타"

    dday_tag = deadline.find('span')

    # 마감일자 추가
    if dday_tag:
      # <span> 태그의 텍스트 추출
      date_text = dday_tag.get_text().strip()
      date_text = date_text[:-3]
      dday = date_text
    else:
      # span 태그 없을시 채용시까지 append
      dday = "채용시까지"

    # db에 공고명, 카테고리, 마감일자, 링크 순으로 삽입
    db.append([name, categorie, dday, href])

print(db)

soup = BeautifulSoup(response.text, "html.parser")

details = []

for i in range(len(db)):
    detail = []

    name = db[i][0]
    categorie = db[i][1]
    url = db[i][3]

    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    left_divs = soup.find('div', class_='left')
    info_divs = left_divs.find_all('div', class_='info')

    detail.append(name)
    detail.append(categorie)
    detail.append(url)

    if info_divs :
        for info_div in info_divs:
            spans = info_div .find_all('span')
            for span in spans:
                text = span.get_text(strip=True).replace('\n', '').replace('\r', '').replace('\t', '').replace(' ', '')
                if not text:
                    text = "none"
                detail.append(text)

    details.append(detail)

print(details)