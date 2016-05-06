#if if 'x'==in (
#This is the main game class, I will be writing the story here. Please import everything here
#Combat is here, modified so we can get new gear
""" Thanks, Ben!"""
class player(object):
        global lvl
        global heart
        def __init__(self,currhp):
            self.currhp=currhp
        def getcurrhp(self):
            return self.currhp
        def gethealth(self):
            return self.currhp
        def lowercurrhp(self,damage):
            self.currhp=self.currhp-damage
        def raisehp(self,restore):
            self.currhp=self.currhp+restore
        def resethp(self):
            self.currhp=heart+lvl
        def sethp(self):
            self.currhp=(heart+lvl)
player=player(1)
def combat(monster,xpgain):
    import sys
    import random
    global lvl
    global sword
    global armor
    global boots
    global heart
    global name
    global playerhealth
    currxp=xpgain
    "Order for stats: Health, attack, defense, speed"
    zombie=[60, 10, 3, 2]
    zl2=[25, 14, 8, 7]
    zl3=[30, 19,]
    dog=[50, 10, 4, 7]
    rainbow_unicorn=[100, 11, 4, 15]
    boss=[200, 50, 20, 120]
    boss2=[400, 100, 40, 10]
    boss3=[200, 150, 20, 175]
    boss
    spider=[40, 9, 12, 12]
    bear=[80, 40, 20, 1]
    Honey_Badger=[100, 100, 100, 100]
    tiger=[60, 20, 20, 20]
    lion=[55, 30, 20, 10]
    giant=[100, 100, 200, 5]
    ogre=[40, 80, 150, 8]
    guard=[50, 40, 50, 25]
    wolf=[25, 60, 0, 70]
    
    
    spelluses=lvl+1
    playerstats=[sword+lvl+5,armor+lvl+3,boots+lvl+2]
    if monster=='zombie':
        monsterhealth=zombie[0]
        monsterstats=zombie
    if monster=='dog':
        monsterhealth=dog[0]
        monsterstats=dog
    if monster=='rainbow_unicorn':
        monsterhealth=rainbow_unicorn[0]
        monsterstats=rainbow_unicorn
    if monster=='boss':
        monsterhealth=boss[0]
        monsterstats=boss
    currmonhealth=monsterhealth
    if monster=='guard':
        monsterhealth=guard[0]
        monsterstats=guard
    while playerhealth > 0 and currmonhealth > 0:
        action=raw_input('[A]ttack or [R]un? >>')
        """if action=='Attack'.lower() or action=='A'.lower():"""
        if 'a'.upper() in action:
                fight_magic=raw_input('Fight or magic? %r spell points left >>' % spelluses)
                if fight_magic=='fight' or fight_magic=='Fight':
                    print 'You attack the %r!' %monster
                    if playerstats[2]>=monsterstats[3]:
                        currmonhealth-=(playerstats[0]-monsterstats[2])
                        print 'The %r attacks!' % monster
                        player.lowercurrhp((monsterstats[1]-playerstats[1]))
                        """playerhealth-=(monsterstats[1]-playerstats[1])"""
                        print 'Monster health='+str(currmonhealth)
                        print 'Your health=%r' % player.gethealth()
                        if player.getcurrhp()<=0:
                            break
                    elif monsterstats[2]<monsterstats[3]:
                        print 'The %r attacks!' % monster
                        player.lowercurrhp(monsterstats[1]-playerstats[1])
                        """playerhealth-=(monsterstats[1]-playerstats[1])"""
                        print 'You attack!'
                        currmonhealth-=(playerstats[0]-monsterstats[2])
                        print 'Monster health='+str(currmonhealth)
                        print 'Your health=%r' % player.gethealth()
                        if player.gethealth()<=0:
                            break
                if (fight_magic=='magic' or fight_magic=='Magic') and spelluses>0:
                    print 'What spell would you like to use? Heal or damage?'
                    spelluse=raw_input('Heal or Damage? >>')
                    if spelluse=='Heal' or spelluse=='heal':
                        print 'A glow floats around you, and you regain health'
                        playerhealth+=(31*lvl)
                        spelluses-=1
                        print 'Your health=' + str(player.gethealth())
                        print 'Spell points left: %r' %spelluses
                        if spelluses==0:
                            print 'You are out of Spell points!'
                    if spelluse=='Damage' or spelluse=='damage':
                        print 'A bolt of power hits the monster!'
                        currmonhealth-=lvl*20
                        print 'Monster health=' + str(currmonhealth)
                        spelluses-=1
                        print 'Spell points left: %r' %spelluses
                        if spelluses==0:
                            print 'You are out of Spell points!'
                elif (fight_magic=='magic' or fight_magic=='Magic') and spelluses<=0:
                    print 'You are out of Spell points!'                                                                          
        elif 'R'.lower() in action:
            c=random.randint(0,1)
            if c==0:
                print 'You made it!'
                return 'Yes!'
            if c==1:
                print 'You didn\'t make it!'
                print 'The monster attacks!'
                """playerhealth-=(monsterstats[1]-playerstats[1])"""
                player.lowercurrhp((monsterstats[1]-playerstats[1]))
                print 'Your health: '+str(player.gettcurrhp())
                if playerhealth<=0:
                    return 'You died!'
        else:
            print 'You can\'t do that!'
    if currmonhealth<=0:
        print 'The monster died!'
        """EXP System"""
        while currxp>0:
            xpneeded=100+lvl*10
            if currxp>=xpneeded:
                    print 'You got %r xp!' % currxp
                    print 'You grew to level ' + str(lvl+1)
                    lvl+=1
                    player.sethp()
                    print 'Damage: %r Defense: %r Speed: %r Health: %r' % (playerstats[0], playerstats[1], playerstats[2],player.getcurrhp())
            currxp-=xpneeded
    if player.gethealth()<=0:
        print 'You die!'
        print 'play again?'
        again=raw_input('y/n>')
        if again=='y' or again=='Y':
            start()
        if again=='n' or again=='N':
            sys.exit()
        return
            

