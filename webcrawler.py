from bs4 import BeautifulSoup
import requests
import mysql.connector





cnx = mysql.connector.connect(user='enro', password='sql123',
                              host='localhost',
                              database='vacancies')
cursor=cnx.cursor()


if False:
    cursor.execute("DELETE FROM jobs")  #clean the table before making a new crawling
    cnx.commit()

    #crawling Monster
    r  = requests.get("https://www.monster.se/jobb/sok/")   
    page=1
    data = r.text
    soup = BeautifulSoup(data)
    while(soup.body.find_all('article', attrs={'class':'js_result_row'})):
        for element in soup.body.find_all('article', attrs={'class':'js_result_row'}):
            company=element.find('span', attrs={'itemprop':'name'}).text
            location=element.find('span', attrs={'itemprop':'address'}).text
            title=element.find('span', attrs={"itemprop":"title"}).text
            print(company)
            print(location)
            print(title)
            query_add=("INSERT INTO jobs (TITLE, COMPANY, LOCATION, APPLIED) VALUES (%s, %s, %s, %s)")
            query_data=(title, company,location,0)
            cursor.execute(query_add,query_data)
            cnx.commit()

        page+=1
        data = r.text
        soup = BeautifulSoup(data)
        r  = requests.get("https://www.monster.se/jobb/sok/?page="+str(page))
        print("https://www.monster.se/jobb/sok/?page="+str(page))


    #crawling stepstone
    r  = requests.get("http://www.stepstone.se/lediga-jobb-i-hela-sverige/sida1/")
    data = r.text
    soup = BeautifulSoup(data)
    page=1
    while(soup.body.find_all('div', attrs={'class':'description'})):
        for element in soup.body.find_all('div', attrs={'class':'description'}):
            title=element.find('h5').text
            company=element.find('span',attrs={'class':'text-bold'}).text
            location=element.find_all('span',attrs={'class':'text-opaque'})[1].text
            print(title)
            print(company)
            print(location)     
            query_add=("INSERT INTO jobs (TITLE, COMPANY, LOCATION, APPLIED) VALUES (%s, %s, %s, %s)")
            query_data=(title, company,location,0)
            cursor.execute(query_add,query_data)
            cnx.commit()
            
        page+=1
        data = r.text
        soup = BeautifulSoup(data)
        r  = requests.get("http://www.stepstone.se/lediga-jobb-i-hela-sverige/sida"+str(page)+"/")
        print("http://www.stepstone.se/lediga-jobb-i-hela-sverige/sida"+str(page)+"/")


