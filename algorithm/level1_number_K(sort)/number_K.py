'''
K번째 수 - 프로그래머스(정렬)
배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

1. array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
2. 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
3. 2에서 나온 배열의 3번째 숫자는 5입니다.

배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, 
commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 
return 하도록 solution 함수를 작성해주세요.

제한사항
- array의 길이는 1 이상 100 이하입니다.
- array의 각 원소는 1 이상 100 이하입니다.
- commands의 길이는 1 이상 50 이하입니다.
- commands의 각 원소는 길이가 3입니다.

입출력 예
array	                commands	                        return
[1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]

입출력 예 설명
[1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. [2, 3, 5, 6]의 세 번째 숫자는 5입니다.
[1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. [6]의 첫 번째 숫자는 6입니다.
[1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. [1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.

풀이
배열을 자르는 슬라이싱을 이용해야 하는 문제.

```commands[0]```번째 숫자부터, ```commands[1]```번째 숫자까지 자르고, ```commands[2]```번째 숫자를 출력
해당 결과를 ```answer``` 배열에 ```return``` 시킨다.

### #1
```py
for command in commands:
        i,j,k = command[0], command[1], command[2]
```
먼저 반복문을 이용하여 i, j, k를 각각 commands의 0번, 1번, 2번으로 지정.

### #2
```py
slicing = array[i-1:j]
slicing.sort()
answer.append(slicing[k-1])
```
이후 ```slicing```이라는 배열에 i번째(i-1)부터 j까지 자르고
제약사항에 따라 배열을 정렬한다.
이후 해당 결과값을 ```answer``` 배열에 삽입하고 ```return``` 한다.

'''

array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]

def solution(array, commands):
    answer = []

    for command in commands:
        i,j,k = command[0], command[1], command[2]
        slicing = array[i-1:j]
        slicing.sort()
        answer.append(slicing[k-1])

    return answer

print(solution(array,commands))