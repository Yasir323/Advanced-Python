import requests
import time
import pandas as pd
import seaborn as sns

sns.set()
base_url = 'http://jsonplaceholder.typicode.com/photos/'


def response_with_session(num_photos=500):
    start_time = time.time()
    count = 0
    session = requests.Session()
    for i in range(num_photos):
        try:
            response = session.get(base_url + str(i + 1))
            # print(response.json())
            assert response.ok == True
        except AssertionError as e:
            count += 1
    time_taken = time.time() - start_time
    print(f'Total time taken to get {num_photos - count} photos with Session: {time_taken}')
    return time_taken


def response_without_session(num_photos=500):
    start_time = time.time()
    count = 0
    for i in range(num_photos):
        try:
            response = requests.get(base_url + str(i + 1))
            # print(response.json())
            assert response.ok == True
        except AssertionError as e:
            count += 1
    time_taken = time.time() - start_time
    print(f'Total time taken to get {num_photos - count} photos without Session: {time_taken}')
    return time_taken

num_requests = [1, 10, 20, 30, 40, 50, 100, 200, 300, 400, 500, 1000, 5000]
# num_requests = [1, 10, 20]
times_without_session = []
times_with_session = []
for n in num_requests:
    times_without_session.append(response_without_session(n))
    times_with_session.append(response_with_session(n))

df = pd.DataFrame(
    list(zip(
        times_without_session,
        times_with_session)
    ),
    columns =['Time taken Without Session', 'Time taken With Session'],
    index=num_requests
)
sns_plot = sns.lineplot(data=df)
sns_plot.set(xlabel='Number of requests', ylabel='Time taken(sec)')
fig = sns_plot.get_figure()
fig.savefig("output.png")