# get-configs

the point of this project is to collect free v2ray configs from telegram channels and put them inside an html file that can be used as a subscription link for softwares like nekoray

if you dont know how to use these files here is a summary of what you have to do:

first you have to have a telegram account and get API ID and API Hash of the account and replace them in /collecting configs/getConfigs.py

there are some libreries like telethon and flask and... that you have to install in order to run the python app

after you installed them you can run getConfigs.py(it will get your telegram number and a code to log you in for the frist time of running it and thats normal)

it will start to fetch the messages from the channel id that you replaced in the getConfigs.py and it will be waiting for new messages

you collected messages already and you can use the api but if you wnat to create the subscription link you should replace API link in the /subscription link/fetchConfigs.js and run a local server inside /subscription link/

hope it helps 😘
