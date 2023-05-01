from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from .models import Description
from home.models import Contact,news,registration,billing

# Create your views here.


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            return render(request, 'login.html')
    # No backend authenticated the credentials
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")

# Portfolio sction starts------------------------------------------------------------>>


# Router sction start----->>

def portfoliopage(request):

    rut1 = Description()
    rut1.img = 'dir.jpg'
    rut1.name = 'DIR-615'
    rut1.link = 'desc615'

    rut2 = Description()
    rut2.img = 'r15.jpg'
    rut2.name = 'D-Link R15'
    rut2.link = 'descr15'
 

    rut3 = Description()
    rut3.img = 'r03.jpg'
    rut3.name = 'D-Link R03'
    rut3.link = 'descr03'


    rut4 = Description()
    rut4.img = 'archerc86.jpg'
    rut4.name = 'TP-Link Archer C86'
    rut4.link = 'descc86'


    rut5 = Description()
    rut5.img = 'archerc50.jpg'
    rut5.name = 'TP-Link Archer C50'
    rut5.link = 'descc50'


    rut6 = Description()
    rut6.img = 'xiaomi.jpg'
    rut6.name = 'Xiaomi Smart Router'
    rut6.link = 'descxiaomi'


    rut7 = Description()
    rut7.img = 'AC1200.jpg'
    rut7.name = 'TP-Link AC 1200'
    rut7.link = 'descac1200'


    rut8 = Description()
    rut8.img = 'dir825.jpg'
    rut8.name = 'DIR-825'
    rut8.link = 'descdir825'

    return render(request, 'port/catalog.html', {'rut1': rut1, 'rut2': rut2, 'rut3': rut3,'rut4': rut4,'rut5': rut5,'rut6': rut6,'rut7': rut7,'rut8': rut8,})

# Router sction start----->>

# Set top box sction start----->>

def portfoliopage1(request):

    rut1 = Description()
    rut1.img = 'airtel.jpg'
    rut1.name = 'Airtel DTH HD'
    rut1.link = 'airteldth'

    rut2 = Description()
    rut2.img = 'd2h.jpg'
    rut2.name = 'd2h HD DTH'
    rut2.link = 'd2hhd'
 

    rut3 = Description()
    rut3.img = 'catvision.jpg'
    rut3.name = 'Catvision'
    rut3.link = 'catvision'


    rut4 = Description()
    rut4.img = 'dishtvfree.jpg'
    rut4.name = 'Dish TV Free'
    rut4.link = 'dishtvfree'


    rut5 = Description()
    rut5.img = 'dishtvsmart.jpg'
    rut5.name = 'Dish TV Smart'
    rut5.link = 'dishtvsmart'


    rut6 = Description()
    rut6.img = 'dishtv.jpg'
    rut6.name = 'Dish TV'
    rut6.link = 'dishtv'


    rut7 = Description()
    rut7.img = 'airtelxtreme.jpg'
    rut7.name = 'Airtel Xtreme'
    rut7.link = 'airtelxtreme'


    rut8 = Description()
    rut8.img = 'd2hstreme.jpg'
    rut8.name = 'd2h Streme'
    rut8.link = 'd2hstreme'

    return render(request, 'port/catalog.html', {'rut1': rut1, 'rut2': rut2, 'rut3': rut3,'rut4': rut4,'rut5': rut5,'rut6': rut6,'rut7': rut7,'rut8': rut8,})

# Set top box sction ends----->>


# Firestick sction Starts----->>

def portfoliopage2(request):

    rut1 = Description()
    rut1.img = 'firetv.jpg'
    rut1.name = 'Fire TV Stick with Alexa'
    rut1.link = 'firetv'

    rut2 = Description()
    rut2.img = 'firetvlite.jpg'
    rut2.name = 'Fire TV Stick Lite with Alexa'
    rut2.link = 'firetvlite'
 

    rut3 = Description()
    rut3.img = 'firetvlite4k.jpg'
    rut3.name = 'Fire TV Stick 4K Lite'
    rut3.link = 'firetvlite4k'


    rut4 = Description()
    rut4.img = 'firetv4kall.jpg'
    rut4.name = 'Fire TV Stick 4K All-in-one'
    rut4.link = 'firetv4kall'


    rut5 = Description()
    rut5.img = 'firesticksony.jpg'
    rut5.name = 'Fire TV Stick with Sony Subscription'
    rut5.link = 'firesticksony'


    return render(request, 'port/catalog.html', {'rut1': rut1, 'rut2': rut2, 'rut3': rut3,'rut4': rut4,'rut5': rut5,})

# Firestick sction ends----->>

# Camera sction Starts----->>

def portfoliopage3(request):

    rut1 = Description()
    rut1.img = 'cp.jpg'
    rut1.name = 'CP PLUS 2MP Full HD Smart Wi-Fi CCTV'
    rut1.link = 'cp'

    rut2 = Description()
    rut2.img = 'mi.jpg'
    rut2.name = 'MI Xiaomi Wireless Home Security Camera'
    rut2.link = 'mi'
 

    rut3 = Description()
    rut3.img = 'tp.jpg'
    rut3.name = 'TP-Link Tapo'
    rut3.link = 'tp'


    rut4 = Description()
    rut4.img = 'qubo.jpg'
    rut4.name = 'Qubo Smart 360 Wi-Fi CCTV'
    rut4.link = 'qubo'


    rut5 = Description()
    rut5.img = 'conbre.jpg'
    rut5.name = 'Conbre MultipleXR2 Pro'
    rut5.link = 'conbre'

    return render(request, 'port/catalog.html', {'rut1': rut1, 'rut2': rut2, 'rut3': rut3,'rut4': rut4,'rut5': rut5,})

# Camera sction ends----->>

# DVRs sction Starts----->>

def portfoliopage4(request):

    rut1 = Description()
    rut1.img = 'hik.jpg'
    rut1.name = 'HIKVISION 4 Channel DVR'
    rut1.link = 'hik'

    rut2 = Description()
    rut2.img = 'cpdvr.jpg'
    rut2.name = 'CP PLUS 1080 4 Channel HD DVR'
    rut2.link = 'cpdvr'
 

    rut3 = Description()
    rut3.img = 'cpdvr8.jpg'
    rut3.name = 'CP PLUS CP-UVR-0801E1-CV2 1080P'
    rut3.link = 'cpdvr8'


    rut4 = Description()
    rut4.img = 'hik8.jpg'
    rut4.name = 'Hikvision Speedlink Infosystems Turbo'
    rut4.link = 'hik8'

    return render(request, 'port/catalog.html', {'rut1': rut1, 'rut2': rut2, 'rut3': rut3,'rut4': rut4,})

# DVRs sction ends----->>

# All in one sction Starts----->>

def portfoliopage5(request):

    rut1 = Description()
    rut1.img = 'cpall.jpg'
    rut1.name = 'CP Plus HD 2.4 MP 4-Channel DVR Kit'
    rut1.link = 'cpall'

    rut2 = Description()
    rut2.img = 'hikall.jpg'
    rut2.name = 'Hikvision 1MP HD Cameras Combo KIT'
    rut2.link = 'hikall'
 

    rut3 = Description()
    rut3.img = 'dahua.jpg'
    rut3.name = 'Dahua 4K Full HD 5MP Cameras Combo KIT'
    rut3.link = 'dahua'


    rut4 = Description()
    rut4.img = 'hiksurv.jpg'
    rut4.name = 'HIKVISION Surveillance Kit of 4+12'
    rut4.link = 'hiksurv'

    return render(request, 'port/catalog.html', {'rut1': rut1, 'rut2': rut2, 'rut3': rut3,'rut4': rut4,})

# All in one sction ends----->>

# HDD sction Starts----->>

def portfoliopage6(request):

    rut1 = Description()
    rut1.img = 'tos.jpg'
    rut1.name = 'TOSHIBA Canvio Basics 1TB'
    rut1.link = 'tos'

    rut2 = Description()
    rut2.img = 'sea.jpg'
    rut2.name = 'Seagate Expansion 2TB External HDD'
    rut2.link = 'sea'
 

    rut3 = Description()
    rut3.img = 'cru.jpg'
    rut3.name = 'Crucial BX500 500GB 2.5-inch SATA'
    rut3.link = 'cru'


    rut4 = Description()
    rut4.img = 'sam.jpg'
    rut4.name = 'Samsung 870 EVO 500GB SATA'
    rut4.link = 'sam'


    return render(request, 'port/catalog.html', {'rut1': rut1, 'rut2': rut2, 'rut3': rut3,'rut4': rut4,})

# HDD sction Starts----->>

# Printers sction Starts----->>

def portfoliopage7(request):

    rut1 = Description()
    rut1.img = 'canon3000.jpg'
    rut1.name = 'Canon Pixma 3000'
    rut1.link = 'canon3000'

    rut2 = Description()
    rut2.img = 'hp.jpg'
    rut2.name = 'HP innktank 315'
    rut2.link = 'hp'
 

    rut3 = Description()
    rut3.img = 'hpl.jpg'
    rut3.name = 'HP Laserjet 138'
    rut3.link = 'hpl'


    rut4 = Description()
    rut4.img = 'canonl.jpg'
    rut4.name = 'Canon Laser Shot'
    rut4.link = 'canonl'

    return render(request, 'port/catalog.html', {'rut1': rut1, 'rut2': rut2, 'rut3': rut3,'rut4': rut4,})

# Printer sction Starts----->>

# Monitor sction Starts----->>

def portfoliopage8(request):

    rut1 = Description()
    rut1.img = 'l.jpg'
    rut1.name = 'Lenovo Q-Series 24 Inch'
    rut1.link = 'l'

    rut2 = Description()
    rut2.img = 's.jpg'
    rut2.name = 'Samsung 24-inch'
    rut2.link = 's'
 

    rut3 = Description()
    rut3.img = 'real.jpg'
    rut3.name = 'Realme 80 cm'
    rut3.link = 'real'


    rut4 = Description()
    rut4.img = 'sony.jpg'
    rut4.name = 'Sony Bravia 80 cm'
    rut4.link = 'sony'

    return render(request, 'port/catalog.html', {'rut1': rut1, 'rut2': rut2, 'rut3': rut3,'rut4': rut4,})

# Monitor sction Starts----->>

#Portfolio sction end------------------------------------------------------------>>

# Router Product Description Section Starts----->>

def description1(request):
    rut1 = Description()
    rut1.link1 = '615'
    rut1.img1 = 'dir615.jpg'
    rut1.img2 = 'dir6151.jpg'
    rut1.img3 = 'dir6152.jpg'
    rut1.name='D-Link DIR - 615'
    rut1.category ='Single - band'
    rut1.price =' 799'
    rut1.info1 = "N 300 Mbps wireless Router with high gain Omni Antenna. Dynamic IP (DHCP) : Yes;Support Multiple operating modes: Router | AP | Repeater | Client;Easy Setup: Super simple set-up with the D-Link Assistant Mobile APP Or with intuitive WEB GUI setup wizard.;Advance security with WPA/WPA2 and firewall NAT, SPI, IP Filter, MAC Filter, DMZ, DDos prevention"
    rut1.info2 = "Always up-to-date with latest features / updates with online firmware upgrade;Support advance features like IPv6, TR-069, VLAN, static Routing etc.;Wireless Guest zone for visitors and wireless client bandwidth limitation;3 years Brand Warranty;N 300 Mbps wireless Router with high gain Omni Antenna. Dynamic IP (DHCP)"
    rut1.info3 = "Control Method: Application;High-Speed Wireless Networking"
    rut1.info4 = "Easy Configuration;Advanced Firewall Features;UPnP Support;Security Protocol: Wpswpa2-Psk Operating System: Windows 7windows"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})

def description2(request):
    rut1 = Description()
    rut1.link1 = 'r15'
    rut1.img1 = 'r15.jpg'
    rut1.img2 = 'r151.jpg'
    rut1.img3 = 'r152.jpg'
    rut1.name = 'D-Link R15 AX1500 Eagle PRO'
    rut1.category ='Dual - band'
    rut1.price = ' 2799'
    rut1.info1 = "Wi-Fi 6 AX 1500 Mbps WAVE 2 Dual band wireless router with 4 high gain Omni Antenna"
    rut1.info2 = "Gigabit Ports -- One Gigabit WAN & Three Gigabit LAN ports for high speed wired connectivity."
    rut1.info3 = "Easy Setup: Super simple set-up with the D-Link Eagle Pro AI Mobile APP Or with intuitive WEB GUI setup wizard."
    rut1.info4 = "D-Link AI Technology: AI Mesh Optimizer, AI Wi-Fi Optimizer, AI Traffic Optimizer, AI Parental Controls D-Link Easy Mesh Support, Can create a mesh network of 1+3 devices. 3 Year Warranty. Supports WPA, WPA2, and the latest WPA3 Wi-fi Security Security Protocol: Wpa2-Psk"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})

def description3(request):
    rut1 = Description()
    rut1.link1 = 'r03'
    rut1.img1 = 'r03.jpg'
    rut1.img2 = 'r031.jpg'
    rut1.img3 = 'r032.jpg'
    rut1.name = 'D-Link R03 N300 Eagle PRO'
    rut1.category ='Single - band'
    rut1.price = ' 809'
    rut1.info1 = "Wi-Fi 4 (802.11n) Technology with 300 Mbps speed;Dipole antenna for data transmission and reception improves range and performance"
    rut1.info2 = "4 x 10/100 Mbps Ethernet LAN ports. 1 x 10/100 Mbps Ethernet WAN port;Easy Setup: Super simple set-up with the D-Link Eagle Pro AI Mobile APP Or with intuitive WEB GUI setup wizard."
    rut1.info3 = "Wireless Comm Standard: 802 11 B;Color Name: White;Item Height: 36.0;Item Weight: 150.0;Included Components: Router, Power Adapter, Ethernet Cable, Qig;Special Features: Access Point Mode;Item Width: 132.0;Item Length: 158.0"
    rut1.info4 = "Always up-to-date with latest features / update with automatic online firmware upgrade;3 years Warranty;Call on toll free no.-1860-2333-999/0832-285-6000/0832-285-630. For E-Mail & Chat Support you can visit- service.dlink.co.in;Security Protocol: Wpa2-Psk"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})

def description4(request):
    rut1 = Description()
    rut1.link1 = 'c86'
    rut1.img1 = 'archerc86.jpg'
    rut1.img2 = 'archerc861.jpg'
    rut1.img3 = 'archerc862.jpg'
    rut1.name = 'TP-Link Archer C86'
    rut1.category ='Dual - band'
    rut1.price = ' 3699'
    rut1.info1 = "802.11ac Wave2 Wi-Fi —— 1300 Mbps on the 5 GHz band and 600 Mbps on the 2.4 GHz band 3×3 MIMO Technology —— Transmitting and receiving data on three streams to pair flawlessly with your 3×3 clients."
    rut1.info2 = "Boosted Wi-Fi Coverage —— Beamforming technology and six external antennas deliver a highly efficient wireless connection."
    rut1.info3 = "MU-MIMO —— To help your devices achieve optimal performance by making communication more efficient"
    rut1.info4 = "Personalized Management —— Advanced features like Parental Controls, Guest Network, and Access Control provide individualized tools for network management.Intelligent Connection —— Smart Connect directs clients to the less congested band and Airtime Fairness optimizes the time usage."
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})

