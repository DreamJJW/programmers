def solution(babbling):
    count = 0

    for b in babbling:
        if "ayaaya" in b or "yeye" in b or "woowoo" in b or "mama" in b:
            continue
        if not b.replace("aya", " ").replace("ye", " ").replace("woo", " ").replace("ma", " ").replace(" ", ""):
            print(b)
            count += 1

    return count



solution(babbling=["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])
# solution(babbling=["aya", "yee", "u", "maa"])
# solution(babbling=["woowo"])


