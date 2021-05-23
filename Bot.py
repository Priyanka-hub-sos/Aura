import webbrowser as wb
url=input("wanna hangout in science or world or something you are passionate about? sceince/passion")

science='https://www.britannica.com/science/life'
passion='https://www.merriam-webster.com/dictionary/passion'

if url[0] == 's' or url[0]== 'S':
    wb.open_new(science)
elif url[0]=='p' or url[0]== 'P':
    wb.open_new(passion)
else:
    print("please choose between science or passion")