#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from itertools import permutations

#Colours
red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
blue="\033[1;34m"
defcol = "\033[0m"

def alert(msg):
	print (red+"["+yellow+"#"+red+"] - "+defcol+msg)

def action(msg):
	print (red+"["+green+"+"+red+"] - "+defcol+msg)

def errorExit(msg):
	sys.exit(red+"["+yellow+"!"+red+"] - "+defcol+"Fatal - "+ msg)

def get(text):
	return raw_input(red+"["+blue+"#"+red+"] - "+defcol+text)

def processBirthday(bd):
	if "/" in bd:
		bd = bd.split("/")
	else:
		bd = bd.split("-")
	day = bd[0]
	month = bd[1]
	year = bd[2]
	
	return [day,month,year]

infos = []
generated = []

alert("=================================")
action("Welcome to S.P.L.G. 0.1")
action("S = Smart")
action("P = Password")
action("L = List")
action("G = Generator")
alert("=================================")

alert("How does it work?")
action("Generate a password list based on")
action("your inputs, e.g. name,surname...")
action("if you don't want to fill in one ")
action("of the required fields, just type")
action(" enter and continue.")
alert("=================================")


ofile = get("Output file(with passwordlist): ")

try:
	out = open(ofile,"w+")
except:
	sys.exit("Failed creating output file: ck")

infos.append(get("Insert name: "))
infos.append(get("Insert surname: "))
infos.extend(processBirthday(get("Birthday (Please use one of those formats: D-M-Y or D/M/Y): ")))
infos.append(get("Nickname: "))

action("Add any additional value, leave empty to start building passwordlist")
x = 'BEGIN'

while x != '':
	x = get("Value: ")
	infos.append(x)

for i in range(0, len(infos)+1):
        for subset in permutations(infos, i):
		if ''.join(subset) not in generated:
			generated.append(''.join(subset))

out.write("\n".join(generated))
action("Generated "+str(len(generated))+" passwords!")
out.close()

	
action(" enter and continue.")
alert("=================================")


ofile = get("Output file(with passwordlist): ")

try:
	out = open(ofile,"w+")
except:
	sys.exit("Failed creating output file: ck")

infos.append(get("Insert name: "))
infos.append(get("Insert surname: "))
infos.extend(processBirthday(get("Birthday (Please use one of those formats: D-M-Y or D/M/Y): ")))
infos.append(get("Nickname: "))

action("Add any additional value, leave empty to start building passwordlist")
x = 'BEGIN'
while x != '':
	x = get("Value: ")
	infos.append(x)

filter(lambda a: a != 2, infos)

for el in infos:
	for sel in infos:
		for tel in infos:
			generated.append(el+sel+tel)

list(set(generated))

out.write("\n".join(generated))
action(str(len(generated))+" passwords generated!")
out.close()

	
