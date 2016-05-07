'''create items up here, name first, then itemtype, then stats, then description, then relevant stat'''

#test tes
#Also, this is the game engine, not the game. once I get it working, I will make a game. Everything here is just test placeholder rooms/items
it1=['test','plot', None, 'it\'s a shiny thing',None]
testsword=['sword','sword',6969,'IMA CUT YOU!','attack']
testarmor=['armor','armor',4555,'woooot','defense']
testboots=['boots','boots',653345,'MAH NAME IS BURRY ARREN','speed']
it2=['test2','plot',None, 'Wow! A game object that won\'t be in the game proper! Spoooky',None]
class room:
    def __init__(self):
        self.description=''
        self.event=None
        self.north=None
        self.south=None
        self.east=None
        self.west=None
        self.talkexec=None
    def setwest(self,num):
        self.west=num
    def seteast(self,num):
        self.east=num
    def setsouth(self,num):
        self.south=num
    def setnorth(self,num):
        self.north=num
    def setdescription(self,description):
        self.description=description
    def setadjacent(self, room, direction):
        if direction=='north':
            self.setnorth(room)
            room.setsouth(self)
        if direction=='south':
            self.setsouth(room)
            room.setnorth(self)
        if direction=="east":
            self.seteast(room)
            room.setwest(self)
        if direction=='west':
            self.setwest(room)
            room.setwest(self)
    def setevent(self,eventtype):
        if eventtype=='talk':
            self.talkexec=0
            self.event='talk'



class player():
    #Everything here works. Forgot what I did so ittl be a lot of work to fix, DO NOT TOUCH!
    def __init__(self,curroom):
        self.curroom=curroom
        self.inventory=[]
        self.equipped=[None,None,None] #Armor, sword, boots
    def equiparmor(self,item):
        self.equipped[0]=item
    def equipsword(self,item):
        self.equipped[1]=item
    def equipboots(self,item):
        self.equipped[2]=item
    def displayinventory(self):
        for thing in range(len(self.inventory)):
            print str(thing+1)+')'+" "+str(self.inventory[thing][0])+' : '+str(self.inventory[thing][3])
        while True:
            exitoritem=raw_input('Type an item number to select it, type equipment to view stats and equipped items, or type exit to close your inventory >>')
            if exitoritem.lower()=='exit':
                self.travel()
            if exitoritem.lower()=='equipment':
                print 'Attack : ' + str(self.equipped[1][2])+ "            "+ str(self.equipped[1][0])
                print 'Defense : ' + str(self.equipped[0][2])+ "            "+ str(self.equipped[0][0])
                print 'Speed : ' + str(self.equipped[2][2])+ "            "+ str(self.equipped[2][0])
            elif exitoritem.lower!='exit':
                try:
                    indexval=int(exitoritem)-1
                    try:
                        self.inventory[indexval]
                    except IndexError:
                        print 'You must enter a valid item number'
                        continue
                except ValueError:
                    print 'Not a valid item'
                    continue
                print ""
                print self.inventory[indexval][0]
                print self.inventory[indexval][3]
                if self.inventory[indexval][4]!=None:
                    print self.inventory[indexval][4]+':'+str(self.inventory[indexval][2])
                    print ""
                    while True:
                        equip=raw_input('Would you like to equip this item? >> ')
                        if equip.lower()[0]=='y':
                            print ""
                            item=self.inventory[indexval]
                            itemtype=self.inventory[indexval][1]
                            if itemtype=='sword':
                                self.equipsword(item)
                            if itemtype=='armor':
                                self.equiparmor(item)
                            if itemtype=='boots':
                                self.equipboots(item)
                            print 'This item has been equipped'
                            print ""
                            self.displayinventory()
                        if equip.lower()[0]=='n':
                            self.displayinventory()
                        else:
                            continue
                print ""
                self.displayinventory()
    def addtoinventory(self,thing):
        self.inventory.append(thing)
    #Movement engine. Slight problem in the 'enterroom' function, python not parsing the return call. If you can fix it, go ahead.
    def changerooms(self,newroom):
        self.curroom=newroom
        self.enterroom()
    def travel(self):
        direction=raw_input('Would you like to view inventory, or go north, south, east, or west?>> ')
        if direction.lower()[0]=='i':
            self.displayinventory()
            self.travel()
        elif 'w' in direction.lower():
            if self.curroom.west==None:
                print 'You can\'t go that way'
                self.travel()
            else:
                self.changerooms(self.curroom.west)
                print 'You go west'
        elif 'n' in direction.lower():
            if self.curroom.north==None:
                print 'You can\'t go that way'
                self.travel()
            else:
                print 'You go north'
                self.changerooms(self.curroom.north)
        elif 'e' in direction.lower():
            if self.curroom.east==None:
                print 'You can\'t go that way'
                self.travel()
            else:
                print 'you go east'
                self.changerooms(self.curroom.east)
        elif 's' in direction.lower():
            if self.curroom.south==None:
                print 'You can\'t go that way'
                self.travel()
            else:
                print 'You go south'
                self.changerooms(self.curroom.south)
                self.travel()
        else:
            print 'You can\'t go that way'
            self.travel()
    #This is the only thing that needs fixing right now, the return isnt being called properly.
    def enterroom(self):
        print self.curroom.description
        if self.curroom.event=='talk' and (self.curroom.talkexec==0 or self.curroom.talkexec==None):
            self.curroom.talkexec=1
            self.travel()
        elif self.curroom.event=='talk' and self.curroom.talkexec==1:
            print 'dafuq?'
            self.travel()
        elif self.curroom.event==None:
            self.travel()

#As of here, everthing is part of the actual game

#Defining rooms
room1=room()
room2=room()
room3=room()
room4=room()
room5=room()
room6=room()

#Setting test room descriptions
room1.setdescription('you enter the corridor. You feel a cold wind blowing on your back')
room2.setdescription('welcome to southland')
room3.setdescription('welcome to eastland')
room4.setdescription('welcome to westland')
room5.setdescription('erlvomr yo northland')
room6.setdescription('the test was one half succesful')

#Setting test room positions
room1.setadjacent(room4,'west')
room1.setadjacent(room5,'north')
room1.setadjacent(room3,'east')
room1.setadjacent(room2,'south')
room4.setadjacent(room6,'east')

#defining the player object
player=player(room1)

#Adding items to player inventory
player.addtoinventory(it1)
player.addtoinventory(it2)
player.addtoinventory(testsword)
player.addtoinventory(testarmor)
player.addtoinventory(testboots)

#equipping test items (Don't delete, or the equipment function will give an error'
player.equipsword(testsword)
player.equiparmor(testarmor)
player.equipboots(testboots)

#Testing stuff, not a category
player.enterroom()
print 'k?'
player.enterroom()
