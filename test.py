k, m = map(int, input().split())
relic = [list(map(int, input().split())) for _ in range(5)]
piece = list(map(int, input().split()))
length = 3
new_relic = [[0] * 5 for _ in range(5)]  # 회전 후 다시 갖다 붙일 배열

def rotate_90(sh, sw, length):
     global relic, new_relic

     for h in range(sh, sh + length) :
         for w in range(sw, sw + length) :
             # 1. 시작 지점 좌표를 (0,0) 기준으로 변환
             oh, ow = h - sh, w - sw
             # 2. 90 회전한 좌표 계산
             rh, rw = ow, length - oh - 1
             # 3. 회전 좌표에 맞게 new_arr 에 값 복사
             new_relic[sh + rh][sw + rw] = relic[h][w]

     for h in range(sh, sh + length) :
        for w in range(sw, sw + length) :
            relic[h][w] = new_relic[h][w]

def rotate_180(sh, sw, length) :
    global relic, new_relic

    for h in range(sh, sh + length) :
        for w in range(sw, sw + length) :
            oh, ow = h - sh, w - sw
            rh, rw = length - ow - 1, length - oh - 1
            new_relic[sh + rh][sw + rw] = relic[h][w]

    for h in range(sh, sh + length) :
        for w in range(sw, sw + length) :
            relic[h][w] = new_relic[h][w]

def rotate_270(sh, sw, length) :
    global relic, new_relic

    for h in range(sh, sh+length) :
        for w in range(sw, sw+length) :
            oh, ow = h - sh, w - sh
            rh, rw = length - ow -1 , oh
            new_relic[sh + rh][sw + rw] = relic[h][w]

    for h in range(sh, sh+length) :
        for w in range(sw, sw+length) :
            relic[h][w] = new_relic[h][w]
