
from bs4 import BeautifulSoup
import requests
import json
import os 


pagenumber = str(1014)


def createList(r1, r2):
    return [item for item in range(r1, r2+1)]

def link_extract(list_of_range):
	targetset = []
	for num in list_of_range:
		print('processing {}'.format(num))
		url = 'https://www.isin.ru/ru/ru_isin/news_c/?keyword22=&search=%CD%E0%E9%F2%E8&only_title22=on&afrom22=01.06.2004&ato22=23.06.2022&NEWS_THEME_ID22=&form_is_submit22=1&page22={}'.format(num)
		r = requests.get(url)
		soup = BeautifulSoup(r.content, 'html.parser')
		links = [a.get('href') for a in soup.find_all('a', href=True)]
		for link in links:
			if '?id22' in link:
				targetset.append(link)
	filename = 'range_{}_{}.json'.format(list_of_range[0],list_of_range[-1])
	with open(filename, 'w') as jsonfile:
		json.dump(targetset, jsonfile)
	return jsonfile





# takes security url id as arg
def existence(sec_id, sec_data):
	sec_id = sec_id[1:]
	filename = '{}.json'.format(sec_id)
	file_exists = os.path.exists(filename)
	if file_exists == False:
		with open(filename, 'w') as jsonfile:
			json.dump(sec_data, jsonfile)
			print('{} forged'.format(sec_id))
	return()



def data_extractor(list_of_ids):
	for sec_id in list_of_ids:
		filename = '{}.json'.format(sec_id)
		file_exists = os.path.exists(filename)
		if file_exists == False:
			site = 'https://www.isin.ru/ru/ru_isin/news_c/{}'.format(sec_id)
			r = requests.get(site)
			soup = BeautifulSoup(r.content, 'html.parser')
			data = soup.find('td', class_='content')
			sec_data = str(data.text)
			with open(filename, 'w') as jsonfile:
				json.dump(sec_data, jsonfile)
				print('{} forged'.format(sec_id))
	return(site)



def targets():
	old = open('range_871_1014.json')
	new = open('range_0_870.json')
	list_of_ids = json.load(new)
	return(list_of_ids)


