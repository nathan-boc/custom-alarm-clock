# from datetime import datetime
# import time

# # Set hour and minute for alarm
# print("Enter hour: ", end="")
# input_hour = int(input())

# print("Enter minute: ", end="")
# input_minute = int(input())

# # Print the current time
# now = datetime.now()
# currentTime = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
# print(currentTime)

# # creates new datetime from entered hour and minute
# input_time = datetime(now.year, now.month, now.day, input_hour, input_minute)

# while(input_time.hour != now.hour or input_time.minute != now.minute):
#     time.sleep(60 - now.second)
        
#     now = datetime.now()
#     currentTime = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
#     print(currentTime)


# print("!!!ALARM GOING OFF!!!")






# START GUI
import pygame

def main():
    
    pygame.init()

    # Window settings
    window_size = (540, 540)
    window_title = "Custom Alarm Clock"
    bg_colour = pygame.Color('#111111')
    
    
    # Button Settings
    btn_light_colour = (170, 170, 170)
    btn_dark_colour = (100, 100, 100)
    
    
    # Initialise window
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption(window_title)
    window.fill(bg_colour)
    
    
    width = window.get_width()
    height = window.get_height()
    
   
    
    smallfont = pygame.font.SysFont('Corbel', 35)

    
    btn = button(200, 200, 100, 100)
    
    running = True
    while running:
        
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("You pressed space!")
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn.isOver(mouse_pos):
                    print("Clicked!")
                    
        
        # Changes colour of button when hovered over
        if btn.isOver(mouse_pos):
            btn.draw(window, string = "hello", colour = (44, 44, 20))
            
        else:
            btn.draw(window, string = "hello")
        
        pygame.display.update()
        
    pygame.quit()
       
        
class button():
    pygame.init()
    
    # Default button settings
    default_font = pygame.font.SysFont('Corbel', 20)
    default_colour = (0, 0, 100)
    default_text_colour = (0, 0, 0)
    
    
    def __init__(self, x, y, width, height):   
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    
    # Draws the button onto the given window
    def draw(self, window, colour = default_colour, font = default_font, text_colour = default_text_colour, string = "", outline = None):
        if outline is not None:
            pygame.draw.rect(window, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(window, colour, (self.x, self.y, self.width, self.height), 0)
    
        if string != "":
            text = font.render(string, True, text_colour)
            window.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
        
    
    # Checks is mouse is hovering over button
    def isOver(self, position):
        if position[0] > self.x and position[0] < self.x + self.width:
            if position[1] > self.y and position[1] < self.y + self.height:
                return True
        
        return False
            
            
if __name__ == "__main__":
    main()
