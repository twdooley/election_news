
from bs4 import BeautifulSoup
import requests
import pandas as pd
from fake_useragent import UserAgent
import time
import random
from datetime import datetime


def get_links(start,stop, scrape_num):
	urls = []
	for i in range(start,stop+1):
		ua = UserAgent()
		user_agent = {'User-agent': ua.random}
		if i == 1:
			page_num = ""
		else:
			page_num = f"page/{i}"
		url = f'https://www.breitbart.com/2020-election/{page_num}'
		response = requests.get(url, headers = user_agent)
		page = response.text
		soup = BeautifulSoup(page, 'lxml')
		link_lst = soup.find('section', class_='aList')
		values = []
		for a in link_lst.find_all('a', href=True):
			value = a['href']
			if '/author/' not in value:
				if value not in values:
					values.append(value)
		values_df = pd.Series(values)
		urls.append(values_df)
	url_df = pd.concat(urls)
    
	prev_df = pd.read_csv(f'breit{scrape_num}.csv')
	stopper = prev_df.iloc[0,3]
	dfs = []
	for row in range(len(url_df)):
		req_headers = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.8',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
		link_art = f'https://www.breitbart.com{url_df.iloc[row]}'
		#time.sleep(4+2.2*random.random())
		print(link_art)
		response_url = requests.get(link_art, headers = req_headers)
		if response_url.status_code != 200:
			#raise ValueError("Website unresponsive")
			print(f'#{row} unresponsive')
			print(response_url.status_code)
			continue
		page_url = response_url.text
		soup_url = BeautifulSoup(page_url, 'lxml')
		author = ''
		date = ''
		dt = ''
		for item in soup_url.find('div', class_='header_byline'):
			auth = item.find('a', title= True)
			if auth is not None:
				author = auth.text
			if item.has_attr('datetime'):
				date = item.text
				dt = item.get('datetime')
		title = soup_url.find('h1').text
		article = soup_url.find('div', class_='entry-content').text
		article = article.replace('\n', ' ')
		if title == stopper:
			dfx = pd.DataFrame(dfs)
			now = datetime.now()
			current_time = str(now.strftime("%m_%d_%H_%M_%S"))
			return dfx.to_csv(f'{current_time}update.csv')
		else:
			indiv_art = {'dt':dt, 'date': date, 'title': title, 'author': author, 'article': article}
			dfs.append(indiv_art)
	dfx = pd.DataFrame(dfs)
	return dfx.to_csv(f'{start}_{stop}.csv')
get_links(1,25,30)

