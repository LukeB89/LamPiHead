############################################################
#origonal code for text to speach and 
#install guide found at:
#http://electronut.in/making-the-raspberry-pi-speak/
#
#thread work based on kamils work:from work shop he held
#
#auther:David o Mahony
#program: Text to speech
#
#
#code uses place holder calls for different therad and values in def that wil be changed
# when team mates have set out there values,
###########################################################

#!/usr/bin/python
import time
# import from parent directory
import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import DynamicObjectV2
Obj = DynamicObjectV2.Class
# put your imports here

###############################
###txt to speek imports########
import pyttsx
import webcolors


#################################
#########################################
##########################text file functions######

def init(self):
	# put your self.registerOutput here
	self.registerOutput("ttos", Obj("playing", False))

#######speach def
def say(msg,self):
        self.message (msg)
        # use sys.argv if needed
        engine = pyttsx.init()
        ###rate of speach
        rate= engine.getProperty('rate')
        engine.setProperty('rate',rate-70)
        engine.say(" the color is ")

        rate= engine.getProperty('rate')
        engine.setProperty('rate',rate-100)
        engine.say(msg)
        engine.runAndWait()
    	

#######talks when face found and lost
##def face(val):
##	#infoms if face seen 
##	if val == 1:
##		say(" Hello, there,  ")
##	elif val == 2:
##		say(" were, did, you, go, ")
################################
######rgb to color text word####
######uses webcolor witch takes the rgb value
#####and outputs the name of the color
##### eg 0,0,0 = black
####code taken from and moded in to code 
####http://stackoverflow.com/questions/9694165/convert-rgb-color-to-english-color-name-#####like-green
##################################
def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name
##################################
	


###exprestion set likly to not be used in sprint two
##def exprestion(val):
##	#check exprestion to say
##	if val == 1:
##		say(" hello, there, see, you, ")
##	elif val == 2:
##		say(" were, did, you, go ")
##	elif val == 3:
##		say(" that, is, not, ")
##	elif val == 4:
##		say(" tht, is, ")
##	else:
##		say(" i, am, a, lamp, and, a, robot, ")
#####################################################
############################################
####################################





def run (self):
    	# put your init and global variables here
    	playing = False
	####facememory rememberes if a face was seen
	#### thus when it constantly sees a face it wont constintly say hello
	### when it loses a face it will only say good by once
	facememory = 0	

	# main loop
    	while 1:
                # put your logic here
         	# you can use: output, getInputs, message 
         	
		##input color true and value of color
		colorset = self.getInputs().colourDTC
		hexthrow = colorset.Hex
	    	rvalue =colorset.R
		gvalue =colorset.G
		bvalue =colorset.B
		#
		##input if there is a shape detected and what it is
##		shapeset = self.getInputs().shape
##		#Svalue =shapeset.X;
##		#
##		##input if face true or False
##		faceset = self.getInputs().face	 
		#    

		####exsprestion######
	    	##if (exsprestionset.playing):	
	    		
	    		####check if to play exprestion
			##playing = True
			##self.output("ttos", Obj("playing", playing))
			##exprestion(exval)

		#####color check######
		#if (colorset.playing):
	
		###check value of color to identify using rgb or its
		### closest match and say it 
		playing = True
		
		self.output("ttos", Obj("playing", playing))
		
		##say("i think the color is ")
    		requested_colour = (rvalue, gvalue, bvalue)
		actual_name, closest_name = get_colour_name(requested_colour)
##		self.message (rvalue)
##		self.message (gvalue)
##		self.message (bvalue)
##		self.message (closest_name)
		say(closest_name,self)
		##time.sleep(5)
		#####face check######
		#if (faceset.playing):
         	#	
		#	###check value of color to identify 
		#	
		#	if (facememory < 2):
		#		playing = True
		#		self.output("ttos", Obj("playing", playing))
	    	#		face(1)
		#		facememory = 2;

		#elif not faceset.value:
         	#	
		#	###check value of color to identify 
		#	
		#	if (facememory == 2):
		#		playing = True
		#		self.output("ttos", Obj("playing", playing))
	    	#		face(2)
		#		facememory = 1;
		#	else: 
		#		playing = False
		#		self.output("ttos", Obj("playing", playing))


		#####shape#############
	    	#if (shapeset.playing): 
	    	#	
		#	###check value of shape to identify 
		#	playing = True
		#	self.output("audio", Obj("playing", playing))
		# 	say(Svalue)

		#####set playing to False so other sound threads will know 
		#####talking is finished
		playing = False
		self.output("ttos", Obj("playing", playing))
	    	

	        # if you want to limit framerate, put it at the end
        	time.sleep(5)
