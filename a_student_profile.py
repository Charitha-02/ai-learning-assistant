import json
import os

FILE_NAME = "student_profile.json"


def save_profile(
    name,
    course,
    year,
    preferred_language,
    study_hours,
    goal
):

    profile = {
        "name": name,
        "course": course,
        "year": year,
        "preferred_language": preferred_language,
        "study_hours": study_hours,
        "goal": goal
    }

    with open(FILE_NAME, "w") as file:

        json.dump(
            profile,
            file,
            indent=4
        )


def load_profile():

    if not os.path.exists(FILE_NAME):

        return None

    with open(FILE_NAME, "r") as file:

        return json.load(file)