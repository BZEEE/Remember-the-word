
#Remember the word version 4 - user defined functions
#This program does the following
#create the window, display the icon and display instructions
#prompt player to press entedr
# display words
# get guess
#display results - output win or condolence message
# end game by closing the window
#replace adjacent duplicate line groups with a for statement 
#limit the occurence of literals


# Main Algorithm
import time
from uagame import Window
def main():
    
    # Create window
    title = 'Remember the word'
    height = 400
    width = 500
    window = Window(title, width, height)
    
    # Display icon
    display_icon(window)
    
    # Display instructions
    text_size = 24
    text_color = 'white'    
    display_instructions(window, text_size, text_color)
    
    # CLEAR THE WINDOW
    window.clear
    
    #Copying and pasting lines 49 to 51 whenever i have to clear the window and display the icon
    #Display the icon
    
    display_icon(window)
    
    #function call to display words 
    word_list = ['orange', 'chair', 'mouse', 'sandwich']
    display_words(window, text_size, text_color, word_list)
    
    # get guess by function call
    guess = get_guess(window, text_size, text_color, start_letter)
    
    #clear the window and display the icon
    window.clear
    # Display the icon
    display_icon(window)   
    
    # Display Results
    answer = word_list[1]
    start_letter = answer[0]
    display_results(window, text_size, text_color, guess, answer)
      
    
    # end game
    end_game(window)
    
#user defined function
def end_game(window):
    x = 0
    end_game = 'press enter to end the game'
    window_height = window.get_height()
    font_height = window.get_font_height()
    y = window_height - font_height
    window.input_string(end_game, x, y)
    window.close    

def display_results(window, text_size, text_color, guess, answer):
    window.set_font_color(text_color)
    window.set_font_size(text_size)
    font_height = window.get_font_height()
    x = 0
    y = 0
    answer = word_list[1]
    start_letter = answer[0]
    congrats_message = "congratulations you guessed right! It was "
    lose_message = "sorry, you guessed " + guess
    correct_answer_message = "the correct answer was chair." + answer
    if guess == answer:
        window.draw_string(congrats_message + guess, x, y)
        
    else:
        window.draw_string(lose_message, x, y)
        y += font_height
        window.draw_string(correct_answer_message, x, y)     
def get_guess(window, text_size, text_color, start_letter):
    x = 0
    y = 0
    prompt2 = "What word starts with the letter " + start_letter + "?"
    window.set_font_size(text_size)
    window.set_font_color(text_color)
    guess = window.input_string(prompt2)
    return guess

def display_icon(window, text_size, text_color):
    # function display the icon
    # -window uagame.Window object on which the icon is displayed
    icon_size = 100
    icon_color = 'purple'
    icon_string = 'UA'
    window.set_font_size(icon_size)
    window.set_font_color(icon_color)
    window_width = Window.get_width()
    icon_width = window.get_string_width(icon_string)
    x_icon = window_width - icon_width
    y_icon = 0
    window.draw_string(icon_string, x_icon, y_icon)    
    
def display_instructions(window):
    # Display instructions
    window.set_font_color(text_color)
    window.set_font_size(text_size)
    x = 0
    y = 0
    font_height = window.get_font_height()
    
    x = 0
    y = 0  
    pause_time = 2
    
def display_words(window, text_size, text_color, x, y, word_list):      
    pause_time = 2
    x = 0
    y = 0
    for word in word_list:
        window.set_font_size(text_size)
        window.set_font_color(text_color)
        window.draw_string(word, x, y)
        time.sleep(pause_time)
        #clear the window and display the icon
        window.clear
        # Display the icon
        display_icon(window)        

main()