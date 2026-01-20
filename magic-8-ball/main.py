#!/usr/bin/env python3
from random import choice

ANSWERS = [
    "Бесспорно",
    "Мне кажется - да",
    "Пока неясно, попробуй снова",
    "Даже не думай",
    "Предрешено",
    "Вероятнее всего",
    "Спроси позже",
    "Мой ответ - нет",
    "Никаких сомнений",
    "Хорошие перспективы",
    "Лучше не рассказывать",
    "По моим данным - нет",
    "Определённо да",
    "Знаки говорят - да",
    "Сейчас нельзя предсказать",
    "Перспективы не очень хорошие",
    "Можешь быть уверен в этом",
    "Да",
    "Сконцентрируйся и спроси опять",
    "Весьма сомнительно",
]


def greet_user():
    print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
    name = input("Как Вас зовут? \n")
    print(f"Привет, {name}!")
    return name


def ask_to_continue():
    while True:
        question = input("Хотите ли Вы задать еще один вопрос? (y/n): ").lower()
        if question in ("y", "yes", "д", "да"):
            return True
        elif question in ("n", "no", "н", "нет"):
            return False
        print("Не совсем понял вас...")


def main():
    user_name = greet_user()

    while True:
        input("Какой вопрос Вас интересует?\n")
        print(choice(ANSWERS))

        if not ask_to_continue():
            print(f"До встречи, {user_name}! Возвращайся, если возникнут вопросы.")
            break


if __name__ == "__main__":
    main()
