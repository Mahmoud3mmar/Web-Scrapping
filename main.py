import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk

root = tk.Tk()
root.title('Web Scraper ')




Job_title=[]
Company_name=[]
Location=[]
Job_skill=[]
Salary=[]
Links=[]
Date=[]
Page_no=1
job=''




def Excution(Page_no):

    def process_input():
        # Get the value of the text field
        input_text = text_field.get()

    def Show_output():
        output="Pages Ended"
        label.config(text=str(output))
    job= process_input()
    while True:

        # Send an HTTP request to the web page
        response = requests.get(f'https://wuzzuf.net/search/jobs/?a=hpb&q={job}&start={Page_no}')

        # save page content /markup
        src = response.content

        # Parse the content  of the web page
        soup = BeautifulSoup(src, 'html.parser')
        Page_Limit = int(soup.find("strong").text)
        if (Page_no == Page_Limit):
            print("Pages Ended , Termiante")
            break

        # Extract the data you want to scrape
        Job_titles = soup.find_all("h2", {"class": "css-m604qf"})
        Company_names = soup.find_all("a", {"class": "css-17s97q8"})
        locations = soup.find_all("span", {"class": "css-5wys0k"})
        Job_skills = soup.find_all("div", {"class": "css-y4udm8"})
        Posted_new = soup.find_all("div", {"class": "css-4c4ojb"})
        Posted_old = soup.find_all("div", {"class": "css-do6t5g"})
        Posted = [*Posted_new, *Posted_old]

        # loop over returned lists to extract  needed info into other lists
        for i in range(len(Job_titles)):
            Job_title.append(Job_titles[i].text.strip())
            Links.append("https://wuzzuf.net" + Job_titles[i].find("a").attrs["href"])

            Company_name.append(Company_names[i].text.strip())
            Location.append(locations[i].text.strip())
            Job_skill.append(Job_skills[i].text.strip())
            Date.append(Posted[i].text)

        Page_no += 1
        Show_output()
        print("Page Switched")

    file_list = [Job_title, Company_name, Location, Job_skill, Date, Links]
    exported = zip_longest(*file_list)
    # create  csv file  and fill it with values
    with open("/Users/Mahmoud Ammar/PycharmProjects/pythonProject6/New Microsoft Excel Worksheet.csv","w") as myfile:
        Wr = csv.writer(myfile)
        Wr.writerow(["Job Title", "Company Name", "Location", "Job Skill", "Date", "Link"])
        Wr.writerows(exported)





label = tk.Label(root)
label.pack()

text_field = tk.Entry(root)
text_field.pack()


Opened_Img = ImageTk.PhotoImage(Image.open("MainWallpaper.jpg"))
myimg = Label(image=Opened_Img).pack()

Button_Excution = Button(root, text='Scrap', padx=10, pady=10, command=lambda: Excution(Page_no))
Button_Excution.pack(expand=True)


root.mainloop()