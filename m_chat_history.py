import json
import os

FILE_NAME = "chat_history.json"


def load_history():

    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_chat(question, answer):

    history = load_history()

    history.append(
        {
            "question": question,
            "answer": answer
        }
    )

    with open(FILE_NAME, "w") as file:

        json.dump(
            history,
            file,
            indent=4
        )