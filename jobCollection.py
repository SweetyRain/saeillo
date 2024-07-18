import requests
import re
from bs4 import BeautifulSoup
from DB import input_db
import datetime
from datetime import timedelta
from exceptList import middle_except, top_except, administrative_district


# 지역 띄어쓰기 삽입
def city_district(address):
    parts = ["도", "시", "구", "로", "길"]

    if "대구" in address:
        region = address[:2] + " " + address[2:]
        return region

    for exception in middle_except:
        if exception in address:
            index = address.index(exception[0])
            region = address[:index] + " " + address[index:index + len(exception)] + " " + address[index + len(exception):]
            return region

    for part in parts:
        address = address.replace(part, part + " ")

    return address.strip()


def beautifulsoup(url):
    response = requests.get(url)
    response.raise_for_status()

    return BeautifulSoup(response.text, "html.parser")


def list_data(url):
    soup = beautifulsoup(url)
    divs = soup.find_all('div', class_='cp-info-in')
    deadlines = soup.select('tr> td:nth-child(5) > div > p:nth-child(2)')

    # 날짜 check용 div
    check_divs = soup.select('tr> td:nth-child(5) > div > p:nth-child(2)')

    return divs, deadlines, check_divs


def detail_data(url):
    soup = beautifulsoup(url)
    left_divs = soup.find('div', class_='left')
    
    #상세 공고 찾는 left_divs 찾지 못할 시 예외처리
    if left_divs is not None:
        info_divs = left_divs.find_all('div', class_='info')
        return info_divs
    else:
        info_divs = False
        return info_divs


# 자정 크롤링 시 등록일이 전날인 경우에만 크롤링 하는 함수
def registration_date_check(check_div):
    now = datetime.datetime.now()

    yesterday = datetime.datetime.now() - timedelta(days=1)
    yesterday = int(yesterday.strftime('%Y%m%d'))

    check = False

    registration_text = check_div.get_text(strip=True)[0:8]
    numbers = re.sub(r'[^0-9]', '', registration_text)
    startline = int("20" + numbers)

    registration_date = int(check_div.get_text(strip=True)[6:8])
    check = yesterday == registration_date
    return check, startline


def parse_data(div, deadline, check_div):
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
        elif "미화" in name:
            categorie = "미화"
        else:
            categorie = "기타"

    # 마감일자 추가
    dday_tag = deadline.find('span')

    if dday_tag:
        # <span> 태그의 텍스트 추출
        date_text = dday_tag.get_text().strip()
        date_text = date_text[:-3]
        numbers = re.sub(r'[^0-9]', '', date_text)
        dday = int("20" + numbers)
    else:
        # span 태그 없을시 채용시까지 append
        dday = 30000000

    # name, categorie, dday, href 리턴
    return name, href, categorie, dday


def get_detail_data(info_divs):
    detail = []
    if info_divs == None:
        return None

    if info_divs:
        # 경력, 학력, 지역, 급여, 고용 형태, 근무 형태, 복리후생 순으로 추출
        # 각각 detail 리스트의 0번 인덱스부터 차례로 append
        for info_div in info_divs:
            spans = info_div.find_all('span')
            for span in spans:
                text = span.get_text(strip=True).replace('\n', '').replace('\r', '').replace('\t', '').replace(' ', '')
                if not text:
                    text = False
                if "font-pink" in span.get('class', []):
                    continue
                detail.append(text)
        # detail의 길이가 7보다 작으면 복리후생이 없는 경우이므로 "없음" append
        if len(detail) < 7:
            detail.append("없음")

    return detail


