import json
import os

FILE_NAME = "history_data.json"


# -----------------------------
# Load Data
# -----------------------------
def load_data():

    if not os.path.exists(FILE_NAME):

        return {
            "chat_history": [],
            "activities": []
        }

    with open(FILE_NAME, "r") as file:

        try:

            return json.load(file)

        except:

            return {
                "chat_history": [],
                "activities": []
            }


# -----------------------------
# Save Data
# -----------------------------
def save_data(data):

    with open(FILE_NAME, "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )


# -----------------------------
# CHAT HISTORY
# -----------------------------
def save_chat(question, answer):

    data = load_data()

    data["chat_history"].append({

        "question": question,
        "answer": answer

    })

    save_data(data)


def get_chat_history():

    data = load_data()

    return data.get(
        "chat_history",
        []
    )


# -----------------------------
# PDF HISTORY
# -----------------------------
def save_activity(activity_type, content, title):

    data = {
        "chat_history": [],
        "activities": []
    }

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as file:

            try:
                data = json.load(file)

            except:
                data = {
                    "chat_history": [],
                    "activities": []
                }

    if "activities" not in data:

        data["activities"] = []

    data["activities"].append(
        {
            "type": activity_type,
            "title": title,
            "content": content
        }
    )

    with open(FILE_NAME, "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )
def get_activities():

    data = load_data()

    return data.get(
        "activities",
        []
    )


# -----------------------------
# DELETE
# -----------------------------
def delete_activity(index):

    data = load_data()

    if index < len(data["activities"]):

        data["activities"].pop(index)

    save_data(data)


# -----------------------------
# RENAME
# -----------------------------
def rename_activity(index, new_name):

    data = load_data()

    if index < len(data["activities"]):

        data["activities"][index]["title"] = new_name

    save_data(data)