# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows a splash screen for 2 seconds,
#   then transitions to the main menu.

from scene import *
import ui
import time

from main_menu_scene import *


class SplashScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        #create size of screen variables
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.center_of_screen_x = self.size_of_screen_x/2
        self.center_of_screen_y = self.size_of_screen_y/2
        
        self.scale_of_sprites = 1.0
        
        # create timer, so that after 2 seconds move to next scene
        self.start_time = time.time()
        
        # add MT blue background color
        background_position = Vector2(self.center_of_screen_x, self.center_of_screen_y)
        self.background = SpriteNode(position = background_position, 
                                     color = 'white', 
                                     parent = self, 
                                     size = self.size)
        self.school_crest = SpriteNode('./assets/sprites/MT_Game_Studio.png',
                                       parent = self,
                                       position = background_position,
                                       size = self.size)
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        # after 2 seconds, move to main menu scene
        if not self.presented_scene and time.time() - self.start_time > 2:
            self.present_modal_scene(MainMenuScene())
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        pass
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