def description5(request):
    rut1 = Description()
    rut1.link1 = 'c50'
    rut1.img1 = 'archerc50.jpg'
    rut1.img2 = 'archerc501.jpg'
    rut1.img3 = 'archerc502.jpg'
    rut1.name = 'TP-Link Archer C50'
    rut1.category ='Dual - band'
    rut1.price = ' 1999'
    rut1.info1 = "Fast Wireless Speed —— Support smooth 4K streaming with AC1200 Wi-Fi;Superior Coverage —— 4 external antennas provide stable wireless connections and optimal coverage"
    rut1.info2 = "Intelligent Connection —— Easy network management at your fingertips with TP-Link Tether IPTV streaming —— Supports IGMP Proxy/Snooping, Bridge and Tag VLAN to optimize IPTV streaming;Access Point Mode —— Supports Access Point mode to create a new Wi-Fi access point"
    rut1.info3 = "In an unlikely case of product quality related issue, we may ask you to reach out to brand’s customer service support and seek resolution. We will require brand proof of issue to process replacement request.;Control Method: Application"
    rut1.info4 = "Operating System: Windows. Future-proof your network with IPv6 (Internet Protocol Version 6) support"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})

def description6(request):

    rut1 = Description()
    rut1.link1 = 'xiaomirouter'
    rut1.img1 = 'xiaomi.jpg'
    rut1.img2 = 'xiaomi1.jpg'
    rut1.img3 = 'xiaomi2.jpg'
    rut1.name = 'Xiaomi Mi Smart Router 4C'
    rut1.category ='Single - band'
    rut1.price = ' 999'
    rut1.info1 = "2.4 GHz Wi-Fi with up to 300Mbps Speed, Ideal for video streaming and web browsing. ROM : 16MB Nor Flash. Management application : Supports web, iOS, and Android"
    rut1.info2 = "4 High-performance antenna for better speed & coverage. Operating temperature: 0–40°C. Storage temperature:-40–70°C"
    rut1.info3 = "Control your network from Anywhere, Anytime with help of Mi Wi-Fi app QoS (Quality of Service) Manage and allocate bandwidth as per activity requirements"
    rut1.info4 = "Parental Control-Control time on internet and content on connected devices Improve network speed with Wi-Fi optimization Coverage Area: up to 400 Sqft"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})

def description7(request):
    rut1 = Description()
    rut1.link1 = 'ac1200'
    rut1.img1 = 'AC1200.jpg'
    rut1.img2 = 'AC12001.jpg'
    rut1.img3 = 'AC12002.jpg'
    rut1.name = 'TP-Link AC1200 Mbps Archer A6'
    rut1.category ='Tri - band'
    rut1.price = ' 2499'
    rut1.info1 = "AC1200 Dual-Band Wi-Fi —— 867 Mbps at 5 GHz and 400 Mbps at 2.4 GHz band"
    rut1.info2 = "MU-MIMO Technology —— Simultaneously transfers data to multiple devices for 2× faster performance"
    rut1.info3 = "Boosted Coverage —— Four external antennas equipped with Beamforming technology extend and concentrate the Wi-Fi signals"
    rut1.info4 = "Access Point Mode —— Supports AP Mode to transform your wired connection into the wireless network; Easy Setup —— Set up your Wi-Fi in minutes with the TP-Link Tether app.; Operating System: Windows; Control Method: Application Control Method: Application; Operating System: Windows"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})

def description8(request):
    rut1 = Description()
    rut1.link1 = '825'
    rut1.img1 = 'dir825.jpg'
    rut1.img2 = 'dir8251.jpg'
    rut1.img3 = 'dir8252.jpg'
    rut1.name = 'D-Link DIR-825'
    rut1.category ='Dual - band'
    rut1.price = ' 2630'
    rut1.info1 = "AC 1200 Mbps WAVE 2 Concurrent dual band wireless Router with 4 High gain Omni Antenna;802.11 a/b/g/n/ac standards with speed of 300 Mbps on 2.4Ghz & 867 Mbps on 5Ghz"
    rut1.info2 = "Gigabit Ports -- One Gigabit WAN & Four Gigabit LAN ports for high speed wired connectivity.;MU-MIMO -- MU-MIMO, which transmits data to multiple wireless devices simultaneously to increase speed and efficiency"
    rut1.info3 = "Multiple Operating modes: Router mode : to access the internet. Access Point mode : to extend wired network over wireless .Repeater mode : to extend the range of existing wireless router."
    rut1.info4 = "Easy Setup: Super simple set-up with the D-Link Assistant Mobile APP Or with intuitive WEB GUI setup wizard Control Method: Application;Operating System: Windows;Security Protocol: Wepwps"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})

# Router Product Description Section ends----->>


# Set top box Product Description Section Starts----->>
def settop1(request):
    rut1 = Description()
    rut1.link1 = 'air'
    rut1.img1 = 'airtel.jpg'
    rut1.img2 = 'airtel1.jpg'
    rut1.img3 = 'airtel2.jpg'
    rut1.name = 'Airtel DTH HD'
    rut1.category = 'Set Top Box'
    rut1.price = ' 1000'
    rut1.info1 = "Airtel HD Set Top Box brings theatre-like experience to your home with HD Premium Quality Video (1080i resolution) and Dolby digital plus 5.1 surround sound"
    rut1.info2 = "Airtel D2H allows you to pause, record and play live TV so that you never miss your favourites as you can watch them later as per your convenience"
    rut1.info3 = "Enjoy free delivery and hassle-free installation of your DTH Set Top Box."
    rut1.info4 = "Any other accessory which is not a part of the standard installation will be charged separately"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def settop2(request):
    rut1 = Description()
    rut1.link1 = 'd2'
    rut1.img1 = 'd2h.jpg'
    rut1.img2 = 'd2h1.jpg'
    rut1.img3 = 'd2h2.jpg'
    rut1.name = 'd2h HD DTH Connection'
    rut1.category = 'Set top box'
    rut1.price = ' 1299'
    rut1.info1 = "OFFER DETAILS : This is HD Set top box connection with 1 month Value Hindi Pack which includes Combo with popular Hindi,GEC, infotainment, News channels along with FTA Channels."
    rut1.info2 = "With this package get 7 popular HD channels for no additional cost when you become an existing d2h Subscriber"
    rut1.info3 = "Features & Support: 1080i Resolution, 5x better picture quality & exceptional clarity & crystal-clear surround sound. 24x7 Customer Care with regional language support."
    rut1.info4 = "5 Year warranty on Set Top Box Delivery & Installation: Home Delivery, Standard Installation and Demo"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def settop3(request):
    rut1 = Description()
    rut1.link1 = 'cat'
    rut1.img1 = 'catvision.jpg'
    rut1.img2 = 'catvision1.jpg'
    rut1.img3 = 'catvision2.jpg'
    rut1.name = 'Catvision DD Free Dish'
    rut1.category = 'Set top Box'
    rut1.price = ' 1350'
    rut1.info1 = "Watch 115 + channels of Doordarshan Freedish service FREE OF COST"
    rut1.info2 = "1080P Full HD DVB-S2"
    rut1.info3 = "Supports USB PVR"
    rut1.info4 = "Easy-to-use Menu. A power of entertainment in your control."
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def settop4(request):
    rut1 = Description()
    rut1.link1 = 'free'
    rut1.img1 = 'dishtvfree.jpg'
    rut1.img2 = 'dishtvfree1.jpg'
    rut1.img3 = 'dishtvfree2.jpg'
    rut1.name = 'Dish TV Free to Air DTH '
    rut1.category = 'Set top Box'
    rut1.price = ' 1049'
    rut1.info1 = "No need to recharge for 2 years to watch free to air channels on this DishTV ZIng Super FTA Set top box"
    rut1.info2 = "Flexibility to add and remove any paid channels of your choice at any time from Dishtv App. This option is available on Dishtv only"
    rut1.info3 = "1 Year Warranty on FTA Set-top box Paid Channels can also be Added 150+ Channels & Services"
    rut1.info4 = "ACTIVATION PROCESS : To activate your Set Top Box Please type: ZING ACT (VC Number)(Customer Name) and Send it to 57575 or 9212012299 EXAMPLE: ZING ACT 12345678901 Name ( Local SMS Charges Apply ) : For any support/assistance call to customer care no. 95017-95017"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def settop5(request):
    rut1 = Description()
    rut1.link1 = 'smart'
    rut1.img1 = 'dishtvsmart.jpg'
    rut1.img2 = 'dishtvsmart1.jpg'
    rut1.img3 = 'dishtvsmart2.jpg'
    rut1.name = 'DishTV Dish SMRT Android'
    rut1.category = 'Set top Box'
    rut1.price = ' 2635'
    rut1.info1 = "OFFER DETAILS: This is Android HD Set top box connection with 1 month Royale Sports Hindi HD Pack. This offer Includes Entertainment, Sports, along with popular kids, movies, news,infotainment channels."
    rut1.info2 = "With Dish SMRT Hub box make your TV/LCD into smart TV and enjoy OTT app, online gaming and other. Get so much more from your TV. The all new SMRT Hub allows you to switch between your favorite OTT channels, apps and games."
    rut1.info3 = "FEATURES & SUPPORT: 1080i Resolution, 5x better picture quality & exceptional clarity & crystal-clear surround sound. 24x7 Customer Care with regional language support."
    rut1.info4 = "Bluetooth Remote with Google Assistance Voice Search and Control Smart Home Devices with Google Assistant Built-in stream entertainment from Mobile to TV, Record content with External Disk Access to Google Play Store to download apps(Internet connection will be needed) Bluetooth Connectivity and a lot more."
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def settop6(request):
    rut1 = Description()
    rut1.link1 = 'dish'
    rut1.img1 = 'dishtv.jpg'
    rut1.img2 = 'dishtv1.jpg'
    rut1.img3 = 'dishtv2.jpg'
    rut1.name = 'DishTV HD DTH'
    rut1.category = 'Set top box'
    rut1.price = ' 2499'
    rut1.info1 = "OFFER DETAILS : This is HD Set top box connection with 1 month Family Saver Odiya pack which Includes Family entertainment with Odiya, GEC, Movies, Music, News channels."
    rut1.info2 = "Rs.2499 Pe Rs.1700 Cash Back offer - 1700 add back in your Dishtv connection as a recharge."
    rut1.info3 = "Features & Support : 1080i Resolution, 5x better picture clarity & surround sound, 24x7 Customer Care with regional language support."
    rut1.info4 = "Warranty - 5 Year on Set Top Box. Delivery & Installation: Free Delivery, Standard Installation and Demo"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def settop7(request):
    rut1 = Description()
    rut1.link1 = 'xtreme'
    rut1.img1 = 'airtelxtreme.jpg'
    rut1.img2 = 'airtelxtreme1.jpg'
    rut1.img3 = 'airtelxtreme2.jpg'
    rut1.name = 'Airtel Xstream Box'
    rut1.category = 'Set top Box'
    rut1.price = ' 1929'
    rut1.info1 = "Turn your TV into a smart TV with access to Google Play Store and enjoy 5000+ apps and games on the big screen."
    rut1.info2 = "A cinematic experience awaits you with high definition 4K picture quality (1080i resolution) and 5.1 Dolby Surround System."
    rut1.info3 = "Choose from 550+ channels to create your own customised plan and switch between TV, OTT and YouTube at just a click."
    rut1.info4 = "Explore your favourite content with a Voice remote powered by Google Assistant and also command your TV DTH Recharge is compulsory for the product."
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def settop8(request):
    rut1 = Description()
    rut1.link1 = 'streme'
    rut1.img1 = 'd2hstreme.jpg'
    rut1.img2 = 'd2hstreme1.jpg'
    rut1.img3 = 'd2hstreme2.jpg'
    rut1.name = 'D2H Stream only Set Top Box'
    rut1.category = 'Set top Box'
    rut1.price = ' 1974'
    rut1.info1 = "OFFER DETAILS: This is Android HD only Set top box connection with 1 month Value Lite Hindi HD Pack. This offer Includes Complete Family entertainment with all Hindi GEC, Movies, Music, News channels along with FTA channels"
    rut1.info2 = "Gigabit Ports -- One Gigabit WAN & Four Gigabit LAN ports for high speed wired connectivity.;MU-MIMO -- MU-MIMO, which transmits data to multiple wireless devices simultaneously to increase speed and efficiency"
    rut1.info3 = "With d2h stream box make your TV/LCD into smart TV and enjoy OTT app, online gaming and other. Get so much more from your TV. The all new d2h Stream allows you to switch between your favorite OTT channels, apps and games."
    rut1.info4 = "FEATURES & SUPPORT: 1080i Resolution, 5x better picture quality & exceptional clarity & crystal-clear surround sound. 24x7 Customer Care with regional language support. It has excelent features like Inbuilt Wifi, Built-in Google Assistant, Dolby Audio, 2K Quad HD, Standard Recording, Bluetooth Remote"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})
# Set top box Product Description Section Ends----->>

# Firestick Product Description Section Starts----->>


