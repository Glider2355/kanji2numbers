from flask import make_response

suji = {
    "零":0,
    "壱":1,
    "弐":2,
    "参":3,
    "四":4,
    "五":5,
    "六":6,
    "七":7,
    "八":8,
    "九":9
}

base_digit = {
    "拾":10,
    "百":100,
    "千":1000
}

digit = {
    "万":10000,
    "億":100000000,
    "兆":1000000000000
}

def kanji2number(kansuji):
    number = 0
    tmp1 = 0
    tmp2 = 0

    # 入力フラグ[suji, base_digit, digit]
    flag = [1, 0, 0]


    for kanji in kansuji:
        # 壱～九→tmp1
        if kanji in suji and flag[0]:
            tmp1 = suji[kanji]
            flag = [0, 1, 1]

        # 拾～千→tmp2
        elif kanji in base_digit and flag[1]:
            tmp2 += tmp1 * base_digit[kanji]
            tmp1 = 0
            flag = [1, 0, 1]
        
        # 万～兆→number
        elif kanji in digit and flag[2]:
            tmp = tmp1 + tmp2
            number += tmp * digit[kanji]
            tmp2 = 0
            flag = [1, 0, 0]
        
        # 変換できない入力
        else:
            return make_response("", 204)

    number += tmp1 + tmp2
    return number