import re
def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z\d\-_.]', '', new_id)
    new_id = re.sub('\\.{2,}', '.', new_id)
    new_id = re.sub('^[.]|[.]$', '', new_id)
    if len(new_id) == 0:
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = re.sub('[.]$', '', new_id)
    if len(new_id) <= 2:
        new_id = new_id[0] + new_id[-1] * 2
    print(new_id)

    

solution(new_id="...!@BaT#*..y.abcdefghijklm")
solution(new_id="z-+.^.")
solution(new_id="=.=")
solution(new_id="123_.def")
solution(new_id="abcdefghijklmn.p")