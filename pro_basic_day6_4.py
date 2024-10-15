import sys
input = sys.stdin.readline

def solution(arr, queries):
    answer = []

    # for i in queries: # i는 queries 리스트의 요소가 되지만, 이후 코드에서 인덱스로 쓰임
    #     # queries 리스트의 요소가 인덱스로 쓰이는 것은 잘못된 접근
    #     t1 = queries[i][0]
    #     t2 = queries[i][1]
    #
    #     tmp = arr[t1]
    #     arr[t1] = arr[t2]
    #     arr[t2] = tmp

    for t1, t2 in queries:
        # 인덱스 t1과 t2의 값 교환
        arr[t1], arr[t2] = arr[t2], arr[t1]

    # 쿼리 적용 후의 arr을 answer에 추가
    answer = arr

    return answer
