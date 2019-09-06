#1
week_time = int(input("일주일에 몇 시간 일해?"))
how_long = int(input("몇 주 일해?"))
how_much = int(input("시급 얼마야?"))
#2
if week_time >= 15:
    week_time += (week_time/5)
#3
salary = int(week_time) * int(how_long) * int(how_much)
print("알바비는", salary)