"""By this file we will decode the crome browser history and it will be saved in History.txt
file in the same file repository withot taking error database is locked
for more information mail me at gabru.ahir@gmail.com"""
import os
import sqlite3

def Find_path():
    User_profile = os.environ.get("USERPROFILE")
    History_path = User_profile + r"\\AppData\Local\Google\Chrome\User Data\Default\History" #Usually this is where the chrome history file is located, change it if you need to.
    return History_path

def Main():
    f=open(Find_path(),'rb')
    x=open('HistoryTemp','wb')
    x.write(f.read())
    f.close()
    x.close()
    data_base = 'HistoryTemp'            
    con = sqlite3.connect(data_base) #Connect to the database
    c = con.cursor()
    c.execute("SELECT url FROM urls")
    #c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name") #Change this to your prefered query
    cc = c.fetchall()
    x=1
    for item in cc:
        print(x,'URL FOUND')
        x+=1
        st = '[+] '+item[0]+'\n'
        #print(st)
        f = open('history.txt','a')
        ddd= str(st)+'\n'
        f.write(ddd)
        f.close()
if __name__ == '__main__':
      Main()
      input('History Entered In "History.txt" \n Press Enter Key To Continue...')
      os.remove('HistoryTemp')
'''
import sqlite3
data_base = Find_path()            
con = sqlite3.connect(data_base) #Connect to the database
c = con.cursor()
c.execute("SELECT url FROM urls")
urls = c.fetchall()
print('\n'.join(urls))
'''
