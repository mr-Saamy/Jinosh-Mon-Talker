# Jinosh-Mon-Talker
A simple python talkbot using SpeechRecognition, PyAudio, and Pyttsx3


# Prerequisites(How to install them(in terminal/command prompt))
   -pip
   #
   -Chatterbot library (pip install chatterbot==0.8.6)
   #
   -Speech Recognition Library (pip3 install speechrecognition)
   #
   -pyttsx3 library(pip insall pyttsx3)
   #
   -pyAudio(installation using .whl file in Windows, In linux(ubuntu/ubuntu based) refer common problems)
   #
   -Python IDE(spyder / vscode / pycharm / jupyter... Idle not recommended)
# 
# 
## note: If using jupyter, please use .ipynb file for others, you can use the .py file
#
#

# Common errors in ubuntu

-> libespeak.so.1: cannot open shared object file: No such file or directory 

	Install the libeseak library using the following command

	sudo apt-get update && sudo apt-get install libespeak1 -y
	
	this will install all the dependancies required for pyttsx3

-> Problems with PyAudio

	-you need to first install a library file called portaudio

	-For that, download portaudio .tar from here

	- http://www.portaudio.com/archives/pa_stable_v190600_20161030.tgz

	-then extract it

	-go into the directory and open the terminal

	-type 'sudo su' to give root permission

	-then type './configure && make'

	-after the config and making is done, type 'make install' this will install the portaudio files
	
	-now, download the pyaudio .tar from here:
	
	- https://files.pythonhosted.org/packages/ab/42/b4f04721c5c5bfc196ce156b3c768998ef8c0ae3654ed29ea5020c749a6b/PyAudio-0.2.11.tar.gz

	-extract it and open the folder extracted

	-open terminal in tne directory and type 'sudo python3 setup.py install'

	-Then install pyAudio via pip by:
		'pip3 install PyAudio'

