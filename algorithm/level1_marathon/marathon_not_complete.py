'''
프로그래머스 level 1 - 완주하지 못한 선수

풀이에 zip 함수를 이용하였다.
zip 함수는 동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수.

sort()를 이용하여 배열을 이름순으로 정렬하고, zip 함수를 이용하여 같은 배열 번호끼리 쌍으로 묶어준다.

반복문에서 참가자 리스트(p)와 완주자 리스트(c)를 zip으로 묶어 비교했을 때 같은 값이 아니면
참가자(p)의 값이 완주하지 못한 선수가 된다.


만약 for문을 다 순회하였지만 반복문 내부의 p(참가자)와 c(완주자)의 값이 같으면
정렬된 참가자 리스트의 끝값([-1])이 완주하지 못한 사람이 된다.

이유는 완주자가 참가자보다 반드시 한명 적다는 전제가 있으므로
순서대로 정렬된 상태라면 마지막 값이 묶이지 않았을 것이기 때문에 [-1]을 리턴한다.


ex) 동명이인이 존재할 때

participant = ['kiki','eden','kante','kante']
completion = ['kiki','eden','kante']
-> zip으로 묶은 결과: eden eden, kante kante, kante titi
-> kante titi가 서로 다르므로 kante가 미완주자.


ex2) zip으로 묶은 p,c의 결과가 동일한 경우

participant = ['kiki','eden','vante']
completion = ['kiki','eden']
-> zip으로 묶은 결과: (kiki, kiki), (eden, eden)
-> vante는 존재하지 않으므로 참가자의 끝값(participant[-1])을 리턴.

'''
# import collections

# participant = ['kiki','eden','vante']
# completion = ['kiki','eden']

# participant.sort()
# completion.sort()

# print(collections.Counter(participant))
# print(collections.Counter(completion))
# answer = collections.Counter(participant) - collections.Counter(completion)
# print(list(answer.keys())[0])
    
# 내 풀이
def solution(participant, completion):
    participant = ['kiki','eden','kante']
    completion = ['kiki','eden']

    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]


'''
collection과 카운터를 이용한 효율적인 풀이법도 있다.

key와 value를 이용한 방법으로, Counter 객체들끼리의 뺄셈도 가능하기 때문에
두 리스트의 차를 구하고 남은 키값은 결국 p에는 있지만 c에는 없다는 뜻이므로 미완주자가 된다.


collections.Counter에 대해 알게 되었으며, zip에 대해서도 보다 자세히 알게 되었다.

ex) 컬렉션의 key, value를 이용
print(collections.Counter(participant))
>>Counter({'eden': 1, 'kiki': 1, 'vante': 1})

print(collections.Counter(completion))
>>Counter({'eden': 1, 'kiki': 1})

answer = collections.Counter(participant) - collections.Counter(completion)
>> Counter({'vante': 1})

print(list(answer.keys())[0])
>> vante

'''
# 다른 사람의 풀이 - 컬렉션
import collections

def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]