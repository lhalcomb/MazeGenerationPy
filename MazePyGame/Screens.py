import pygame as py

class Screen():
    def __init__(self, width = 600, height = 600, title=None, background_color = (0, 0, 0)):

        self.width = width
        self.height = height
        self.title = title
        self.background_color = background_color
        self.currentState = False

    

    def makeCurrentScreen(self):
        #set caption of the current screen
        py.display.set_caption(self.title)
        #change the state to true, meaning that it is the current screen 
        self.currentState = True
        #display the height and width of the screen 
        self.screen = py.display.set_mode((self.width, self.height))
    
    # THIS WILL SET THE STATE OF A CURRENT STATE TO OFF
    def endCurrentScreen(self):
        self.CurrentState = False
 
    # THIS WILL CONFIRM WHETHER THE NAVIGATION OCCURS
    def checkUpdate(self, background_color):
        # HERE FILL IS THE COLOR CODE
        self.background_color = background_color
        return self.CurrentState
 
    # THIS WILL UPDATE THE SCREEN WITH
    # THE NEW NAVIGATION TAB
    def screenUpdate(self):
        if self.CurrentState:
            self.screen.fill(self.background_color)
 
    # RETURNS THE TITLE OF THE SCREEN
    def returnTitle(self):
        return self.screen