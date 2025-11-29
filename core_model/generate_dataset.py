import random
import pandas as pd

rows = 200  # number of samples

data = []

for _ in range(rows):
    time_on_page = random.randint(5, 180)
    pages_visited = random.randint(1, 10)
    idle_time = random.randint(0, 60)
    click_count = random.randint(0, 15)
    scroll_depth = random.randint(0, 100)
    return_visitor = random.randint(0, 1)
    sentiment_score = random.choice([-1, 0, 1])
    message_length_avg = random.randint(1, 40)
    negative_keywords = random.randint(0, 5)
    response_delay = random.randint(0, 20)
    device_type = random.choice(["mobile", "desktop"])
    first_visit = 1 - return_visitor

    # simple rule to generate realistic risk
    if idle_time > 40 or sentiment_score == -1 or negative_keywords >= 3:
        dropoff_risk = "High"
    elif idle_time > 20 or pages_visited <= 2:
        dropoff_risk = "Medium"
    else:
        dropoff_risk = "Low"

    data.append([
        time_on_page, pages_visited, idle_time, click_count, scroll_depth,
        return_visitor, sentiment_score, message_length_avg,
        negative_keywords, response_delay, device_type,
        first_visit, dropoff_risk
    ])

df = pd.DataFrame(data, columns=[
    "time_on_page","pages_visited","idle_time","click_count","scroll_depth",
    "return_visitor","sentiment_score","message_length_avg","negative_keywords",
    "response_delay","device_type","first_visit","dropoff_risk"
])

df.to_csv("dataset.csv", index=False)
print("Dataset generated successfully!")
