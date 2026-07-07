import json
import os

FILE_NAME = "study_history.json"


def save_study_plan(
    subject,
    roadmap
):

    data = []

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as file:

            try:
                data = json.load(file)

            except:
                data = []

    data.append(
        {
            "subject": subject,
            "roadmap": roadmap
        }
    )

    with open(FILE_NAME, "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )


def get_study_history():

    if not os.path.exists(FILE_NAME):

        return []

    with open(FILE_NAME, "r") as file:

        return json.load(file)