# 인텔리제이 자바

1. https://whitepaek.tistory.com/56

1. file -> 프로젝트 스트럭쳐

2. https://whitepaek.tistory.com/13

# 에러

- IDE에서 out 폴더에 jar 라이브러리를 복사하지 못해서 발생한 것. 그리고 해결책으로 lib 폴더를 복사해서 붙여넣는 걸 제시한다.

3. https://stackoverflow.com/questions/24520842/intellij-13-tomcat-error-configuring-application-listener-of-class-org-springfra


# 설정

1. File -> Project Structure 

2. Project -> Java SDK 설정 1.8

2. libraries -> + 버튼 클릭후 libs 폴더 내 모든 jar 파일 추가

3. modules -> sources 탭에서 src 폴더 선택하고 sources 클릭

4. output 빌드 경로 지정 : Inherit ~ 

5. dependencies 지정 -> java 1.8 SDK, 라이브러리 추가 (libraries 에서 추가한 것 )

6. + 버튼 클릭 후 add -> web 선택

7. Facets -> +버튼 클릭 후 web을 선택

8. Artifacts Exploded 설정: + -> Web Applicatioin : Exploded -> from modules 로 설정 가능하다. 이 때 라이브러리도 같이 포함되어야 함.(부가적으로 Meniifest가 프로젝트의 WebContent/META-INF/MANIFEST.mf를 참조하고 있는지 확인)

9. Artifacts Archive 설정: "+" 버튼을 클릭하여 Application : Archive 를 클릭하여 위에서 생성한 exploded 설정을 참조시켜준다.

8. artifacts -> 아웃풋 빌드 경로 지정 : paths 탭에서 compiler output에서 "use module ~ 선택"

9. classes 경로 지정 -> add java ee facet resource

10. lib 경로 지정 -> add library files -> libs

11. tomcat -> 탐캣 설치한 다음 -> configure 해당 탐캣 설치 파일에 conf있는 폴더로.. /usr/local/Cellar/tomcat/9.0.41/libexec

12. deployment 해당 web_exploded 선택한 다음 application context => / 로 수정

13. 실행하면 새로운 웹 페이지가 로컬에서 뜨고... 해당 내용 배포하려면 

14. build -> all artifact-> build 하면  out->artifcats->web폴더에 해당 war파일 생성. 이 war파일을 업로드하는 것

15. elasticbeansTalk에 업로드가 잘못되었을 경우 빠르게 어플리케이션 버전 -> 마지막 배포했던 내용으로 재배포

16. https://winmargo.tistory.com/196