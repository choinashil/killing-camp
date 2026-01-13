def solution(today, terms, privacies):
    def format_date(date_str):
        year, month, day = map(int, date_str.split('.'))
        return (year * 12 * 28) + (month * 28) + day

    answer = []
    formatted_today = format_date(today)

    memo = {}
    for term in terms:
        name, month = term.split(' ')
        memo[name] = int(month) * 28

    for index, privacy in enumerate(privacies):
        date, term = privacy.split(' ')
        if formatted_today >= format_date(date) + memo[term]:
            answer.append(index + 1)

    return answer


print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))  # [1, 3]
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))  # [1, 4, 5]

679551
