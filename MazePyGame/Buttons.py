import pygame as py


# NAVIGATION BUTTON CLASS
 
 
class Button():
 
    # INITIALIZATION OF BUTTON
    # COMPONENTS LIKE POSITION OF BUTTON,
    # COLOR OF BUTTON, FONT COLOR OF BUTTON, FONT SIZE,
    # TEXT INSIDE THE BUTTON
    def __init__(self, x, y, sx, sy, bcolour,
                 fbcolour, font, fcolour, text):
        # ORIGIN_X COORDINATE OF BUTTON
        self.x = x
        # ORIGIN_Y COORDINATE OF BUTTON
        self.y = y
        # LAST_X COORDINATE OF BUTTON
        self.sx = sx
        # LAST_Y COORDINATE OF BUTTON
        self.sy = sy
        # FONT SIZE FOR THE TEXT IN A BUTTON
        self.fontsize = 25
        # BUTTON COLOUR
        self.bcolour = bcolour
        # RECTANGLE COLOR USED TO DRAW THE BUTTON
        self.fbcolour = fbcolour
        # BUTTON FONT COLOR
        self.fcolour = fcolour
        # TEXT IN A BUTTON
        self.text = text
        # CURRENT IS OFF
        self.CurrentState = False
        # FONT OBJECT FROM THE SYSTEM FONTS
        self.buttonf = py.font.SysFont(font, self.fontsize)
 
    # DRAW THE BUTTON FOR THE TWO
    # TABS MENU_SCREEN AND CONTROL TABS MENU
    def showButton(self, display):
        if(self.CurrentState):
            py.draw.rect(display, self.fbcolour,
                         (self.x, self.y,
                          self.sx, self.sy))
        else:
            py.draw.rect(display, self.fbcolour, 
                         (self.x, self.y,
                          self.sx, self.sy))
        # RENDER THE FONT OBJECT FROM THE SYSTEM FONTS
        textsurface = self.buttonf.render(self.text,
                                          False, self.fcolour)
 
        # THIS LINE WILL DRAW THE TEXT SURFACE ONTO THE SCREEN
        display.blit(textsurface, 
                     ((self.x + (self.sx/2) -
                       (self.fontsize/2)*(len(self.text)/2) -
                       5, (self.y + (self.sy/2) -
                           (self.fontsize/2)-4))))
 
    # THIS FUNCTION CAPTURE WHETHER 
    # ANY MOUSE EVENT OCCUR ON THE BUTTON
    def focusCheck(self, mousepos, mouseclick):
        if(mousepos[0] >= self.x and mousepos[0] <= self.x +
                self.sx and mousepos[1] >= self.y and mousepos[1]
                <= self.y + self.sy):
            self.CurrentState = True
            # IF MOUSE BUTTON CLICK THEN
            # NAVIGATE TO THE NEXT OR PREVIOUS TABS
            return mouseclick[0]
 
        else:
            # ELSE LET THE CURRENT STATE TO BE OFF
            self.CurrentState = False
            return False