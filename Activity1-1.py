roster = {
    "Amara":[92,88,95],
    "Leo":[70,65,80],
}

def addStudent(roster_dict, name, data):
    roster_dict[name] = data

addStudent(roster, "John", ["Science", "Math"])
addStudent(roster, "Jenny", ["PE", "History", "English"])
addStudent(roster, "Mia", [85, 90, 88])

print(roster)

averages = {
    student: round(sum(scores) / len(scores), 2)
    for student, scores in roster.items()
    if type(scores[0]) != str and (sum(scores) / len(scores)) > 80
}

print(averages)