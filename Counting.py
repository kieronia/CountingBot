import requests,time,os
token1 = "123" #insert user token string - this gives access to your accs so never give it away to randoms etc
token2 = "ABC" #^^^ - use google to find out how to get it - go in inspect element, local storage, scroll to the bottom, control R and copy the token quickly
channelid = "1234512345" #use discord devlopers mode and right click it or copy the last number of the url when looking in that channel in a browser
number = int(1) #set this to whatever chat is at 



while True:
	headers = {'Authorization': token1, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
	number_send = requests.post(f'https://discordapp.com/api/v6/channels/{channelid}/messages', json={'content': number}, headers=headers).status_code
	if number_send == 200:
		print(f"'{number}' Sent successfully from account 1!")
		os.system(f"title Currently at Number {number}")
		number = int(number)
		number = number + 1
		number = str(number)
	else:
		input("Error - Check Channel ID Is Valid And Tokens Are Valid And That You Have A Stable Internet Connection!\n>")
	time.sleep(15)
	headers = {'Authorization': token2, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
	number_send = requests.post(f'https://discordapp.com/api/v6/channels/{channelid}/messages', json={'content': number}, headers=headers).status_code
	if number_send == 200:
		print(f"'{number}' Sent successfully from account 2!")
		os.system(f"title Currently at Number {number}")
		number = int(number)
		number = number + 1
		number = str(number)
	else:
		input("Error - Check Channel ID Is Valid And Tokens Are Valid And That You Have A Stable Internet Connection!\n>")

	time.sleep(15)#sure u can speed the process up but might get tokens require verification or get them disabled
