#coding="utf-8"
from smtplib import SMTP
from bs4 import BeautifulSoup
from requests import get,exceptions,Session
from json import load,dump
from dotenv import load_dotenv
from os import system,getenv
from time import sleep
from numpy import zeros,mean
from random import choice

dongu=1
hataSayi=0
load_dotenv("bs_4.env")
myMailAdress = getenv("EMAIL_ADDRESS")
password = getenv("EMAIL_PASSWORD")
beklenecekSaniye=30
dosyaListSıra=0
maillist=[
"alikucuk27@hotmail.com",
"15541554zaza@gmail.com"]
# Proxy sözlüğü
proxies = {
    'http': 'socks5://127.0.0.1:9150',
    'https': 'socks5://127.0.0.1:9150',
}
cookies = {
    'JSESSIONID': '13F38F02DC992028565C6C813C7244E7.accstorefront-7f87d59ff9-q9klg',
    'userCartInfo': '0-0-0',
    'RMAUserID': 'b50fbe43-7243-4efe-82ce-958710d15704',
    'anonymous-consents': '%5B%5D',
    'ROUTE': '.accstorefront-7f87d59ff9-q9klg',
    'mnuid': 'HwMEd2cCiImASkpaAwdhAg==',
    '__cf_bm': 'RQ1ZquGDFYz9bYJZBJ.LyKtUa30VO62PynPDUTZDeUI-1728219273-1.0.1.1-flWDlUomWqHLAcl5PmHyg_Vh6vLQDUVLJarDumKk33EC4AKv1rOy5O4QU5hcgAouBfaHJStbbKH1kOXUtZd26g',
    '_cfuvid': 'FrVIPniNrWS5Jd0XGFsg2VVH8frezi4Im9znw5iqgHo-1728219273614-0.0.1.1-604800000',
    '_gcl_aw': 'GCL.1728219274.Cj0KCQjw6oi4BhD1ARIsAL6pox2BfzR4vCGP6o8YD7XDOoei-4KM6PwOpOFEaTnMS1hgR81jtQART4kaAq1rEALw_wcB',
    '_gcl_dc': 'GCL.1728219274.Cj0KCQjw6oi4BhD1ARIsAL6pox2BfzR4vCGP6o8YD7XDOoei-4KM6PwOpOFEaTnMS1hgR81jtQART4kaAq1rEALw_wcB',
    '_gcl_gs': '2.1.k1$i1728219273',
    '_gcl_au': '1.1.471876139.1728219274',
    'pfx_lastclick': 'adwords',
    '_fbp': 'fb.1.1728219273825.295751618886650226',
    '_sgf_user_id': '-428746128047652863',
    '_sgf_session_id': '-428746128047652864',
    'cto_bundle': 'sKDC_V9CYjY3TmNublhiTWlweFl1a251JTJCRHN4NGNCJTJGMFZOY0x0MjZNVk5JbGhrQ0I4c3NUcUUyNWhsOHRBSjBRTHVENlUlMkI0TTkyelA1MGNQWUZGOGd2WGRSUE1CS0tDRzd6YlcwOXpsMGsxQlpaVVdWNTYxVjhsZU4wQUo1TTF4VXUlMkYwd0tOc0NSbGl6RkFLS25XRCUyRmJ3UnNmZCUyRkJUSFU2WUNNa1ViJTJCcEw0bTdYNkwlMkYlMkJteCUyRkU4NlRtZWlTSXg0cmJSalVIczJRdGslMkI0VXk0V05zMiUyQlZCNmRBJTNEJTNE',
    '_sgf_exp': '',
    '_pk_ref.1.1357': '%5B%22Search%20%2F%2F%20Brand%20%2F%2F%20Exact%22%2C%22%22%2C1728219274%2C%22%22%5D',
    '_pk_id.1.1357': '242156cdea68a4b5.1728219274.',
    '_pk_ses.1.1357': '1',
    '_ga': 'GA1.1.682791908.1728219274',
    '_uetsid': '1bc28cb083e211efaaa213c7af2fa8dd|9et78x|2|fps|0|1740',
    '_clck': '1dh6dn9%7C2%7Cfps%7C0%7C1740',
    '_ga_K72QB8D6RV': 'GS1.1.1728219274.1.0.1728219274.60.0.3883017',
    '_clsk': 'm1glz%7C1728219274657%7C1%7C0%7Cx.clarity.ms%2Fcollect',
    '__rtbh.uid': '%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%2213F38F02DC992028565C6C813C7244E7.accstorefront-7f87d59ff9-q9klg%22%7D',
    '_tt_enable_cookie': '1',
    '_ttp': 'smux_cQn2rGoeQU4ZPXHkxsZ4MB',
    '_uetvid': 'ad0acc10692c11ee9596ad0a577a9eec|1x0328u|1728219274926|2|1|bat.bing.com/p/insights/c/x',
    '_ga_6FW5RQ62HT': 'GS1.1.1728219274.1.0.1728219277.57.0.0'
}