def fire1(request):
    rut1 = Description()
    rut1.link1 = 'fir'
    rut1.img1 = 'firetv.jpg'
    rut1.img2 = 'firetv1.jpg'
    rut1.img3 = 'firetv2.jpg'
    rut1.name = 'Fire TV Stick with Alexa'
    rut1.category = 'Plug and play'
    rut1.price = ' 3999'
    rut1.info1 = "Latest generation of our best-selling Fire TV device - 50% more powerful than the 2nd generation for fast streaming in Full HD. Includes Alexa Voice Remote with power and volume buttons."
    rut1.info2 = "Less clutter, more control - All-new Alexa Voice Remote (3rd Gen) lets you use your voice to search and launch shows across apps. All-new preset buttons get you to favorite apps quickly. Plus, control power and volume on your TV and soundbar with a single remote."
    rut1.info3 = "Home theater audio with Dolby Atmos - Feel scenes come to life with immersive Dolby Atmos audio on select titles with compatible home audio systems."
    rut1.info4 = "Tens of thousands of movies and shows from Prime Video, Netflix, Disney+ Hotstar, Zee5, SonyLIV, Sun NXT, ALT Balaji, Discovery Plus and many other Apps. Subscription fees may apply."
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def fire2(request):
    rut1 = Description()
    rut1.link1 = 'fir1'
    rut1.img1 = 'firetvlite.jpg'
    rut1.img2 = 'firetvlite1.jpg'
    rut1.img3 = 'firetvlite2.jpg'
    rut1.name = 'Fire TV Stick Lite'
    rut1.category = 'Plug and play'
    rut1.price = ' 2999'
    rut1.info1 = "Our most affordable Fire TV stick - Enjoy fast streaming in Full HD. Comes with all-new Alexa Voice Remote Lite (now with app control)."
    rut1.info2 = "Access to more than a million movies and TV show episodes from Prime Video, Netflix, Disney+ Hotstar, ZEE5, SonyLIV, Sun NXT, ALT Balaji, Discovery+ and many other apps. Subscription fees may apply."
    rut1.info3 = "What’s free - YouTube, YouTube Kids, MXPlayer, TVFPlay, YuppTV and many more. Easily search, play, pause, rewind, or forward content with just your voice. Simply say Alexa, find comedies."
    rut1.info4 = "Watch movies, web series, news, sports & kids content on your TV. Comes with parental control. Subscription fees may apply. Easy to set up and stays hidden – plug in behind your TV into an HDMI port, turn on the TV and connect to the internet to set up."
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def fire3(request):
    rut1 = Description()
    rut1.link1 = 'fir2'
    rut1.img1 = 'firetvlite4k.jpg'
    rut1.img2 = 'firetvlite4k1.jpg'
    rut1.img3 = 'firetvlite4k2.jpg'
    rut1.name = 'Fire TV Stick 4K Max streaming'
    rut1.category = 'Plug and Play'
    rut1.price = ' 6499'
    rut1.info1 = "Our most powerful streaming stick - 40% more powerful than Fire TV Stick 4K, with faster app starts and more fluid navigation."
    rut1.info2 = "Cinematic experience - Watch in vibrant 4K Ultra HD with support for Dolby Vision, HDR, HDR10 + and immersive Dolby Atmos audio(on select titles) Endless entertainment - Stream thousands of movies and TV episodes. Watch favorites from Netflix, Prime Video, Disney + Hotstar and many more apps. Subscription fees may apply."
    rut1.info3 = "Also compatible with the next-gen Wi-Fi 6 routers. Enjoy smoother 4K streaming across multiple Wi-Fi 6 compatible devices"
    rut1.info4 = "Live TV - Watch live TV, news, and sports with subscriptions to SonyLIV, Voot, Discovery+, and others. Alexa Voice Remote - Search and launch content with your voice. Get to favorite apps quickly with preset buttons. Control power and volume with one remote."
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def fire4(request):
    rut1 = Description()
    rut1.link1 = 'fir3'
    rut1.img1 = 'firetv4kall.jpg'
    rut1.img2 = 'firetv4kall1.jpg'
    rut1.img3 = 'firetv4kall2.jpg'
    rut1.name = 'Fire TV Stick 4K with all-new Alexa, Dolby Vision'
    rut1.category = 'Plug and play'
    rut1.price = ' 4999'
    rut1.info1 = "Cinematic experience - Watch in vibrant 4K Ultra HD with support for Dolby Vision, HDR, and HDR10+.Home theater audio with Dolby Atmos - Feel scenes come to life with support for immersive Dolby Atmos audio on select titles with compatible home audio systems"
    rut1.info2 = "Endless entertainment - Choose from thousands of movies and TV episodes. Enjoy favorites from Prime Video, Disney + Hotstar, Netflix, Zee5, Sony LIV, Apple TV and others. Subscription fees may apply.Watch Live TV – TV shows, news, reality shows and more from your favorite TV channels(supported by subscribed Apps), all in one place under Live Tab, direct from Fire TV home screen"
    rut1.info3 = "All-new Alexa Voice Remote - Search and launch content with your voice. Get to favorite apps quickly with preset buttons. Control power and volume with one remote.Control your smart home - Ask Alexa to check weather, dim the lights, view live camera feeds, stream music and more."
    rut1.info4 = "Simple and intuitive - Quickly access your favorite apps, live TV, and things you use most, all from the main menu.Easy to set up, compact enough to stay hidden - Plug in behind your TV, turn on the TV, and connect to the internet to get set up"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def fire5(request):
    rut1 = Description()
    rut1.link1 = 'fir4'
    rut1.img1 = 'firesticksony.jpg'
    rut1.img2 = 'firesticksony1.jpg'
    rut1.img3 = 'firesticksony2.jpg'
    rut1.name = 'Fire TV Stick + Sony LIV Combo'
    rut1.category = 'Plug and Play'
    rut1.price = ' 4599'
    rut1.info1 = "Latest generation of our best-selling Fire TV device - 50% more powerful than the 2nd generation for fast streaming in Full HD. Includes Alexa Voice Remote with power and volume buttons."
    rut1.info2 = "Enjoy free access to Sony LIV for a year with the Fire TV Stick Plus. Fire TV Stick - 4999, Sony LIV - Rs 999. Total value of Fire TV Stick and subscription is Rs 5998. Subscription fees may be applicable from the second year.Home theater audio with Dolby Atmos - Feel scenes come to life with immersive Dolby Atmos audio on select titles with compatible home audio systems."
    rut1.info3 = "Tens of thousands of movies and shows from Sony LIV, Zee5, Voot Select, Prime Video, Netflix, Disney + Hotstar, Sun NXT, ALT Balaji, Discovery Plus and many other Apps. Subscription fees may apply.What’s included – A one-year subscription to Sony LIV. Additionally, enjoy YouTube, YouTube Kids, MXPlayer, TVFPlay, YuppTV and many more services for free."
    rut1.info4 = "The serial number associated with your device may be shared by Amazon with the participating App providers to enable activation of the purchased subscriptions. Fire TV Stick is also available without this offer."
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})

#firestick product description ends

#----------------------------------Internet Section ends-------------------------------------------------------#

#----------------------------------Survelliance Section starts-------------------------------------------------------#

# Camera Product Description Section Starts----->>


def camera1(request):
    rut1 = Description()
    rut1.link1 = 'cm'
    rut1.img1 = 'cp.jpg'
    rut1.img2 = 'cp1.jpg'
    rut1.img3 = 'cp2.jpg'
    rut1.name = 'CP PLUS 2MP Full HD Smart Wi-Fi'
    rut1.category = '360° degree camera'
    rut1.price = ' 1699'
    rut1.info1 = "1080p full HD Plug & Play Wi-Fi PT camera, which enables crisp images that reveal the smallest details with absolute clarity. Now, Works with Alexa & Ok Google so you can go hands-free and enjoy the safety of a smart home. 36o Degree View offered by this EzyKam, saves cost and trouble of installing multiple cameras in any space to cover the full view of the area.Home-on-Phone, View the live video footage of your home/office anytime anywhere in the world on your phone."
    rut1.info2 = "Hassle-free Installation, Connect to your local Wi-Fi in a moment. Simply select a network, input the password, and you are good to go;Talk to the person on the other side while you see their live video feed and stay connected to your loved ones around the clock. Up to 128GB SD Card supported."
    rut1.info3 = "EzyKam + Supports Mobile APP with 4 Split Live Views.EzyKam + Supports Web Client with 9 Split Live Views.Material Type: Metal Included Components: Camera And Usb Specific Uses For Product: Surveillance"
    rut1.info4 = "Motion Detection & Human Detection : Human Detection avoids false alarms from moving pets. Smart Tracking function makes the camera follow moving objects, records real-time videos and sends instant alerts to your mobile."
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def camera2(request):
    rut1 = Description()
    rut1.link1 = 'cm1'
    rut1.img1 = 'mi.jpg'
    rut1.img2 = 'mi1.jpg'
    rut1.img3 = 'mi2.jpg'
    rut1.name = 'MI Xiaomi Wireless Home Security Camera'
    rut1.category = '360° degree camera'
    rut1.price = ' 2999'
    rut1.info1 = "Our most affordable Fire TV stick - Enjoy fast streaming in Full HD. Comes with all-new Alexa Voice Remote Lite (now with app control)."
    rut1.info2 = "Access to more than a million movies and TV show episodes from Prime Video, Netflix, Disney+ Hotstar, ZEE5, SonyLIV, Sun NXT, ALT Balaji, Discovery+ and many other apps. Subscription fees may apply."
    rut1.info3 = "What’s free - YouTube, YouTube Kids, MXPlayer, TVFPlay, YuppTV and many more. Easily search, play, pause, rewind, or forward content with just your voice. Simply say Alexa, find comedies."
    rut1.info4 = "Watch movies, web series, news, sports & kids content on your TV. Comes with parental control. Subscription fees may apply. Easy to set up and stays hidden – plug in behind your TV into an HDMI port, turn on the TV and connect to the internet to set up."
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def camera3(request):
    rut1 = Description()
    rut1.link1 = 'cm2'
    rut1.img1 = 'tp.jpg'
    rut1.img2 = 'tp1.jpg'
    rut1.img3 = 'tp2.jpg'
    rut1.name = 'TP-Link Tapo 360°'
    rut1.category = '360° degree camera'
    rut1.price = ' 2999'
    rut1.info1 = "Ultra-High-Definition Video —— Records every image in crystal-clear 3MP definition Pan and Tilt —— 360º horizontal range"
    rut1.info2 = "Advanced Night Vision —— Provides a visual distance of up to 30 ft Motion Detection and Notifications —— Notifies you when the camera detects movement"
    rut1.info3 = "Sound and Light Alarm —— Trigger light and sound effects to frighten away unwanted visitors Two-Way Audio —— Enables communication through a built-in microphone and speaker"
    rut1.info4 = "Safe Storage —— Locally stores up to 256 GB on a microSD card, equal to 512 hours(21 days) of footage. (Based on laboratory conditions) Voice Control —— Free Up Your Hands with Voice Control. Works with the Google Assistant and Amazon Alexa. (Google Assistant and Amazon Alexa are not available in all languages and countries)"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def camera4(request):
    rut1 = Description()
    rut1.link1 = 'cm3'
    rut1.img1 = 'qubo.jpg'
    rut1.img2 = 'qubo1.jpg'
    rut1.img3 = 'qubo2.jpg'
    rut1.name = 'Qubo Smart 360 Wi-Fi CCTV'
    rut1.category = '360 degree camera'
    rut1.price = '2490'
    rut1.info1 = "PROUDLY INDIAN: Qubo Smart Cam 360 is Designed & Made in INDIA. Engineered for the Security Needs of the Indian Market; TRUST OF HERO GROUP: Our Round-the-Clock Customer Service & Wide field Network not only resolves your all concerns & queries but rather ensures complete peace of mind for Lifetime."
    rut1.info2 = "360 COVERAGE: The smart security camera supports Multi-Directional rotation of the lens ensuring that there are no blind spots. NOTE: Qubo Smart Cam 360 is designed to be used indoors only."
    rut1.info3 = "THEFT PROOF CLOUD STORAGE: Unlike traditional CCTV cameras, you can secure your recordings on cloud storage based in India. Your private home moments stay with you even if the device is stolen"
    rut1.info4 = "PERSON DETECTION WITH INTRUDER ALARM : The secutity camera has Advanced AI capabilities that can smartly detect & notify whenever a person is detected. You can also ring an automatic loud siren in case of an intrusion."
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def camera5(request):
    rut1 = Description()
    rut1.link1 = 'cm4'
    rut1.img1 = 'conbre.jpg'
    rut1.img2 = 'conbre1.jpg'
    rut1.img3 = 'conbre2.jpg'
    rut1.name = 'Conbre MultipleXR2 Pro'
    rut1.category = '360 degree camera'
    rut1.price = ' 1299'
    rut1.info1 = "COVER EVERY CORNER WITH 360 DEGREE VIEW : Rotate camera horizontally or vertically from anywhere in the world using mobile application.Product works on 4G only with minimum 2mbps speed. Power adapter input :100-240Vac 50/60Hz 0.3A Max."
    rut1.info2 = "READY ON THE GO: This smart wireless camera is designed with easy setup feature for do-it-yourself installation by using V380 mobile application available in your handsets market place"
    rut1.info3 = "DAY AND NIGHT VISION: Night vision up to 16-feet - never miss a moment, day or night, with visibility up to 16 feet in complete darkness. Communicate with family, friends and your pets on mobile devices. Talk to camera or listen to camera, there is no distance to communicate with anyone."
    rut1.info4 = "SEAMLESS CONNECTIVITY WITH MOBILE/TABLET: Quick Wi-Fi setup(Does not support 5G wi-fi network)) via iOS or Android Smartphone using supplied APP DETECT MOTION IN YOUR ABSENCE: HD night vision with inbuilt IR lens. MOTION DETECTION: Will send alerts whenever any motion is detected."
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})

# camera product description ends


# All-in-one Product Description Section Starts----->>


def all1(request):
    rut1 = Description()
    rut1.link1 = 'al1'
    rut1.img1 = 'cpall.jpg'
    rut1.img2 = 'cpall1.jpg'
    rut1.img3 = 'cpall2.jpg'
    rut1.name = 'CP Plus HD 2.4 MP 4-Channel DVR Kit'
    rut1.category = 'All-in-one'
    rut1.price = '9500'
    rut1.info1 = "HD 2. 4 MP 4-Channel DVR Kit"
    rut1.info2 = "Comes with 2 Dome, 2 Bullet Camera"
    rut1.info3 = "Comes with 2 Years Warranty"
    rut1.info4 = "1 TB HDD and All Required Accessories"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def all2(request):
    rut1 = Description()
    rut1.link1 = 'al2'
    rut1.img1 = 'hikall.jpg'
    rut1.img2 = 'hikall1.jpg'
    rut1.img3 = 'hikall2.jpg'
    rut1.name = 'Hikvision 1MP HD Cameras Combo KIT'
    rut1.category = 'All-in-one'
    rut1.price = '9329'
    rut1.info1 = "Hikvision 1MP (720P) 4CH Turbo HD Mini DVR with 2 Dome & 2 Bullet Cameras Combo Kit without Hard Disk. Hikvision DS-6004HGHI-F1/ECO (1MP) (720P) 4CH Turbo HD Mini DVR"
    rut1.info2 = "1Pcs, Hikvision DS2CE51C0T-IRP/ECO 1MP Dome Cameras 2Pcs, Hikvision DS2CE11C0T-IRP/ECO 1MP Bullet Cameras 2Pcs, 90Mtr Copper Cable 1Bundle, 4CH Power Supply, BNC"
    rut1.info3 = "8Pcs, DC 4Pcs. Hard Disk & Installation is not included. DVR"
    rut1.info4 = "Description: H.264 & Dual-stream video compression. Support both HD-TVI /analog and AHD cameras with adaptive"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def all3(request):
    rut1 = Description()
    rut1.link1 = 'al3'
    rut1.img1 = 'dahua.jpg'
    rut1.img2 = 'dahua1.jpg'
    rut1.img3 = 'dahua2.jpg'
    rut1.name = 'Dahua 4K Full HD 5MP Cameras Combo KIT'
    rut1.category = 'All-in-one'
    rut1.price = '18500'
    rut1.info1 = "Dahua Full HD 8 CH DVR ( Model ) - DH-XVR4B08H-I - 1 Nos"
    rut1.info2 = "Dahua 5 MP Bullete Camera - 3 Nos"
    rut1.info3 = "Dahua 5 MP Dome Camera - 1 Nos 2 TB Hard Drive - 1 Nos, "
    rut1.info4 = "CCTV 3+1 Cable Roll - 1 Nos,12V 5AMP SMPS - 1 Nos,BNC Connectors - 8 Nos,DC Connectors - 4 Nos"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def all4(request):
    rut1 = Description()
    rut1.link1 = 'al4'
    rut1.img1 = 'hiksurv.jpg'
    rut1.img2 = 'hiksurv1.jpg'
    rut1.img3 = 'hiksurv2.jpg'
    rut1.name = 'HIKVISION Surveillance Kit of 4+12'
    rut1.category = 'All-in-one'
    rut1.price = '27990'
    rut1.info1 = "Comes with 16 Ch. DVR"
    rut1.info2 = "Comes with All Accessories"
    rut1.info3 = "Surveillance Kit"
    rut1.info4 = "2 years warranty"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})

# All-in-one product description ends

# DVRs Product Description Section Starts----->>


