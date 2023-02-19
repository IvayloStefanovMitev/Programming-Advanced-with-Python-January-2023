def students_credits(*args):
    diploma_credits = 240
    diyan_credits = 0
    courses = {}
    result = []
    for info in args:
        data = info.split('-')
        diyan_credits += (int(data[3]) / int(data[2])) * int(data[1])
        courses[data[0]] = (int(data[3]) / int(data[2])) * int(data[1])

    if diyan_credits >= diploma_credits:
        result.append(f"Diyan gets a diploma with {diyan_credits:.1f} credits.")
    else:
        result.append(f"Diyan needs {diploma_credits - diyan_credits:.1f} credits more for a diploma.")

    for course, points in sorted(courses.items(), key=lambda x: -x[1]):
        result.append(f"{course} - {points:.1f}")

    return "\n".join(result)


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