url="https://www.teknosa.com"
urlList=[
"https://www.teknosa.com/outlet?s=%3Arelevance%3Acategory%3A101001%3Abrand%3A2008&text=",
"https://www.teknosa.com/outlet?s=%3AbestSellerPoint-desc%3Acategory%3A116004&text=",
"https://www.teknosa.com/outlet?s=%3Arelevance%3Acategory%3A117%3Abrand%3A2179&text=",
"https://www.teknosa.com/outlet?s=%3Arelevance%3Acategory%3A100%3Acategory%3A100001%3ApriceValue%3Amin-100000&text=",
"https://www.teknosa.com/outlet?sort=price-desc&s=%3Arelevance%3Acategory%3A101001%3Abrand%3A2489%3ApriceValue%3Amin-100000",
"https://www.teknosa.com/outlet?s=%3Arelevance%3Acategory%3A117%3Abrand%3A2306&text=",
"https://www.teknosa.com/outlet?s=%3Arelevance%3Acategory%3A116%3Acategory%3A116006&text="
]
urlListlen=len(urlList)
dosyaList=["tcltv.txt","pc.txt","dyson.txt","telefon.txt","samsungtv.txt","karcher.txt","oyunpc.txt"]
urunSayisi=zeros(len(urlList),dtype=int)
headers = [
    {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15"
    },
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    },
    
    {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"
    },
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:90.0) Gecko/20100101 Firefox/90.0"
    },
    {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
    },
    {
        "User-Agent": "Mozilla/5.0 (Linux; Ubuntu 20.04; rv:87.0) Gecko/20100101 Firefox/87.0"
    },
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"
    },
    {
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36"
    },
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
    },
    {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Nexus 5X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36"
    }
]

##############################################################################>
##############################################################################>
##############################################################################>
##############################################################################>
##############################################################################>

def sendToMail(self,i,send):
    pass
    # i=f"{self[1]} {self[2]} {i}\n\nDÖNGÜ:{dongu} teknosa_bot tarafından gonderildi"
    # konu=self[0]
    # server=SMTP("smtp.gmail.com","587")
    # server.starttls()
    # server.login(myMailAdress,password)
    # server.sendmail(myMailAdress,send,f"Subject:{konu}\n\n{i}".encode('utf-8'))
    # server.close()
def temizle():
    system("clear")
def dosya(liste,yontem,islem):
    with open(liste,yontem,encoding="utf-8") as file:
        if islem=="kur":
            pass
        elif islem=="oku":
            global rediction
            rediction=load(file)
        elif islem=="yaz":
            dump(diction,file,allow_nan=True)
        else:
            print("hatali islem")
def yaz(yazılacak):
    print(yazılacak)
def veriKazi(sayfa):
    html=Session().get(urlList[dosyaListSıra]+"&page="+str(sayfa),headers={"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"},allow_redirects=False,timeout=10)
    soup=BeautifulSoup(html.content,"lxml")
    return soup
def kontrol(tipi):
    if tipi=="EKLENEN":
        sozluk1=diction
        sozluk2=rediction
    elif tipi=="SILINEN" or "FIYAT":
        sozluk1=rediction
        sozluk2=diction
    else:
        yaz("hatali islem")
        return
    if tipi=="FIYAT":
        for i in sozluk1:
            for a in sozluk2:
                if i.count(a)==1:
                    if sozluk1[i][1]!=sozluk2[a][1]:
                        tip=["YENI FIYAT",sozluk1[i][0],f"\nYeni fiyat: {sozluk2[i][1]}\nEski fiyat: {sozluk1[i][1]}\nOrtalama fiyat: {webPrice(sozluk1[i][0])}\n"]
                        yaz(f"{tip[0]} {i} FIYAT {tip[1]}\n{tip[2]}\n")
                        mail(tip,i)
                        break
        return
    for i in sozluk1:
        abc=0
        for a in sozluk2:
            if i.count(a)==1:
                abc+=1
        if abc==0:
            tip=[tipi,sozluk1[i][0],f"\nFiyat: {sozluk1[i][1]}\nOrtalama fiyat: {webPrice(sozluk1[i][0])}\n"]
            yaz(f"{tip[0]} {i} FIYAT {tip[1]}\n{tip[2]}\n")
            mail(tip,i)
