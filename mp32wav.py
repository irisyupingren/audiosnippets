import os, glob, eyed3, ntpath, shutil
import scipy.io.wavfile as wavfile

def convertDirMP3ToWav(dirName, Fs, nC, useMp3TagsAsName = False):
	'''
	This function converts the MP3 files stored in a folder to WAV. If required, the output names of the WAV files are based on MP3 tags, otherwise the same names are used.
	ARGUMENTS:
	 - dirName:		the path of the folder where the MP3s are stored
	 - Fs:			the sampling rate of the generated WAV files
	 - nC:			the number of channesl of the generated WAV files
	 - useMp3TagsAsName: 	True if the WAV filename is generated on MP3 tags
	'''

	types = (dirName+os.sep+'*.mp3',) # the tuple of file types
	filesToProcess = []

	# tag = eyeD3.Tag()	

	for files in types:
		filesToProcess.extend(glob.glob(files))		

	for f in filesToProcess:
		wavFileName = f.replace(".mp3",".wav")		
		command = "avconv -i \"" + f + "\" -ar " +str(Fs) + " -ac " + str(nC) + " \"" + wavFileName + "\"";
		print command
		os.system(command.decode('unicode_escape').encode('ascii','ignore').replace("\0",""))

convertDirMP3ToWav("/Users/IrisYupingRen/Downloads/inputpath", 44100, 2)