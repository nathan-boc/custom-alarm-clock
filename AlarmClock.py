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
    window_size = (540, 540)
    window_title = "Custom Alarm Clock"
    bg_colour = pygame.Color('#111111')
    
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption(window_title)
    window.fill(bg_colour)
    
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("You pressed space!")
                    
        pygame.display.update()
        
pygame.quit()


if __name__ == "__main__":
    main()
