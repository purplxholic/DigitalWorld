'''All widgets would be on FloatLayout(self.floatt),BoxLayout(self.layout), StackLayout(self.tryout)
Written by Zanette Cheng
Group: Chan Jia Hui, Joshua Lim, Jian Li, Zanette Cheng
15F02
For Digital World 1D 2016
Product: R.I.O.T

Builder in Kivy language is not used in this GUI'''

'''What is RIOT GUI about?
This code is a prototupe for the RIOT accompaniant app. Here, security guards would be usins this app to aid them in patrolling
the school campus, on top of their regular patrolling around the school. 
Currently, this app has 3 screens - Main Menu, 'Personal' - screen containing the processed information from Firebase and 
'ebot' - screen containing information regarding the ebots and processed information from Firebase. There will be 3 buttons to navigate between
the three screens.
The limitation of this GUI prototype is that cannot handle auto-refreshing feature. If the refreshing is too fast (eg time interval too short,
ebot keeps meeting humans that scans, both ebot and firebase would haywire and cause Kivy GUI to crash.   
'''
#libraries needed 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.image import Image
import time
import firebase

url =  "https://amber-inferno-7736.firebaseio.com/" # URL to Firebase database
token = "ZHIUQ3plvoQxl64sHHRBDZwWhQaQ5rjlnz9dgIkW" # unique token used for authentication
fire = firebase.FirebaseApplication(url, token)
     
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        Window.clearcolor=(1,1,1,1) #Master background colour 
        self.layout=BoxLayout(orientation ='vertical', spacing = 10) #padding of 10 between the buttons

        # Welcome Screen Title
        self.title = Label(text='[size=60][font=Impact Label][color=000000]Welcome to[/color]\n[color=000000]R.I.O.T[/font] \n[font=yorkwhiteletter] RACCOON.INTERNET.OF.THINGS[/color][/size][/font]', halign='center', markup = True)
        self.layout.add_widget(self.title)
        
        #buttons
        #background_color is to remove the bg colour to make the button background transparent
        self.switchbutton = Button(text="[size=50][font=yorkwhiteletter][color=000000]ENTER[/color][/font][/size]", background_color=(1,1,1,0),size_hint = (0.2,0.2), pos_hint ={'x':0.4,'y': 0.0}, halign='center', markup = True ,on_press=self.changeToPersonal) #default change to the screen containing the personal information
        self.layout.add_widget(self.switchbutton)
        self.quitbutton = Button(text="[size=50][color=000000][font=yorkwhiteletter]QUIT[/font][/color][/size]" , background_color=(1,1,1,0),size_hint=[0.2,0.2], pos_hint=({'x':0.4,'y':0.0}), markup = True, on_press=self.quitApp)
        self.layout.add_widget(self.quitbutton)

        self.add_widget(self.layout)
    
    def changeToPersonal(self, value): #default screen to see after clicking 'enter' is the 'Personal' page 
        self.manager.transition.direction = 'left'
    	self.manager.current= 'individual'

    def quitApp(self, value): #to quit
        App.get_running_app().stop()


