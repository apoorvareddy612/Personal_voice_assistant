import speech_recognition as sr
import pyttsx3
import pywhatkit as kit

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
  try:
      with sr.Microphone() as source:
          print("Listening...")
          voice = listener.listen(source)
          command = listener.recognize_google(voice)
          command = command.lower()

          print(command)

  except:
      pass

  return command

def run_siri():
    command = take_command()
    if 'play' in command:
        talk('playing')
        print('playing')
        kit.playonyt(command)

    if 'send' in command:
        talk('sending')
        print('sending...')
        #sorry this number is random you can change the mobile number to whom ever you want to send the message!!
        kit.sendwhatmsg("+919452380123",command[4:],23,20,1)

    if 'search' in command:
        talk('searching')
        print('searching')
        kit.search(command[6:])

    if 'find about' in command:
        talk('finding information about {}'.format(command[10:]))
        print("Finding")
        kit.info(command[10:], lines = 5)

    else:
        talk("I don't know what are you talking about")

run_siri()
