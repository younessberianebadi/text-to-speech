# Text to speech GUI using Python

The text-to-speech (TTS) is the process of converting words into a vocal audio form. The program, tool, or software takes an input text from the user, and using methods of natural language processing understands the linguistics of the language being used, and performs logical inference on the text.

This processed text is passed into the next block where digital signal processing is performed on the processed text. Using many algorithms and transformations this processed text is finally converted into a speech format.This entire process involves the synthesizing of speech.

This seems like quite a complicated process, but thanks to python and the gTTS module, this process can be simplified to just a few lines of code.

The installation of the gTTS module is simple and can be done using the following command in the command prompt terminal:

For windows:
	py -m pip install gTTS
For Linux:
	pip install gTTS

gTTS (Google Text-to-Speech) is a Python library and CLI tool to interface with Google Translate text-to-speech API. We will import the gTTS library from the gtts module which can be used for speech translation.

My project uses the gTTS module to convert a text entered by the user, using a Tkinter GUI, the program gets the value entered in an "entry" and a simple click on the "listen" button calls a fuction that does the work.

![Screenshot](/Screenshots/Screenshot.png)

This function will create an audio file which contains the result we want, plays it and deletes it after.

The gTTS module can be used extensively on other languages such as French, German, Hindi, etc., as well. This is extremely useful when there is a communication barrier and the user is unable to convey his messages to people. Text-to-speech is a great help to the visually impaired people or people with other disabilities as it can help them by assisting in the text to speech translation. There are also many ideas possible with the gTTS module and it can be used for other languages as well.
There is potential for a lot of awesome projects with the same.

Enjoy! :+1: