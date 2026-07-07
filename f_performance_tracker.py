import json
import os
from datetime import datetime
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.cluster import KMeans
import numpy as np
FILE_NAME = "performance_data.json"


def save_score(
    subject,
    score,
    total,
    weak_topics=None,
    strong_topics=None
):

    percentage = round(
        (score / total) * 100,
        2
    )

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
        "score": score,
        "total": total,
        "percentage": percentage,
        "weak_topics": weak_topics or [],
        "strong_topics": strong_topics or [],
        "date": datetime.now().strftime("%Y-%m-%d")
    }
)
    with open(FILE_NAME, "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )


def get_performance():

    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def get_average_score():

    data = get_performance()

    if len(data) == 0:
        return 0

    total = 0

    for item in data:
        total += item["percentage"]

    return round(
        total / len(data),
        2
    )


def get_all_weak_topics():

    data = get_performance()

    weak_topics = []

    for item in data:

        weak_topics.extend(
            item.get(
                "weak_topics",
                []
            )
        )

    return list(
        set(weak_topics)
    )


def get_all_strong_topics():

    data = get_performance()

    strong_topics = []

    for item in data:

        strong_topics.extend(
            item.get(
                "strong_topics",
                []
            )
        )

    return list(
        set(strong_topics)
    )
def get_subject_scores():

    data = get_performance()

    subjects = {}

    for item in data:

        subject = item["subject"]

        if subject not in subjects:

            subjects[subject] = []

        subjects[subject].append(
            item["percentage"]
        )

    result = {}

    for subject, scores in subjects.items():

        result[subject] = round(
            sum(scores) / len(scores),
            2
        )

    return result
def get_learning_streak():

    data = get_performance()

    if len(data) == 0:
        return 0

    dates = []

    for item in data:

        if "date" in item:

            dates.append(
                item["date"]
            )

    return len(
        set(dates)
    )
def get_achievements():

    data = get_performance()

    achievements = []

    if len(data) >= 1:

        achievements.append(
            "🏅 First Quiz Completed"
        )

    if len(data) >= 5:

        achievements.append(
            "🥈 5 Quizzes Completed"
        )

    if len(data) >= 10:

        achievements.append(
            "🥇 10 Quizzes Completed"
        )

    average = get_average_score()

    if average >= 80:

        achievements.append(
            "🏆 Score Above 80%"
        )

    if average >= 90:

        achievements.append(
            "👑 Top Performer"
        )

    return achievements
def get_mock_interview_score():

    data = get_performance()

    if len(data) == 0:
        return 0

    average = get_average_score()

    return round(
        average * 0.9,
        2
    )
def predict_next_score():

    data = get_performance()

    if len(data) == 0:
        return None

    scores = []

    for item in data:
        scores.append(item["percentage"])

    if len(scores) == 1:
        return scores[0]

    if len(scores) == 2:
        return round(
            (scores[0] + scores[1]) / 2,
            2
        )

    recent_scores = scores[-3:]

    predicted = (
        recent_scores[-1] * 0.5 +
        recent_scores[-2] * 0.3 +
        recent_scores[-3] * 0.2
    )

    return round(predicted, 2)
def classify_learner_kmeans():

    data = get_performance()

    if len(data) < 3:

        average = get_average_score()

        if average >= 80:
            return "🟢 Advanced Learner"

        elif average >= 60:
            return "🟡 Intermediate Learner"

        else:
            return "🔴 Beginner Learner"

    scores = []

    for item in data:

        scores.append(
            item["percentage"]
        )

    X = np.array(scores).reshape(-1, 1)

    kmeans = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    kmeans.fit(X)

    latest_cluster = kmeans.predict(
        [[scores[-1]]]
    )[0]

    centers = kmeans.cluster_centers_.flatten()

    sorted_clusters = np.argsort(centers)

    if latest_cluster == sorted_clusters[0]:

        return "🔴 Beginner Learner"

    elif latest_cluster == sorted_clusters[1]:

        return "🟡 Intermediate Learner"

    else:

        return "🟢 Advanced Learner"
def classify_learner():

    average_score = get_average_score()

    if average_score >= 80:

        return "🏆 Advanced Learner"

    elif average_score >= 60:

        return "🟢 Intermediate Learner"

    else:

        return "🔴 Beginner Learner"
def calculate_placement_probability(
    average_score,
    mock_score,
    resume_score
):

    probability = (
        average_score * 0.4 +
        mock_score * 0.3 +
        resume_score * 0.3
    )

    return round(
        probability,
        2
    )