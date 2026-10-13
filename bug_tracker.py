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

def filter_bugs(bugs,status,severity):
    status=status.strip().lower()
    severity=severity.strip().lower()
    result=[]
    for bug in bugs:
        if bug["status"] == status and bug["severity"] == severity:
            result.append(bug)
    return result
print(filter_bugs(bugs," OPEN ","High"))
print(filter_bugs(bugs,"closed","high"))
print(filter_bugs(bugs,"waiting","high"))

def add_bug(bugs,title,severity):
    title=title.strip()
    severity=severity.strip().lower()
    if len(title)<5:
        return None
    if severity not in ("low","medium","high"):
        return None
    max_id=0
    for bug in bugs:
        if bug["id"]>max_id:
            max_id=bug["id"]
    new_id=max_id+1
    new_bug={"id": new_id, "title": title, "severity": severity, "status": "open"}
    bugs.append(new_bug)
    return new_id
print(add_bug(bugs," Не открывается профиль ","HIGH"))
print(add_bug(bugs,'asdas', 'urgent'))