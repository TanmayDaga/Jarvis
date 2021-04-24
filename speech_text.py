import speech_recognition as sr
import pyttsx3

# TODO


class SpeechText:
    def __init__(self) -> None:
        """Provides an interface for listening and speaking"""

        # initialising objects for recognition
        self.__r = sr.Recognizer()

        # Initialising objects for say function
        self.__engine = pyttsx3.init('nsss')  # nsss mac voice api name

        self.__voices = self.__engine.getProperty('voices')  # just temp use

        # can be used to display voices to user
        self.personNamesList = [i for i in enumerate(
            [l.id.split('.')[-1] for l in self.__voices])]  # [(index, personName),.....]

        # set default voice of alex
        self.__engine.setProperty('voice', self.__voices[0].id)

    def say(self, text):
        """Says the given  text"""
        self.__engine.say(text)
        self.__engine.runAndWait()

    def listen(self):
        """If user said something it will return string else None"""

        with sr.Microphone() as source:

            self.__r.adjust_for_ambient_noise(source, duration=0.2)
            audio = self.__r.listen(source)
            try:
                text = self.__r.recognize_google(audio)
                return text
            except Exception as e:
                return None

    def setVoice(self, index: int):
        """Sets the voice at given index"""

        self.__engine.setProperty(
            'voice', self.__voices[index].id)

    def tryVoice(self, index: int, text="Hello World"):
        """speaks the given text with specific voice"""

        initialVoice = self.getVoice()
        self.setVoice(index)
        self.say(text)
        self.__engine.setProperty('voice', initialVoice)

    def getVoice(self):
        """Get the present voice"""

        return self.__engine.getProperty('voice')
