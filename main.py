questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]
count = 0
balls = 0
ready = input("Привет! Предлагаю проверить свои знания английского! \
Наберите \"ready\", чтобы начать!")

if ready == "ready":

    print("введите пропущенное слово!")

    for i in range(len(questions)):
        chance = 3
        while chance != 0:
            user_answer = input(f"{questions[i]}: ")

            if user_answer == answers[i]:
                count += 1
                print("Ответ верный!")
                if chance != 0:
                    balls += chance
                else:
                    chance += 1
                    balls += chance
                break
            else:
                chance -= 1
                print(f"Осталось попыток: {chance}, попробуйте еще раз!")

            if chance == 0:
                print(f"Увы, но нет. Верный ответ: {answers[i]}")
                break
    percent = count / 3 * 100
    print(f"Вот и все! Вы ответили на {count} \
вопросов из 3 верно, вы набрали {balls} баллов и {round(percent)}%.")

else:
    print("Кажется, вы не хотите играть. Очень жаль")























