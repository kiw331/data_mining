from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

# 진행 중인 대회 페이지의 url을 파싱
def get_competition_url(open_comp):

    listpage_url = 'https://dacon.io/competitions'
    
    # URL을 열고 해당 페이지 HTML 파싱
    html = urllib.request.urlopen(listpage_url)
    daconcomp = BeautifulSoup(html, 'html.parser')

    # a태그 중에서 class 속성값이 "clearfix" 모두 찾기 (상위 페이지에 있는 모든 대회)
    all_comp = daconcomp.find_all('a', attrs={'class': 'clearfix'})

    # 상위 페이지의 모든 대회중 진행 중인 대회의 url크롤링
    for comp in all_comp:
        
        # 진행 중인 대회는 class속성값이 'dday'인 태그의 텍스트가 "참가신청중"이라고 표시됨
        if comp.find('div', class_='dday').text.strip() == '참가신청중':
    
            #해당하는 대회의 url을 open_comp리스트에 저장
            open_comp.append('https://dacon.io' + comp.get('href') + 'description')
            
            
# 진행 중인 대회 정보 파싱
def get_competition_information(open_comp, result):
    
    for comp in open_comp:
        
        # URL을 열고 해당 페이지 HTML 파싱
        html = urllib.request.urlopen(comp)
        soup = BeautifulSoup(html, 'html.parser')
        
        #대회명
        name = soup.title.string 
        
        #분야
        field = soup.h2.string.replace("\n", "")
        
        #현재 참가자
        participants = soup.find('li', class_='d-inline text-body-2').get_text(strip=True).replace("\n", "")
        index = participants.find('명')
        participants = participants[:index+1] #~명까지 나오도록 전처리
        
        #상금
        reward = soup.find('li', attrs={'class': "text-body-2"}).get_text(strip=True).replace("상금 :", "").replace("\n", "").replace(" ", "")
        
        result.append([name, field, participants, reward])
        
def main():
    
    # 진행 중인 대회 url과 최종 결과를 저장한 리스트
    open_comp, result = [], []
    
    # 진행 중인 대회 페이지가 있는 리스트 크롤링
    get_competition_url(open_comp)
    
    # 진행 대회 정보: 대회명, 분야, 진행기간, 상금 크롤링
    get_competition_information(open_comp,result)
    
    # pandas로 테이블 형태의 데이터프레임 생성
    dacon_tbl = pd.DataFrame(result, columns = ('name', 'field', 'participants','reward'))
    
    # 한글출력을 위해 인코딩 cp949, 쓰기모드, 첫번째 열을 인덱스가 됨
    dacon_tbl.to_csv('res/dacon1.csv', encoding = 'cp949', mode = 'w', index = True)
    del result[:]

if __name__ == '__main__':
    main()
    
    
    
    
