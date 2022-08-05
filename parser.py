import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# Job listings are listed under the resultsContainer
results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_="card-content")

# iterate through all jobs


def find_all_jobs():
    for job_element in job_elements:
        title = job_element.find("h2", class_="title")
        company = job_element.find("h3", class_="company")
        location = job_element.find("p", class_="location")


        # print(title.text.strip(), company.text.strip(), location.text.strip())
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower())

# python_jobs only got the h2 tag that mentioned the keyword, "python." It is three generations down from the parent job card, so to get the card with all the job info, we have to call job.parent.parent.parent to get to the root.

python_job_elements = [job.parent.parent.parent for job in python_jobs]

for job in python_job_elements:
    links = job.find_all("a")
    # First link is just a learn more link, the second one is the actual job
    link = links[1]
    link_url = link["href"]
    print(f'Apply here: {link_url}\n')
