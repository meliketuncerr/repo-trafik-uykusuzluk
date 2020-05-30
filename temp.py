from twilio.rest import Client
import cv2
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
sum_eyes = 0
count = 0
while 1:
    sum_eyes=0 
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]       
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        for (ex,ey,ew,eh) in eyes:             
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            sum_eyes = ex+ey+ew+eh #eğer koordinatlar toplamı 0'dan büyükse tespit ettiğini anlarız
    if sum_eyes==0: #eğer tespit etmezse
          count=count+1
          print("Not found")
          if count==100:  #eğer 100 kez algılamazsa ki bu da 4-5 saniyeye tekabül ediyor
                #ChromeDriverManager().install()
                print("Wake UP!!!!!!!!!")
                driver = webdriver.Chrome(ChromeDriverManager().install())  
                url = "https://www.youtube.com/watch?v=4rsXvmv7ty0&list=PLDIoUOhQQPlVr3qepMVRsDe4T8vNQsvno"
                driver.get(url) #youtube url sini açar
                print(driver.title)
#bu iki girdi Account SID ve Auth Token         
                client = Client("AC0cb9d1626885aece8ea1466c809ecaa8", "84629baf89b344023c67659ba342e0c4")
#atacağın numara "to" kendi numaranız, "from" twilio numaranız (kayıt olunca veriyor)
#body kısmı ise ileteceğiniz mesaj                  
                #      +12058436069
                client.messages.create(to="+905445901958", 
                       from_="+12244781894", 
                       body="Wake Uppp")
                
    else:
          print("Found")
        

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