def insert_data():
    url_list = [
        'https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?careerTo=&keywordJobCd=&occupation=&templateInfo=&shsyWorkSecd=&rot2WorkYn=&payGbn=&resultCnt=50&keywordJobCont=N&cert=&cloDateStdt=&moreCon=&minPay=&codeDepth2Info=11000&isChkLocCall=&sortFieldInfo=DATE&major=&resrDutyExcYn=&eodwYn=&sortField=DATE&staArea=&sortOrderBy=DESC&keyword=&termSearchGbn=all&carrEssYns=&benefitSrchAndOr=O&disableEmpHopeGbn=&webIsOut=&actServExcYn=&maxPay=&keywordStaAreaNm=N&emailApplyYn=&listCookieInfo=DTL&pageCode=&codeDepth1Info=11000&keywordEtcYn=&publDutyExcYn=&keywordJobCdSeqNo=&exJobsCd=&templateDepthNmInfo=&computerPreferential=&regDateStdt=&employGbn=&empTpGbcd=&region=&infaYn=&resultCntInfo=50&siteClcd=all&cloDateEndt=&sortOrderByInfo=DESC&currntPageNo=8&indArea=&careerTypes=&searchOn=Y&tlmgYn=&subEmpHopeYn=&academicGbn=&templateDepthNoInfo=&foriegn=&mealOfferClcd=&station=&moerButtonYn=Y&holidayGbn=&srcKeyword=&enterPriseGbn=all&academicGbnoEdu=noEdu&cloTermSearchGbn=all&keywordWantedTitle=N&stationNm=&benefitGbn=&keywordFlag=&notSrcKeyword=&essCertChk=&isEmptyHeader=&depth2SelCode=&_csrf=e2b6ac54-5a4d-4535-a89d-7fecc6e9ca7d&keywordBusiNm=N&preferentialGbn=&rot3WorkYn=&pfMatterPreferential=B&regDateEndt=&staAreaLineInfo1=11000&staAreaLineInfo2=1&pageIndex=1&termContractMmcnt=&careerFrom=&laborHrShortYn=#viewSPL',
        'https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?careerTo=&keywordJobCd=&occupation=&templateInfo=&shsyWorkSecd=&rot2WorkYn=&payGbn=&resultCnt=50&keywordJobCont=N&cert=&cloDateStdt=&moreCon=&minPay=&codeDepth2Info=11000&isChkLocCall=&sortFieldInfo=DATE&major=&resrDutyExcYn=&eodwYn=&sortField=DATE&staArea=&sortOrderBy=DESC&keyword=&termSearchGbn=all&carrEssYns=&benefitSrchAndOr=O&disableEmpHopeGbn=&webIsOut=&actServExcYn=&maxPay=&keywordStaAreaNm=N&emailApplyYn=&listCookieInfo=DTL&pageCode=&codeDepth1Info=11000&keywordEtcYn=&publDutyExcYn=&keywordJobCdSeqNo=&exJobsCd=&templateDepthNmInfo=&computerPreferential=&regDateStdt=&employGbn=&empTpGbcd=&region=&infaYn=&resultCntInfo=50&siteClcd=all&cloDateEndt=&sortOrderByInfo=DESC&currntPageNo=1&indArea=&careerTypes=&searchOn=Y&tlmgYn=&subEmpHopeYn=&academicGbn=&templateDepthNoInfo=&foriegn=&mealOfferClcd=&station=&moerButtonYn=Y&holidayGbn=&srcKeyword=&enterPriseGbn=all&academicGbnoEdu=noEdu&cloTermSearchGbn=all&keywordWantedTitle=N&stationNm=&benefitGbn=&keywordFlag=&notSrcKeyword=&essCertChk=&isEmptyHeader=&depth2SelCode=&_csrf=e2b6ac54-5a4d-4535-a89d-7fecc6e9ca7d&keywordBusiNm=N&preferentialGbn=&rot3WorkYn=&pfMatterPreferential=B&regDateEndt=&staAreaLineInfo1=11000&staAreaLineInfo2=1&pageIndex=2&termContractMmcnt=&careerFrom=&laborHrShortYn=#viewSPL',
        'https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?careerTo=&keywordJobCd=&occupation=&templateInfo=&shsyWorkSecd=&rot2WorkYn=&payGbn=&resultCnt=50&keywordJobCont=N&cert=&cloDateStdt=&moreCon=&minPay=&codeDepth2Info=11000&isChkLocCall=&sortFieldInfo=DATE&major=&resrDutyExcYn=&eodwYn=&sortField=DATE&staArea=&sortOrderBy=DESC&keyword=&termSearchGbn=all&carrEssYns=&benefitSrchAndOr=O&disableEmpHopeGbn=&webIsOut=&actServExcYn=&maxPay=&keywordStaAreaNm=N&emailApplyYn=&listCookieInfo=DTL&pageCode=&codeDepth1Info=11000&keywordEtcYn=&publDutyExcYn=&keywordJobCdSeqNo=&exJobsCd=&templateDepthNmInfo=&computerPreferential=&regDateStdt=&employGbn=&empTpGbcd=&region=&infaYn=&resultCntInfo=50&siteClcd=all&cloDateEndt=&sortOrderByInfo=DESC&currntPageNo=2&indArea=&careerTypes=&searchOn=Y&tlmgYn=&subEmpHopeYn=&academicGbn=&templateDepthNoInfo=&foriegn=&mealOfferClcd=&station=&moerButtonYn=Y&holidayGbn=&srcKeyword=&enterPriseGbn=all&academicGbnoEdu=noEdu&cloTermSearchGbn=all&keywordWantedTitle=N&stationNm=&benefitGbn=&keywordFlag=&notSrcKeyword=&essCertChk=&isEmptyHeader=&depth2SelCode=&_csrf=e2b6ac54-5a4d-4535-a89d-7fecc6e9ca7d&keywordBusiNm=N&preferentialGbn=&rot3WorkYn=&pfMatterPreferential=B&regDateEndt=&staAreaLineInfo1=11000&staAreaLineInfo2=1&pageIndex=3&termContractMmcnt=&careerFrom=&laborHrShortYn=#viewSPL',
        'https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?careerTo=&keywordJobCd=&occupation=&templateInfo=&shsyWorkSecd=&rot2WorkYn=&payGbn=&resultCnt=50&keywordJobCont=N&cert=&cloDateStdt=&moreCon=&minPay=&codeDepth2Info=11000&isChkLocCall=&sortFieldInfo=DATE&major=&resrDutyExcYn=&eodwYn=&sortField=DATE&staArea=&sortOrderBy=DESC&keyword=&termSearchGbn=all&carrEssYns=&benefitSrchAndOr=O&disableEmpHopeGbn=&webIsOut=&actServExcYn=&maxPay=&keywordStaAreaNm=N&emailApplyYn=&listCookieInfo=DTL&pageCode=&codeDepth1Info=11000&keywordEtcYn=&publDutyExcYn=&keywordJobCdSeqNo=&exJobsCd=&templateDepthNmInfo=&computerPreferential=&regDateStdt=&employGbn=&empTpGbcd=&region=&infaYn=&resultCntInfo=50&siteClcd=all&cloDateEndt=&sortOrderByInfo=DESC&currntPageNo=3&indArea=&careerTypes=&searchOn=Y&tlmgYn=&subEmpHopeYn=&academicGbn=&templateDepthNoInfo=&foriegn=&mealOfferClcd=&station=&moerButtonYn=Y&holidayGbn=&srcKeyword=&enterPriseGbn=all&academicGbnoEdu=noEdu&cloTermSearchGbn=all&keywordWantedTitle=N&stationNm=&benefitGbn=&keywordFlag=&notSrcKeyword=&essCertChk=&isEmptyHeader=&depth2SelCode=&_csrf=e2b6ac54-5a4d-4535-a89d-7fecc6e9ca7d&keywordBusiNm=N&preferentialGbn=&rot3WorkYn=&pfMatterPreferential=B&regDateEndt=&staAreaLineInfo1=11000&staAreaLineInfo2=1&pageIndex=4&termContractMmcnt=&careerFrom=&laborHrShortYn=#viewSPL',
        'https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?careerTo=&keywordJobCd=&occupation=&templateInfo=&shsyWorkSecd=&rot2WorkYn=&payGbn=&resultCnt=50&keywordJobCont=N&cert=&cloDateStdt=&moreCon=&minPay=&codeDepth2Info=11000&isChkLocCall=&sortFieldInfo=DATE&major=&resrDutyExcYn=&eodwYn=&sortField=DATE&staArea=&sortOrderBy=DESC&keyword=&termSearchGbn=all&carrEssYns=&benefitSrchAndOr=O&disableEmpHopeGbn=&webIsOut=&actServExcYn=&maxPay=&keywordStaAreaNm=N&emailApplyYn=&listCookieInfo=DTL&pageCode=&codeDepth1Info=11000&keywordEtcYn=&publDutyExcYn=&keywordJobCdSeqNo=&exJobsCd=&templateDepthNmInfo=&computerPreferential=&regDateStdt=&employGbn=&empTpGbcd=&region=&infaYn=&resultCntInfo=50&siteClcd=all&cloDateEndt=&sortOrderByInfo=DESC&currntPageNo=4&indArea=&careerTypes=&searchOn=Y&tlmgYn=&subEmpHopeYn=&academicGbn=&templateDepthNoInfo=&foriegn=&mealOfferClcd=&station=&moerButtonYn=Y&holidayGbn=&srcKeyword=&enterPriseGbn=all&academicGbnoEdu=noEdu&cloTermSearchGbn=all&keywordWantedTitle=N&stationNm=&benefitGbn=&keywordFlag=&notSrcKeyword=&essCertChk=&isEmptyHeader=&depth2SelCode=&_csrf=e2b6ac54-5a4d-4535-a89d-7fecc6e9ca7d&keywordBusiNm=N&preferentialGbn=&rot3WorkYn=&pfMatterPreferential=B&regDateEndt=&staAreaLineInfo1=11000&staAreaLineInfo2=1&pageIndex=5&termContractMmcnt=&careerFrom=&laborHrShortYn=#viewSPL',
        'https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?careerTo=&keywordJobCd=&occupation=&templateInfo=&shsyWorkSecd=&rot2WorkYn=&payGbn=&resultCnt=50&keywordJobCont=N&cert=&cloDateStdt=&moreCon=&minPay=&codeDepth2Info=11000&isChkLocCall=&sortFieldInfo=DATE&major=&resrDutyExcYn=&eodwYn=&sortField=DATE&staArea=&sortOrderBy=DESC&keyword=&termSearchGbn=all&carrEssYns=&benefitSrchAndOr=O&disableEmpHopeGbn=&webIsOut=&actServExcYn=&maxPay=&keywordStaAreaNm=N&emailApplyYn=&listCookieInfo=DTL&pageCode=&codeDepth1Info=11000&keywordEtcYn=&publDutyExcYn=&keywordJobCdSeqNo=&exJobsCd=&templateDepthNmInfo=&computerPreferential=&regDateStdt=&employGbn=&empTpGbcd=&region=&infaYn=&resultCntInfo=50&siteClcd=all&cloDateEndt=&sortOrderByInfo=DESC&currntPageNo=5&indArea=&careerTypes=&searchOn=Y&tlmgYn=&subEmpHopeYn=&academicGbn=&templateDepthNoInfo=&foriegn=&mealOfferClcd=&station=&moerButtonYn=Y&holidayGbn=&srcKeyword=&enterPriseGbn=all&academicGbnoEdu=noEdu&cloTermSearchGbn=all&keywordWantedTitle=N&stationNm=&benefitGbn=&keywordFlag=&notSrcKeyword=&essCertChk=&isEmptyHeader=&depth2SelCode=&_csrf=e2b6ac54-5a4d-4535-a89d-7fecc6e9ca7d&keywordBusiNm=N&preferentialGbn=&rot3WorkYn=&pfMatterPreferential=B&regDateEndt=&staAreaLineInfo1=11000&staAreaLineInfo2=1&pageIndex=6&termContractMmcnt=&careerFrom=&laborHrShortYn=#viewSPL',
        'https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?careerTo=&keywordJobCd=&occupation=&templateInfo=&shsyWorkSecd=&rot2WorkYn=&payGbn=&resultCnt=50&keywordJobCont=N&cert=&cloDateStdt=&moreCon=&minPay=&codeDepth2Info=11000&isChkLocCall=&sortFieldInfo=DATE&major=&resrDutyExcYn=&eodwYn=&sortField=DATE&staArea=&sortOrderBy=DESC&keyword=&termSearchGbn=all&carrEssYns=&benefitSrchAndOr=O&disableEmpHopeGbn=&webIsOut=&actServExcYn=&maxPay=&keywordStaAreaNm=N&emailApplyYn=&listCookieInfo=DTL&pageCode=&codeDepth1Info=11000&keywordEtcYn=&publDutyExcYn=&keywordJobCdSeqNo=&exJobsCd=&templateDepthNmInfo=&computerPreferential=&regDateStdt=&employGbn=&empTpGbcd=&region=&infaYn=&resultCntInfo=50&siteClcd=all&cloDateEndt=&sortOrderByInfo=DESC&currntPageNo=6&indArea=&careerTypes=&searchOn=Y&tlmgYn=&subEmpHopeYn=&academicGbn=&templateDepthNoInfo=&foriegn=&mealOfferClcd=&station=&moerButtonYn=Y&holidayGbn=&srcKeyword=&enterPriseGbn=all&academicGbnoEdu=noEdu&cloTermSearchGbn=all&keywordWantedTitle=N&stationNm=&benefitGbn=&keywordFlag=&notSrcKeyword=&essCertChk=&isEmptyHeader=&depth2SelCode=&_csrf=e2b6ac54-5a4d-4535-a89d-7fecc6e9ca7d&keywordBusiNm=N&preferentialGbn=&rot3WorkYn=&pfMatterPreferential=B&regDateEndt=&staAreaLineInfo1=11000&staAreaLineInfo2=1&pageIndex=7&termContractMmcnt=&careerFrom=&laborHrShortYn=#viewSPL'
        ]
    for url in url_list:

        # jobData 딕셔너리 형태로 데이터 저장
        jobData = {}
        divs, deadlines, check_divs = list_data(url)
        for div, deadline, check_div in zip(divs, deadlines, check_divs):

            # 등록일이 어제인 데이터만 크롤링
            check, startline = registration_date_check(check_div)
            # if date_check == False:
            #     continue

            name, href, categorie, dday = parse_data(div, deadline, check_div)
            if href:
                info_divs = detail_data(href)
                if info_divs == None:
                    print(name)
                    continue
                else:
                    detail = get_detail_data(info_divs)

            jobData["name"] = name
            jobData["href"] = href
            jobData["categorie"] = categorie

            # detail[0]: 관계없음
            # detail[1]: 학력무관
            # detail[2]: 서울특별시중랑구망우로262
            # detail[3]: 시급13,000원 / 월급227만원이상 / 연봉2,600만원
            # detail[4]: 기간의정함이없는근로계약
            # detail[5]: '주5일근무(주소정근로시간:40시간)'
            # detail[6]: 복지 / 기본 = "없음"

            if False in detail:
                continue

            jobData["fullregion"] = detail[2]

            # 괄호 전 지역만 추출
            if "(" in detail[2]:
                # 괄호가 들어간 위치를 찾아 그 위치 전까지만 추출
                index = detail[2].find("(")
                region = detail[2][:index]
            else:
                region = detail[2]

            for ad in administrative_district:
                if ad in region:
                    region = region.replace(ad, " ").strip()

            exception_handled = False # 지역 예외 처리 여부 표시

            # 지역 요약을 위한 예외 처리
            for exception in middle_except:
                if exception in region:
                    index = region.find(exception)
                    region = region[:index + len(exception)]
                    jobData["region"] = city_district(region)
                    exception_handled = True
                    break

            if not exception_handled:
                if "구" in region:
                    index = region.find("구")
                    region = region[:index + 1]
                    jobData["region"] = city_district(region)
                elif "로" in region:
                    index = region.find("로")
                    region = region[:index + 1]
                    jobData["region"] = city_district(region)
                elif "군" in region:
                    index = region.find("군")
                    region = region[:index + 1]
                    jobData["region"] = city_district(region)
                elif "면" in region:
                    index = region.find("면")
                    region = region[:index + 1]
                    jobData["region"] = city_district(region)

            jobData["startday"] = startline
            jobData["dday"] = dday
            jobData["career"] = detail[0]
            jobData["Education"] = detail[1]

            # pay
            if "월급" in detail[3]:
                jobData["pay"] = int(re.sub(r'[^0-9]', '', detail[3][:9]) + "0000")

            elif "연봉" in detail[3]:
                jobData["pay"] = int(re.sub(r'[^0-9]', '', detail[3][:8]) + "0000") // 12

            # 시급으로 표기된 경우
            else:
                # 급여에서 숫자만 추출(ex) 13,500원인 경우 13500만 추출)
                hourlyRate = re.sub(r'[^0-9]', '', detail[3][2:9])
                # 근무 형태에서 주소정근로시간 추출
                workweek = detail[5][1]
                if workweek == '':
                    workweek = 1
                jobData["pay"] = 4 * int(workweek) * int(hourlyRate)

            jobData["employmentType"] = detail[4][:12]
            jobData["workType"] = int(detail[5][1])
            jobData["welfare"] = detail[6]

            # print(jobData)
            # break
            # DB.py 내 jobData 함수를 이용하여 mysql에 데이터 적재
            input_db(jobData)


if __name__ == "__main__":
    insert_data()