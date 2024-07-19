//지역 보여주기
var cat1_num = new Array(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17);
var cat1_name = new Array('서울','부산','대구','인천','광주','대전','울산','세종','경기','충북','충남','전남','경북','경남','제주','강원','전북');

var cat2_num = new Array();
var cat2_name = new Array();

cat2_num[1] = new Array(18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42);
cat2_name[1] = new Array('서울 강남구','서울 강동구','서울 강북구','서울 강서구','서울 관악구','서울 광진구','서울 구로구','서울 금천구','서울 노원구','서울 도봉구','서울 동대문구','서울 동작구','서울 마포구','서울 서대문구','서울 서초구','서울 성동구','서울 성북구','서울 송파구','서울 양천구','서울 영등포구','서울 용산구','서울 은평구','서울 종로구','서울 중구','서울 중랑구');

cat2_num[2] = new Array(43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58);
cat2_name[2] = new Array('부산 강서구','부산 금정구','부산 기장군','부산 남구','부산 동구','부산 동래구','부산 부산진구','부산 북구','부산 사상구','부산 사하구','부산 서구','부산 수영구','부산 연제구','부산 영도구','부산 중구','부산 해운대구');

cat2_num[3] = new Array(59,60,61,62,63,64,65,66);
cat2_name[3] = new Array('대구 군위군','대구 남구','대구 달서구','대구 달성군','대구 동구','대구 북구','대구 서구','대구 수성구','대구 중구');

cat2_num[4] = new Array(67,68,69,70,71,72,73,74,75,76);
cat2_name[4] = new Array('인천 강화군','인천 계양구','인천 남동구','인천 동구','인천 남구','인천 미추홀구','인천 부평구','인천 서구','인천 연수구','인천 옹진군','인천 중구');

cat2_num[5] = new Array(77,78,79,80,81);
cat2_name[5] = new Array('광주 광산구','광주 남구','광주 동구','광주 북구','광주 서구');

cat2_num[6] = new Array(82,83,84,85,86);
cat2_name[6] = new Array('대전 대덕구','대전 동구','대전 서구','대전 유성구','대전 중구');

cat2_num[7] = new Array(87,88,89,90,91);
cat2_name[7] = new Array('울산 남구','울산 동구','울산 북구','울산 울주군','울산 중구');

cat2_num[8] = new Array(92);
cat2_name[8] = new Array('세종');

cat2_num[9] = new Array(93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143);
cat2_name[9] = new Array('경기 가평군','경기 고양시','경기 고양시 덕양구','경기 고양시 일산동구','경기 고양시 일산서구','경기 과천시','경기 광명시','경기 광주시','경기 구리시','경기 군포시','경기 김포시','경기 남양주시','경기 동두천시','경기 부천시','경기 부천시 소사구','경기 부천시 오정구','경기 부천시 원미구','경기 성남시','경기 성남시 분당구','경기 성남시 수정구','경기 성남시 중원구','경기 수원시','경기 수원시 권선구','경기 수원시 장안구','경기 수원시 영통구','경기 수원시 장안구','경기 수원시 팔달구','경기 시흥시','경기 안산시','경기 안산시 단원구','경기 안산시 상록구','경기 안성시','경기 안양시','경기 안양시 동안구','경기 안양시 만안구','경기 양주시','경기 양평군','경기 여주시','경기 연천군','경기 오산시','경기 용인시','경기 용인시 기흥구','경기 용인시 수지구','경기 용인시 처인구','경기 의왕시','경기 의정부시','경기 이천시','경기 파주시','경기 평택시','경기 포천시','경기 하남시','경기 화성시');

cat2_num[10] = new Array(144,145,146,147,148,149,150,151,152,153,154,155,156,157,158);
cat2_name[10] = new Array('충북 괴산군','충북 단양군','충북 보은군','충북 영동군','충북 옥천군','충북 음성군','충북 제천시','충북 증평군','충북 진천군','충북 청주시','충북 청주시 상당구','충북 청주시 서원구','충북 청주시 청원구','충북 청주시 흥덕구','충북 충주시');

cat2_num[11] = new Array(159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175);
cat2_name[11] = new Array('충남 계룡시','충남 공주시','충남 금산군','충남 논산시','충남 당진시','충남 보령시','충남 부여군','충남 서산시','충남 서천군','충남 아산시','충남 예산군','충남 천안시','충남 천안시 동남구','충남 천안시 서북구','충남 청양군','충남 태안군','충남 홍성군');

cat2_num[12] = new Array(176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197);
cat2_name[12] = new Array('전남 강진군','전남 고흥군','전남 곡성군','전남 광양시','전남 구례군','전남 나주시','전남 담양군','전남 목포시','전남 무안군','전남 보성군','전남 순천시','전남 신안군','전남 여수시','전남 영광군','전남 영암군','전남 완도군','전남 장성군','전남 장흥군','전남 진도군','전남 함평군','전남 해남군','전남 화순군');