def dvr1(request):
    rut1 = Description()
    rut1.link1 = 'dv1'
    rut1.img1 = 'hik.jpg'
    rut1.img2 = 'hik1.jpg'
    rut1.img3 = 'hik2.jpg'
    rut1.name = 'HIKVISION 4 Channel DVR'
    rut1.category = '4-channel'
    rut1.price = '3150'
    rut1.info1 = "HIKVISION 4 Channel 1080P Lite Upto 2MP H.265 DVR"
    rut1.info2 = "HDTVI/AHD/CVI/CVBS/IP video input[Support all brands cameras Upto 2MP]"
    rut1.info3 = "H.265+ DVR with higher compression rate"
    rut1.info4 = "Encoding ability up to 1080p lite @ 25/30 fps .Up to 5 channel IP camera input"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def dvr2(request):
    rut1 = Description()
    rut1.link1 = 'dv2'
    rut1.img1 = 'cpdvr.jpg'
    rut1.img2 = 'cpdvr1.jpg'
    rut1.img3 = 'cpdvr2.jpg'
    rut1.name = 'CP PLUS 1080 4 Channel HD DVR'
    rut1.category = '4-channel'
    rut1.price = '2790'
    rut1.info1 = "4 ch. 1080P lite cosmic HD DVR / support upto 2.4MP IP Camera"
    rut1.info2 = "Auto adaptive HDCVI/AHD/TVI/CVBS signals / all channel 1080P lite real time recording"
    rut1.info3 = "H.264 dual-stream video compression / HDMI / VGA simultaneous video output"
    rut1.info4 = "Support 1 SATA HDD up to 6TB, 2 USB2.0 / mobile software: iCMOB, gCMOB .CMS software: KVMS, KVMS pro"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def dvr3(request):
    rut1 = Description()
    rut1.link1 = 'dv3'
    rut1.img1 = 'cpdvr8.jpg'
    rut1.img2 = 'cpdvr81.jpg'
    rut1.img3 = 'cpdvr82.jpg'
    rut1.name = 'CP PLUS CP-UVR-0801E1-CV2'
    rut1.category = '8-channel'
    rut1.price = ' 3730'
    rut1.info1 = "Support 2MP Cameras and support upto 5MP IP camera"
    rut1.info2 = "Supports 1 SATA HDD up to 6TB, 2 USB2.0"
    rut1.info3 = "Mobile Software: iCMOB, gCMOB"
    rut1.info4 = "2 years warranty"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def dvr4(request):
    rut1 = Description()
    rut1.link1 = 'dv4'
    rut1.img1 = 'hik8.jpg'
    rut1.img2 = 'hik8.jpg'
    rut1.img3 = 'hik8.jpg'
    rut1.name = 'Hikvision Speedlink Infosystems Turbo HD 5 MP Metal DVR with 16 Inch 2 SATA'
    rut1.category = '16-channel'
    rut1.price = '25999'
    rut1.info1 = "16-ch videoand4-ch audio input, H.265+/H.265/H.264+/H.264 encoding for the main stream, and H.265/H.264 for the sub-stream of analog cameras"
    rut1.info2 = "Self-adaptive HDTVI/HDCVI/AHD/CVBS signal input,Connectable to H.265+/H.265/H.264+/H.264 IP cameras"
    rut1.info3 = "Up to 5 MP resolution for recording . HDMI output at up to 4K(3840x2160) resolution"
    rut1.info4 = "Long distance transmission over UTP and coaxial cable, 16-ch synchronous playback"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})

# DVRs product description ends


# HDD and SSD Product Description Section Starts----->>

def ssd1(request):
    rut1 = Description()
    rut1.link1 = 'ss1'
    rut1.img1 = 'tos.jpg'
    rut1.img2 = 'tos1.jpg'
    rut1.img3 = 'tos2.jpg'
    rut1.name = 'TOSHIBA Canvio Basics 1TB'
    rut1.category = 'HDD'
    rut1.price = '3999'
    rut1.info1 = "Super speed USB 3.0 port"
    rut1.info2 = "Easy plug-n-play operation"
    rut1.info3 = "Built-in internal shock sensor"
    rut1.info4 = "Country of Origin: Philippines"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def ssd2(request):
    rut1 = Description()
    rut1.link1 = 'ss2'
    rut1.img1 = 'sea.jpg'
    rut1.img2 = 'sea1.jpg'
    rut1.img3 = 'sea2.jpg'
    rut1.name = 'Seagate One Touch 2TB External HDD'
    rut1.category = 'HDD'
    rut1.price = '5999'
    rut1.info1 = "Safely and easily manage 2 TB of photos, videos, movies, and more with hardware encrypted password-protection."
    rut1.info2 = "The perfect external hard drive for Windows or Mac, simply back up files with a single click or schedule automatic daily, weekly or monthly backups. Reformatting may be required for use with Time Machine."
    rut1.info3 = "Get an extra layer of protection for your data with the included 3 year Rescue Data Recovery Services."
    rut1.info4 = "Edit, manage, and share photos with a four-month membership to Adobe Creative Cloud Photography plan and one-year complimentary subscription to Mylio Create."
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def ssd3(request):
    rut1 = Description()
    rut1.link1 = 'ss3'
    rut1.img1 = 'cru.jpg'
    rut1.img2 = 'cru1.jpg'
    rut1.img3 = 'cru2.jpg'
    rut1.name = 'Crucial BX500 500GB 2.5-inch SATA 3D NAND Internal SSD'
    rut1.category = 'SSD'
    rut1.price = '2199'
    rut1.info1 = "The new Crucial BX500 500GB Internal Solid State Drive improves your overall system responsiveness. It delivers sequential Read and Write speeds of up to 550MB/s and 500MB/s respectively."
    rut1.info2 = "Being 3X faster than a standard HDD, this SATA Crucial SSD lets you feel the difference with super-fast OS boot times and application loads. It also features SSD Endurance (TBW) of 120 Terabytes."
    rut1.info3 = "With an operating temperature of 0°c to 70°c the 500GB SSD is designed to withstand any harsh operating environment. Equipped with advanced features like Thermal monitoring, Multistep data integrity algorithm the SSD ensures reliable performance."
    rut1.info4 = "The BX500 comes with a 3 year warranty and has undergone dozens of SSD qualification test, making it thoroughly tried, tested and proven."
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def ssd4(request):
    rut1 = Description()
    rut1.link1 = 'ss4'
    rut1.img1 = 'sam.jpg'
    rut1.img2 = 'sam1.jpg'
    rut1.img3 = 'sam2.jpg'
    rut1.name = 'Samsung 870 EVO 500GB SATA'
    rut1.category = 'SSD'
    rut1.price = '3829'
    rut1.info1 = "Sequential Read speeds up to 7,000MB/s. Performance varies based on system hardware and configuration"
    rut1.info2 = "Interface : PCIe 4.0 NVMe (PCIe Gen 4.0 x 4). Form Factor : M.2 (2280)"
    rut1.info3 = "Cache Memory: Samsung 1 GB DDR4 SDRAM 5-Year Limited Warranty or 600 TBW Limited Warranty."
    rut1.info4 = "Designed for tech enthusiasts, hardcore gamers, and professionals who blazing fast speed. To maximize the performance of the 980 PRO, please check whether your system supports PCIe 4.0 at the Intel or AMD website."
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})

# HDD and SSD product description ends

# Printer Product Description Section Starts----->>
def printer1(request):
    rut1 = Description()
    rut1.link1 = 'prin1'
    rut1.img1 = 'canon3000.jpg'
    rut1.img2 = 'canon30001.jpg'
    rut1.img3 = 'canon30002.jpg'
    rut1.name = 'Canon PIXMA G3000'
    rut1.category = 'Ink-tank'
    rut1.price = '14499'
    rut1.info1 = "Print, Scan, Copy;2 Additional Black ink bottles inside the box, along with 1 set of Cyan, Magenta, Yellow and Black Ink bottle (Total 6 ink bottles)"
    rut1.info2 = "Print Speed (A4): 8.8/5.0 (Mono/Colour) images per minute; Prints a 10.16 x 15.24cm borderless photo in 60s;4800x1200 dpi, Borderless Printing. CIS Flatbed Scanner, up to 600x1200 dpi, up to 21 copies"
    rut1.info3 = "Ink Bottle GI-790.C,M,Y,K: Standard Yield Mono 6000 prints#. Composite Colour 7000 prints#. Inbox Mono 18000 prints#;**Cost per print - 9 paise (Black & White), 33 paise (Colour) - As per ISO standards; Warranty – One Year onsite or 15000 Prints whichever is earlier*"
    rut1.info4 = "100 sheets Paper Input, 50 sheets Paper Output;100 sheets Paper Input, 50 sheets Paper Output"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def printer2(request):
    rut1 = Description()
    rut1.link1 = 'prin2'
    rut1.img1 = 'hp.jpg'
    rut1.img2 = 'hp1.jpg'
    rut1.img3 = 'hp2.jpg'
    rut1.name = 'HP Ink Tank 315 All-in-one'
    rut1.category = 'Ink-tank'
    rut1.price = '10799'
    rut1.info1 = "Printer type: inktank; Functions: printer; printer output: Monochrome; Connectivity: USB 2.0/ WiFi /airprint supported (No); Scanner (No)"
    rut1.info2 = "OS Compatibility: Windows 11; Windows 10; Windows 8; Windows Vista; macOS X 10.10 Yosemite; macOS 10.11 El Capitan; macOS 10.12 Sierra; Hardware Interface:USB 2.0 ; Enlarge/reduce option: No; Duplex: Manual"
    rut1.info3 = "Printer Page size: A4, B5, Letter, Legal (A4: 60 to 90 g/m²; HP envelopes: 75 to 90 g/m²; HP cards: up to 200 g/m²; HP 10 x 15 cm photo paper: up to 300 g/m²); Maximum Input Sheet Capacity: 60; Power wattage of printer: 10 Watts"
    rut1.info4 = "Special Features: Charging Port; Ideal Usage: Office; Included Components: Inkjet Printer 1N, (Black Ink Cartridge 1N,Color Ink Cartridge 1N,Power Cord 1N, USB Cable 1N,User Manual 5N) ."
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def printer3(request):
    rut1 = Description()
    rut1.link1 = 'prin3'
    rut1.img1 = 'hpl.jpg'
    rut1.img2 = 'hpl1.jpg'
    rut1.img3 = 'hpl2.jpg'
    rut1.name = 'HP Laserjet 138fnw Monochrome Compact'
    rut1.category = 'Laser-printer'
    rut1.price = '20799'
    rut1.info1 = "Printer type: Laser; Functions: Print, Copy, Scan, Fax; Printer output: Monochrome; Connectivity: USB/ WiFi-Direct, airprint supported - No; Scanner - Yes; Scanner resolution - Upto 600 dpi"
    rut1.info2 = "OS Compatibility: Windows: 7 (32/64 bit), 2008 Server R2, 8 (32/64 bit), 8.1 (32/64 bit), 10 (32/64 bit), 2012 Server, 2016 Server, macOS v10.14 Mojave, macOS v10.13 High Sierra, macOS v10.12 Sierra, OS X v10.11 El Capitan; Mobile connectivity - Yes; Hardware Interface - Ethernet, USB 2.0; Enlarge/reduce option - No; Duplex - Auto"
    rut1.info3 = "Printer Page size: A4, B5, Letter, Legal Maximum Input Sheet Capacity: 150 sheet input, 100 sheet output Duty Cycle - 10000 Pages Compatible ink: QUINK W1112A / 110A Premium Black Additional Printer Function Power wattage of printer - Active Printing: 300 watts, Ready: 38 watts, Sleep: 1.9 watts, Manual off: 0.2 watts"
    rut1.info4 = "Special Features: Get productive MFP performance at an price. Print, scan and copy, produce high-quality results, and print and scan from your phone;BEST-IN-CLASS MOBILE APP : HP Smart App - Get the app that's designed to control your printer. Get simple setup and print, scan, and copy from your phone with the HP Smart app. Connect via Wi-Fi or Ethernet and you'll be all set for mobile printing success"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def printer4(request):
    rut1 = Description()
    rut1.link1 = 'prin4'
    rut1.link1 = 'prin'
    rut1.img1 = 'canonl.jpg'
    rut1.img2 = 'canonl1.jpg'
    rut1.img3 = 'canonl2.jpg'
    rut1.name = 'Canon Laser Shot LBP2900B Mono Printer'
    rut1.category = 'Laser-printer'
    rut1.price = '22990'
    rut1.info1 = "Printer type: Functions: Print Only ; Printer output: Monochrome ; Connectivity: USB ; Scanner: No ; Scanner resolution: NA"
    rut1.info2 = "Maximum Print Speed (color): NA, Maximum Print Speed (Monochrome):12 ppm ; Print cost Monochrome: Rs 3.2 ; Print cost color: NA ;Maximum Print Resolution (Monochrome): 600 x 600dpi"
    rut1.info3 = "Special Features: High speed printing ; Ideal Usage : Home Office, Office; Included Components: Printer, Cartridge 303/303TS, User Software CD-ROM, Getting Started Guide, Power Cord"
    rut1.info4 = "Warranty - 1 year warranty from the date of purchase.Use only genuine Canon ink. Using counterfeit ink will harm your printer as well as render your warranty void."
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})

# Printer product description ends


# monitor Product Description Section Starts----->>
def tv1(request):
    rut1 = Description()
    rut1.link1 = 'mon1'
    rut1.img1 = 'l.jpg'
    rut1.img2 = 'l1.jpg'
    rut1.img3 = 'l2.jpg'
    rut1.name = 'Lenovo Q-Series 24 Inch '
    rut1.category = 'Monitor'
    rut1.price = '12699'
    rut1.info1 = "Display: 23.8-inch FHD(1920x1080) Monitor | IPS Panel Visual Experience: 16.7 Million Colours | 99 % sRGB | Brightness: 300 nits | Anti-Glare"
    rut1.info2 = "Aspect Ratio: 16: 9 | Viewing Angle: 178°/ 178° (Horizontal/Vertical) Design: NearEdgeless Ultra-slim Monitor | Tilt: -5°/ 22° | Lift Ranga 80mm | VESA Compatible Wall Mount(100x100)"
    rut1.info3 = "Refresh Rate: 75Hz | Response Time: 4ms | AMD Freesync | | Voltage: 15 Volts Warranty: This Monitor comes with Lenovo Authorised 3 Years Onsite Warranty"
    rut1.info4 = "Special features: Height Adjustment, Colour space upto 120% sRGB, Built-in speakers, Anti-Glare, Wall mountable"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def tv2(request):
    rut1 = Description()
    rut1.link1 = 'mon2'
    rut1.img1 = 's.jpg'
    rut1.img2 = 's1.jpg'
    rut1.img3 = 's2.jpg'
    rut1.name = 'Samsung 24-inch'
    rut1.category = 'Monitor'
    rut1.price = '9399'
    rut1.info1 = "24 inch Samsung Monitor - 1, 920 x 1, 080 Resolution IPS Panel Monitor 3-sided borderless display for All-expansive view"
    rut1.info2 = "Fluid pictures with 75hz refresh rate | 5 ms response time | 250cd/m2 Brightness(Typical) Aspect Ratio: 16: 9 | 178° Horizontal and Vertical Viewing Angle"
    rut1.info3 = "FreeSync and Game Mode to adjust any game and fill screen"
    rut1.info4 = "Eye Saver Mode and Flicker free to reduce eye strain Connectivity : D-Sub Port, HDMI"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def tv3(request):
    rut1 = Description()
    rut1.link1 = 'mon3'
    rut1.img1 = 'real.jpg'
    rut1.img2 = 'real1.jpg'
    rut1.img3 = 'real2.jpg'
    rut1.name = 'Realme 80 cm (32 Inches) HD Ready Smart'
    rut1.category = 'TV'
    rut1.price = '14000'
    rut1.info1 = "Connectivity: 3 HDMI Ports to connect set top box, Blu Ray players, gaming console | 2 USB Ports to connect hard drives and other USB devices | 1 VGA Slot to connect your Laptop/PC | 1 Headphone Jack | 1 AV Input Slot | 1 AV Output Slot | RF Slot"
    rut1.info2 = "Sound: 24 Watts Output | Quad Speakers | Dolby Audio | Cinematic Surround Sound"
    rut1.info3 = "Display: Ultra Bright Display | Chroma Boost Picture Engine | 178 Degree Viewing Angle | Brightness: 400nits Smart TV Features: Certified Android 9.0 (Pie) | In-Built Wi-Fi | In-Built Chromecast | 1GB RAM | 8GB ROM | In Built Apps: Netflix, Prime Video, Disney+Hotstar, Youtube"
    rut1.info4 = "Installation: For Installation/Wall Mounting/Demo Of This Product Once Delivered, Directly Contact_Us And Provide Product's Model Name And Seller's Details Mentioned On Your Invoice. The Service Center Will Allot You A Convenient Slot For The Service Warranty: 1 Year Standard Manufacturer Warranty And 2 Years Warranty On Panel From Realme"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})


