from random import *

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Как тебя зовут?')
name = input()
print(f'Привет, {name}')
while True:
    quest = input('Спроси меня. ')
    if quest != '':
        print(choice(answers))
    else:
        continue
    quest = input("Хочешь задать еще один вопрос? да/нет")
    if quest == 'да':
        continue
    else:
        print('Возвращайся если возникнут вопросы!')
        break
