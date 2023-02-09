def solution(id_list, report, k):
    report = set(report)
    answer =  {x:0 for x in id_list}
    # {'muzi': 1, 'frodo': 2, 'apeach': 0, 'neo': 2}
    reports = {x:0 for x in id_list}
    # {'muzi': 2, 'frodo': 1, 'apeach': 1, 'neo': 0}

    for x in report:
        reports[x.split()[1]] += 1
    for x in report:
        if reports[x.split()[1]] >= k:
            answer[x.split()[0]] += 1

    print(reports)
    print(answer)
    print(list(answer.values()))



solution(id_list=["muzi", "frodo", "apeach", "neo"],
         report=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], k = 2)

# solution(id_list=["con", "ryan"], report=["ryan con", "ryan con", "ryan con", "ryan con"], k = 3)