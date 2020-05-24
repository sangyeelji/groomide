CorpCode 폴더안에
CORPCODE.xml 파일은
OPENDART API로 추출한 파일입니다.
해당 파일을 얻기 위해서는 아래와 같은 URL를 사용합니다.
https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key=9cb99dacf06918fac2a4d6c8c886b01498c57d4b

위의 URL로 요청시 xml파일 형식으로 다운로드 되는데 파일의 확장자를 zip파일로 변경후 압축를 풀면 위의 xml파일이 생성됩니다.

현재 OPEN DART에서 사용되는 기업 고유번호와 주식 코드가 다르기 때문에 기업의 고유 번호를 얻기위해서는 해당 파일을 파싱해야됩니다.
