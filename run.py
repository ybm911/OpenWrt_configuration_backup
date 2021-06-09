import requests, re, sys, yaml
from bs4 import BeautifulSoup

if sys.argv[1] == "-c":
    pass
else:
    sys.exit()
config_file = sys.argv[2]

with open(config_file, 'r') as config:
    information = yaml.load(config.read(), Loader=yaml.FullLoader)
    ip = information['ip']
    password = information['password']
    username = information['username']

session = requests.session()

burp0_url1 = "http://" + ip + "/"
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36/8mqQhSuL-09", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://" + ip + "", "Connection": "close", "Referer": "http://" + ip + "/", "Upgrade-Insecure-Requests": "1"}
burp0_data1 = {"luci_username": username, "luci_password": password}
re1 = session.post(burp0_url1, headers=burp0_headers, data=burp0_data1)


burp0_url2 = "http://" + ip + "/cgi-bin/luci/admin/system/flashops"
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36/8mqQhSuL-09", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Referer": "http://" + ip + "/cgi-bin/luci/admin/system/flashops", "Upgrade-Insecure-Requests": "1"}
re2 = session.get(burp0_url2, headers=burp0_headers)
token_html_soup = BeautifulSoup(re2.text, "html.parser")
send_token = token_html_soup.find_all('form', class_ = 'inline')[0].find('input')['value']


burp0_url3 = "http://" + ip + "/cgi-bin/luci/admin/system/flashops/backup"
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36/8mqQhSuL-09", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://" + ip + "", "Connection": "close", "Referer": "http://" + ip + "/cgi-bin/luci/admin/system/flashops", "Upgrade-Insecure-Requests": "1"}
burp0_data2 = {"token": send_token, "backup": "%E7%94%9F%E6%88%90%E5%A4%87%E4%BB%BD"}
backup_binary = session.post(burp0_url3, headers=burp0_headers, data=burp0_data2)
backup_name = backup_binary.headers['Content-Disposition']
re_backup_name = re.compile(r'backup-OpenWrt-(.*).tar.gz')
# print backup_name
backup_name = re_backup_name.search(backup_name).group(0)
print(backup_name)
with open(backup_name, "wb") as mid:
    mid.write(backup_binary.content)
