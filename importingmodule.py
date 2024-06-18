import pyttsx3,os

engine = pyttsx3.init()

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate

volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level

voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[0].id) 
engine.say("Hey My Name is Hamza Ali Khan and i am so Excited that I got selected in Bytewise Limited Fellowship Program! Yippie!!")
engine.runAndWait()

myDir = "/"
contents = os.listdir(myDir)
print(contents)
