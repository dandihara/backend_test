# backend_test

- 사용 라이브러리  
- asgiref==3.5.0
- Django==4.0.2
- django-filter==21.1
- djangorestframework==3.13.1
- importlib-metadata==4.11.1
- Markdown==3.3.6
- psycopg2==2.9.3
- pytz==2021.3
- sqlparse==0.4.2
- tzdata==2021.5
- zipp==3.7.0



 # / (1번안 결과물- 단순 카운팅 결과값)

 - Parameter : x
 - 각 속성에 맞는 결과값 도출
 
 # /entrance (1번안 결과물 - 입장 카운팅 결과값)
 
 - Parameter : x
 - 위와 동일하게 결과물 출력 가능

# /concept<str:name>(2번안)

-Parameter : name(str, table name)
- 자체 모델 접근에서 검색 키워드를 사용하지 못함.
 
# /table/<str:name> (3번안)

- Parameter : name(table name)
- 위와 동일.

