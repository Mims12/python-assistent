import pyttsx3
import datetime
import os
import webbrowser
e = datetime.datetime.now()

pyttsx3.speak("Hi there, please tell me what can I help you with")
print("Hi there , please tell me what can I help you with")
print()

pyttsx3.speak("please choose from below mentioned options")
print("Please choose from below mentioned options")

while True:
  print("A. Know current time and Date ")
  print("B. Open firefox web browser ")
  print("C. Open a text editor ")
  print("D. Have some great coding session")
  print("E. Or you just want to have some fun") 
  print("F. nothing")
  print()

  #pyttsx3.speak("Please write down your requirement")
  print("Please write down your requirement : ",end=' ')

  req = input()

  if ("time" in req) or ("date" in req) or ("A" in req) or ("A." in req):
    print (e.strftime("%Y-%m-%d %H:%M:%S")) 
    pyttsx3.speak(e.strftime("%Y-%m-%d %H:%M:%S"))
 
  elif (("open" in req) or ("run" in req) or ("execute" in req))and ("firefox" in req) or ("B" in req):
    os.system("firefox")
    pyttsx3.speak("Here yo go")
  
  elif(("open" in req) or ("run" in req) or ("execute" in req)) and (("text editor" in req) or ("editor" in req)) or ("C" in req):
    pyttsx3.speak("Please choose from the following list of editors")
    print("Please choose from the following list of editors")
    print()
    print("Visual Studio code")
    print("Notepad")  
    print("WordPad")
    print()
    print("Please write down your requirement:", end=' ')
    
    text= input()
    if("code" in text)or (" visual studio" in text) or ("visual studio code" in text):
       pyttsx3.speak("Here yo go")
       os.system("code")
    elif("notepad" in text):
      pyttsx3.speak("Here yo go")
      os.system("notepad")
      
    elif("wordpad" in text):
      pyttsx3.speak("Here yo go")
      os.system("wordpad") 
  
  elif ("code" in req) or ("coding" in req) or ("D" in req):
    webbrowser.open('https://www.geeksforgeeks.org/data-structures/') 
    pyttsx3.speak("Here yo go") 
    
  elif (("me" in req)and ("fun" in req)) or ("enjoy" in req) or ("E" in req):
    pyttsx3.speak("Please tell me what would you like to do")
    print("Please tell me what would you like  to do ")
    print()
    while True:
      print("Watch a movie")
      print("Listen to a song")
      print("Surf youtube")  
      print("Do painting")
      print("Would you like me to tell you some jokes")
      print("Nothing")
      
      print("Please write down your requirement:", end=' ')
      reqs = input()
      
      if("movie" in reqs) or ("movies" in reqs):
         pyttsx3.speak("Have a great movie time")
         os.system("Popcorn-time")
         
       
      elif("listen" in reqs) or ("songs" in reqs) or ("song" in reqs):
         pyttsx3.speak("Enjoy your songs")
         os.system("wmplayer")
         
      
      elif("youtube" in reqs): 
         pyttsx3.speak("Here yo go") 
         webbrowser.open('https://www.youtube.com/') 
      
      elif("paint" in reqs) or ("painting" in reqs): 
         pyttsx3.speak("Here yo go") 
         os.system("mspaint")      
      
      elif("joke" in reqs) or ("jokes" in reqs):
         pyttsx3.speak("okay")
         pyttsx3.speak("Two men were chatting in a bar. One says Where are you from?.Second man replies ,I come from somewhere ,where we do not end a sentence, with a preposition. Alright, says the first man, Where are you from idiot?")
         
      elif("nothing" in reqs):
         pyttsx3.speak(" I hope you enjoyed")
         break
         
  elif("nothing" in req )or ("F" in req):
     pyttsx3.speak("Thank you have a good day")
     break
     
           
       
      
  