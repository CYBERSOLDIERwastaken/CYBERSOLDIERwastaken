import time

VersionInfo = "Foundation Terminal 9.0"
TerminalInfo = " \n Hazırlayan : Emirhan (P1) \n Amaç: Benim için (Emirhan) aslında herşey bunu yazmamdan birkaç gün önce başladı \n Python öğrenmeye çalışıyordum ve partik yapmak için aklıma bu tarz bir fikir geldi \n Ama Hikaye olaraak: \n 1980 lerde SCP vakfı için hazırlanan bir terminal \n diyebiliriz."






class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[33m'
    FAIL = '\033[31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    TEST = '\033[93m'

print(bcolors.FAIL + VersionInfo +  bcolors.ENDC) #Loading
time.sleep(1)
print (bcolors.WARNING + "Loading")
time.sleep(1)
print (".")
time.sleep(0.5)
print ("..")
time.sleep(0.5)
print ("..." + bcolors.ENDC)
time.sleep(0.5)
print(bcolors.HEADER + "Database verilerine erişim sağlandı" + bcolors.ENDC)
time.sleep(0.5)
print (bcolors.WARNING +"....")
time.sleep(0.5)
print ("....." + bcolors.ENDC)
time.sleep(0.5)
print(bcolors.HEADER + "Veri düzenlemesi tamamlandı" + bcolors.ENDC)
time.sleep(0.31)
print (bcolors.WARNING + "......" + bcolors.ENDC)
time.sleep(1)
print ("")
print ("Terminal taraması başlatılıyor...")
time.sleep(0.11)
print ("Renk testi başlatılıyor...")
time.sleep(0.112)
print(bcolors.FAIL + "1/10" +  bcolors.ENDC)
time.sleep(0.1)
print(bcolors.BOLD + "2/10" +  bcolors.ENDC)
time.sleep(0.1)
print(bcolors.ENDC + "3/10" +  bcolors.ENDC)
time.sleep(0.1)
print(bcolors.HEADER + "4/10" +  bcolors.ENDC)
time.sleep(0.1)
print(bcolors.OKBLUE + "5/10" +  bcolors.ENDC)
time.sleep(0.1)
print(bcolors.OKCYAN + "6/10" +  bcolors.ENDC)
time.sleep(0.1)
print(bcolors.OKGREEN + "7/10" +  bcolors.ENDC)
time.sleep(0.1)
print(bcolors.WARNING + "8/10" +  bcolors.ENDC)
time.sleep(0.1)
print(bcolors.UNDERLINE + "9/10" +  bcolors.ENDC)
time.sleep(0.1)
print(bcolors.TEST + "10/10" + bcolors.ENDC)
time.sleep(0.05)
print("Renk testi başarılı!")
print("Veri testi başlatılıyor...")
time.sleep(0.2)
print("Veri testi başarılı")
print (bcolors.HEADER + "Hata ile karşılaşırsanız yöneticiye bildirin" + bcolors.ENDC)
print ("")
time.sleep(0.09)
print ("Loading completed, Terminal is online and ready.")
print ("")
print ("")
print ("")

Komutlar = [ "Redacted", "1", "2", "3", "4", "5", "6" "Help", "SCP-096", "SCP-173", "CASSIE", "PA"  ] #Yazı verileri
Komutlar[0] = ""
Komutlar[1] = "<<< İsim: Emirhan ||| Yaş: 13 ||| Erişim Seviyesi: 4 ||| Görev: Vakıf Baş Teknisyeni >>>"
Komutlar[2] = "<<< İsim: Ertürk ||| Yaş: 14 ||| Erişim Seviyesi: 5 ||| Görev: 05 Konseyi >>>"
Komutlar[3] = "<<< İsim: Viper ||| Yaş: 13 ||| Erişim Seviyesi: 4 ||| Görev: MTF Operatörü >>>"
Komutlar[4] = "<<< İsim: Rigel ||| Yaş: 15 ||| Erişim Seviyesi: 3 ||| Görev: Bilim İnsanı >>>"
Komutlar[5] = "<<< İsim: Sevil Ecrin ||| Yaş: 15 ||| Erişim Seviyesi: 3 ||| Görev: Bilim İnsanı >>>"
Komutlar[6] = "<<< İsim: Sylox ||| Yaş: 15 ||| Erişim Seviyesi: 1 ||| Görev: Hademe >>>"
Komutlar[7] = (bcolors.BOLD + "<<< P1-P6 Vakıf personel bilgisi -pa hepsini gösterir- ||| '.' Çıkış ||| 'Login' Terminale erişim için gereklidir. \n ||| CASSIE ||| 'Help' , 'Yardım' ve '?' bu yazıyı görüntüler. >>> \n [ Daha fazla bilgi için TerminalInfo ]" + bcolors.ENDC)
Komutlar[8] = "Sınıf: Euclid | Özel Muhafaza Prosedürleri: SCP-096, her zaman 5x5x5 m hava geçirmez çelik bir küp hücrede saklanacaktır. Herhangi bir çatlak veya deliğe karşı haftalık kontroller yapılması zorunludur. SCP-096'nın hücresinde kesinlikle herhangi bir kamera veya optik cihaz bulunmayacaktır. Güvenlik personeli, SCP-096'nın hücrenin içinde bulunduğundan emin olmak için önceden kurulmuş basınç sensörleri ve lazer dedektörleri kullanacaktır. SCP-096 veya tasvirlerinin her türlü fotoğraf, video veya kaydı, Dr. ███ ve O5-█ onayı olmadığı sürece kesinlikle yasaktır. | Açıklama: SCP-096, yaklaşık 2.38 metre uzunluğunda insansı bir yaratıktır. SCP-096 çok düşük vücut kütlesine sahiptir ve vücut analizi beslenme bozukluğuna işaret etmektedir. Kollar, varlığın vücudunun geri kalanıyla orantısız olarak yaklaşık 1,5 metre uzunluğundadır. Cilt, pigmentasyondan yoksundur ve vücut üzerinde tüy görünmemektedir.SCP-096'nın çenesi, ortalama bir insanın dört (4) katı kadar açılabilir. Pigmentasyondan yoksun olan gözlerinin haricindeki diğer yüz özellikleri ortalama bir insana benzer şekildedir. SCP-096'nın kör olup olmadığı henüz bilinmemektedir. Yüksek beyin fonksiyonlarına ait hiçbir işaret göstermemekte ve akıllı olarak kabul edilmemektedir. Hücrenin içindeki basınç sensörlerinin gösterdiğine göre SCP-096 normalde son derece uysaldır ve günün çoğunu doğu duvarına doğru dikilerek geçirir. Ancak, bir kişi SCP-096'nın yüzünü, doğrudan video kaydı veya hatta bir fotoğraf aracılığıyla gördüğünde, şiddetli bir duygusal stres aşamasına girecektir. SCP-096 yüzünü elleriyle kapatacak, çığlık atmaya ve ağlamaya başlayacaktır. İlk görüldüğünden yaklaşık bir (1) ila iki (2) dakika sonra, SCP-096 yüzünü gören kişiye doğru koşmaya başlayacaktır(bu noktadan sonra kişiden SCP-096-1 olarak bahsedilecektir). Belgelenen hızlar otuz beş (35) km/s ile ███ km/saat arasındadır ve SCP-096-1'in uzaklığına bağlı olarak değişmekte gibi görünmektedir. Bu noktada, bilinen hiçbir malzeme veya yöntem SCP-096'nın ilerlemesini engelleyemez. SCP-096-1'in konumunun SCP-096 üzerinde bir etkisi yok gibi görünmektedir, varlık SCP-096-1'in konumunu anında bilebilmektedir. Not: Bu tepki resim tasvirleri görüldüğünde ortaya çıkmaz. (bknz Doküman 096-1). SCP-096, SCP-096-1'in konumuna vardığında onu öldürmeye ve [VERİ ÇIKARILDI] başlayacaktır. Vakaların %100'ünde SCP-096-1'den hiçbir iz kalmamıştır. Sonrasında SCP-096 bir kaç dakika oturacak ve sakinliğine ve uysallığına geri dönecektir. Daha sonra [VERİ ÇIKARILDI] doğal yaşam alanına geri dönme girişiminde bulunacaktır. Vakıf gizliliğinin ihlali ve büyük sivil kayıplara yol açacak kitlesel bir zincirleme reaksiyon olasılığı nedeniyle, SCP-096'nın kontrol altına alınması Alfa önceliğindedir.Dr. ███ SCP-096'nın derhal yok edilmesi için dilekçe verdi. (bkz. Mülakat 096-1). - Dilekçe onay bekliyor. - İmha Dilekçesi onaylandı ve Dr. ███ tarafından [VERİ ÇIKARILDI]'da gerçekleştirilecek. Bakınız Vaka-096-1-A.  DAHA FAZLA BİLGİ İÇİN: http://scpvakfi.wikidot.com/scp-096 "    

PA = "<<< İsim: Emirhan ||| Yaş: 13 ||| Erişim Seviyesi: 4 ||| Görev: Vakıf Baş Teknisyeni >>> <<< İsim: Ertürk ||| Yaş: 14 ||| Erişim Seviyesi: 5 ||| Görev: 05 Konseyi >>> <<< İsim: Viper ||| Yaş: 13 ||| Erişim Seviyesi: 4 ||| Görev: MTF Operatörü >>> <<< İsim: Rigel ||| Yaş: 15 ||| Erişim Seviyesi: 3 ||| Görev: Bilim İnsanı >>> <<< İsim: Sevil Ecrin ||| Yaş: 15 ||| Erişim Seviyesi: 3 ||| Görev: Bilim İnsanı >>> <<< İsim: Sylox ||| Yaş: 15 ||| Erişim Seviyesi: 1 ||| Görev: Hademe >>>"




print (Komutlar[7])
print ("")
while True: #Girilen komut kısmı ve cevap
    print ("")
    command = input('Terminal: ').strip()
    if command == 'Login':
        print('<<< Error Code : 0035 | Erişim sınırlaması kaldırıldı. >>>')
    elif command == 'pa':
        print(PA)
    elif command == 'PA':
        print(PA)        
    elif command == 'P1':
        print(Komutlar[1])  
    elif command == 'P2': 
        print(Komutlar[2])
    elif command == 'P3':
        print(Komutlar[3])
    elif command == 'P4':
        print(Komutlar[4])    
    elif command == 'P5':
        print(Komutlar[5])
    elif command == 'P6':
        print(Komutlar[6])    #45-59'a kadar olan kodlar Personel bilgisi kodudur ve büyük harfli halidir.
    elif command == 'p1':   
        print(Komutlar[1])  
    elif command == 'p2': 
        print(Komutlar[2])
    elif command == 'p3':
        print(Komutlar[3])
    elif command == 'p4':
        print(Komutlar[4])    
    elif command == 'p5':
        print(Komutlar[5])
    elif command == 'p6':
        print(Komutlar[6])    #59-71'a kadar olan kodlar Personel bilgisi kodudur ve küçük harfli halidir.
    elif command == 'Help':
        print(Komutlar[7])
    elif command == 'Yardım':
        print(Komutlar[7])       
    elif command == '?':
        print(Komutlar[7])        
    elif command == 'SCP-096':   
        print("")
        print("")
        print(Komutlar[8])
    elif command == '096':   
        print("")
        print("")
        print(Komutlar[8])
    elif command == 'CASSIE':
        print(bcolors.OKBLUE + "CASSIE - Central Autonomic Service System for Internal Emergencies - Dahili Acil Durumlar için Merkezi Otonom Hizmet Sistemi ||| C.A.S.S.I.E 'i başlatmak için 'start CASSIE'")
    elif command == 'Central Autonomic Service System for Internal Emergencies':
        print("CASSIE - Central Autonomic Service System for Internal Emergencies - Dahili Acil Durumlar için Merkezi Otonom Hizmet Sistemi ||| C.A.S.S.I.E 'i başlatmak için 'start CASSIE'")
    elif command == 'Dahili Acil Durumlar için Merkezi Otonom Hizmet Sistemi':
        print("CASSIE - Central Autonomic Service System for Internal Emergencies - Dahili Acil Durumlar için Merkezi Otonom Hizmet Sistemi ||| C.A.S.S.I.E 'i başlatmak için 'start CASSIE'")
    elif command == 'cassie':
        print("CASSIE - Central Autonomic Service System for Internal Emergencies - Dahili Acil Durumlar için Merkezi Otonom Hizmet Sistemi ||| C.A.S.S.I.E 'i başlatmak için 'start CASSIE'" + bcolors.ENDC)
    elif command == 'start cassie':
        print("ACTIVATING C.A.S.S.I.E SYSTEM")
        time.sleep(0.39)
        print("C.A.S.S.I.E IS ONLINE")
        time.sleep(0.4)
        print("Scanning Facility Situation .")
        time.sleep(0.4)
        print("Scanning Facility Situation ..")
        time.sleep(0.4)
        print("Scanning Facility Situation ...")
        time.sleep(0.35)
        print("FACILITY SCAN ERROR")
        print ("")
        print("Please restart and config C.A.S.S.I.E before activate ")
        print("C.A.S.S.I.E IS OFFLINE")
    elif command == 'START CASSIE':
        print("ACTIVATING C.A.S.S.I.E SYSTEM")
        time.sleep(0.39)
        print("C.A.S.S.I.E IS ONLINE")
        time.sleep(0.4)
        print("Scanning Facility Situation .")
        time.sleep(0.4)
        print("Scanning Facility Situation ..")
        time.sleep(0.4)
        print("Scanning Facility Situation ...")
        time.sleep(0.66)
        print(bcolors.FAIL +  "FACILITY SCAN ERROR" + bcolors.ENDC)
        print ("")
        print("Please restart and config C.A.S.S.I.E before activate ")
        print(bcolors.FAIL + "C.A.S.S.I.E IS OFFLINE" + bcolors.ENDC )
    elif command == 'CASSIE start config = TUR safe_mode': 
        print("C.A.S.S.I.E Başlatılıyor")
        time.sleep(0.39)
        print("C.A.S.S.I.E aktif")
        time.sleep(0.4)
        print(bcolors.OKGREEN + "TESİS STATÜSÜ TARANIYOR.")
        time.sleep(0.4)
        print("TESİS STATÜSÜ TARANIYOR ..")
        time.sleep(0.4)
        print("TESİS STATÜSÜ TARANIYOR ...")
        time.sleep(0.35)
        print("TESİS TARAMASI BAŞARILI" + bcolors.ENDC)
        print ("")
        print("TARAMA SONUÇLARI")
        print("C.A.S.S.I.E Sisteminin aktifleşmesini gerektiren bir durum bulunmamaktadır, Rapor yönetime gönderildikten sonra C.A.S.S.I.E deaktifleşecek." +  bcolors.ENDC)
        print("SCP itemi: 6 = 049, 096, 106, 500, 008, 002 ")
        time.sleep(0.31)
        print("Class D Personel: 90 | Bilim insanı/Araştırma görevlisi: 22 | Gardiyan/MTF: 21")
        time.sleep(0.4)
        print(bcolors.FAIL + "C.A.S.S.I.E deaktif." +  bcolors.ENDC)
    elif command == 'CASSIE start config = ENG safe_mode':
        print(".")
        time.sleep(0.01)
        print("C.A.S.S.I.E IS STARTING")
        time.sleep(0.01)
        print("..")
        time.sleep(0.01)
        print("...")
        time.sleep(0.1) 
        print("C.A.S.S.I.E IS STARTING")
        time.sleep(0.39)
        print("C.A.S.S.I.E ONLINE")
        time.sleep(0.4)
        print(bcolors.OKGREEN + "FACILITY IS SCANNING.")
        time.sleep(0.4)
        print("FACILITY IS SCANNING ..")
        time.sleep(0.4)
        print("FACILITY IS SCANNING ...")
        time.sleep(0.35)
        print("FACILITY SCAN SUCCESFUL" + bcolors.ENDC)
        print ("")
        print("SCAN RESULTS:")
        print("There is no situation that requires the activation of the C.A.S.S.I.E System, C.A.S.S.I.E will be deactivated after the report is sent to the management." +  bcolors.ENDC)
        print("SCP(s): 6 = 049, 096, 106, 500, 008, 002 ")
        time.sleep(0.31)
        print("Class D Personel: 90 | Scientist: 22 |Guard/MTF: 21")
        time.sleep(0.4)
        print(bcolors.FAIL + "C.A.S.S.I.E DEACTIVE." +  bcolors.ENDC)
    elif command == 'TerminalInfo':
        print(TerminalInfo)    
    elif command == 'quit':
        break    
    elif command == '.':
        break 
    else:
        print('Veri/Komut bulunamadı veya erişim yetkiniz yetmiyor.')
        
        
        
        
        
        
        
        #     elif command == '':
        #       print(Komutlar[])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Yol : "C:\Dosyalar\Yazılım\Python\Foundation Terminal 6-0.py"