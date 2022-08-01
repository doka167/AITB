import requests
from bs4 import BeautifulSoup
jobs=[]
expYears =[]
pageCounter = 0
while True:
    urlResult = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q=php&start={pageCounter}")
    markup = urlResult.content
    bs = BeautifulSoup(markup,'lxml')
    jobHeadings = bs.find_all('h2',{"class":"css-m604qf"})
    #jobAnchors = bs.find_all('a' , {"class": "css-o171kl"})
    #jobLocation = bs.find_all('span', {"class" :"css-5w"})
    experinceYears = bs.find_all('span')
    if jobHeadings == [] :
        break
    for i in jobHeadings:
        jobs.append(i.text)
    for i in experinceYears:
        if "Exp" in i.text:
            expYears.append(i.text)
    jobHeadings = []
    pageCounter+=1




with open('jobs.txt' , 'w') as jobsFile:
    for job in jobs:
        jobsFile.write(job)
    print("jobs added successfully")
    
with open('experince.txt' , 'w') as ExpFile:
    for exp in expYears:
        ExpFile.write(exp)
    print("EXP added successfully")


with open('jobs.txt' , 'r') as JobsFile:
    print(JobsFile.read())
        
print("------------------------------------------------------------------------")

with open('experince.txt' , 'r') as ExpFile:
    print(ExpFile.read())
        








