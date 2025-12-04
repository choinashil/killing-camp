def solution(today, terms, privacies):
    def calculate_date(date):
        year, month, day = map(int, date.split('.'))
        return (year * 12 * 28) + (month * 28) + day

    answer = []
    terms_dict = {}
    for term in terms:
        t, m = term.split(' ')
        terms_dict[t] = calculate_date(today) - (int(m) * 28)

    for i, privacy in enumerate(privacies):
        date_str, t = privacy.split(' ')
        d = calculate_date(date_str)

        if d <= terms_dict[t]:
            answer.append(i + 1)

    return answer


print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))  # [1, 3]
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))  # [1, 4, 5]