class PersonalScreen(Screen):

    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        Window.clearcolor=(1,1,1,1) #change master bg colour, RGB in .% , last is a binary: 1 = On, 0 = Off . Currently the colour is white
        #Layouts
        self.tryout = StackLayout(orientation ='lr-bt') #buttons would be placed from left to right first then bottom to top => the buttons would be stacked at the bottom from left to right first 
        self.floatt = FloatLayout() #free size 

        #variable for def gettinginformation()
        self.counter = 0 

        #title of the screen to be seen
        self.floatt.add_widget(Label(text='[color=000000][size=40][font=yorkwhiteletter]Last Screened Individual[/size][/font][/color]',size_hint= (0.5,0.2), halign='center',markup=True,pos_hint={'x':0.05,'y':0.8}))

        #information , left column. FIXED TEXT 
        '''x is moving left right, y is moving up and down
        0.0 for y is in the middle. to move down, use -ve 
        column of the table is fixed at x=0.2, or 0.2 left relative to floatlayout'''

        self.Lname=Label(text='[color=000000][size=40][font=Impact Label Reversed]Name\nBatch[/font][/size][/color]',markup = True,pos_hint={'x':-0.2,'y':0.1})
        self.Lid=Label(text='[color=000000][size=40][font=Impact Label Reversed]Card ID[/font][/size][/color]',markup = True,pos_hint={'x':-0.2,'y':0.0})
        self.Llocation = Label(text='[color=000000][size=40][font=Impact Label Reversed]Location[/font][/size][/color]',markup = True,pos_hint={'x':-0.2,'y':-0.1})
        self.Ltime=Label(text='[color=000000][size=40][font=Impact Label Reversed]Time\nDate[/font][/size][/color]',markup = True,pos_hint={'x':-0.2,'y':-0.2})

        self.floatt.add_widget(self.Lname)
        self.floatt.add_widget(self.Lid)
        self.floatt.add_widget(self.Ltime)
        self.floatt.add_widget(self.Llocation)
       
        #widgets to get information, depending on the card ID received, RHS column of information
        #currently made RHS columns contain a '-' to show no information is being displayed    
        self.namee = Label(text='[color=000000][size=40][font=Impact Label Reversed]-[/size][/font][/color]',halign='center',markup=True,pos_hint={'x':0.2,'y':0.1})
        self.Rid=Label(text='[color=000000][size=40][font=Impact Label Reversed]-[/size][/font][/color]',markup=True,pos_hint={'x':0.2,'y':0.0})
        self.Rlocation = Label(text='[color=000000][size=40][font=Impact Label Reversed]-[/size][/font][/color]',markup=True,pos_hint={'x':0.2,'y':-0.1})
        self.Rtime = Label(text='[color=000000][size=40][font=Impact Label Reversed]%s[/size][/font][/color]' %(time.strftime("%H:%M:%S\n%d/%m/%Y")),markup=True,pos_hint={'x':0.2,'y':-0.2})
        
        self.floatt.add_widget(self.namee)
        self.floatt.add_widget(self.Rid)
        self.floatt.add_widget(self.Rtime)
        self.floatt.add_widget(self.Rlocation)

        #fixed buttons at the bottom of the screen to navigate
        self.switchtomenu = Button(text='[size=50][font=yorkwhiteletter][color=000000]MENU[/font][/size][/color]',markup=True, size_hint=(0.2,0.2),background_color=(1,1,1,0),on_press=self.changeToMenu)
        self.switchtoebot = Button(text='[size=50][font=yorkwhiteletter][color=000000]EBOTS[/font][/size][/color]', markup=True,size_hint=(0.2,0.2),background_color=(1,1,1,0),on_press=self.changeToebots)
        self.switchtopersonal = Button(text='[size=50][font=yorkwhiteletter][color=000000]INDIVIDUAL[/font][/size][/color]', markup=True,size_hint=(0.2,0.2),background_color=(1,1,1,0),on_press=self.changeToPersonal)
        
        self.tryout.add_widget(self.switchtoebot)
        self.tryout.add_widget(self.switchtopersonal)
        self.tryout.add_widget(self.switchtomenu)

        # button to trigger gettinginformation 
        self.refresh=Button(text='[size=50][font=yorkwhiteletter][color=000000]REFRESH[/font][/size][/color]', markup = True, size_hint=(0.2,0.2),background_color=(1,1,1,0),on_press=self.gettinginformation)
        self.tryout.add_widget(self.refresh)

        #add layouts
        self.add_widget(self.tryout)
        self.add_widget(self.floatt)


    def gettinginformation(self,value):
        #example dictionary acting as a database that kivy would check against 
        self.known = {'162,180,172,117,207':'Joshua Lim\nFreshmore','345,456,567':'Chua Ah Bheng\nSenior','154,168,144,85,247':'Hoo Jian Li\nFreshmore','225,19,229,43,60':'Donald Trump\nPOTUS Candidate'} 

        #getting information from Firebase 
        self.cardno = fire.get('/cardID/') #information is received in string 
        self.intruder = fire.get('/intruder/') #actual ; received in boolean 
        # self.intruder = False #<--- variable for testing 
        # self.cardno = '345,456,67' #<--- variable for testing

        ''' from the raspberry pi , self.intruder is given a default state of False. so when the state remains false, kivy app will check against
        self.known to anlayse if the person is a registered user or not. if it is, self.intruder changes to True. 
        False is sent over from raspberry pi when  
        1. Invalid card is scanned 
        2. Valid card is scanned 
        occurs
        the only time that self.intruder is read as True from the raspberry pi would be when the intruder does not scan the card at all.'''

        if self.intruder == False: #if given that self.intruder is False
            for number in self.known:
                if self.cardno == number:
                    self.intruder = False
                if self.cardno != number:
                    self.intruder = True

        #guards will click the 'refresh' button to capture information
        if self.intruder== True:
            if self.counter ==0:
                self.refresh.text = '[size=50][font=yorkwhiteletter][color=000000]CLEAR[/font][/size][/color]' #to change the text of the button 
                self.namee.text = '[color=ff0000][size=40][font=Impact Label Reversed]INTRUDER-\nNO CARD DETECTED[/color][/size][/font]' #no valid name thus "intruder" is displayed instead
                self.Rtime.text = '[color=000000][size=40][font=Impact Label Reversed]%s[/size][/font][/color]' %(time.strftime("%H:%M:%S\n%d/%m/%Y")) #to update time
                self.angryface = Image(source='C:\Users\The Gt Zan\Pictures\leangryface.PNG',pos_hint={'x':0.2,'y':0.3}) #an angry face 
                self.floatt.add_widget(self.angryface)
                self.Rlocation.text = '[color=ff0000][size=40][font=Impact Label Reversed]FAB LAB[/color][/size][/font]'
                fire.put('/','veriFlag',2) #placing into firebase to signal to ebot to play evil toned music 
                print 'Gave firebase a 2!'  # to check whether successful or not in the command prompt/ terminal 

                #if-else case: if no card info is received, then a '-' is seen. if card info is received then the card info is displayed
                if self.cardno == '':
                    self.Rid.text = '[color=000000][size=40][font=Impact Label Reversed]-[/font][/size][/color]'
                else:
                    self.Rid.text = '[color=000000][size=35][font=Impact Label Reversed]%s[/font][/size][/color]'%(self.cardno)
            else:
                #to revert back 
                self.floatt.remove_widget(self.angryface)
                self.namee.text = '[color=000000][size=40]-[/size][/color]'
                self.Rid.text ='[color=000000][size=40][font=Impact Label Reversed]-[/size][/font][/color]'
                self.Rlocation.text = '[color=000000][size=40][font=Impact Label Reversed]-[/size][/font][/color]'
                self.Rtime.text = '[color=000000][size=40][font=Impact Label Reversed]%s[/size][/font][/color]' %(time.strftime("%H:%M:%S\n%d/%m/%Y")) #to update time 
                self.refresh.text = '[size=50][font=yorkwhiteletter][color=000000]REFRESH[/font][/size][/color]'
                fire.put('/','intruder',False) #to switch back the boolean from self.intruder to the default False 

        else:
            if self.counter ==0:
                fire.put('/','veriFlag',1) #placing into firebase to signal to ebot to play happy toned music
                print 'Gave firebase a 1!' # to check whether successful or not
                self.refresh.text = '[size=50][font=yorkwhiteletter][color=000000]CLEAR[/font][/size][/color]'
                d = self.known
                c = self.cardno
                name = d[c] #to retrieve information from database. the corresponding student info is retrieved 
                self.happyface = Image(source='C:\Users\The Gt Zan\Pictures\lehappyface.PNG',pos_hint={'x':0.2,'y':0.3})
                self.floatt.add_widget(self.happyface)
                self.Rtime.text = '[color=000000][size=40][font=Impact Label Reversed]%s[/size][/font][/color]' %(time.strftime("%H:%M:%S\n%d/%m/%Y")) #to update time
                self.namee.text = '[color=007700][size=40][font=Impact Label Reversed]%s[/font][/color]' %(name) 
                self.Rid.text = '[color=000000][size=35][font=Impact Label Reversed]%s[/font][/color]' %(self.cardno)
                self.Rlocation.text = '[color=007700][size=40][font=Impact Label Reversed]CC02[/font][/color]'
            else:
            #revert back to the initial '-' symbols 
                self.floatt.remove_widget(self.happyface) #remove the happy face image when cleared 
                self.namee.text = '[color=000000][size=40]-[/size][/color]'
                self.Rlocation.text = '[color=000000][size=40][font=Impact Label Reversed]-[/font][/color]'
                self.Rid.text ='[color=000000][size=40][font=Impact Label Reversed]-[/size][/font][/color]'
                self.Rtime.text = '[color=000000][size=40][font=Impact Label Reversed]%s[/size][/font][/color]' %(time.strftime("%H:%M:%S\n%d/%m/%Y")) #to update time 
                self.refresh.text = '[size=50][font=yorkwhiteletter][color=000000]REFRESH[/font][/size][/color]'
        
        self.counter +=1 #is to increase
        self.counter = self.counter % 2 #mod two so that counter remains at 0 or 1 only
        # print  self.intruder #to check whether the correct information is received, seen in command prompt 
        return self.refresh.text

    def changeToMenu(self,value):
        self.manager.transition.direction = 'right'
        self.manager.current= 'menu'

    def changeToebots(self,value):
        self.manager.transition.direction = 'right'
        self.manager.current= 'bots'
        
    def changeToPersonal(self,value):
        self.manager.transition.direction = 'right'
        self.manager.current= 'individual'
    

