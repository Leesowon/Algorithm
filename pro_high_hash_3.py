# 2024-10-09

def solution(phone_book):
    # 1. 해시맵 생성, 해당 key에 대한 value는 1
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        jubdoo = ""
        for number in phone_number:
            jubdoo += number
            if jubdoo in hash_map and jubdoo != phone_number:
                return False
    return True


ph = ["119", "97674223", "1195524421"]
solution(ph)