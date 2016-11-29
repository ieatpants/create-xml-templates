#get list of filenames for all mp4 files in current directory
import glob, os
os.chdir(".")

NamesWithExtension = glob.glob("*.mp4")
videoFileNames = NamesWithExtension

#remove .mp4 extension and save to array
for index in range(len(NamesWithExtension)):
    videoFileNames[index] = videoFileNames[index][:-4]

#create new xml files. each named the same as one of the mp4 files
#add templated dummy content to be manually updated

for index in range(len(videoFileNames)):
	file = open(videoFileNames[index]+".xml", "w")
	lines_of_text = ["<playlist version=\"1\">","\n"*2,"<trackList>","\n"*2,"<track>","\n","<title>1. Introduction</title>","\n","<annotation></annotation>","\n","<location>",videoFileNames[index],".mp4</location>","\n","<meta rel=\"start\">0</meta>","\n","<duration>00:01</duration>","\n","</track>","\n"*2,"<track>","\n","<title>2. Chapter 2</title>","\n","<annotation></annotation>","\n","<location>",videoFileNames[index],".mp4</location>","\n","<meta rel=\"start\">220</meta>","\n","<duration>03:40</duration>","\n","</track>","\n"*2,"<track>","\n","<title>3. Chapter 3</title>","\n","<annotation></annotation>","\n","<location>",videoFileNames[index],".mp4</location>","\n","<meta rel=\"start\">488</meta>","\n","<duration>8:08</duration>","\n","</track>","\n"*2,"<track>","\n","<title>4. Chapter 4</title>","\n","<annotation></annotation>","\n","<location>",videoFileNames[index],".mp4</location>","\n","<meta rel=\"start\">1132</meta>","\n","<duration>18:52</duration>","\n","</track>","\n"*2,"<track>","\n","<title>5. Chapter 5</title>","\n","<annotation></annotation>","\n","<location>",videoFileNames[index],".mp4</location>","\n","<meta rel=\"start\">1644</meta>","\n","<duration>27:24</duration>","\n","</track>","\n"*2,"<track>","\n","<title>6. Chapter 6</title>","\n","<annotation></annotation>","\n","<location>",videoFileNames[index],".mp4</location>","\n","<meta rel=\"start\">1930</meta>","\n","<duration>32:10</duration>","\n","</track>","\n"*2,"</trackList>","\n","</playlist>"]
	file.writelines(lines_of_text)
	file.close()
