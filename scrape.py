from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

webdriver_path = r"C:\Users\sayhi\OneDrive\Bureau\cdriver"


def loadCards(id):
    url = 'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&view_all_page_id='+id+'&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=page&media_type=all' 
    driver = webdriver.Chrome(webdriver_path) 
    driver.get(url)
    time.sleep(5)
    endPage=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/div[6]/div[3]/div/div[1]/div/div/div/div/div')
    time.sleep(8)
    driver.execute_script("arguments[0].scrollIntoView()",endPage)
    time.sleep(10)
    block_cards = driver.find_elements(By.CSS_SELECTOR,'div.xrvj5dj.xdq2opy.xexx8yu.xbxaen2.x18d9i69.xbbxn1n.xdoe023.xbumo9q.x143o31f.x7sq92a.x1crum5w > div.xh8yej3')
    print(len(block_cards))
    return block_cards
    
def getCardInfo(card):
    data={}
# date diffusion , id , status et #platform

    content1=card.find_elements(By.CSS_SELECTOR,"div.x3nfvp2.x1e56ztr")
    for index, value in enumerate(content1):
            
        if (index ==0):
            ajout=value.find_element(By.CSS_SELECTOR,"span.x8t9es0.xw23nyj.xo1l8bm.x63nzvj.x108nfp6.xq9mrsl.x1h4wwuj.xeuugli")
            data['Status'] = ajout.text
                
        if (index == 1):
            ajout=value.find_element(By.CSS_SELECTOR,"span.x8t9es0.xw23nyj.xo1l8bm.x63nzvj.x108nfp6.xq9mrsl.x1h4wwuj.xeuugli")
            data['Date De Diffusion'] = ajout.text
        if( index == 3):
            ajout=value.find_element(By.CSS_SELECTOR,"span.x8t9es0.xw23nyj.xo1l8bm.x63nzvj.x108nfp6.xq9mrsl.x1h4wwuj.xeuugli")
            data['ID']=ajout.text
#image et video publier
    img_element = card.find_elements(By.TAG_NAME, 'img')
    vid_element = card.find_elements(By.TAG_NAME,'video')
    
    if(len(img_element)>len(vid_element)):
        data['Nom_page']=img_element[0].get_attribute('alt')
        data['Image_Publier']=img_element[0].get_attribute('src')
    if(len(img_element)==len(vid_element)):
        data['Nom_Page']=vid_element[0].get_attribute('alt')   
        data['Video_Publier']=vid_element[0].get_attribute('src')
#type
    sponsored=card.find_elements(By.CSS_SELECTOR,"div._4ik4._4ik5")
    data['type']=sponsored[0].text
#description
    description=card.find_elements(By.CSS_SELECTOR,("div._7jyr._a25- > span.x8t9es0.xw23nyj.xo1l8bm.x63nzvj.x108nfp6.xq9mrsl.x1h4wwuj.xeuugli > div > div > div"))
    if(len(description)>0):
        data['Description']=description[0].text

    return(data)

def getData(url):
    data=[]
    cards=loadCards(url)
    
    for card in cards:
          data.append(getCardInfo(card))
          

    return data  
                
data=getData('117627008288878')
print(data)