def tv4(request):
    rut1 = Description()
    rut1.link1 = 'mon4'
    rut1.img1 = 'sony.jpg'
    rut1.img2 = 'sony1.jpg'
    rut1.img3 = 'sony2.jpg'
    rut1.name = 'Sony Bravia 80 cm (32 inches) HD Ready'
    rut1.category = 'Laser-printer'
    rut1.price = '25990'
    rut1.info1 = "Resolution: HD Ready(1366x768) | Refresh Rate: 50 hertz Connectivity: 2 HDMI ports to connect set top box, Blu Ray players, gaming console | 2 USB ports to connect hard drives and other USB devices"
    rut1.info2 = "Sound : 20 Watts Output | Open Baffle Speaker | ClearAudio+ technology | TV MusicBox Smart TV Features: Amazon Prime Video | Smart TV | Screen Mirroring | Netflix | HDR Gaming Display: HDR | X-Reality Pro | Motionflow XR"
    rut1.info3 = "Warranty Information: 1 year warranty provided by the manufacture from the date of purchase"
    rut1.info4 = "Installation: Brand will contact for installation for this product once delivered. Contact Sony for assistance (Please visit brand website for toll free numbers) and provide product's model name and seller's details mentioned on your invoice. The service center will allot you a convenient slot for the service"
    return render(request, 'port/portfolio-details.html', {'rut1': rut1})

# monitor product description ends

#url section starts


def description1a(request):
    rut1 = Description()
    rut1.link1 = '615'
    rut1.img1 = 'dir615.jpg'
    rut1.img2 = 'dir6151.jpg'
    rut1.img3 = 'dir6152.jpg'
    rut1.name = 'D-Link DIR - 615'
    rut1.category = 'Single - band'
    rut1.price = ' 799'
    rut1.info1 = "N 300 Mbps wireless Router with high gain Omni Antenna. Dynamic IP (DHCP) : Yes;Support Multiple operating modes: Router | AP | Repeater | Client;Easy Setup: Super simple set-up with the D-Link Assistant Mobile APP Or with intuitive WEB GUI setup wizard.;Advance security with WPA/WPA2 and firewall NAT, SPI, IP Filter, MAC Filter, DMZ, DDos prevention"
    rut1.info2 = "Always up-to-date with latest features / updates with online firmware upgrade;Support advance features like IPv6, TR-069, VLAN, static Routing etc.;Wireless Guest zone for visitors and wireless client bandwidth limitation;3 years Brand Warranty;N 300 Mbps wireless Router with high gain Omni Antenna. Dynamic IP (DHCP)"
    rut1.info3 = "Control Method: Application;High-Speed Wireless Networking"
    rut1.info4 = "Easy Configuration;Advanced Firewall Features;UPnP Support;Security Protocol: Wpswpa2-Psk Operating System: Windows 7windows"
    return render(request, 'billing.html', {'rut1': rut1})


def description2a(request):
    rut1 = Description()
    rut1.link1 = 'r15'
    rut1.img1 = 'r15.jpg'
    rut1.img2 = 'r151.jpg'
    rut1.img3 = 'r152.jpg'
    rut1.name = 'D-Link R15 AX1500 Eagle PRO'
    rut1.category = 'Dual - band'
    rut1.price = ' 2799'
    rut1.info1 = "Wi-Fi 6 AX 1500 Mbps WAVE 2 Dual band wireless router with 4 high gain Omni Antenna"
    rut1.info2 = "Gigabit Ports -- One Gigabit WAN & Three Gigabit LAN ports for high speed wired connectivity."
    rut1.info3 = "Easy Setup: Super simple set-up with the D-Link Eagle Pro AI Mobile APP Or with intuitive WEB GUI setup wizard."
    rut1.info4 = "D-Link AI Technology: AI Mesh Optimizer, AI Wi-Fi Optimizer, AI Traffic Optimizer, AI Parental Controls D-Link Easy Mesh Support, Can create a mesh network of 1+3 devices. 3 Year Warranty. Supports WPA, WPA2, and the latest WPA3 Wi-fi Security Security Protocol: Wpa2-Psk"
    return render(request, 'billing.html', {'rut1': rut1})


def description3a(request):
    rut1 = Description()
    rut1.link1 = 'r03'
    rut1.img1 = 'r03.jpg'
    rut1.img2 = 'r031.jpg'
    rut1.img3 = 'r032.jpg'
    rut1.name = 'D-Link R03 N300 Eagle PRO'
    rut1.category = 'Single - band'
    rut1.price = ' 809'
    rut1.info1 = "Wi-Fi 4 (802.11n) Technology with 300 Mbps speed;Dipole antenna for data transmission and reception improves range and performance"
    rut1.info2 = "4 x 10/100 Mbps Ethernet LAN ports. 1 x 10/100 Mbps Ethernet WAN port;Easy Setup: Super simple set-up with the D-Link Eagle Pro AI Mobile APP Or with intuitive WEB GUI setup wizard."
    rut1.info3 = "Wireless Comm Standard: 802 11 B;Color Name: White;Item Height: 36.0;Item Weight: 150.0;Included Components: Router, Power Adapter, Ethernet Cable, Qig;Special Features: Access Point Mode;Item Width: 132.0;Item Length: 158.0"
    rut1.info4 = "Always up-to-date with latest features / update with automatic online firmware upgrade;3 years Warranty;Call on toll free no.-1860-2333-999/0832-285-6000/0832-285-630. For E-Mail & Chat Support you can visit- service.dlink.co.in;Security Protocol: Wpa2-Psk"
    return render(request, 'billing.html', {'rut1': rut1})


def description4a(request):
    rut1 = Description()
    rut1.link1 = 'c86'
    rut1.img1 = 'archerc86.jpg'
    rut1.img2 = 'archerc861.jpg'
    rut1.img3 = 'archerc862.jpg'
    rut1.name = 'TP-Link Archer C86'
    rut1.category = 'Dual - band'
    rut1.price = ' 3699'
    rut1.info1 = "802.11ac Wave2 Wi-Fi —— 1300 Mbps on the 5 GHz band and 600 Mbps on the 2.4 GHz band 3×3 MIMO Technology —— Transmitting and receiving data on three streams to pair flawlessly with your 3×3 clients."
    rut1.info2 = "Boosted Wi-Fi Coverage —— Beamforming technology and six external antennas deliver a highly efficient wireless connection."
    rut1.info3 = "MU-MIMO —— To help your devices achieve optimal performance by making communication more efficient"
    rut1.info4 = "Personalized Management —— Advanced features like Parental Controls, Guest Network, and Access Control provide individualized tools for network management.Intelligent Connection —— Smart Connect directs clients to the less congested band and Airtime Fairness optimizes the time usage."
    return render(request, 'billing.html', {'rut1': rut1})


def description5a(request):
    rut1 = Description()
    rut1.link1 = 'c50'
    rut1.img1 = 'archerc50.jpg'
    rut1.img2 = 'archerc501.jpg'
    rut1.img3 = 'archerc502.jpg'
    rut1.name = 'TP-Link Archer C50'
    rut1.category = 'Dual - band'
    rut1.price = ' 1999'
    rut1.info1 = "Fast Wireless Speed —— Support smooth 4K streaming with AC1200 Wi-Fi;Superior Coverage —— 4 external antennas provide stable wireless connections and optimal coverage"
    rut1.info2 = "Intelligent Connection —— Easy network management at your fingertips with TP-Link Tether IPTV streaming —— Supports IGMP Proxy/Snooping, Bridge and Tag VLAN to optimize IPTV streaming;Access Point Mode —— Supports Access Point mode to create a new Wi-Fi access point"
    rut1.info3 = "In an unlikely case of product quality related issue, we may ask you to reach out to brand’s customer service support and seek resolution. We will require brand proof of issue to process replacement request.;Control Method: Application"
    rut1.info4 = "Operating System: Windows. Future-proof your network with IPv6 (Internet Protocol Version 6) support"
    return render(request, 'billing.html', {'rut1': rut1})


def description6a(request):

    rut1 = Description()
    rut1.link1 = 'xiaomirouter'
    rut1.img1 = 'xiaomi.jpg'
    rut1.img2 = 'xiaomi1.jpg'
    rut1.img3 = 'xiaomi2.jpg'
    rut1.name = 'Xiaomi Mi Smart Router 4C'
    rut1.category = 'Single - band'
    rut1.price = ' 999'
    rut1.info1 = "2.4 GHz Wi-Fi with up to 300Mbps Speed, Ideal for video streaming and web browsing. ROM : 16MB Nor Flash. Management application : Supports web, iOS, and Android"
    rut1.info2 = "4 High-performance antenna for better speed & coverage. Operating temperature: 0–40°C. Storage temperature:-40–70°C"
    rut1.info3 = "Control your network from Anywhere, Anytime with help of Mi Wi-Fi app QoS (Quality of Service) Manage and allocate bandwidth as per activity requirements"
    rut1.info4 = "Parental Control-Control time on internet and content on connected devices Improve network speed with Wi-Fi optimization Coverage Area: up to 400 Sqft"
    return render(request, 'billing.html', {'rut1': rut1})


def description7a(request):
    rut1 = Description()
    rut1.link1 = 'ac1200'
    rut1.img1 = 'AC1200.jpg'
    rut1.img2 = 'AC12001.jpg'
    rut1.img3 = 'AC12002.jpg'
    rut1.name = 'TP-Link AC1200 Mbps Archer A6'
    rut1.category = 'Tri - band'
    rut1.price = ' 2499'
    rut1.info1 = "AC1200 Dual-Band Wi-Fi —— 867 Mbps at 5 GHz and 400 Mbps at 2.4 GHz band"
    rut1.info2 = "MU-MIMO Technology —— Simultaneously transfers data to multiple devices for 2× faster performance"
    rut1.info3 = "Boosted Coverage —— Four external antennas equipped with Beamforming technology extend and concentrate the Wi-Fi signals"
    rut1.info4 = "Access Point Mode —— Supports AP Mode to transform your wired connection into the wireless network; Easy Setup —— Set up your Wi-Fi in minutes with the TP-Link Tether app.; Operating System: Windows; Control Method: Application Control Method: Application; Operating System: Windows"
    return render(request, 'billing.html', {'rut1': rut1})


def description8a(request):
    rut1 = Description()
    rut1.link1 = '825'
    rut1.img1 = 'dir825.jpg'
    rut1.img2 = 'dir8251.jpg'
    rut1.img3 = 'dir8252.jpg'
    rut1.name = 'D-Link DIR-825'
    rut1.category = 'Dual - band'
    rut1.price = ' 2630'
    rut1.info1 = "AC 1200 Mbps WAVE 2 Concurrent dual band wireless Router with 4 High gain Omni Antenna;802.11 a/b/g/n/ac standards with speed of 300 Mbps on 2.4Ghz & 867 Mbps on 5Ghz"
    rut1.info2 = "Gigabit Ports -- One Gigabit WAN & Four Gigabit LAN ports for high speed wired connectivity.;MU-MIMO -- MU-MIMO, which transmits data to multiple wireless devices simultaneously to increase speed and efficiency"
    rut1.info3 = "Multiple Operating modes: Router mode : to access the internet. Access Point mode : to extend wired network over wireless .Repeater mode : to extend the range of existing wireless router."
    rut1.info4 = "Easy Setup: Super simple set-up with the D-Link Assistant Mobile APP Or with intuitive WEB GUI setup wizard Control Method: Application;Operating System: Windows;Security Protocol: Wepwps"
    return render(request, 'billing.html', {'rut1': rut1})

# Router Product Description Section ends----->>


# Set top box Product Description Section Starts----->>
def settop1a(request):
    rut1 = Description()
    rut1.link1 = 'air'
    rut1.img1 = 'airtel.jpg'
    rut1.img2 = 'airtel1.jpg'
    rut1.img3 = 'airtel2.jpg'
    rut1.name = 'Airtel DTH HD'
    rut1.category = 'Set Top Box'
    rut1.price = ' 1000'
    rut1.info1 = "Airtel HD Set Top Box brings theatre-like experience to your home with HD Premium Quality Video (1080i resolution) and Dolby digital plus 5.1 surround sound"
    rut1.info2 = "Airtel D2H allows you to pause, record and play live TV so that you never miss your favourites as you can watch them later as per your convenience"
    rut1.info3 = "Enjoy free delivery and hassle-free installation of your DTH Set Top Box."
    rut1.info4 = "Any other accessory which is not a part of the standard installation will be charged separately"
    return render(request, 'billing.html', {'rut1': rut1})


def settop2a(request):
    rut1 = Description()
    rut1.link1 = 'd2'
    rut1.img1 = 'd2h.jpg'
    rut1.img2 = 'd2h1.jpg'
    rut1.img3 = 'd2h2.jpg'
    rut1.name = 'd2h HD DTH Connection'
    rut1.category = 'Set top box'
    rut1.price = ' 1299'
    rut1.info1 = "OFFER DETAILS : This is HD Set top box connection with 1 month Value Hindi Pack which includes Combo with popular Hindi,GEC, infotainment, News channels along with FTA Channels."
    rut1.info2 = "With this package get 7 popular HD channels for no additional cost when you become an existing d2h Subscriber"
    rut1.info3 = "Features & Support: 1080i Resolution, 5x better picture quality & exceptional clarity & crystal-clear surround sound. 24x7 Customer Care with regional language support."
    rut1.info4 = "5 Year warranty on Set Top Box Delivery & Installation: Home Delivery, Standard Installation and Demo"
    return render(request, 'billing.html', {'rut1': rut1})


def settop3a(request):
    rut1 = Description()
    rut1.link1 = 'cat'
    rut1.img1 = 'catvision.jpg'
    rut1.img2 = 'catvision1.jpg'
    rut1.img3 = 'catvision2.jpg'
    rut1.name = 'Catvision DD Free Dish'
    rut1.category = 'Set top Box'
    rut1.price = ' 1350'
    rut1.info1 = "Watch 115 + channels of Doordarshan Freedish service FREE OF COST"
    rut1.info2 = "1080P Full HD DVB-S2"
    rut1.info3 = "Supports USB PVR"
    rut1.info4 = "Easy-to-use Menu. A power of entertainment in your control."
    return render(request, 'billing.html', {'rut1': rut1})


