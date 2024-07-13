import requests
import re
from bs4 import BeautifulSoup
from DB import input_db
from datetime import date

def beatifulsoup(url):
    response = requests.get(url)
    response.raise_for_status()

    return BeautifulSoup(response.text, "html.parser")

def list_data(url):
    soup = beatifulsoup(url)
    divs = soup.find_all('div', class_='cp-info-in')
    deadlines = soup.select('tr> td:nth-child(5) > div > p:nth-child(2)')

    return divs, deadlines

def detail_data(url):
    soup = beatifulsoup(url)
    left_divs = soup.find('div', class_='left')
    info_divs = left_divs.find_all('div', class_='info')

    return info_divs

def registration_date_check(div):
    p = div.find('p')
    if "dday mt10" not in p.get('class', []):
        registration_date = p.get_text(strip=True)
        today = str(date.today())[-2:]
        check = today == registration_date

    return check

def parse_data(div, deadline):
    a_tag = div.find('a')

    if a_tag:
        # href를 워크넷 상세페이지에 맞는 형식으로 변경
        href = 'https://www.work.go.kr/' + a_tag.get('href')
        name = a_tag.get_text(strip=True)

        # 카테고리 분류
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
        numbers = re.sub(r'[^0-9]', '', date_text)
        dday = int("20" + numbers)
    else:
        # span 태그 없을시 채용시까지 append
        dday = -1

    # name, categorie, dday, href 리턴
    return name, href, categorie, dday
def get_detail_data(info_divs):
    detail = []
    if info_divs:
        # 경력, 학력, 지역, 급여, 고용 형태, 근무 형태, 복리후생 순으로 추출
        # 각각 detail 리스트의 0번 인덱스부터 차례로 append
        for info_div in info_divs:
            spans = info_div.find_all('span')
            for span in spans:
                text = span.get_text(strip=True).replace('\n', '').replace('\r', '').replace('\t', '').replace(' ', '')
                if not text:
                    text = "none"
                if "font-pink" in span.get('class', []):
                    continue
                detail.append(text)
        # detail의 길이가 7보다 작으면 복리후생이 없는 경우이므로 "없음" append
        if len(detail) < 7:
            detail.append("없음")

    return detail

def insert_data():

    url_list = ['https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?careerTo=&keywordJobCd=&occupation=&templateInfo=&shsyWorkSecd=&rot2WorkYn=&payGbn=&resultCnt=30&keywordJobCont=N&cert=&cloDateStdt=&moreCon=&minPay=&codeDepth2Info=11000&isChkLocCall=&sortFieldInfo=DATE&major=&resrDutyExcYn=&eodwYn=&sortField=DATE&staArea=&sortOrderBy=DESC&keyword=&termSearchGbn=all&carrEssYns=&benefitSrchAndOr=O&disableEmpHopeGbn=&webIsOut=&actServExcYn=&maxPay=&keywordStaAreaNm=N&emailApplyYn=&listCookieInfo=DTL&pageCode=&codeDepth1Info=11000&keywordEtcYn=&publDutyExcYn=&keywordJobCdSeqNo=&exJobsCd=&templateDepthNmInfo=&computerPreferential=&regDateStdt=&employGbn=&empTpGbcd=&region=&infaYn=&resultCntInfo=30&siteClcd=all&cloDateEndt=&sortOrderByInfo=DESC&currntPageNo=2&indArea=&careerTypes=&searchOn=Y&tlmgYn=&subEmpHopeYn=&academicGbn=&templateDepthNoInfo=&foriegn=&mealOfferClcd=&station=&moerButtonYn=Y&holidayGbn=&srcKeyword=&enterPriseGbn=all&academicGbnoEdu=noEdu&cloTermSearchGbn=all&keywordWantedTitle=N&stationNm=&benefitGbn=&keywordFlag=&notSrcKeyword=&essCertChk=&isEmptyHeader=&depth2SelCode=&_csrf=3d5649ca-a311-49e1-8aba-6ae9e9acbe85&keywordBusiNm=N&preferentialGbn=&rot3WorkYn=&pfMatterPreferential=B&regDateEndt=&staAreaLineInfo1=11000&staAreaLineInfo2=1&pageIndex=1&termContractMmcnt=&careerFrom=&laborHrShortYn=#viewSPL']
    for url in url_list:

        #jobData 딕셔너리 형태로 데이터 저장
        jobData = {}
        divs, deadlines = list_data(url)
        for div, deadline in zip(divs, deadlines):
            date_check = registration_date_check(div)
            if date_check == "false":
                continue

            name, href, categorie, dday = parse_data(div, deadline)
            if href:
                info_divs = detail_data(href)
                detail = get_detail_data(info_divs)
            jobData["name"] = name
            jobData["href"] = href
            jobData["categorie"] = categorie

            #괄호 전 지역만 추출
            if "(" in detail[2]:
                index = detail[2].find("(")
                region = detail[2][:index]
            else: region = detail[2]

            #지역 요약을 위한 예외 처리
            if "구로구" in region:
                index = region.find("구")
                jobData["region"] = region[:index + 3]
            elif "구" in region:
                index = region.find("구")
                jobData["region"] = region[:index+1]
            elif "로" in region:
                index = region.find("로")
                jobData["region"] = region[:index+1]
            elif "군" in region:
                index = region.find("군")
                jobData["region"] = region[:index + 1]

            jobData["dday"] = dday
            jobData["career"] = detail[0]
            jobData["Education"] = detail[1]

            # 월급으로 형태 변경
            if "월급" in detail[3]:
                jobData["pay"] = int(detail[3][2:5] + "0000")

            # 시급으로 표기된 경우
            else:
                # 급여에서 숫자만 추출(ex) 13,500원인 경우 13500만 추출)
                hourlyRate = re.sub(r'[^0-9]', '', detail[3][2:9])
                # 근무 형태에서 주소정근로시간 추출
                workweek = re.sub(r'[^0-9]', '', detail[5][-5:])
                jobData["pay"] = 4 * int(workweek) * int(hourlyRate)

            jobData["employmentType"] = detail[4][:12]
            jobData["workType"] = detail[5][:5]
            jobData["welfare"] = detail[6]

            #DB.py 내 jobData 함수를 이용하여 mysql에 데이터 적재
            input_db(jobData)

if __name__ == "__main__":
    insert_data()