bugs=[
    {"id": 1, "title": "Не работает вход",
     "severity": "high", "status": "open"},
    {"id": 2, "title": "Опечатка на главной странице",
     "severity": "low", "status": "closed"},
    {"id": 3, "title": "Не сохраняется расписание",
    "severity": "high", "status": "open"},
    {"id": 4, "title": "Неверный цвет кнопки",
     "severity": "medium", "status": "open"}
]
def find_bug(bugs,bug_id):
    for bug in bugs:
        if bug["id"] == bug_id:
            return bug
    return None
print(find_bug(bugs,1))
print(find_bug(bugs,2))
print(find_bug(bugs,3))
print(find_bug(bugs,4))
print(find_bug(bugs,99))