def settop4a(request):
    rut1 = Description()
    rut1.link1 = 'free'
    rut1.img1 = 'dishtvfree.jpg'
    rut1.img2 = 'dishtvfree1.jpg'
    rut1.img3 = 'dishtvfree2.jpg'
    rut1.name = 'Dish TV Free to Air DTH '
    rut1.category = 'Set top Box'
    rut1.price = ' 1049'
    rut1.info1 = "No need to recharge for 2 years to watch free to air channels on this DishTV ZIng Super FTA Set top box"
    rut1.info2 = "Flexibility to add and remove any paid channels of your choice at any time from Dishtv App. This option is available on Dishtv only"
    rut1.info3 = "1 Year Warranty on FTA Set-top box Paid Channels can also be Added 150+ Channels & Services"
    rut1.info4 = "ACTIVATION PROCESS : To activate your Set Top Box Please type: ZING ACT (VC Number)(Customer Name) and Send it to 57575 or 9212012299 EXAMPLE: ZING ACT 12345678901 Name ( Local SMS Charges Apply ) : For any support/assistance call to customer care no. 95017-95017"
    return render(request, 'billing.html', {'rut1': rut1})


def settop5a(request):
    rut1 = Description()
    rut1.link1 = 'smart'
    rut1.img1 = 'dishtvsmart.jpg'
    rut1.img2 = 'dishtvsmart1.jpg'
    rut1.img3 = 'dishtvsmart2.jpg'
    rut1.name = 'DishTV Dish SMRT Android'
    rut1.category = 'Set top Box'
    rut1.price = ' 2635'
    rut1.info1 = "OFFER DETAILS: This is Android HD Set top box connection with 1 month Royale Sports Hindi HD Pack. This offer Includes Entertainment, Sports, along with popular kids, movies, news,infotainment channels."
    rut1.info2 = "With Dish SMRT Hub box make your TV/LCD into smart TV and enjoy OTT app, online gaming and other. Get so much more from your TV. The all new SMRT Hub allows you to switch between your favorite OTT channels, apps and games."
    rut1.info3 = "FEATURES & SUPPORT: 1080i Resolution, 5x better picture quality & exceptional clarity & crystal-clear surround sound. 24x7 Customer Care with regional language support."
    rut1.info4 = "Bluetooth Remote with Google Assistance Voice Search and Control Smart Home Devices with Google Assistant Built-in stream entertainment from Mobile to TV, Record content with External Disk Access to Google Play Store to download apps(Internet connection will be needed) Bluetooth Connectivity and a lot more."
    return render(request, 'billing.html', {'rut1': rut1})


def settop6a(request):
    rut1 = Description()
    rut1.link1 = 'dish'
    rut1.img1 = 'dishtv.jpg'
    rut1.img2 = 'dishtv1.jpg'
    rut1.img3 = 'dishtv2.jpg'
    rut1.name = 'DishTV HD DTH'
    rut1.category = 'Set top box'
    rut1.price = ' 2499'
    rut1.info1 = "OFFER DETAILS : This is HD Set top box connection with 1 month Family Saver Odiya pack which Includes Family entertainment with Odiya, GEC, Movies, Music, News channels."
    rut1.info2 = "Rs.2499 Pe Rs.1700 Cash Back offer - 1700 add back in your Dishtv connection as a recharge."
    rut1.info3 = "Features & Support : 1080i Resolution, 5x better picture clarity & surround sound, 24x7 Customer Care with regional language support."
    rut1.info4 = "Warranty - 5 Year on Set Top Box. Delivery & Installation: Free Delivery, Standard Installation and Demo"
    return render(request, 'billing.html', {'rut1': rut1})


def settop7a(request):
    rut1 = Description()
    rut1.link1 = 'xtreme'
    rut1.img1 = 'airtelxtreme.jpg'
    rut1.img2 = 'airtelxtreme1.jpg'
    rut1.img3 = 'airtelxtreme2.jpg'
    rut1.name = 'Airtel Xstream Box'
    rut1.category = 'Set top Box'
    rut1.price = ' 1929'
    rut1.info1 = "Turn your TV into a smart TV with access to Google Play Store and enjoy 5000+ apps and games on the big screen."
    rut1.info2 = "A cinematic experience awaits you with high definition 4K picture quality (1080i resolution) and 5.1 Dolby Surround System."
    rut1.info3 = "Choose from 550+ channels to create your own customised plan and switch between TV, OTT and YouTube at just a click."
    rut1.info4 = "Explore your favourite content with a Voice remote powered by Google Assistant and also command your TV DTH Recharge is compulsory for the product."
    return render(request, 'billing.html', {'rut1': rut1})


def settop8a(request):
    rut1 = Description()
    rut1.link1 = 'streme'
    rut1.img1 = 'd2hstreme.jpg'
    rut1.img2 = 'd2hstreme1.jpg'
    rut1.img3 = 'd2hstreme2.jpg'
    rut1.name = 'D2H Stream only Set Top Box'
    rut1.category = 'Set top Box'
    rut1.price = ' 1974'
    rut1.info1 = "OFFER DETAILS: This is Android HD only Set top box connection with 1 month Value Lite Hindi HD Pack. This offer Includes Complete Family entertainment with all Hindi GEC, Movies, Music, News channels along with FTA channels"
    rut1.info2 = "Gigabit Ports -- One Gigabit WAN & Four Gigabit LAN ports for high speed wired connectivity.;MU-MIMO -- MU-MIMO, which transmits data to multiple wireless devices simultaneously to increase speed and efficiency"
    rut1.info3 = "With d2h stream box make your TV/LCD into smart TV and enjoy OTT app, online gaming and other. Get so much more from your TV. The all new d2h Stream allows you to switch between your favorite OTT channels, apps and games."
    rut1.info4 = "FEATURES & SUPPORT: 1080i Resolution, 5x better picture quality & exceptional clarity & crystal-clear surround sound. 24x7 Customer Care with regional language support. It has excelent features like Inbuilt Wifi, Built-in Google Assistant, Dolby Audio, 2K Quad HD, Standard Recording, Bluetooth Remote"
    return render(request, 'billing.html', {'rut1': rut1})
# Set top box Product Description Section Ends----->>

# Firestick Product Description Section Starts----->>


def fire1a(request):
    rut1 = Description()
    rut1.link1 = 'fir'
    rut1.img1 = 'firetv.jpg'
    rut1.img2 = 'firetv1.jpg'
    rut1.img3 = 'firetv2.jpg'
    rut1.name = 'Fire TV Stick with Alexa'
    rut1.category = 'Plug and play'
    rut1.price = ' 3999'
    rut1.info1 = "Latest generation of our best-selling Fire TV device - 50% more powerful than the 2nd generation for fast streaming in Full HD. Includes Alexa Voice Remote with power and volume buttons."
    rut1.info2 = "Less clutter, more control - All-new Alexa Voice Remote (3rd Gen) lets you use your voice to search and launch shows across apps. All-new preset buttons get you to favorite apps quickly. Plus, control power and volume on your TV and soundbar with a single remote."
    rut1.info3 = "Home theater audio with Dolby Atmos - Feel scenes come to life with immersive Dolby Atmos audio on select titles with compatible home audio systems."
    rut1.info4 = "Tens of thousands of movies and shows from Prime Video, Netflix, Disney+ Hotstar, Zee5, SonyLIV, Sun NXT, ALT Balaji, Discovery Plus and many other Apps. Subscription fees may apply."
    return render(request, 'billing.html', {'rut1': rut1})


def fire2a(request):
    rut1 = Description()
    rut1.link1 = 'fir1'
    rut1.img1 = 'firetvlite.jpg'
    rut1.img2 = 'firetvlite1.jpg'
    rut1.img3 = 'firetvlite2.jpg'
    rut1.name = 'Fire TV Stick Lite'
    rut1.category = 'Plug and play'
    rut1.price = ' 2999'
    rut1.info1 = "Our most affordable Fire TV stick - Enjoy fast streaming in Full HD. Comes with all-new Alexa Voice Remote Lite (now with app control)."
    rut1.info2 = "Access to more than a million movies and TV show episodes from Prime Video, Netflix, Disney+ Hotstar, ZEE5, SonyLIV, Sun NXT, ALT Balaji, Discovery+ and many other apps. Subscription fees may apply."
    rut1.info3 = "What’s free - YouTube, YouTube Kids, MXPlayer, TVFPlay, YuppTV and many more. Easily search, play, pause, rewind, or forward content with just your voice. Simply say Alexa, find comedies."
    rut1.info4 = "Watch movies, web series, news, sports & kids content on your TV. Comes with parental control. Subscription fees may apply. Easy to set up and stays hidden – plug in behind your TV into an HDMI port, turn on the TV and connect to the internet to set up."
    return render(request, 'billing.html', {'rut1': rut1})


def fire3a(request):
    rut1 = Description()
    rut1.link1 = 'fir2'
    rut1.img1 = 'firetvlite4k.jpg'
    rut1.img2 = 'firetvlite4k1.jpg'
    rut1.img3 = 'firetvlite4k2.jpg'
    rut1.name = 'Fire TV Stick 4K Max streaming'
    rut1.category = 'Plug and Play'
    rut1.price = ' 6499'
    rut1.info1 = "Our most powerful streaming stick - 40% more powerful than Fire TV Stick 4K, with faster app starts and more fluid navigation."
    rut1.info2 = "Cinematic experience - Watch in vibrant 4K Ultra HD with support for Dolby Vision, HDR, HDR10 + and immersive Dolby Atmos audio(on select titles) Endless entertainment - Stream thousands of movies and TV episodes. Watch favorites from Netflix, Prime Video, Disney + Hotstar and many more apps. Subscription fees may apply."
    rut1.info3 = "Also compatible with the next-gen Wi-Fi 6 routers. Enjoy smoother 4K streaming across multiple Wi-Fi 6 compatible devices"
    rut1.info4 = "Live TV - Watch live TV, news, and sports with subscriptions to SonyLIV, Voot, Discovery+, and others. Alexa Voice Remote - Search and launch content with your voice. Get to favorite apps quickly with preset buttons. Control power and volume with one remote."
    return render(request, 'billing.html', {'rut1': rut1})


def fire4a(request):
    rut1 = Description()
    rut1.link1 = 'fir3'
    rut1.img1 = 'firetv4kall.jpg'
    rut1.img2 = 'firetv4kall1.jpg'
    rut1.img3 = 'firetv4kall2.jpg'
    rut1.name = 'Fire TV Stick 4K with all-new Alexa, Dolby Vision'
    rut1.category = 'Plug and play'
    rut1.price = ' 4999'
    rut1.info1 = "Cinematic experience - Watch in vibrant 4K Ultra HD with support for Dolby Vision, HDR, and HDR10+.Home theater audio with Dolby Atmos - Feel scenes come to life with support for immersive Dolby Atmos audio on select titles with compatible home audio systems"
    rut1.info2 = "Endless entertainment - Choose from thousands of movies and TV episodes. Enjoy favorites from Prime Video, Disney + Hotstar, Netflix, Zee5, Sony LIV, Apple TV and others. Subscription fees may apply.Watch Live TV – TV shows, news, reality shows and more from your favorite TV channels(supported by subscribed Apps), all in one place under Live Tab, direct from Fire TV home screen"
    rut1.info3 = "All-new Alexa Voice Remote - Search and launch content with your voice. Get to favorite apps quickly with preset buttons. Control power and volume with one remote.Control your smart home - Ask Alexa to check weather, dim the lights, view live camera feeds, stream music and more."
    rut1.info4 = "Simple and intuitive - Quickly access your favorite apps, live TV, and things you use most, all from the main menu.Easy to set up, compact enough to stay hidden - Plug in behind your TV, turn on the TV, and connect to the internet to get set up"
    return render(request, 'billing.html', {'rut1': rut1})


def fire5a(request):
    rut1 = Description()
    rut1.link1 = 'fir4'
    rut1.img1 = 'firesticksony.jpg'
    rut1.img2 = 'firesticksony1.jpg'
    rut1.img3 = 'firesticksony2.jpg'
    rut1.name = 'Fire TV Stick + Sony LIV Combo'
    rut1.category = 'Plug and Play'
    rut1.price = ' 4599'
    rut1.info1 = "Latest generation of our best-selling Fire TV device - 50% more powerful than the 2nd generation for fast streaming in Full HD. Includes Alexa Voice Remote with power and volume buttons."
    rut1.info2 = "Enjoy free access to Sony LIV for a year with the Fire TV Stick Plus. Fire TV Stick - 4999, Sony LIV - Rs 999. Total value of Fire TV Stick and subscription is Rs 5998. Subscription fees may be applicable from the second year.Home theater audio with Dolby Atmos - Feel scenes come to life with immersive Dolby Atmos audio on select titles with compatible home audio systems."
    rut1.info3 = "Tens of thousands of movies and shows from Sony LIV, Zee5, Voot Select, Prime Video, Netflix, Disney + Hotstar, Sun NXT, ALT Balaji, Discovery Plus and many other Apps. Subscription fees may apply.What’s included – A one-year subscription to Sony LIV. Additionally, enjoy YouTube, YouTube Kids, MXPlayer, TVFPlay, YuppTV and many more services for free."
    rut1.info4 = "The serial number associated with your device may be shared by Amazon with the participating App providers to enable activation of the purchased subscriptions. Fire TV Stick is also available without this offer."
    return render(request, 'billing.html', {'rut1': rut1})

# firestick product description ends

# ----------------------------------Internet Section ends-------------------------------------------------------#

# ----------------------------------Survelliance Section starts-------------------------------------------------------#

# Camera Product Description Section Starts----->>


def camera1a(request):
    rut1 = Description()
    rut1.link1 = 'cm1'
    rut1.img1 = 'cp.jpg'
    rut1.img2 = 'cp1.jpg'
    rut1.img3 = 'cp2.jpg'
    rut1.name = 'CP PLUS 2MP Full HD Smart Wi-Fi'
    rut1.category = '360° degree camera'
    rut1.price = '1699'
    rut1.info1 = "1080p full HD Plug & Play Wi-Fi PT camera, which enables crisp images that reveal the smallest details with absolute clarity. Now, Works with Alexa & Ok Google so you can go hands-free and enjoy the safety of a smart home. 36o Degree View offered by this EzyKam, saves cost and trouble of installing multiple cameras in any space to cover the full view of the area.Home-on-Phone, View the live video footage of your home/office anytime anywhere in the world on your phone."
    rut1.info2 = "Hassle-free Installation, Connect to your local Wi-Fi in a moment. Simply select a network, input the password, and you are good to go;Talk to the person on the other side while you see their live video feed and stay connected to your loved ones around the clock. Up to 128GB SD Card supported."
    rut1.info3 = "EzyKam + Supports Mobile APP with 4 Split Live Views.EzyKam + Supports Web Client with 9 Split Live Views.Material Type: Metal Included Components: Camera And Usb Specific Uses For Product: Surveillance"
    rut1.info4 = "Motion Detection & Human Detection : Human Detection avoids false alarms from moving pets. Smart Tracking function makes the camera follow moving objects, records real-time videos and sends instant alerts to your mobile."
    return render(request, 'billing.html', {'rut1': rut1})