""" Fixed up some errors in the code, and added the or statement again, but it works. If there are errors, play with indentation"""




Cheats = 1
            
    
global playerhealth 
import time
global sword
global boots
global heart
global armor
global lvl
global Cheats
global MoveL
global MoveR
global MoveF
global MoveB
global DodgeL
global DodgeR
global Room
    
lvl=1
sword=8
boots=15
heart=100
armor=5
def start():
        def cont():
            while True:
                cont=raw_input('Press Enter to Continue')
                break
def cheats ():
    print'Cheats:'
    Cheats=raw_input('>>')
    Cheats=Cheats
    if Cheats=='Rosetta':
        Cheats=1
        sword=120
        lvl=100
        print'You got the Comet Rocket!'
    else:
        print'No Cheats, okay, cool with me!'
def name():
    print 'What is your name?'
    x=raw_input('>>')
    global Name
    Name=x
    
    if Name=='Dev' or Name=='dev':
        print 'Welcome, User of Awesomeness'
        Name='Dev'
    else:
        print 'So, your name is %r?' % Name
        n = raw_input('Are you sure? >>')
        if n =='No' or n=='no':
            print 'Okay'
            name()
        elif n == 'Yes' or n=='yes':
            print'Any Cheats?'
            cheats()
        else:
            print"That's not an option"
            name()

    player.sethp()
    playerhealth=heart+lvl
    while True:
        if player.getcurrhp()>0:
            """This is just a test story, so don't worry about it being really, really bad!"""
            """No problem"""
            print "You wake up in a government lab."
            print "You are strapped to a chair and can't move your body, you can only look left or right"
            z=raw_input('>>')
            if (z == 'Look Left'or z == 'look left' or z=='Left' or z== 'left'):
                print 'There seems to be a Lead sliding door. it may be a way out once you get out of the chair.'
                start()
            elif z == 'Look Right' or z== 'Look right' or z=='look right' or z== 'right' or z== 'Right':
                print 'You see a human-like figure being shot in the chest over and over'
                cont()
                print 'It\'s Willy! But he seems to be a zombie.'
                cont()
                print 'They release the straps on Willy\'s chair and "he" comes toward you.'
                cont()
                print '"We\'re sorry, %r but we need to preform this test."' % Name
                combat('zombie',110)
                print '"So, Mr.%r, you have done better than expected!" You kick him, and start to run.' % Name
                cont()
                print 'Another Door'
                cont()
                print 'There is a hallway outside! You walk forward, but you hear barking! A large squad of attack dogs are coming!'
                combat('dog',20)
                print 'The next one attacks!'
                combat('dog',20)
                print 'And the next one!'
                combat('dog',20)
                print 'You break free of the dogs, and sprint down the hallway! A door is starting to close!'
                import random
                doorcheck=random.randint(0,1)
                if doorcheck==0:
                    print 'You make it through the door. You land on a conveyor belt that is slowly pulling you toward blades! Do you jump off, or do you stay?'
                    while True:
                            jumpgo=raw_input('>>')
                            if jumpgo=='stay' or jumpgo=='Stay':
                                break
                            if jumpgo=='Jump' or jumpgo=='jump':
                                break
                            else:
                                print 'You can\'t do that!'
                            print 'You fall toward the ground, nearly breaking your leg. You stand up, and look around. You are in a small cavern, it is dark, and there is a creaking sound. You hear a groaning sound, and you look through the door.'
                            cont()
                            print 'There is a biohazard symbol on the door. You walk in, past a sign. "Old experiment bay" the groaning sound gets louder, and a zombie attacks!'
                            combat('zombie',20)
                            print 'The next one attacks!'
                            combat('zombie',20)
                            if player.gethealth()<=0:
                                break
                            print 'You limp out the door, and a zombie reaches through. You kick it, and it runs away. You sit down and relax.'
                    if jumpgo=='Stay' or jumpgo=='stay':
                            print 'You see a glinting light, and walk over. It is a sword!'
                            print 'Got a basic sword!'
                            sword=15
                            print 'A blade whizzes past your face, and you jump off the conveyor.'
                            cont()
                            print 'You fall toward the ground, nearly breaking your leg. You stand up, and look around. You are in a small cavern, it is dark, and there is a creaking sound. You hear a groaning sound, and you look through the door.'
                            cont()
                            print 'There is a biohazard symbol on the door. You walk in, past a sign. "Old experiment bay" the groaning sound gets louder, and a zombie attacks!'
                            combat('zombie',20)
                            if player.gethealth()<=0:
                                break
                            print 'You limp backwards, but there is a zombie behind you!'
                            combat('zombie',20)

                            print 'The next one attacks!'
                            combat('zombie',20)
                            if player.gethealth()<=0:
                                break
                            print 'You limp out the door, and a zombie reaches through. You kick it, and it runs away. You sit down and relax.'     
                            print 'You feel your strength come back to you, and you explore this strange place.'
                            player.sethealth()
                            print 'There is a wall nearby, and a broken file drawer. You walk over, and the bottom door is open.'
                            cont()
                            print 'You pick up the first file you see. Inside, it says "The nano sword project is progressing well. A weaker sword was sent to the trash heap yesterday, and, though still functional, lacked the abilities of later swords."'
                            cont()
                            print '"The gamma radiation has caused ill effects on some of the workers here, and a lot of them have been saying strange things. Yesterday, Markus attacked me. While he was restrained, he bit me. It seems this radiation causes insanity in some subjects"'
                            cont()
                            print '"T boson radiation has interfered with some experiments. The idiots in lab 12 brought someone through. He\'s muttering nonsense, saying his name is %r. We wiped his memories, and sent him upstairs. In a few years, they might take him out of storage and decide what to do with him"' % Name
                            cont()
                            print '"I\'m having some sort of mental prolems. Yesterday, I blacked out and when I came to, A guard was pointing his gun at me, saying I bit him."'
                            cont()
                            print '"Markus went insane yesterday. We locked him in vault nine. He started biting people, and when we finally locked him up, his flesh had started to rot."'
                            cont()
                            print '"My blackouts are becoming more and more frequent. We made a prototype for the nanosword"'
                            cont()
                            print '"People have been reported to be biting people. I am having constant blackouts, and am locking myself up for everyone elses good"'
                            cont()
                            print '"Last entry: Experiment leader Stevonson has met the same fate as Markus. We fear all bitten personel will meet that fate, and we are sealing off experiment bay 11. There is possible research into how to create these... Things. We are abandoning the nanosword project for good."'
                            cont()
                        
                if doorcheck==1:
                    print 'The door seals before you could make it! The last two dogs pounce on you!'
                    combat('dog',20)
                    if player.gethealth()<=0:
                        break
                    print 'The next one runs away'
                    cont()
                    print 'A glinting chestplate to the ground out of a grate in the celing. A hand reaches fron the celing and picks you up. You put the vest on'
                    armor=10
                    print 'A man is standing at the top of the grate. Pulling you to the side, he whispers, "We need to get out of here. The experiments are coming!"'
                    cont()
                    print '"%r! You need to open this door!" You hear the moan of the zombies behind you, and you run over to the control panel. Pressing the button, you are taken to a GUI' % Name
                    cont()
                    print 'A riddle shows up on screen. "If Y=x and x+7*2=20, then what is the Y-th letter of the alphabet?"'
                    x=raw_input('f,h,w,v? >>')
                    if x=='f':
                        print 'The door slides open, and you jump through'
                        print '???: My name is Josh, and I am the last survivor of experiment 12'
                        print 'Josh: Let me see your weapon" You hand him the pipe you picked up while escaping"'
                        print 'Josh: Do you remember how you got here?'
                        cont()
                        print '%r: N- No' %Name
                        print 'Josh: You must be the person they brought through from lab 12'
                        print 'Josh: Here, take this. He hands you a sword that seems to almost glow. "It\'s one of the last nano-swords. Take care of it.'
                        if Cheats=='Rosetta':
                           sword=120
                        else: 
                            print 'The door remains shut, and the zombies attack!'   
            else:
                print 'You can only look left or right'
                start()
                
    if player.getcurrhp()<=0:
        print 'Would you like to play again?'
        restart=raw_input('Play again? [Y/N] >>')
        if 'Y'.lower() in restart:
            rungame()
        if 'N'.lower() in restart:
            print 'Come back soon!'
            return
        
    

def rungame():   
    name()
    global name
    start()
    def help():
        help=raw_input('>>')
        if 'H'.lower() in help:
            print 'Yer Meem'
    help()
rungame()
