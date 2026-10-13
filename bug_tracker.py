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

def filter_bugs(bugs,status,severity):
    status=status.strip().lower()
    severity=severity.strip().lower()
    result=[]
    for bug in bugs:
        if bug["status"] == status and bug["severity"] == severity:
            result.append(bug)
    return result

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

def change_status(bugs,bug_id,new_status):
    new_status=new_status.strip().lower()
    if new_status not in ("open","in_progress","closed"):
        return "invalid_status"
    bug=find_bug(bugs,bug_id)
    if bug is None:
        return "not_found"
    current=bug["status"].strip().lower()
    if current==new_status:
        return "forbidden"
    allowed=False
    if current=="open" and new_status=="in_progress":
        allowed=True
    elif current=="in_progress" and new_status in ("open","closed"):
        allowed=True
    elif current=="closed" and new_status=="open":
        allowed=True
    if not allowed:
        return "forbidden"
    bug["status"]=new_status
    return "updated"

def build_report(bugs):
    total=len(bugs)
    by_status={"open": 0,"in_progress": 0, "closed": 0}
    by_severity={"high": 0, "medium": 0, "low": 0}
    unresolved_high=0
    for bug in bugs:
        status=bug["status"].strip().lower()
        severity=bug["severity"].strip().lower()
        if status in by_status:
            by_status[status]+=1
        if severity in by_severity:
            by_severity[severity]+=1
        if severity=="high" and status !="closed":
            unresolved_high+=1
    return {
        "total": total,
        "by_status": by_status,
        "by_severity": by_severity,
        "unresolved_high": unresolved_high
    }

def start_selected(bugs,ids):
    if not ids:
        return False
    if len(ids)!=len(set(ids)):
        return False
    for bug_id in ids:
        bug=find_bug(bugs,bug_id)
        if bug is None or bug["status"].strip().lower() != "open":
            return False
    for bug_id in ids:
        find_bug(bugs,bug_id)["status"]="in_progress"
    return True

while True:
    print("1-find_bug")
    print("2-filter_bugs")
    print("3-add_bug")
    print("4-change_status")
    print("5-build_report")
    print("6-start_selected")
    print("0-выход")
    choice=input("Выбор: ").strip()
    if choice=="0":
        break
    elif choice=="1":
        bug_id=int(input("ID: "))
        print(find_bug(bugs,bug_id))
    elif choice=="2":
        status=input("Статус: ")
        severity=input("Серьёзность: ")
        print(filter_bugs(bugs,status,severity))
    elif choice=="3":
        title=input("Название: ")
        severity=input("Серьёзность: ")
        print(add_bug(bugs,title,severity))
    elif choice=="4":
        bug_id=int(input("ID: "))
        new_status=input("Новый статус: ")
        print(change_status(bugs,bug_id,new_status))
    elif choice=="5":
        print(build_report(bugs))
    elif choice=="6":
        raw=input("ID через пробел: ")
        ids=[int(i) for i in raw.split()]
        print(start_selected(bugs,ids))
    else:
        print("Нет такой команды")