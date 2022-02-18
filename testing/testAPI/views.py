from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from django.apps import apps
from django.db.models import Count
from django.db import connection

from .models import *
# 통계 환자 수 (전체 / 성별 / 인종별 / 민족별 / 사망)
class CounterView(APIView):
    def get(self,req):
        result = {}
        gender_code = {8507 : 'Male' , 8532 : 'Female'}
        # 성별(두가지라 for문 사용 x) !
        gender = Person.objects.values('gender_concept__concept_id').annotate(gender_count = Count('gender_concept__concept_id'))
        result['gender'] = {}
        for v in gender:
            result['gender'][gender_code[v['gender_concept__concept_id']]] = v['gender_count']
        # 인종
        race = Person.objects.values('race_concept__concept_id').annotate(race_count = Count('race_concept__concept_id'))
        result['race'] = {}
        for r in race:
            try:
                result['race'][Concept.objects.get(concept_id = r['race_concept__concept_id']).concept_name] = r['race_count']
            except Concept.DoesNotExist:
                return Response("Wrong input code!")
        # 민족
        eth = Person.objects.values('ethnicity_source_value').annotate(eth_count = Count('ethnicity_source_value'))
        result['eth'] = {}
        eth = list(eth)
        for e in eth:
            result['eth'][e['ethnicity_source_value']] = e['eth_count']

        # 사망 수
        result['death'] = Death.objects.count()
        result['Total'] = sum(result['gender'].values())
        return Response({'result' : result})

# 방문 수 (방문 유형 별 / 성별 방문 수 / 인종별 / 민족별 방문 수 /방문시 연령대별 방문 수)
class EntranceView(APIView):
    def get(self,req):
        result = {}
        visit_concept_code = {9201 : 'Inpatient Visit' , 9202 : 'Outpatient Visit' , 9203 : 'Emergency Room Visit'}
        gender_code = {8507 : 'Male' , 8532 : 'Female'}
        
        #상황 유별 방문 회수
        visit_data = VisitOccurrence.objects.values('visit_concept__concept_id').annotate(concept_count = Count('visit_concept__concept_id'))
        result['visit'] = {}
        for v in visit_data:
            result['visit'][visit_concept_code[v['visit_concept__concept_id']]] = v['concept_count']
        
        #성별별 방문 횟수
        result['visit_gender'] = {}
        visit_gender = VisitOccurrence.objects.values('person__gender_concept__concept_id').annotate(gender_count = Count('person__gender_concept__concept_id'))
        result['visit_gender'] = {}
        for v in visit_gender:
            result['visit_gender'][gender_code[v['person__gender_concept__concept_id']]] = v['gender_count']
        
        #인종별 방문 횟수
        result['visit_race'] = {}
        visit_race = VisitOccurrence.objects.values('person__race_concept__concept_id').annotate(race_count = Count('person__race_concept__concept_id'))
        for v in visit_race:
            try:
                result['visit_race'][Concept.objects.get(concept_id = v['person__race_concept__concept_id']).concept_name] = v['race_count']
            except Concept.DoesNotExist:
                return Response("Wrong input code!")
        #민족별 방문 횟수
        result['visit_eth'] = {}
        visit_eth = VisitOccurrence.objects.values('person__ethnicity_source_value').annotate(eth_count = Count('person__ethnicity_source_value'))
        for v in visit_eth:
           result['visit_eth'][v['person__ethnicity_source_value']] = v['eth_count']
        return Response({'result' : result})

# person / VisitOccurrence / drugExposure /death /ConditionOccurrence
class SearchView(ListAPIView):
    # 이름을 넘겨주면 그 모델에서 사용되는 concept 값들을 다 가져온다. 중복제거.
    # concept table과 관계가 있는 컬럼들을 모조리 가져와 검색
    def list(self,req,name):
        model_list = apps.get_app_config('testAPI').get_models()
        model_list = [m._meta.label.split(".")[1] for m in model_list]
        print(model_list)
        result = []
        
        # for m in model_list:
        #     if m._meta.label.split(".")[1] == 'Concept':
        #         #print(m._meta.fields)
        #         related = m._meta.related_objects
        #         for r in related:
        #             print(r.identity[2])
        #             if r.identity[2] is not None:
        #                 result.append(r.identity[2])
        #         break
        
        return Response({'result' : result})
class GetTableValuesView(ListAPIView):
    def list(self,req,name):
        tables = connection.introspection.table_names()
        person = Person._meta.get_fields()
        print(person[0])
        name = "Person"
        if name in tables:
            print(name._meta.get_fields())
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST) 
        return Response({'result' : tables})