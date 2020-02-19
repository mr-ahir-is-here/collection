di={'0': 'T,9F', '1': 'm59;', '2': ',}.R', '3': 'CT}h', '4': 'E ?$', '5': 'Sv 5', '6': '=3T]', '7': 'IWev', '8': 'J\nT=', '9': 'Nz%9', 'a': 'VR~7', 'b': 'N\te4', 'c': 'x757', 'd': '6!5\n', 'e': 'O?9p', 'f': 'k7Cb', 'g': 'w<ay', 'h': '*sPY', 'i': '"86y', 'j': 'Ca}6', 'k': '#iU0', 'l': 'V=!=', 'm': 'pv%t', 'n': 'h@_O', 'o': 'KIU,', 'p': '-`=H', 'q': 'w6*!', 'r': '`^XM', 's': 'B&~~', 't': '+!PJ', 'u': 'swo"', 'v': '[j+.', 'w': ';|b&', 'x': '%%&^', 'y': 'nhG ', 'z': '{cr!', 'A': '@PA|', 'B': '>VHw', 'C': 'P%#w', 'D': 'U\x0cTv', 'E': 'Ae]7', 'F': 'O|*-', 'G': 'J,A ', 'H': 'wJv<', 'I': '%w)+', 'J': '~CWd', 'K': '4[$>', 'L': '?:v6', 'M': 'N\x0c^t', 'N': 'Wq5P', 'O': 'e@si', 'P': 'CJ*Q', 'Q': ' I=&', 'R': 'w\x0br.', 'S': '>m=|', 'T': '$`B\x0c', 'U': '=g$6', 'V': '|3MZ', 'W': '.".\'', 'X': 'e"Pm', 'Y': 'L#- ', 'Z': ',jl1', '!': 's$e ', '"': 'J^*]', '#': 'w!.n', '$': '0\x0b7\r', '%': '+k\\$', '&': '(y6P', "'": '\\b<<', '(': '(wAZ', ')': '+ ey', '*': '*kmE', '+': 'EG&8', ',': 'J;x0', '-': ':Cop', '.': '+{Z6', '/': '\\0)x', ':': '*%fx', ';': '&1$x', '<': 'J.SY', '=': '?}Ij', '>': '?;Ip', '?': '>z]q', '@': 'O7Kz', '[': 'BW\x0c?', '\\': 'c{tX', ']': 'Aqad', '^': 'yV\x0c\x0b', '_': '`]~C', '`': ']\\v^', '{': 'aOsy', '|': '.l1G', '}': 'qLNp', '~': '5dBo', ' ': '%O\x0c@', '\t': "Zx'G", '\n': 'WTc:', '\r': 'R\x0b(t', '\x0b': '~{AU', '\x0c': 'wHg '}
def insert():
    domain=input('enter domain')
    user=input('user')
    pas=input('pass')
    s=domain+"||"+user+"||"+pas+'\n'
    z=''
    for ii in s:
        z+=di[ii]
    x= open('enc','a')
    x.write(z)
    x.close()
def read():
    b=open('enc','r').read()
    inu=0
    z,data=[],[]
    pri=''
    for ii in range(len(b)//4):
            z.append(b[inu:inu+4])
            inu+=4
    for item in z:
        pri+=(list(di.keys())[list(di.values()).index(item)])
    pri=pri[:len(pri)-1]
    for i in pri.split('\n'):
            data.append(i.split('||'))
    for i in data:
            print('--------------------')
            for ii in i:
                    print(ii)
            print("--------------------")