cat2_num[13] = new Array(198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221);
cat2_name[13] = new Array('경북 경산시','경북 경주시','경북 고령군','경북 구미시','경북 김천시','경북 문경시','경북 봉화군','경북 상주시','경북 성주군','경북 안동시','경북 영덕군','경북 영양군','경북 영주시','경북 영천시','경북 예천군','경북 울릉군','경북 울진군','경북 의성군','경북 청도군','경북 청송군','경북 칠곡군','경북 포항시','경북 포항시 남구','경북 포항시 북구');

cat2_num[14] = new Array(222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244);
cat2_name[14] = new Array('경남 거제시','경남 거창군','경남 고성군','경남 김해시','경남 남해군','경남 밀양시','경남 사천시','경남 산청군','경남 양산시','경남 의령군','경남 진주시','경남 창녕군','경남 창원시','경남 창원시 마산합포구','경남 창원시 마산회원구','경남 창원시 성산구','경남 창원시 의창구','경남 창원시 진해구','경남 통영시','경남 하동군','경남 함안군','경남 함양군','경남 합천군');

cat2_num[15] = new Array(245,246,247);
cat2_name[15] = new Array('제주 서귀포시','제주 제주시','제주');

cat2_num[16] = new Array(248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265);
cat2_name[16] = new Array('강원 강릉시','강원 고성군','강원 동해시','강원 삼척시','강원 속초시','강원 양구군','강원 양양군','강원 영월군','강원 원주시','강원 인제군','강원 정선군','강원 철원군','강원 춘천시','강원 태백시','강원 평창군','강원 홍천군','강원 화천군','강원 횡성군');

cat2_num[17] = new Array(266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281);
cat2_name[17] = new Array('전북 고창군','전북 군산시','전북 김제시','전북 남원시','전북 무주군','전북 부안군','전북 순창군','전북 완주군','전북 익산시','전북 임실군','전북 장수군','전북 전주시','전북 전주시 덕진구','전북 전주시 완산구','전북 정읍시','전북 진안군');


function cat1_change( target_value) {
    target_value;
    var target = document.getElementById("district-buttons");
    target.innerHTML = "";  // 기존 내용을 초기화.

    if (cat1_name[target_value-1]) {
        console.log(target_value+"  "+"   "+cat2_name[target_value]);
        cat2_name[target_value].forEach(function(name) {
            var li = document.createElement("li");

            // 시에 따른 구,군 버튼 생성
            var button = document.createElement("button");
            button.type = "button";
            button.className = "btn";
            button.value = name;
            button.name="region_2"
            button.textContent = name;
            button.style ="width:170px;height:80px;"
            button.onclick = function() {
                cat2_change(button.value);

            };
            li.appendChild(button);
            target.appendChild(li);
        });

    }
}



function cat2_change(cat2_value) {
    console.log(cat2_value);  // 선택한 구/군 값으로 원하는 작업을 수행할 수 있습니다.
    document.getElementById('selected_region').value = cat2_value;  // 숨겨진 입력 필드의 값을 업데이트

}


function checkOnlyOne(element) {

    const checkboxes
        = document.getElementsByName("region_1");

    checkboxes.forEach((cb) => {
      cb.checked = false;
    })

    element.checked = true;
}


function fn_SearchReset() {

   const form = document.getElementById('personal_form');
   const checkboxes = form.querySelectorAll('input[type="checkbox"]');
   // 체크박스를 하나씩 순회하며 선택을 해제합니다.
   checkboxes.forEach(checkbox => {
       checkbox.checked = false;
   });

   const region_checkboxes_2
       = document.getElementsByName("region_2");

       region_checkboxes_2.forEach((cb) => {
       cb.checked = false;
   });

   const region_checkboxes
        = document.getElementsByName("region_1");

        region_checkboxes.forEach((cb) => {
        cb.checked = false;
    });

    // 숨겨진 입력 필드의 값을 초기화합니다.
    document.getElementById('selected_region').value = '';
    document.getElementById('selected_holiday').value = '';
    document.getElementById('selected_waged').value = '';

}

// updateSelectedWaged 함수 정의
function updateSelectedWaged() {
    var checkboxes = document.querySelectorAll('input[name="wage-checkbox"]');
    var hiddenInput = document.getElementById('selected_waged');
    var selectedValues = [];

    checkboxes.forEach(function(checkbox) {
        if (checkbox.checked) {
            selectedValues.push(checkbox.value);
        }
    });

    // 숨겨진 입력 필드의 값을 업데이트합니다.
    hiddenInput.value = selectedValues.join(',');
}

// updateSelectedHoliday 함수 정의
function updateSelectedHoliday() {
    var checkboxes = document.querySelectorAll('input[name="holiday-checkbox"]');
    var hiddenInput = document.getElementById('selected_holiday');
    var selectedValues = [];

    checkboxes.forEach(function(checkbox) {
        if (checkbox.checked) {
            selectedValues.push(checkbox.value);
        }
    });

    // 숨겨진 입력 필드의 값을 업데이트합니다.
    hiddenInput.value = selectedValues.join(',');
}

// 폼의 submit 이벤트 리스너 추가
document.getElementById('wageForm').addEventListener('submit', function(event) {
    // 폼 제출 전에 체크박스의 값을 숨겨진 입력 필드에 설정합니다.
    updateSelectedWaged();
    updateSelectedHoliday();
});