class ebotsScreen(Screen):
    '''this class is written without real time function for monitoring the ebots location due to the limitations of our knowledge on the ebots.
    hence, the information is superimposed with pictures instead. however, should self.intruder == True , this screen will be triggered to example
    display how guards will be alerted by the app after pressing the refresh button'''
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.tryout = StackLayout(orientation ='lr-bt') 
        self.floatt = FloatLayout()

        #variable for gettinginformation()
        self.counter = 0
        # Title of the screen
        self.floatt.add_widget(Label(text='[color=000000][size=40][font=yorkwhiteletter]EBOTS INFORMATION[/font][/size][/color]', size_hint=(0.5,0.2),markup=True,pos_hint={'x':0.05,'y':0.8}))
    
        #information on ebots with 'good' status 
        self.ebotgoodpic = Image(source='C:\Users\The Gt Zan\Pictures\ebotinfo.PNG')
        self.floatt.add_widget(self.ebotgoodpic)    

        #buttons at the bottom 
        self.switchtomenu = Button(text='[size=50][font=yorkwhiteletter][color=000000]MENU[/font][/size][/color]',markup=True, size_hint=(0.2,0.2),background_color=(1,1,1,0),on_press=self.changeToMenu)
        self.switchtoebot = Button(text='[size=50][font=yorkwhiteletter][color=000000]EBOTS[/font][/size][/color]', markup=True,size_hint=(0.2,0.2),background_color=(1,1,1,0),on_press=self.changeToebots)
        self.switchtopersonal = Button(text='[size=50][font=yorkwhiteletter][color=000000]INDIVIDUAL[/font][/size][/color]', markup=True,size_hint=(0.2,0.2),background_color=(1,1,1,0),on_press=self.changeToPersonal)
        self.tryout.add_widget(self.switchtoebot)
        self.tryout.add_widget(self.switchtopersonal)
        self.tryout.add_widget(self.switchtomenu)

        #getting information 
        self.refresh=Button(text='[size=50][font=yorkwhiteletter][color=000000]REFRESH[/font][/size][/color]', markup = True, size_hint=(0.2,0.2),background_color=(1,1,1,0),on_press=self.gettinginformation)
        self.tryout.add_widget(self.refresh)

        #add layouts
        self.add_widget(self.tryout)
        self.add_widget(self.floatt)
    
    def gettinginformation(self,value):

        self.intruder = fire.get('/intruder/') #actual 
        # self.intruder = True #variable for testing only

        if self.intruder == True: 
            if self.counter == 0: 
                self.refresh.text = '[size=50][font=yorkwhiteletter][color=000000]CLEAR[/font][/size][/color]'
                self.ebotgoodpic.pos_hint={'x':0.0,'y':0.15} #to move the image upwards
                self.ebotintruderfound= Image(source='C:\Users\The Gt Zan\Pictures\ebotinforbad.PNG',pos_hint={'x':0.0,'y':-0.1})
                self.floatt.add_widget(self.ebotintruderfound)
            else:
                #upon clearing, the ebot page will only show info of the robots in 'normal' status 
                self.ebotgoodpic.pos_hint = {'x':0.0,'y':0.0} 
                self.floatt.remove_widget(self.ebotintruderfound) #to clear intruder status ebot when the button in state 'clear' is pressed 
                self.refresh.text = '[size=50][font=yorkwhiteletter][color=000000]REFRESH[/font][/size][/color]'
        else: #self.intruder == False , there isn't a need to display the warning 'intruder detected' ebot alert
            if self.counter ==0:
                self.refresh.text = '[size=50][font=yorkwhiteletter][color=000000]CLEAR[/font][/size][/color]'
                self.ebotgoodpic.pos_hint={'x':0.0,'y':0.0} 
            else:
                self.refresh.text = '[size=50][font=yorkwhiteletter][color=000000]REFRESH[/font][/size][/color]'

        self.counter +=1 #is to increase
        self.counter = self.counter % 2 #mod two so that counter remains at 0 or 1 only
        # print self.intruder #for monitoring on command prompt only  
        return self.refresh.text

    def changeToMenu(self,value):
        self.manager.transition.direction = 'right'
        self.manager.current= 'menu'

    def changeToebots(self,value):
        self.manager.transition.direction = 'right'

        self.manager.current= 'bots'
        
    def changeToPersonal(self,value):
        self.manager.transition.direction = 'right'
        self.manager.current= 'individual'
    
        

#to manage the screens
class RIOTApp(App):
	def build(self):
            sm=ScreenManager()
            ms=MenuScreen(name='menu')
            cb = ebotsScreen(name='bots')
            pe = PersonalScreen(name='individual')
            sm.add_widget(ms)
            sm.add_widget(cb)
            sm.add_widget(pe)
            sm.current='menu'
            return sm

if __name__=='__main__':
	RIOTApp().run()