def camera2a(request):
    rut1 = Description()
    rut1.link1 = 'cm2'
    rut1.img1 = 'mi.jpg'
    rut1.img2 = 'mi1.jpg'
    rut1.img3 = 'mi2.jpg'
    rut1.name = 'MI Xiaomi Wireless Home Security Camera'
    rut1.category = '360° degree camera'
    rut1.price = ' 2999'
    rut1.info1 = "Our most affordable Fire TV stick - Enjoy fast streaming in Full HD. Comes with all-new Alexa Voice Remote Lite (now with app control)."
    rut1.info2 = "Access to more than a million movies and TV show episodes from Prime Video, Netflix, Disney+ Hotstar, ZEE5, SonyLIV, Sun NXT, ALT Balaji, Discovery+ and many other apps. Subscription fees may apply."
    rut1.info3 = "What’s free - YouTube, YouTube Kids, MXPlayer, TVFPlay, YuppTV and many more. Easily search, play, pause, rewind, or forward content with just your voice. Simply say Alexa, find comedies."
    rut1.info4 = "Watch movies, web series, news, sports & kids content on your TV. Comes with parental control. Subscription fees may apply. Easy to set up and stays hidden – plug in behind your TV into an HDMI port, turn on the TV and connect to the internet to set up."
    return render(request, 'billing.html', {'rut1': rut1})


def camera3a(request):
    rut1 = Description()
    rut1.link1 = 'cm2'
    rut1.img1 = 'tp.jpg'
    rut1.img2 = 'tp1.jpg'
    rut1.img3 = 'tp2.jpg'
    rut1.name = 'TP-Link Tapo 360°'
    rut1.category = '360° degree camera'
    rut1.price = ' 2999'
    rut1.info1 = "Ultra-High-Definition Video —— Records every image in crystal-clear 3MP definition Pan and Tilt —— 360º horizontal range"
    rut1.info2 = "Advanced Night Vision —— Provides a visual distance of up to 30 ft Motion Detection and Notifications —— Notifies you when the camera detects movement"
    rut1.info3 = "Sound and Light Alarm —— Trigger light and sound effects to frighten away unwanted visitors Two-Way Audio —— Enables communication through a built-in microphone and speaker"
    rut1.info4 = "Safe Storage —— Locally stores up to 256 GB on a microSD card, equal to 512 hours(21 days) of footage. (Based on laboratory conditions) Voice Control —— Free Up Your Hands with Voice Control. Works with the Google Assistant and Amazon Alexa. (Google Assistant and Amazon Alexa are not available in all languages and countries)"
    return render(request, 'billing.html', {'rut1': rut1})


def camera4a(request):
    rut1 = Description()
    rut1.link1 = 'cm3'
    rut1.img1 = 'qubo.jpg'
    rut1.img2 = 'qubo1.jpg'
    rut1.img3 = 'qubo2.jpg'
    rut1.name = 'Qubo Smart 360 Wi-Fi CCTV'
    rut1.category = '360 degree camera'
    rut1.price = '2490'
    rut1.info1 = "PROUDLY INDIAN: Qubo Smart Cam 360 is Designed & Made in INDIA. Engineered for the Security Needs of the Indian Market; TRUST OF HERO GROUP: Our Round-the-Clock Customer Service & Wide field Network not only resolves your all concerns & queries but rather ensures complete peace of mind for Lifetime."
    rut1.info2 = "360 COVERAGE: The smart security camera supports Multi-Directional rotation of the lens ensuring that there are no blind spots. NOTE: Qubo Smart Cam 360 is designed to be used indoors only."
    rut1.info3 = "THEFT PROOF CLOUD STORAGE: Unlike traditional CCTV cameras, you can secure your recordings on cloud storage based in India. Your private home moments stay with you even if the device is stolen"
    rut1.info4 = "PERSON DETECTION WITH INTRUDER ALARM : The secutity camera has Advanced AI capabilities that can smartly detect & notify whenever a person is detected. You can also ring an automatic loud siren in case of an intrusion."
    return render(request, 'billing.html', {'rut1': rut1})


def camera5a(request):
    rut1 = Description()
    rut1.link1 = 'cm4'
    rut1.img1 = 'conbre.jpg'
    rut1.img2 = 'conbre1.jpg'
    rut1.img3 = 'conbre2.jpg'
    rut1.name = 'Conbre MultipleXR2 Pro'
    rut1.category = '360 degree camera'
    rut1.price = ' 1299'
    rut1.info1 = "COVER EVERY CORNER WITH 360 DEGREE VIEW : Rotate camera horizontally or vertically from anywhere in the world using mobile application.Product works on 4G only with minimum 2mbps speed. Power adapter input :100-240Vac 50/60Hz 0.3A Max."
    rut1.info2 = "READY ON THE GO: This smart wireless camera is designed with easy setup feature for do-it-yourself installation by using V380 mobile application available in your handsets market place"
    rut1.info3 = "DAY AND NIGHT VISION: Night vision up to 16-feet - never miss a moment, day or night, with visibility up to 16 feet in complete darkness. Communicate with family, friends and your pets on mobile devices. Talk to camera or listen to camera, there is no distance to communicate with anyone."
    rut1.info4 = "SEAMLESS CONNECTIVITY WITH MOBILE/TABLET: Quick Wi-Fi setup(Does not support 5G wi-fi network)) via iOS or Android Smartphone using supplied APP DETECT MOTION IN YOUR ABSENCE: HD night vision with inbuilt IR lens. MOTION DETECTION: Will send alerts whenever any motion is detected."
    return render(request, 'billing.html', {'rut1': rut1})

# camera product description ends


# All-in-one Product Description Section Starts----->>


def all1a(request):
    rut1 = Description()
    rut1.link1 = 'al1'
    rut1.img1 = 'cpall.jpg'
    rut1.img2 = 'cpall1.jpg'
    rut1.img3 = 'cpall2.jpg'
    rut1.name = 'CP Plus HD 2.4 MP 4-Channel DVR Kit'
    rut1.category = 'All-in-one'
    rut1.price = '9500'
    rut1.info1 = "HD 2. 4 MP 4-Channel DVR Kit"
    rut1.info2 = "Comes with 2 Dome, 2 Bullet Camera"
    rut1.info3 = "Comes with 2 Years Warranty"
    rut1.info4 = "1 TB HDD and All Required Accessories"
    return render(request, 'billing.html', {'rut1': rut1})


def all2a(request):
    rut1 = Description()
    rut1.link1 = 'al2'
    rut1.img1 = 'hikall.jpg'
    rut1.img2 = 'hikall1.jpg'
    rut1.img3 = 'hikall2.jpg'
    rut1.name = 'Hikvision 1MP HD Cameras Combo KIT'
    rut1.category = 'All-in-one'
    rut1.price = '9329'
    rut1.info1 = "Hikvision 1MP (720P) 4CH Turbo HD Mini DVR with 2 Dome & 2 Bullet Cameras Combo Kit without Hard Disk. Hikvision DS-6004HGHI-F1/ECO (1MP) (720P) 4CH Turbo HD Mini DVR"
    rut1.info2 = "1Pcs, Hikvision DS2CE51C0T-IRP/ECO 1MP Dome Cameras 2Pcs, Hikvision DS2CE11C0T-IRP/ECO 1MP Bullet Cameras 2Pcs, 90Mtr Copper Cable 1Bundle, 4CH Power Supply, BNC"
    rut1.info3 = "8Pcs, DC 4Pcs. Hard Disk & Installation is not included. DVR"
    rut1.info4 = "Description: H.264 & Dual-stream video compression. Support both HD-TVI /analog and AHD cameras with adaptive"
    return render(request, 'billing.html', {'rut1': rut1})


def all3a(request):
    rut1 = Description()
    rut1.link1 = 'al3'
    rut1.img1 = 'dahua.jpg'
    rut1.img2 = 'dahua1.jpg'
    rut1.img3 = 'dahua2.jpg'
    rut1.name = 'Dahua 4K Full HD 5MP Cameras Combo KIT'
    rut1.category = 'All-in-one'
    rut1.price = '18500'
    rut1.info1 = "Dahua Full HD 8 CH DVR ( Model ) - DH-XVR4B08H-I - 1 Nos"
    rut1.info2 = "Dahua 5 MP Bullete Camera - 3 Nos"
    rut1.info3 = "Dahua 5 MP Dome Camera - 1 Nos 2 TB Hard Drive - 1 Nos, "
    rut1.info4 = "CCTV 3+1 Cable Roll - 1 Nos,12V 5AMP SMPS - 1 Nos,BNC Connectors - 8 Nos,DC Connectors - 4 Nos"
    return render(request, 'billing.html', {'rut1': rut1})


def all4a(request):
    rut1 = Description()
    rut1.link1 = 'al4'
    rut1.img1 = 'hiksurv.jpg'
    rut1.img2 = 'hiksurv1.jpg'
    rut1.img3 = 'hiksurv2.jpg'
    rut1.name = 'HIKVISION Surveillance Kit of 4+12'
    rut1.category = 'All-in-one'
    rut1.price = '27990'
    rut1.info1 = "Comes with 16 Ch. DVR"
    rut1.info2 = "Comes with All Accessories"
    rut1.info3 = "Surveillance Kit"
    rut1.info4 = "2 years warranty"
    return render(request, 'billing.html', {'rut1': rut1})

# All-in-one product description ends

# DVRs Product Description Section Starts----->>


def dvr1a(request):
    rut1 = Description()
    rut1.link1 = 'dv1'
    rut1.img1 = 'hik.jpg'
    rut1.img2 = 'hik1.jpg'
    rut1.img3 = 'hik2.jpg'
    rut1.name = 'HIKVISION 4 Channel DVR'
    rut1.category = '4-channel'
    rut1.price = '3150'
    rut1.info1 = "HIKVISION 4 Channel 1080P Lite Upto 2MP H.265 DVR"
    rut1.info2 = "HDTVI/AHD/CVI/CVBS/IP video input[Support all brands cameras Upto 2MP]"
    rut1.info3 = "H.265+ DVR with higher compression rate"
    rut1.info4 = "Encoding ability up to 1080p lite @ 25/30 fps .Up to 5 channel IP camera input"
    return render(request, 'billing.html', {'rut1': rut1})


def dvr2a(request):
    rut1 = Description()
    rut1.link1 = 'dv2'
    rut1.img1 = 'cpdvr.jpg'
    rut1.img2 = 'cpdvr1.jpg'
    rut1.img3 = 'cpdvr2.jpg'
    rut1.name = 'CP PLUS 1080 4 Channel HD DVR'
    rut1.category = '4-channel'
    rut1.price = '2790'
    rut1.info1 = "4 ch. 1080P lite cosmic HD DVR / support upto 2.4MP IP Camera"
    rut1.info2 = "Auto adaptive HDCVI/AHD/TVI/CVBS signals / all channel 1080P lite real time recording"
    rut1.info3 = "H.264 dual-stream video compression / HDMI / VGA simultaneous video output"
    rut1.info4 = "Support 1 SATA HDD up to 6TB, 2 USB2.0 / mobile software: iCMOB, gCMOB .CMS software: KVMS, KVMS pro"
    return render(request, 'billing.html', {'rut1': rut1})


def dvr3a(request):
    rut1 = Description()
    rut1.link1 = 'dv3'
    rut1.img1 = 'cpdvr8.jpg'
    rut1.img2 = 'cpdvr81.jpg'
    rut1.img3 = 'cpdvr82.jpg'
    rut1.name = 'CP PLUS CP-UVR-0801E1-CV2'
    rut1.category = '8-channel'
    rut1.price = ' 3730'
    rut1.info1 = "Support 2MP Cameras and support upto 5MP IP camera"
    rut1.info2 = "Supports 1 SATA HDD up to 6TB, 2 USB2.0"
    rut1.info3 = "Mobile Software: iCMOB, gCMOB"
    rut1.info4 = "2 years warranty"
    return render(request, 'billing.html', {'rut1': rut1})


def dvr4a(request):
    rut1 = Description()
    rut1.link1 = 'dv4'
    rut1.img1 = 'hik8.jpg'
    rut1.img2 = 'hik8.jpg'
    rut1.img3 = 'hik8.jpg'
    rut1.name = 'Hikvision Speedlink Infosystems Turbo HD 5 MP Metal DVR with 16 Inch 2 SATA'
    rut1.category = '16-channel'
    rut1.price = '25999'
    rut1.info1 = "16-ch videoand4-ch audio input, H.265+/H.265/H.264+/H.264 encoding for the main stream, and H.265/H.264 for the sub-stream of analog cameras"
    rut1.info2 = "Self-adaptive HDTVI/HDCVI/AHD/CVBS signal input,Connectable to H.265+/H.265/H.264+/H.264 IP cameras"
    rut1.info3 = "Up to 5 MP resolution for recording . HDMI output at up to 4K(3840x2160) resolution"
    rut1.info4 = "Long distance transmission over UTP and coaxial cable, 16-ch synchronous playback"
    return render(request, 'billing.html', {'rut1': rut1})

# DVRs product description ends


# HDD and SSD Product Description Section Starts----->>

def ssd1a(request):
    rut1 = Description()
    rut1.link1 = 'ss1'
    rut1.img1 = 'tos.jpg'
    rut1.img2 = 'tos1.jpg'
    rut1.img3 = 'tos2.jpg'
    rut1.name = 'TOSHIBA Canvio Basics 1TB'
    rut1.category = 'HDD'
    rut1.price = '3999'
    rut1.info1 = "Super speed USB 3.0 port"
    rut1.info2 = "Easy plug-n-play operation"
    rut1.info3 = "Built-in internal shock sensor"
    rut1.info4 = "Country of Origin: Philippines"
    return render(request, 'billing.html', {'rut1': rut1})


def ssd2a(request):
    rut1 = Description()
    rut1.link1 = 'ss2'
    rut1.img1 = 'sea.jpg'
    rut1.img2 = 'sea1.jpg'
    rut1.img3 = 'sea2.jpg'
    rut1.name = 'Seagate One Touch 2TB External HDD'
    rut1.category = 'HDD'
    rut1.price = '5999'
    rut1.info1 = "Safely and easily manage 2 TB of photos, videos, movies, and more with hardware encrypted password-protection."
    rut1.info2 = "The perfect external hard drive for Windows or Mac, simply back up files with a single click or schedule automatic daily, weekly or monthly backups. Reformatting may be required for use with Time Machine."
    rut1.info3 = "Get an extra layer of protection for your data with the included 3 year Rescue Data Recovery Services."
    rut1.info4 = "Edit, manage, and share photos with a four-month membership to Adobe Creative Cloud Photography plan and one-year complimentary subscription to Mylio Create."
    return render(request, 'billing.html', {'rut1': rut1})


def ssd3a(request):
    rut1 = Description()
    rut1.link1 = 'ss3'
    rut1.img1 = 'cru.jpg'
    rut1.img2 = 'cru1.jpg'
    rut1.img3 = 'cru2.jpg'
    rut1.name = 'Crucial BX500 500GB 2.5-inch SATA 3D NAND Internal SSD'
    rut1.category = 'SSD'
    rut1.price = '2199'
    rut1.info1 = "The new Crucial BX500 500GB Internal Solid State Drive improves your overall system responsiveness. It delivers sequential Read and Write speeds of up to 550MB/s and 500MB/s respectively."
    rut1.info2 = "Being 3X faster than a standard HDD, this SATA Crucial SSD lets you feel the difference with super-fast OS boot times and application loads. It also features SSD Endurance (TBW) of 120 Terabytes."
    rut1.info3 = "With an operating temperature of 0°c to 70°c the 500GB SSD is designed to withstand any harsh operating environment. Equipped with advanced features like Thermal monitoring, Multistep data integrity algorithm the SSD ensures reliable performance."
    rut1.info4 = "The BX500 comes with a 3 year warranty and has undergone dozens of SSD qualification test, making it thoroughly tried, tested and proven."
    return render(request, 'billing.html', {'rut1': rut1})


