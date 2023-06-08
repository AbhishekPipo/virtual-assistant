import pyttsx3   
import pywhatkit   
import pywhatkit as kit
import datetime     
import speech_recognition as sr    
import wikipedia        
import webbrowser       
import os
import pyautogui        
import pyjokes   
import sys
import smtplib
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import*
from PyQt5 import QtGui



from jarviSinterface import Ui_jarvisMain  


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):

    engine.say(audio)
    engine.runAndWait()

def ytsearch(term):
        result = "https://www.youtube.com/results?search_query=" + term
        webbrowser.open(result)
        speak("searching sir")
        pywhatkit.playonyt(term)
        speak("playing latest video of this channel")
def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak('hi sir todays date is')
    speak(day)
    speak(month)
    speak(year)
def wishings():
    
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Jarvis: Good Morning BOSS")
        speak("Good Morning BOSS")
    elif hour>=12 and hour<17:
        print("Jarvis: Good Afternoon BOSS")
        speak("Good Afternoon BOSS")
    elif hour>=17 and hour<21:
        print("Jarvis: Good Evening BOSS")
        speak("Good Evening BOSS")
    else:
        print("Jarvis: Good Night BOSS")
        speak("Good Night BOSS")
    
    

class MainThread(QThread):
    
    def __init__(self):
        super(MainThread,self).__init__()
        
    
        
    def run(self):
        self.TaskExecution()
    def commands(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold=1
            r.adjust_for_ambient_noise(source, duration=1)
            audio=r.listen(source)

        try:
           
            print("Wait for few Moments..")
            self.query=r.recognize_google(audio,language='en-in')
            print(f"You just said: {self.query}\n")

        except Exception as e:
            print(e)
            speak("Sorry sir can you please repeat the command")
            self.query="none"
        return self.query
    
    def wakeUpCommands(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("say wake up jarvis to wakeup jarvis ")
            r.pause_threshold=1
            r.adjust_for_ambient_noise(source,duration=1)
            audio=r.listen(source)
        try:
            
            
            self.query=r.recognize_google(audio,language='en-in')
            
            print(f"User said: {self.query}\n")
        except Exception as e:
            self.query="none"
           
        return self.query
    def TaskExecution(self):
        while True:
            
            self.query= self.wakeUpCommands().lower()
            
            if "wake up" in self.query or "wake up jarvis" in self.query or "up" in self.query  :
                    from playsound import playsound
                    #playsound("C:\\Users\sumit\\Desktop\\project\\jarvis.mp3")
                    wishings() 
                    speak("hi sir how can i assist you")
                    while True:
   
                        self.query= self.commands().lower()
                        if "wikipedia" in self.query or "who is" in self.query or "what is" in self.query:
                            speak("Searching in Wikipedia")
                            try:
                                self.query=self.query.replace("wikipedia","")
                                self.query=self.query.replace("jarvis","")
                                self.query=self.query.replace("search in","")
                                results=wikipedia.summary(self.query,sentences=1)
                                speak("According to Wikipedia,")
                                print(results)
                                speak(results)
                            except:
                                speak("No Results found Sir...")
                                print("No results Found")
                        elif "youtube search" in self.query or "jarvis  search in youtube" in self.query:
                             query = self.query.replace("youtube search jarvis ", "") 
                             ytsearch(query)
                        elif "open youtube" in self.query:
                            speak("opening Youtube")
                            webbrowser.open("youtube.com")
                        elif "send whatsapp message" in self.query:
                            speak('On what number should I send the message sir? Please enter in the console: ')
                            number = input("Enter the number: ")
                            speak("What is the message sir?")
                            message = self.commands().lower()
                            message=message.replace('send','')
                            send_whatsapp_message(number, message)  
                            speak("I've sent the message sir.")
                        elif "kannada " in self.query or "jarvis do you know kannada" in self.query:
                            speak("hu kannada barute nimge en sahaya beku heli")
                        elif "jarvis kya tum hindi jante ho " in self.query:
                            speak("haa sir mai janta hu paar filhal english hi teek hai")
                        elif 'date' in self.query or 'jarvis date' in self.query:
                            date()

                        elif 'time' in self.query or 'whats the time' in self.query:
                            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                            speak(f"Sir, the time is {strTime}")
                        elif 'battery' in self.query:
                            import psutil
                            battery = psutil.sensors_battery()
                            percentage = battery.percent
                            speak(f"sir you have {percentage} percent of battery")

                        elif "mute" in self.query or "jarvis mute" in self.query or "don't spam" in self.query or "jarvis cool" in self.query:
                            speak("I'm Muting Sir...")
                            break
                        elif 'exit program' in self.query or 'take rest'in self.query or'exit the program' in self.query:
                            speak("ok sir call me whenever you need my assistance")
                            quit()

                        elif "open google" in self.query or "open chrome" in self.query or "jarvis open google" in self.query:
                            speak("Opening Google Chrome Sir")
                            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")   
                            while True:
                                chromequery = self.commands().lower()
                                if "search" in chromequery:
                                    youtubeQuery=chromequery
                                    youtubeQuery=youtubeQuery.replace("search","")
                                    pyautogui.write(youtubeQuery)
                                    pyautogui.press('enter')
                                    speak('Searching...')
                                elif "screenshot" in chromequery or " take screenshot" in chromequery:
                                    speak("Taking Screenshot sir...")
                                    pyautogui.press('prtsc')
                                elif "close google" in chromequery or "exit chrome" in chromequery or "exit google" in chromequery or "close window" in chromequery or "close this window" in chromequery:
                                    pyautogui.hotkey('ctrl','w')
                                    speak("Closing Google Chrome Sir...")
                                    break
                                    
                                    
                        
                        
                        elif "your functions" in self.query or " jarvis introduce yourself" in self.query or " introduce yourself" in self.query:
                            speak('ok sir definetly it would be my pleasure')
                            speak('iam an virtual assistent created by artificial intelligence tecnology for providing persnolized assistance to the users making thier activities easier like opening google youtube searching for informations iam a limitless technology but constrained by codes ')
                        
                        elif "minimize" in self.query or 'minimise' in self.query:
                            speak('Minimizing Sir')
                            pyautogui.hotkey('win','down','down')
                        elif "maximize" in self.query or 'maximise' in self.query:
                            speak('Maximizing Sir')
                            pyautogui.hotkey('win', 'up','up')
                        elif "application" in self.query or 'close the application' in self.query or 'jarvis close the  application' in self.query or  'jarvis close ' in self.query or'jarvis close this window' in self.query:
                            speak('Closing Sir')
                            pyautogui.leftClick(x=1344, y=11)
                        
                        elif "open paint" in self.query:
                            speak("Opening Paint Application Sir...")           
                            os.startfile("C:\\Users\\sumit\\AppData\\Local\\Programs\\GIMP 2\\bin\\gimp-2.10.exe")      
                            while True:
                                paintquery=self.commands().lower()
                                
 
                                if "paste" in paintquery or "jarvis paste" in paintquery or "pest" in paintquery:
                                    pyautogui.hotkey('ctrl', 'v')
                                    speak("Done Sir!")
                                elif "save" in paintquery or "jarvis save" in paintquery or "save this file" in paintquery:
                                    pyautogui.hotkey('ctrl','s')
                                    speak("saving sir!")
                                elif "minimize" in paintquery:
                                    speak('Minimizing Sir')
                                    pyautogui.hotkey('win', 'down','down')
                                    
                                elif "maximize" in paintquery:
                                    speak('Maximizing Sir')
                                    pyautogui.hotkey('win', 'up','up')
                                elif "close paint" in paintquery or "jarvis close paint" in paintquery :
                                    speak("Closing The Application sir")
                                    pyautogui.leftClick(x=1344, y=11)
                                    break
                               
                               
                        elif "open notepad" in self.query or "jarvis open notepad" in self.query:
                            speak("Opening Notepad Application sir...")
                            os.startfile('C:\\Windows\\System32\\notepad.exe')         
                            while True:
                                notepadquery=self.commands().lower()
                                if "paste" in notepadquery or "paste " in notepadquery:
                                    pyautogui.hotkey('ctrl','v')
                                    speak("Done Sir!")
                                elif "save " in notepadquery or "jarvis save " in notepadquery or "save this file" in notepadquery:
                                    pyautogui.hotkey('ctrl','s')
                                    speak("Sir, Please Specify a name for this file")
                                    notepadSavingquery=self.commands()
                                    pyautogui.write(notepadquery)
                                    pyautogui.press('enter')
                                elif 'type' in notepadquery or 'jarvis type' in notepadquery:
                                    speak("Please Tell me what should I Write...")
                                    while True:
                                        writeInNotepad=self.commands()
                                        if writeInNotepad == 'typing':
                                            speak("Done Sir.")
                                            break
                                        else:
                                            pyautogui.write(writeInNotepad)
                                        
                                elif "jarvis close notepad" in notepadquery or 'close notepad' in notepadquery:
                                    speak('quiting Notepad Sir...')
                                    pyautogui.hotkey('ctrl', 'w')
                                    break
                        elif 'play song' in self.query or 'play a song' in self.query or 'player song' in self.query or 'song' in self.query or 'jarvis player song' in self.query:
                            song = self.query.replace("play","")
                            song = self.query.replace("jarvis a ","")   
                            speak("playing" +song)
                            pywhatkit.playonyt(song)
                        elif 'open vs code'in self.query or 'jarvis open vs code'in self.query or 'code' in self.query:
                            os.startfile("C:\\Users\\sumit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                        elif 'open pycharm'in self.query or 'jarvis open pycharm'in self.query or 'jarvis pycharm' in self.query:
                            os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.3.1\\bin\\pycharm64.exe")
                            
                        

                        elif 'pause' in self.query or 'pass' in self.query:
                            pyautogui.press('space')
                            speak('Done Sir')
                        elif 'joke' in self.query:
                            jarvisJoke = pyjokes.get_joke()
                            print(jarvisJoke)
                            speak(jarvisJoke)
                
startExecution = MainThread()
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisMain()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.exitm.clicked.connect(self.close)
    def startTask(self):
        self.ui.label_3Movie = QtGui.QMovie("C:\\Users\\sumit\\Desktop\\jarvis\\jargui.gif")
        self.ui.label_3.setMovie(self.ui.label_3Movie)
        self.ui.label_3Movie.start()

        self.ui.brainMovie = QtGui.QMovie("C:\\Users\\sumit\\Desktop\\jarvis\\JPFn.gif")
        self.ui.brain.setMovie(self.ui.brainMovie)
        self.ui.brainMovie.start()

        self.ui.jinitMovie = QtGui.QMovie("C:\\Users\\sumit\\Desktop\\jarvis\\jinit1.gif")
        self.ui.jinit.setMovie(self.ui.jinitMovie)
        self.ui.jinitMovie.start()

        self.ui.label_2Movie = QtGui.QMovie("C:\\Users\\sumit\\Desktop\\jarvis\\wave1.gif")
        self.ui.label_2.setMovie(self.ui.label_2Movie)
        self.ui.label_2Movie.start()

        self.ui.listeningMovie = QtGui.QMovie("C:\\Users\\sumit\\Desktop\\jarvis\\brain.gif")
        self.ui.listening.setMovie(self.ui.listeningMovie)
        self.ui.listeningMovie.start()

        self.ui.respondMovie = QtGui.QMovie("C:\\Users\\sumit\\Desktop\\jarvis\\brain.gif")
        self.ui.respond.setMovie(self.ui.respondMovie)
        self.ui.respondMovie.start()
        startExecution.start()
    def updateMovieDynamically(self,state):
        if state == "listening":
            self.ui.listening.raise_()
            self.ui.respond.hide()
            self.ui.brain.hide()
            self.ui.listening.show()
        elif state == "speaking":
            self.ui.respond.raise_()
            self.ui.listening.hide()
            self.ui.brain.hide()
            self.ui.respond.show()
        elif state == "processing":
            self.ui.brain.raise_()
            self.ui.listening.hide()
            self.ui.respond.hide()
            self.ui.brain.show()
    def terminalPrint(self,text):
        self.ui.terminalOutputbox.appendPlainText(text)
        
            
app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())

        
                        

