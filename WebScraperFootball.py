from urllib.request import urlopen
from bs4 import BeautifulSoup
i = 0
#output_fileother = open('Probowl.csv', "a")

#symbolslist = ["aapl"]                                                        
while i < 2600:
	url_request = 'https://www.pro-football-reference.com/play-index/psl_finder.cgi?request=1&match=total&year_min=1920&year_max=2017&season_start=1&season_end=-1&pos%5B%5D=qb&pos%5B%5D=rb&pos%5B%5D=wr&pos%5B%5D=te&pos%5B%5D=e&pos%5B%5D=t&pos%5B%5D=g&pos%5B%5D=c&pos%5B%5D=ol&pos%5B%5D=dt&pos%5B%5D=de&pos%5B%5D=dl&pos%5B%5D=ilb&pos%5B%5D=olb&pos%5B%5D=lb&pos%5B%5D=cb&pos%5B%5D=s&pos%5B%5D=db&pos%5B%5D=k&pos%5B%5D=p&draft_year_min=1936&draft_year_max=2017&draft_slot_min=1&draft_slot_max=500&draft_pick_in_round=pick_overall&conference=any&draft_pos%5B%5D=qb&draft_pos%5B%5D=rb&draft_pos%5B%5D=wr&draft_pos%5B%5D=te&draft_pos%5B%5D=e&draft_pos%5B%5D=t&draft_pos%5B%5D=g&draft_pos%5B%5D=c&draft_pos%5B%5D=ol&draft_pos%5B%5D=dt&draft_pos%5B%5D=de&draft_pos%5B%5D=dl&draft_pos%5B%5D=ilb&draft_pos%5B%5D=olb&draft_pos%5B%5D=lb&draft_pos%5B%5D=cb&draft_pos%5B%5D=s&draft_pos%5B%5D=db&draft_pos%5B%5D=k&draft_pos%5B%5D=p&c1stat=pro_bowls&c1comp=gt&c1val=1&c5val=1.0&order_by=pass_td&offset=' + str(i)
	with urlopen(url_request) as htmlfile:
   	 	soup = BeautifulSoup(htmlfile)
   	 	#print(soup.find_all('tbody'))
   	 	a = soup.findAll('td')
   	 	print(a)
   	 	#while j < 100:
   	 	#a[j][0]
   	 	z =0
   	 	while z < (600):
   	 		print(a[z].text)
   	 		#print(a[z].text)
   	 		#this is the team
   	 		#print(a[4].text)
   	 		#this is the number of apperances
   	 		#print(a[5].text)
   	 		b = a[z].text
   	 		apperances = a[z + 5]
   	 		output_line = b
   	 		#output_fileother.write(b + ',' + str(apperances) + '\n')
   	 		z += 1
   	 		#z+=6	
   	 	i += 100
#output_fileother.close()


   	 	
