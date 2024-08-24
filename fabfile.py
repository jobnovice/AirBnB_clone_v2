from fabric import *
#this fabric file creates tarballl file for the webs tatic foder in the airbnb clone repo 

def do_pack():
	local("tar -czvf web_static.tgz web_static")

do_pack()
