from random import choice
import random
from colorama import init,Fore

init(autoreset=True)

lang_choice = input("Выберите язык \n1 - ru / 2 - eng: ").lower()

if lang_choice == '1':
    score = 0
    while True:
        input("готов? (Enter): ")

        ruwords = ["электротрансформатор",
                   "автоэлектростеклоподъемники",
                   "переосвидетельствоваться",
                   "интернационализироваться",
                   "библиотека",
                   "разработчик",
                   "программирование",
                   "переключатель",
                   "представление",
                   "автоматизация",
                   "вселенная",
                   "взаимодействие",
                   "многозадачность",
                   "документирование",
                   "совместимость",
                   "трансформация",
                   "масштабирование",
                   "локализация",
                   "пользователь",
                   "синхронизация",
                   "протокол",
                   "вычисление",
                   "приложение",
                   "холодильник",
                   "фотография",
                   "телевизор",
                   "водопроводчик",
                   "домофон",
                   "радиостанция",
                   "многосерийность",
                   "кулинария",
                   "гастрономия",
                   "антарктика",
                   "экономичность",
                   "одушевленность",
                   "парикмахерская",
                   "стоматолог",
                   "экскурсовод",
                   "подоконник",
                   "автомобиль",
                   "далбаеб",
                   "акробатика",
                   "повседневность",
                   "карусель",
                   "головоломка",
                   "сумеречность",
                   "пчеловодство",
                   "метеостанция",
                   "вулканизация",
                   "аквариумистика",
                   "водопад",
                   "аквапарк"
                   ]

        random_choice = random.choice(ruwords)

        print(random_choice)

        word = input('')
        if word == random_choice:
            score += 1
            print(f"{Fore.GREEN}Правильно!{Fore.RESET} Очки: {score}")


        else:
            print(f'{Fore.RED}Неправильно!{Fore.RESET} Очки: {score}')
            score -= 1



elif lang_choice == '2':
    score = 0
    while True:
        input("start? (Enter): ")

        engwords = ["waterfall",
"butterfly",
"lemonade",
"adventure",
"photography",
"toothbrush",
"skyscraper",
"bookshelf",
"watermelon",
"binoculars",
"firefighter",
"friendship",
"playground",
"storyteller",
"snowblower",
"backpacker",
"grandmother",
"countryside",
"marshmallow",
"rollercoaster",
"environment",
"sunglasses",
"dishwasher",
"lighthouse",
"settlement",
"excitement",
"marketplace",
"electricity",
"helicopter",
"celebration",
"documentary",
"expedition",
"hummingbird",
"strawberry",
"skyscraping",
"cheeseburger",
"treetopper",
"grandfather",
"sportswear",
"daydreamer",
"sandcastle",
"windbreaker",
"storytelling",
"snowboarding",
"blueberry",
"flashlight",
"gardenhose",
"rainshadow",
"musicology",
"sleepwalker"
                    ]

        random_choice = random.choice(engwords)

        print(random_choice)

        word = input('')
        if word.lower() == random_choice.lower():
            score += 1
            print(f"{Fore.GREEN}Right!{Fore.RESET} score:", score)

        else:
            print(f'{Fore.RED}Not right!{Fore.RESET} score:', score)
            score -= 1
else:
    print("неверный ввод языка!")