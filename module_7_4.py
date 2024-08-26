team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = "Победа команды Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = "Победа команды Волшебники Данных!"
else:
    challenge_result = "Ничья"

print("В команде Мастера кода: %s участников" % team1_num)
print("В команде Волшебники данных: %s участников" % team2_num)
print("Итого сегодня в командах: %d и %d участников\n" % (team1_num, team2_num))

print("Команда Мастера кода решила задач: {} !".format(score_1))
print("Команда Волшебники данных решила задач: {} !\n".format(score_2))

print("Команда Мастера решили задачи за {} с !".format(team1_time))
print("Волшебники данных решили задачи за {} с !\n".format(team2_time))

print(f"Команды решили {score_1} и {score_2} задач.\n")
print(f"Результат битвы: {challenge_result}\n")

print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!.")
