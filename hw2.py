#!/usr/bin/env python
# coding: utf-8

# In[30]:


import urllib.request
from bs4 import BeautifulSoup


# ## Q1(a)

# In[33]:


seed_url = "https://press.un.org/en"

urls = [seed_url]    #queue of urls to crawl
seen = [seed_url]    #stack of urls seen so far
opened = []          #we keep track of seen urls so that we don't revisit them
saved = []
number_index = 1
maxNumUrl = 10; 
print("Starting with url="+str(urls))


# In[34]:


while len(urls) > 0 and len(saved) < maxNumUrl:
    # DEQUEUE A URL FROM urls AND TRY TO OPEN AND READ IT
    try:
        curr_url=urls.pop(0)
        print("Trying to access= "+curr_url)
        req = urllib.request.Request(curr_url,headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urllib.request.urlopen(req).read()
        opened.append(curr_url)

    except Exception as ex:
        print("Unable to access= "+curr_url)
        print(ex)
        continue    #skip code below

    # IF URL OPENS, CHECK WHICH URLS THE PAGE CONTAINS
    # ADD THE URLS FOUND TO THE QUEUE url AND seen
    soup = BeautifulSoup(webpage)  #creates object soup
    # Put child URLs into the stack
    tags = soup.find_all('a', href = True, hreflang="en")
    for tag in tags: #find tags with links
        if "Press Release" or "PRESS RELEASE" in tag.text:
            if "crisis" in soup.text.lower():
                childUrl = tag['href'] #extract just the link
                o_childurl = childUrl
                childUrl = urllib.parse.urljoin(seed_url, childUrl)
                
                if seed_url in childUrl and childUrl not in seen:
                    urls.append(childUrl)
                    seen.append(childUrl)
                    saved.append(childUrl)
                    with open("1_" + str(number_index) + ".txt",
                             "w") as file:
                        file.write(str(soup))
                        number_index += 1
                else:
                    print("######")
            else:
                print("no crisis")
        else:
            print("not press release")
        


# In[35]:


print("num. of URLs seen = %d, and scanned = %d" % (len(seen), len(opened)))
print("List of seen URLs:")
print(saved)


# ## Q1(b)

# In[36]:


base_url = "https://www.europarl.europa.eu/news/en/press-room/page/"
opened_total = [] 
opened = []
saved = []
start, end = 0, 500
maxNumUrl = 10; #set the maximum number of urls to visit


# In[37]:


for num in range(start, end + 1):  
    seed_url = f"{base_url}{num}"
    urls = [seed_url]    #queue of urls to crawl
    seen = [seed_url]    #stack of urls seen so far
       
    while len(urls) > 0 and len(opened_total) < maxNumUrl:
        # DEQUEUE A URL FROM urls AND TRY TO OPEN AND READ IT
        try:
            curr_url=urls.pop(0)
            print("num. of URLs in stack: %d " % len(urls))
            print("Trying to access= "+curr_url)
            req = urllib.request.Request(curr_url,headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urllib.request.urlopen(req).read()
            opened.append(curr_url)

        except Exception as ex:
            print("Unable to access= "+curr_url)
            print(ex)
            continue    #skip code below

        # IF URL OPENS, CHECK WHICH URLS THE PAGE CONTAINS
        # ADD THE URLS FOUND TO THE QUEUE url AND seen
        soup = BeautifulSoup(webpage)  #creates object soup
        # Put child URLs into the stack
        links = soup.find_all('a', href = True)
        for link in links: #find tags with links
            if "crisis" in soup.text.lower():
                span_tag = link.find_parent("span", class_="ep_name")
                if ("PLENARY SESSION" or "Plenary session" in span_tag.text):
                        childUrl = link['href'] #extract just the link
                        o_childurl = childUrl
                        childUrl = urllib.parse.urljoin(seed_url, childUrl)
                        if seed_url in childUrl and childUrl not in seen:
                            print("***urls.append and seen.append***")
                            urls.append(childUrl)
                            seen.append(childUrl)
                            saved.append(childUrl)
                        else:
                            print("######")
                else:
                    print("not Plenary session")
            else:
                print("no crsis")


# In[40]:


print("num. of URLs seen = %d, and scanned = %d" % (len(seen), len(opened)))
print("List of seen URLs:")
print(saved)


# In[371]:


seen_total

