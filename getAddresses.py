from bs4 import BeautifulSoup
import requests

shops = ["Boxcar+Social", "Nutbar+(Assembly+Chef's+Hall)", "Versus+Coffee", "Odin+Cafe+Bar", "Blackrock+Coffee+(now+closed)", "Manic+Coffee", "Strange+Love+Coffee",
         "Dark+Horse+Espresso+Bar", "Quantum+Coffee", "Hopper+Coffee", "Reunion+Island", "Hailed+Coffee", "Empire+Espresso", "Marvel+Coffee+Co", "Soul+Chocolate",
         "Hot+Black+Coffee", "Gloria+Espresso+and+Coffee+Bar", "Hale+Coffee", "Field+Trip+Coffee+and+Espresso", "Tampered+Press", "i+deal+coffee", "Baker+and+Scone",
         "Capital+Espresso", "Fix+Coffee+Bikes", "Death+in+Venice+Gelato+Company", "Cherry+Bomb", "Rooster+Coffee", "Lit+Espresso+Bar", "Full+of+Beans", "Cygnet+Coffee",
         "Merchants+of+Green+Coffee", "Early+Bird+Coffee+and+Kitchen", "The+Brockton+Haunt", "Run+&+Gun+Coffee", "Bud's+Coffee+Bar", "Cafe+Plenty", "Soma+Chocolatemaker",
         "Thor+Espresso+Bar", "Mercury+Espresso+Bar", "Red+Rocket+Coffee", "Propeller+Coffee+Co", "Bicerin+Espresso+Bar", "Creeds+Coffee+Bar", "Jimmy's+Coffee", "FIKA+Cafe",
         "Dogs+and+Coffee+(now+closed)", "Livelihood+Café", "Extra+Butter+Coffee", "Soufi's", "Neo+Coffee+Bar", "Major+Treat+Coffee", "The+Library+Specialty+Coffee",
         "Dineen+Coffee+Co", "Brodflour", "French+Made", "Piedmont+Coffee+Bar", "Black+Canary+Espresso", "Mast+Coffee", "Bampot+Bohemian+House+of+Tea", "Simit+and+Chai",
         "Agenda+Cafe", "Te+Aro", "Coffee+and+Clothing", "Shy+Coffee+Co", "Jacked+Up+Coffee", "Tandem+Coffee", "De+Mello+Palheta+Specialty+Coffee+Roasters", "Little+Pebbles",
         "The+Merseyside", "Milky's+Coffee", "Pilot+Coffee+Roasters", "Bluestone+Lane+Downtown+Coffee+Shop", "Wallace+Espresso", "Ella's+Uncle", "Outpost+Coffee+Roasters",
         "Ezra's+Pound", "First+&+Last+Coffee+Shop", "The+Good+Neighbour", "Krave+Coffee", "Sam+James+Coffee+Bar", "Moonbean+Coffee+Company", "Safehouse+Coffee", "Cops+Toronto",
         "Cafe+Con+Leche", "Clove+Apple+Cafe", "The+Abbott+of+Parkdale", "Cozy+Coffee+Co", "Supernova+Coffee", "Rialto+Espresso+Bar", "Happy+Coffee+and+Wine", "Black+Cat+Espresso+Bar",
         "Maderas+Cafe", "Goldstruck+Coffee", "Five+Elements+Espresso+Bar", "Rise+Espresso", "Hamers+Coffee", "Forget+Me+Not+Cafe", "Le+Gourmand"]

className = 'LrzXr'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
tag = 'span'
nameAddress = {}

for shop in shops:
    url = 'https://google.ca/search?q=' + shop + '+toronto'

    print('Currently getting ' + shop.replace('+', ' ') + ' address')

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    address = soup.find('span', class_='LrzXr')

    if address == None:
        print('Address didn\'t resolve')
        nameAddress[shop.replace('+', ' ')] = 'none'
    else:
        print(shop.replace('+', ' ') + ' address is ' + str(address.text))
        nameAddress[shop.replace('+', ' ')] = str(address.text)

print(nameAddress)
