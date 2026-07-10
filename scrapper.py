import requests
from bs4 import BeautifulSoup


def search_incruit(keyword):
    url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    lis = soup.find_all("li", class_="c_col")
    jobs=[]

    for li in lis:
        company=li.find("a",class_="cpname").text
        title=li.find("div",class_="cell_mid").find("div",class_="cl_top").find("a").text
        location=li.find("div",class_="cl_md").find_all("span")[0].text
        link=li.find("div",class_="cell_mid").find("div",class_="cl_top").find("a").get("href")
        
        job_data={
            "company":company,
            "title":title,
            "location":location,
            "link":link
        }
        jobs.append(job_data)

    return(jobs)

def search_saramin(keyword):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    url = f"https://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=recently&searchword={keyword}"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    lis = soup.find_all("div", class_="item_recruit")
    jobs=[]
    

    for li in lis:
            company = li.find("strong", class_="corp_name").text
            title = li.find("h2", class_="job_tit").find("a").text
            location = li.find("div", class_="job_condition").find("span").text
            link = li.find("h2", class_="job_tit").find("a").get("href")

            job_data = {
                "company": company,
                "title": title,
                "location": location,
                "link" : "https://www.saramin.co.kr" + li.find("h2", class_="job_tit").find("a").get("href")
            }

            jobs.append(job_data)

    return jobs



