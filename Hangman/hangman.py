#from tkinter import * as tk
import tkinter as tk
import tkinter.messagebox
from tkinter import *
import random
import playsound

class Hangman(Frame):

    bad_tries_count = 0
    can = 0
    gam = 0
    word = "NIGHTMARE"
    arr = [0,0]
    guessed = ""


    def reset_game(self):
        self.guessed = ""
        self.bad_tries_count = 0
        self.arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        #self.word = "IMAGINE"
        self.word=self.random_word()

        self.paint_body(self.can)
        self.paint_game(self.gam)

    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.parent = parent
        
       
        self.pack(fill=BOTH, expand=1)
        
        body = Canvas(self, 
           width=cw,
           height=ch)
        body.place(x=cw + 2,y=0)
              
        game = Canvas(self, 
           width=cw,
           height=ch)
        
        game.place(x=0,y=0)

       
        self.winfo_toplevel().title("Hangman") 
        self.can = body
        self.bind_all("<Key>", self.onKeyPressed)
       
        self.gam = game

        self.reset_game()


    def onKeyPressed(self, e):
     
        # Get keypress
        key = e.keysym
        key=key.upper()
        if len(key)>1 or key<"A" or key>"Z": return


        # See if pressed key is in the word
        l = self.word.find(key.upper())
        if l > -1:
            # So mark all matching letters as found
            for i in range(1,len(self.word) + 1):
                if self.word[i - 1] == key.upper():
                    self.arr[i] = 1
            playsound._playsoundWin("ding.mp3",False)
        else:
            # Increment bad tries count
        
            l = self.guessed.find(key.upper())
            if l== -1:
                self.bad_tries_count +=1
                playsound._playsoundWin("wrong.mp3",False)
            else:
                playsound._playsoundWin("wrong2.mp3",False)

        # Update gussed letters list
        l = self.guessed.find(key.upper())
        if l == -1:
            self.guessed = self.guessed + key.upper()


        # Redraw screen
        self.paint_body(self.can)
        self.paint_game(self.gam)
    
        # Check for win
        won = 'Y'
        for i in range(1,len(self.word) + 1):
            if self.arr[i] == 0:
                won = 'N'
        if won == 'Y':
            playsound._playsoundWin("success.mp3",False)
            tkinter.messagebox.showinfo("Wow!","You won!")
            self.reset_game()


        # CHeck for loss
        if self.bad_tries_count > 7:
            playsound._playsoundWin("death.mp3",False)
            tkinter.messagebox.showinfo("Boo!","You lost!\nWord was:"+self.word)
            self.reset_game()


    def paint_body(self,canvas):

        canvas.delete("all")
        # Border
        canvas.create_rectangle(2,2,cw,ch)

        if self.bad_tries_count > 0 :
            # Base
            canvas.create_rectangle(10,ch - 10,cw - 20,ch - 20,fill="brown")

        if self.bad_tries_count > 1 :
            # Upright
            canvas.create_rectangle(cw - 30,ch - 350,cw - 20,ch - 20,fill="brown")
       
        if self.bad_tries_count > 2 :        
           # Beam
           canvas.create_rectangle(cw - 120,ch - 360,cw - 20,ch - 350,fill="brown")

        if self.bad_tries_count > 3 :        
           # Rope
           canvas.create_rectangle(cw - 105,ch - 360,cw - 95,ch - 320,fill="yellow")

        if self.bad_tries_count > 5 :        
           # Body
           canvas.create_oval(cw - 140,ch - 260,cw - 60,ch - 120,fill="blue")

        if self.bad_tries_count > 4 :        
           # Head
           canvas.create_oval(cw - 120,ch - 320,cw - 80,ch - 260,fill="pink")

        if self.bad_tries_count > 6 :        
           # Arms
           x = cw - 145
           y = ch - 240
           xs = x + 20
           ys = y + 80
           canvas.create_oval(x,y,xs,ys,fill="pink")
           x = x + 70
           xs = xs + 70
           canvas.create_oval(x,y,xs,ys,fill="pink")

        if self.bad_tries_count > 7 :        
           # Feet
           x = cw - 120
           y = ch - 140
           xs = x + 10
           ys = y + 30
           canvas.create_rectangle(x,y,xs,ys,fill="pink")
           x = x - 10
           y = y + 30
           ys = ys + 10

           canvas.create_rectangle(x,y,xs,ys,fill="red")

           x = cw - 85
           y = ch - 140
           xs = x + 10
           ys = y + 30
           canvas.create_rectangle(x,y,xs,ys,fill="pink")
           x = x + 20
           y = y + 30
           xs = xs - 10
           ys = ys + 10

           canvas.create_rectangle(x,y,xs,ys,fill="red")

        if self.bad_tries_count > 8 :        
           # Dead
           self.bad_tries_count = 0
           self.paint_body(self.can)

    def paint_game(self,canvas):

        canvas.delete("all")
        # Border
        canvas.create_rectangle(2,2,cw,ch)
        s = ""
        for i in range(1,len(self.word) + 1):
            if self.arr[i] == 1 :
                s = s + self.word[i - 1]
            else:
                s = s + "-"
        
        canvas.create_text(10,20,text="Clue:",font="Consolas 12",anchor=NW)
        canvas.create_text(10,40,text=s,font="Consolas 20",anchor=NW)

        canvas.create_text(10,80,text="Guessed Letters:",font="Consolas 12",anchor=NW)
        canvas.create_text(10,100,text=self.guessed,font="Consolas 20",width=100,anchor=NW)

    def random_word(self):
        wrds="SOLUBLE|SUMMON|SERIAL|MISUNDERSTANDING|RIGHTEOUSNESS|WHISTLE|CLEARING|EARTHQUAKE|UNINTENDED|HACK|PULSE|DEEPEN|TICK|ANTEBELLUM|SNOB|UNKEMPT|CURRICULUM|DRYING|DAYDREAM|DIFFERENTIAL|OVERGROW|LASER|DANCER|GROWN|HUGE|BOOMER|VECTOR|SQUEEZE|PROFUSION|SOBER|WILY|JOLLY|GOGGLE|REGISTRATION|CHRONOLOGY|DEFLECT|RACY|NATURE|DEFICIENCY|APPRAISER|MISTRESS|INHABIT|NEWBORN|FICTITIOUS|BROILER|DEVASTATED|NAMED|STAIR|DEVOTED|INCENDIARY|FRESHMAN|UNBORN|NATURALISM|PUNCH|ENDlESS|DECLINE|UNIFORMED|MALAYSIAN|PALETTE|AIDE|PARDON|RECKLESS|EXPORT|PENICILLIN|INDIAN|SEAT|WATCHDOG|BOND|FRAGMENTATION|UPHOLSTERY|TRICK|SHORTSTOP|AXIAL|SEIZE|PASSPORT|DEPOT|ALLEYWAY|HEROIC|HATCH|SENATE|FILM|MONSTROUS|CERAMIC|RUMBLE|NEGLECT|GRACIOUS|SHATTERED|DIVERSIFIED|MOSQUITO|COUCH|STAIRCASE|HELP|WINDMILL|INCIPIENT|BOIL|VOCALIST|SKATER|FROND|DOOM|EFFICIENT|"
        wrds+="DEGREE|INFRINGEMENT|OSTRICH|SHOW|DESCEND|POLEMIC|RECURRING|PICNIC|POSTERITY|BOUNCING|THRESHOLD|CALCIUM|INJECTION|SHRIVEL|UPSIDE|RECOGNIZABLE|OPENER|EMBRYO|TRADING|DILUTION|CLOSE|PRIMACY|STEROIDS|INSIDER|EVACUATE|DILIGENT|RECITE|BANJO|OVERBLOWN|ADVENT|POCKET|STANCE|CONTESTED|RESOLUTION|BOLD|FOIL|EXCEL|BRISTLE|ROUTER|WAVELENGTH|SPECIAL|FANATIC|AIRCRAFT|MORE|CREMATE|AIL|LUSH|PARALLEL|DIABETES|WEEK|AUTOMOTIVE|TENTATIVE|CONCERN|REDRESS|SIMPLIFICATION|FINGER|ENTRENCHED|TRANSPORT|SPEECH|GILL|FIBERGLASS|DEPLETED|QUIET|MAINLAND|EVOLVE|COSMOPOLITAN|WIND|EASEL|SUM|POP|MASTERMIND|CART|MONIKER|PEA|ARCHED|VICTIMIZE|SELFINTEREST|PARADOXICAL|DEFECTION|SHALLOW|POKE|VINE|RAISING|SWAY|RAMP|CONCEPTUALIZATION|UNCONSCIONABLE|RAGE|MEMORANDUM|FIGHT|ANTIGEN|BLOODLESS|MEDIATION|NUTRITION|PRAISE|GRAND|TIRE|REPRESS|DISTAL|EMPHYSEMA|"
        wrds+="TALKATIVE|ENDING|TRANSCENDENT|LEAVE|NEWSMAN|PLOP|OPPRESS|BALLPLAYER|TICKING|TURBAN|ECONOMICAL|SPOILED|DRAFT|SENTIENT|INSECURITY|DYNASTY|CRACKDOWN|FLASH|BEDROOM|PARTY|ANTIQUE|DEFINING|AMORPHOUS|SANDWICH|ABORT|ROOKIE|SWITCH|SELLOUT|RICOCHET|PRICK|DIVISIVE|NUMB|SMOG|SYNOPSIS|TRAIN|PHENOMENAL|APPEARANCE|SWIPE|MOVER|CYNICAL|AGITATED|VENTURE|IMPAIR|LOCKOUT|RATIONALIZE|CITIZENRY|BROADEN|CHOPPER|LOCALE|PARADE|PROFIT|OCCASIONAL|CONTAMINATION|FLEETING|STAY|OMIT|RAISIN|LANDSCAPE|CUT|FIGHTING|HIGH-RESOLUTION|PARENT|TRAP|BURGEONING|MANGO|NAMED|RIGHT|THEORETICAL|DETERIORATION|HANDLEBAR|UPROOT|CLASSIC|LEAVE|IMPERSONATE|YEAR-LONG|AUTOMOBILE|SYMPTOMATIC|IDLE|NEWBORN|WITCHCRAFT|MONTH|PACT|PERMISSIVE|FINNISH|FLEXIBLE|JETLINER|ASTOUNDING|EJECT|EXERCISE|MEMORABLE|SLIP|LOGISTICS|DIET|RIPPED|PERISH|LIGHTING|ALLOT|SPANISH|SANDINISTA|HERON|"
        wrds+="LITIGATE|BACKGROUND|RESETTLEMENT|SENTENCING|WASP|CHIEF|EXASPERATE|RESEMBLE|GORGE|CHARACTER|BAIL|PORTUGUESE|LOOSEN|GOUGE|COMMUNE|TWIN|SUPERSTITION|OPIATE|KINDRED|DOG|EDITING|SEGREGATED|CONTRADICTORY|BLOCKED|WEEKEND|INTELLECT|PREVALENT|TUNNEL|IDENTIFIABLE|LAID-BACK|MATCHUP|ADVANCE|DIVE|ARTICULATED|HARMLESS|VERSATILITY|DRUNKEN|LEADERSHIP|EMBLEM|THOROUGHFARE|FOODSTUFF|MEET|MAILED|POLLEN|STATESMAN|AMBER|CHARCOAL|DIVERSION|CHANCE|MISSED|GENDERED|UNWANTED|TRIGGER|INTIMIDATE|APPEAR|ELUDE|WISE|ITCHY|WINNINGS|PROCEDURAL|STORYTELLER|UNWRAPPED|FLASH|WEEK|EMISSION|AWARENESS|ABUSER|AFFORD|CARDINAL|CLAMOR|DETERMINANT|HALFWAY|SOUNDBITE|TUMBLE|USHER|WIN-WIN|MEDIEVAL|DISASTROUS|LEFT-HAND|WATERING|TREK|QUANTUM|MYSTERIOUS|FORWARD|MULTIMEDIA|PERSISTENT|PROFICIENCY|PLANTAIN|ACCOST|ANGLO-SAXON|ANIMAL|BUDDY|PESTO|RETREAT|OUTSTRIP|EXCISE|BENCH|OUTWEIGH|VERY|SADDLE"
        a=wrds.split("|")
        #print (len(a))
        random.seed()
        r=random.randrange(len(a))
        return a[r]



# Initialise window
root = Tk()
root.geometry("404x402")
cw = 200
ch = 400 
# Create app object
hm = Hangman(root)

# Start app event loop
root.mainloop()




