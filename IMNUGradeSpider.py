#todo: keep alive in loginning, and get information from system.

import requests
import re



#testID and testPSD
#username = '*'
#password = '*'



# url
LoginUrl = "http://eip.imnu.edu.cn/EIP/syt/login/Login.htm"
checkCodeUrl = 'http://eip.imnu.edu.cn/EIP/syt/login/captcha.htm?code='
righturl = "http://eip.imnu.edu.cn:80/EIP/sytsso/other.htm?appId=NEWJWXT&uuid=ff8080815742d0ba015742d54b710004"
gardeUrl = "http://210.31.186.11/qbcj"

#agent
headerAgent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}



# build session
sessionBuild = requests.session()


#get check code
def getCheckCode():
    try:
        valueCode = sessionBuild.get(checkCodeUrl, headers=headerAgent)
        f = open("valueCode.png", 'wb')
        f.write(valueCode.content)
        f.close()
        code = input("CheckNumber:")
        data['verification'] = str(code)
        print(data)
    except:
        print("Wrong in getting check code.")



#post data and get text
def spiderLoginandLogin(data):
    try:
        r = sessionBuild.post(LoginUrl, data, headerAgent)
        print(r.cookies.get_dict(),r.content,r.text,r.request,r.url,r.status_code)

        r1 = sessionBuild.get(righturl, headers = headerAgent)

        r2 = sessionBuild.get(gardeUrl, headers = headerAgent)
        return r2.text
    except:
        print("Spider in dangerous!")


#filter
def filter(text):
    v = text.replace("\t", '')
    v1 = v.replace("\n", '')
    v2 = v1.replace(' ', '')
    v3 = v2.replace("\r", '')
    #print(v3)
    value = re.findall(r'<td>(.*?)</td>', v3)

    #print(value)
    #print(value[0], value[1])
    return value

if __name__ == '__main__':

    username = input("U login name:")
    password = input("U login password:")

    # data
    data = {"username": username,
            "password": password,
            "verification": ''}

    getCheckCode()
    text = spiderLoginandLogin(data)
    value = filter(text)

    #devide
    b = list()
    for i in range(0, len(value), 8):
        b.append(value[i:i+8])
    for i in range(0,int(len(value)/8)):# 总字符串数／每一list中字符串数 ＝ 总课程数
        print(b[i])