def ssd4a(request):
    rut1 = Description()
    rut1.link1 = 'ss4'
    rut1.img1 = 'sam.jpg'
    rut1.img2 = 'sam1.jpg'
    rut1.img3 = 'sam2.jpg'
    rut1.name = 'Samsung 870 EVO 500GB SATA'
    rut1.category = 'SSD'
    rut1.price = '3829'
    rut1.info1 = "Sequential Read speeds up to 7,000MB/s. Performance varies based on system hardware and configuration"
    rut1.info2 = "Interface : PCIe 4.0 NVMe (PCIe Gen 4.0 x 4). Form Factor : M.2 (2280)"
    rut1.info3 = "Cache Memory: Samsung 1 GB DDR4 SDRAM 5-Year Limited Warranty or 600 TBW Limited Warranty."
    rut1.info4 = "Designed for tech enthusiasts, hardcore gamers, and professionals who blazing fast speed. To maximize the performance of the 980 PRO, please check whether your system supports PCIe 4.0 at the Intel or AMD website."
    return render(request, 'billing.html', {'rut1': rut1})

# HDD and SSD product description ends

# Printer Product Description Section Starts----->>


def printer1a(request):
    rut1 = Description()
    rut1.link1 = 'prin1'
    rut1.img1 = 'canon3000.jpg'
    rut1.img2 = 'canon30001.jpg'
    rut1.img3 = 'canon30002.jpg'
    rut1.name = 'Canon PIXMA G3000'
    rut1.category = 'Ink-tank'
    rut1.price = '14499'
    rut1.info1 = "Print, Scan, Copy;2 Additional Black ink bottles inside the box, along with 1 set of Cyan, Magenta, Yellow and Black Ink bottle (Total 6 ink bottles)"
    rut1.info2 = "Print Speed (A4): 8.8/5.0 (Mono/Colour) images per minute; Prints a 10.16 x 15.24cm borderless photo in 60s;4800x1200 dpi, Borderless Printing. CIS Flatbed Scanner, up to 600x1200 dpi, up to 21 copies"
    rut1.info3 = "Ink Bottle GI-790.C,M,Y,K: Standard Yield Mono 6000 prints#. Composite Colour 7000 prints#. Inbox Mono 18000 prints#;**Cost per print - 9 paise (Black & White), 33 paise (Colour) - As per ISO standards; Warranty – One Year onsite or 15000 Prints whichever is earlier*"
    rut1.info4 = "100 sheets Paper Input, 50 sheets Paper Output;100 sheets Paper Input, 50 sheets Paper Output"
    return render(request, 'billing.html', {'rut1': rut1})


def printer2a(request):
    rut1 = Description()
    rut1.link1 = 'prin2'
    rut1.img1 = 'hp.jpg'
    rut1.img2 = 'hp1.jpg'
    rut1.img3 = 'hp2.jpg'
    rut1.name = 'HP Ink Tank 315 All-in-one'
    rut1.category = 'Ink-tank'
    rut1.price = '10799'
    rut1.info1 = "Printer type: inktank; Functions: printer; printer output: Monochrome; Connectivity: USB 2.0/ WiFi /airprint supported (No); Scanner (No)"
    rut1.info2 = "OS Compatibility: Windows 11; Windows 10; Windows 8; Windows Vista; macOS X 10.10 Yosemite; macOS 10.11 El Capitan; macOS 10.12 Sierra; Hardware Interface:USB 2.0 ; Enlarge/reduce option: No; Duplex: Manual"
    rut1.info3 = "Printer Page size: A4, B5, Letter, Legal (A4: 60 to 90 g/m²; HP envelopes: 75 to 90 g/m²; HP cards: up to 200 g/m²; HP 10 x 15 cm photo paper: up to 300 g/m²); Maximum Input Sheet Capacity: 60; Power wattage of printer: 10 Watts"
    rut1.info4 = "Special Features: Charging Port; Ideal Usage: Office; Included Components: Inkjet Printer 1N, (Black Ink Cartridge 1N,Color Ink Cartridge 1N,Power Cord 1N, USB Cable 1N,User Manual 5N) ."
    return render(request, 'billing.html', {'rut1': rut1})


def printer3a(request):
    rut1 = Description()
    rut1.link1 = 'prin3'
    rut1.img1 = 'hpl.jpg'
    rut1.img2 = 'hpl1.jpg'
    rut1.img3 = 'hpl2.jpg'
    rut1.name = 'HP Laserjet 138fnw Monochrome Compact'
    rut1.category = 'Laser-printer'
    rut1.price = '20799'
    rut1.info1 = "Printer type: Laser; Functions: Print, Copy, Scan, Fax; Printer output: Monochrome; Connectivity: USB/ WiFi-Direct, airprint supported - No; Scanner - Yes; Scanner resolution - Upto 600 dpi"
    rut1.info2 = "OS Compatibility: Windows: 7 (32/64 bit), 2008 Server R2, 8 (32/64 bit), 8.1 (32/64 bit), 10 (32/64 bit), 2012 Server, 2016 Server, macOS v10.14 Mojave, macOS v10.13 High Sierra, macOS v10.12 Sierra, OS X v10.11 El Capitan; Mobile connectivity - Yes; Hardware Interface - Ethernet, USB 2.0; Enlarge/reduce option - No; Duplex - Auto"
    rut1.info3 = "Printer Page size: A4, B5, Letter, Legal Maximum Input Sheet Capacity: 150 sheet input, 100 sheet output Duty Cycle - 10000 Pages Compatible ink: QUINK W1112A / 110A Premium Black Additional Printer Function Power wattage of printer - Active Printing: 300 watts, Ready: 38 watts, Sleep: 1.9 watts, Manual off: 0.2 watts"
    rut1.info4 = "Special Features: Get productive MFP performance at an price. Print, scan and copy, produce high-quality results, and print and scan from your phone;BEST-IN-CLASS MOBILE APP : HP Smart App - Get the app that's designed to control your printer. Get simple setup and print, scan, and copy from your phone with the HP Smart app. Connect via Wi-Fi or Ethernet and you'll be all set for mobile printing success"
    return render(request, 'billing.html', {'rut1': rut1})


def printer4a(request):
    rut1 = Description()
    rut1.link1 = 'prin4'
    rut1.link1 = 'prin'
    rut1.img1 = 'canonl.jpg'
    rut1.img2 = 'canonl1.jpg'
    rut1.img3 = 'canonl2.jpg'
    rut1.name = 'Canon Laser Shot LBP2900B Mono Printer'
    rut1.category = 'Laser-printer'
    rut1.price = '22990'
    rut1.info1 = "Printer type: Functions: Print Only ; Printer output: Monochrome ; Connectivity: USB ; Scanner: No ; Scanner resolution: NA"
    rut1.info2 = "Maximum Print Speed (color): NA, Maximum Print Speed (Monochrome):12 ppm ; Print cost Monochrome: Rs 3.2 ; Print cost color: NA ;Maximum Print Resolution (Monochrome): 600 x 600dpi"
    rut1.info3 = "Special Features: High speed printing ; Ideal Usage : Home Office, Office; Included Components: Printer, Cartridge 303/303TS, User Software CD-ROM, Getting Started Guide, Power Cord"
    rut1.info4 = "Warranty - 1 year warranty from the date of purchase.Use only genuine Canon ink. Using counterfeit ink will harm your printer as well as render your warranty void."
    return render(request, 'billing.html', {'rut1': rut1})

# Printer product description ends


# monitor Product Description Section Starts----->>
def tv1a(request):
    rut1 = Description()
    rut1.link1 = 'mon1'
    rut1.img1 = 'l.jpg'
    rut1.img2 = 'l1.jpg'
    rut1.img3 = 'l2.jpg'
    rut1.name = 'Lenovo Q-Series 24 Inch '
    rut1.category = 'Monitor'
    rut1.price = '12699'
    rut1.info1 = "Display: 23.8-inch FHD(1920x1080) Monitor | IPS Panel Visual Experience: 16.7 Million Colours | 99 % sRGB | Brightness: 300 nits | Anti-Glare"
    rut1.info2 = "Aspect Ratio: 16: 9 | Viewing Angle: 178°/ 178° (Horizontal/Vertical) Design: NearEdgeless Ultra-slim Monitor | Tilt: -5°/ 22° | Lift Ranga 80mm | VESA Compatible Wall Mount(100x100)"
    rut1.info3 = "Refresh Rate: 75Hz | Response Time: 4ms | AMD Freesync | | Voltage: 15 Volts Warranty: This Monitor comes with Lenovo Authorised 3 Years Onsite Warranty"
    rut1.info4 = "Special features: Height Adjustment, Colour space upto 120% sRGB, Built-in speakers, Anti-Glare, Wall mountable"
    return render(request, 'billing.html', {'rut1': rut1})


def tv2a(request):
    rut1 = Description()
    rut1.link1 = 'mon2'
    rut1.img1 = 's.jpg'
    rut1.img2 = 's1.jpg'
    rut1.img3 = 's2.jpg'
    rut1.name = 'Samsung 24-inch'
    rut1.category = 'Monitor'
    rut1.price = '9399'
    rut1.info1 = "24 inch Samsung Monitor - 1, 920 x 1, 080 Resolution IPS Panel Monitor 3-sided borderless display for All-expansive view"
    rut1.info2 = "Fluid pictures with 75hz refresh rate | 5 ms response time | 250cd/m2 Brightness(Typical) Aspect Ratio: 16: 9 | 178° Horizontal and Vertical Viewing Angle"
    rut1.info3 = "FreeSync and Game Mode to adjust any game and fill screen"
    rut1.info4 = "Eye Saver Mode and Flicker free to reduce eye strain Connectivity : D-Sub Port, HDMI"
    return render(request, 'billing.html', {'rut1': rut1})


def tv3a(request):
    rut1 = Description()
    rut1.link1 = 'mon3'
    rut1.img1 = 'real.jpg'
    rut1.img2 = 'real1.jpg'
    rut1.img3 = 'real2.jpg'
    rut1.name = 'Realme 80 cm (32 Inches) HD Ready Smart'
    rut1.category = 'TV'
    rut1.price = '14000'
    rut1.info1 = "Connectivity: 3 HDMI Ports to connect set top box, Blu Ray players, gaming console | 2 USB Ports to connect hard drives and other USB devices | 1 VGA Slot to connect your Laptop/PC | 1 Headphone Jack | 1 AV Input Slot | 1 AV Output Slot | RF Slot"
    rut1.info2 = "Sound: 24 Watts Output | Quad Speakers | Dolby Audio | Cinematic Surround Sound"
    rut1.info3 = "Display: Ultra Bright Display | Chroma Boost Picture Engine | 178 Degree Viewing Angle | Brightness: 400nits Smart TV Features: Certified Android 9.0 (Pie) | In-Built Wi-Fi | In-Built Chromecast | 1GB RAM | 8GB ROM | In Built Apps: Netflix, Prime Video, Disney+Hotstar, Youtube"
    rut1.info4 = "Installation: For Installation/Wall Mounting/Demo Of This Product Once Delivered, Directly Contact_Us And Provide Product's Model Name And Seller's Details Mentioned On Your Invoice. The Service Center Will Allot You A Convenient Slot For The Service Warranty: 1 Year Standard Manufacturer Warranty And 2 Years Warranty On Panel From Realme"
    return render(request, 'billing.html', {'rut1': rut1})


def tv4a(request):
    rut1 = Description()
    rut1.link1 = 'mon4'
    rut1.img1 = 'sony.jpg'
    rut1.img2 = 'sony1.jpg'
    rut1.img3 = 'sony2.jpg'
    rut1.name = 'Sony Bravia 80 cm (32 inches) HD Ready'
    rut1.category = 'Laser-printer'
    rut1.price = '25990'
    rut1.info1 = "Resolution: HD Ready(1366x768) | Refresh Rate: 50 hertz Connectivity: 2 HDMI ports to connect set top box, Blu Ray players, gaming console | 2 USB ports to connect hard drives and other USB devices"
    rut1.info2 = "Sound : 20 Watts Output | Open Baffle Speaker | ClearAudio+ technology | TV MusicBox Smart TV Features: Amazon Prime Video | Smart TV | Screen Mirroring | Netflix | HDR Gaming Display: HDR | X-Reality Pro | Motionflow XR"
    rut1.info3 = "Warranty Information: 1 year warranty provided by the manufacture from the date of purchase"
    rut1.info4 = "Installation: Brand will contact for installation for this product once delivered. Contact Sony for assistance (Please visit brand website for toll free numbers) and provide product's model name and seller's details mentioned on your invoice. The service center will allot you a convenient slot for the service"
    return render(request, 'billing.html', {'rut1': rut1})

# monitor product description ends

#url section ends


def home(request):
    return render(request,'index.html')

def querries(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        querries = Contact(name=name, email=email,subject=subject,message=message,)
        querries.save()
        messages.success(request, "Your form has been successfully submitted..!!")
    return render(request,'index.html')

def newuser(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        newuser = registration(fname=fname, lname=lname, username=username, password=password, email=email,)
        newuser.save()
        messages.success(request, "You're Registration is successful your id will be activated within 10 minutes..!!")
    return render(request,'form.html')

def newsletters(request):
    if request.method == "POST":
        email = request.POST.get('email')
        newsletters = news(email=email)
        newsletters.save()
        messages.success(request, "Thanks for subscribing IT Solution..!!")
    return render(request,'index.html')

def delivery(request):
    if request.method == "POST":
        pname = request.POST.get('pname')
        pcategory = request.POST.get('pcategory')
        pprice = request.POST.get('pprice')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        payment = request.POST.get('payment')
        transaction = request.POST.get('transaction')
        transaction1 = request.POST.get('transaction1')
        delivery = billing(pname=pname,pcategory=pcategory,pprice=pprice,fname=fname, lname=lname, username=username, email=email, phone=phone, address1=address1, address2=address2, city=city, state=state, zip=zip, payment=payment,transaction=transaction,transaction1=transaction1)
        delivery.save()
        messages.success(request, "Your order has been placed and will be delivered soon..!!")
    return render(request,'billing.html')

    #Plans section starts------------------------>

def plan1(request):
    rut1 = Description()
    rut1.name = 'Trial plan'
    rut1.category = 'Wi-fi service'
    rut1.price = '299'
    # messages.success(
    #     request, "Your order has been placed and your plan will be activated within 10 minutes..!!")
    return render(request, 'billing.html', {'rut1': rut1})


def plan2(request):
    rut1 = Description()
    rut1.name = 'Business plan'
    rut1.category = 'Wi-fi service'
    rut1.price = '899'
    # messages.success(
    #     request, "Your order has been placed and your plan will be activated within 10 minutes..!!")
    return render(request, 'billing.html', {'rut1': rut1})


def plan3(request):
    rut1 = Description()
    rut1.name = 'Home plan'
    rut1.category = 'Laser-Wi-fi service'
    rut1.price = '599'
    # messages.success(
    #     request, "Your order has been placed and your plan will be activated within 10 minutes..!!")
    return render(request, 'billing.html', {'rut1': rut1})

# Plan section ends ------------------------------>