def mail(tip,i):
    for liste in maillist:
        sendToMail(tip,i,liste)
def bekle(saniye):
    sleep(saniye)
def sayac(saniye):
    global dosyaListSıra
    dosyaListSıra=0
    while 0!=saniye:
        bekle(1)
        temizle()
        print(f"Yeni döngüye kalan: {saniye}\nDöngü: {dongu}")
        saniye-=1
def urunSayi():
    bilgi=veriKazi(0).find("h2",{"class":"hidden"}).string
    urunSaysı=int(bilgi.strip("Outlet ürünleri için  adet ürün bulundu"))
    return urunSaysı
def urunSayiKontrol():
    temizle()
    print(f"{kategoriName} ürün sayısı kontrol ediliyor...\nToplam adım: {urlListlen}\nAdım: {str(dosyaListSıra+1)}")   
def webPrice(isim):
    while True:
        try:
            html3 = get(f'https://www.google.com/search?q={isim}&tbm=shop').content
            soup3 = BeautifulSoup(html3, "html.parser")
            liste3 = list()
            for i in soup3.find_all("span", {"class": "HRLxBb"}):
                liste3.append(int(''.join(filter(str.isdigit, i.text))[:-2]))
        except:
            pass
        else:
            sonuc=str(mean(liste3,dtype=int))
            if len(sonuc)>3:
                return sonuc[:-3]+"."+sonuc[-3:]+",00 TL"
            else:
                return sonuc+",00 TL"
##############################################################################>
##############################################################################>
##############################################################################>
##############################################################################>
##############################################################################>


# sendToMail(["OPEN FILE","",""],"",maillist[1])
while True:
    try:
        while dosyaListSıra!=len(urlList):
            try:
                kategoriName=veriKazi(0).find_all("button",{"class":"filter-delete"})[-1].text.strip()
            except:
                pass
            if (urunSayisi[dosyaListSıra]!=urunSayi()) or (dongu%15==0):
                urunSayiKontrol()
                urunSayisi[dosyaListSıra]=urunSayi()
                temizle()
                diction={}
                sayfa=0
                bilgi=veriKazi(0).find("h2",{"class":"hidden"}).string
                urunSaysı=int(bilgi.strip("Outlet ürünleri için  adet ürün bulundu"))
                dosya(dosyaList[dosyaListSıra],"r","oku")
                yaz(kategoriName+" "+bilgi)
                bulunanUrun=0
                dogru=True
                while dogru:
                    indeks=0
                    productContainer=veriKazi(sayfa).find("div",{"class":"products"})
                    soup_isim=productContainer.find_all("h3",{"class":"prd-title prd-title-style"})
                    soup_fiyat=productContainer.find_all("span",{"class":"prc prc-last"})
                    soup_link=productContainer.find_all("a",{"class":"prd-link"})
                    link_lst=[]
                    fiyat_lst=[]
                    isim_lst=[]
                    for link in soup_link:
                        link=link.get("href")
                        link_lst.append(link)
                    for fiyat in soup_fiyat:
                        fiyat=fiyat.string.strip()
                        fiyat_lst.append(fiyat)
                    for isim in soup_isim:
                        isim=isim.string.strip()
                        isim_lst.append(isim)
                    for link in link_lst:
                        diction[url+link]=[isim_lst[indeks],fiyat_lst[indeks]]
                        indeks+=1
                        bulunanUrun+=1
                        temizle()
                        yaz(f"{kategoriName} {bilgi} döngü: {dongu}\nUrun: {bulunanUrun}")
                        if bulunanUrun>urunSaysı+1:
                            raise exceptions.HTTPError("Request HTTPError hatasi.")
                        if len(diction)==urunSaysı:
                            dogru=False
                            break
                    bekle(5)
                    sayfa+=1
                kontrol("EKLENEN")
                kontrol("SILINEN")
                kontrol("FIYAT")
                dosya(dosyaList[dosyaListSıra],"w","yaz")
                dosyaListSıra+=1
            else:
                urunSayiKontrol()
                dosyaListSıra+=1
                continue
        dongu+=1
        sayac(beklenecekSaniye)
    except exceptions.HTTPError as hata:
        urunSayisi[dosyaListSıra]=0
        sendToMail(["HATA",kategoriName," "],hata,maillist[1])
        yaz(hata)
    except Exception as hata:
        urunSayisi[dosyaListSıra]=0
        yaz(hata)
    