from tkinter import *
from tkinter import messagebox
import random
import math
import json
from operator import itemgetter
from datetime import datetime
import unicodedata
from collections import Counter



SENTENCE = ""
WRONGINPUTCOUNT = 0
WRONGINPUTSTHATSENTENCE = 0
CORRECTINPUTCOUNT = 0
TOTALWORDSCOUNT = 0
PERFECT_SENTENCES = 0
TIME = 0
wpm = 0
wrong_words_lst = []
window3_open = False
window2_open = False

#Initialize window
window = Tk()
window.title("Typing Practice")
window.minsize(width=800, height=550)
window.config(pady=100, padx=170, bg="#baafa5")


#Function to produce a new sentence for the test
def initialize_sentence():
    try:
        with open("sentences.txt","r") as file:
            list_of_sentences = file.readlines()
            global SENTENCE
            SENTENCE = random.choice(list_of_sentences)
            quiz_sentence.config(text=SENTENCE, )
    except:
        print("The sentences.txt file cannot be found")

#Function to check input against sentence: Changes from red and green
def checking(*args):
    if user_input.get() == SENTENCE[0:len(user_input.get())]:
        global CORRECTINPUTCOUNT
        CORRECTINPUTCOUNT += 1
        user_input.config(fg="green")
    else:
        user_input.config(fg="red")
        global WRONGINPUTCOUNT, WRONGINPUTSTHATSENTENCE, wrong_words_lst
        WRONGINPUTCOUNT += 1
        WRONGINPUTSTHATSENTENCE += 1
        wrong_words_lst.append(user_input.get()[-1])


#Function to store info from the practice. To add on more info next time
def storing_info(event):
    counting_total_words_and_reseting_entry()
    initialize_sentence()

#Function to call on "enter" and at the end, obtains info for wpm, accuracy, perfect sentences and mistakes
def counting_total_words_and_reseting_entry():
    global TOTALWORDSCOUNT, SENTENCE, PERFECT_SENTENCES, WRONGINPUTCOUNT, WRONGINPUTSTHATSENTENCE
    info = user_input.get()
    if not info.strip():
        TOTALWORDSCOUNT += 0
        user_input.delete(0, END)
    else:
        TOTALWORDSCOUNT += len(info.split(" "))
        user_input.delete(0, END)
    if WRONGINPUTSTHATSENTENCE == 0:
        if unicodedata.normalize("NFKC", info.strip()) == unicodedata.normalize("NFKC", SENTENCE.strip()):
            PERFECT_SENTENCES += 1
    WRONGINPUTSTHATSENTENCE = 0


#Function to call when time runs out, to display & store info, then reset game
def show_stats():
    counting_total_words_and_reseting_entry()
    user_input.config(state="disabled")
    start_test_button.config(state="normal")
    calculate_display_score()
    global WRONGINPUTCOUNT, CORRECTINPUTCOUNT, TOTALWORDSCOUNT, wpm, wrong_words_lst
    WRONGINPUTCOUNT = 0
    CORRECTINPUTCOUNT = 0
    TOTALWORDSCOUNT = 0
    PERFECT_SENTENCES = 0
    wpm = 0
    wrong_words_lst = []



#Function to calculate score & display it in messagebox then calls another function
def calculate_display_score():
    global TOTALWORDSCOUNT,CORRECTINPUTCOUNT,WRONGINPUTCOUNT, wpm, PERFECT_SENTENCES, wrong_words_lst
    wpm = TOTALWORDSCOUNT/(TIME/60)
    if CORRECTINPUTCOUNT + WRONGINPUTCOUNT == 0:
        accuracy = 0
    else:
        accuracy = CORRECTINPUTCOUNT*100 / (CORRECTINPUTCOUNT + WRONGINPUTCOUNT)
    current_datetime = datetime.now() # Get current datetime
    datetime_string = current_datetime.strftime('%Y-%m-%d %H:%M') # Convert to string
    try:
        most_frequence_mistak = max(Counter(wrong_words_lst), key=Counter(wrong_words_lst).get)
        most_frequence_mistake = f"Key: [ {most_frequence_mistak} ]"
    except ValueError:
        most_frequence_mistake = "nil"

    data_dictionary = {
        wpm: {
            "WPM": f"{wpm:.1f}",
            "Accuracy": f"{accuracy:.2f}%",
            "Perfect sentences": PERFECT_SENTENCES,
            "Date & Time": datetime_string,
            "Common Misclick": most_frequence_mistake
        }
    }

    try:
        with open("data.json", "r") as file:
            data_dict = json.load(file)
            last_4_keys = list(data_dict.keys())[-4:]
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}  # Start with an empty dictionary if file is missing or corrupted
        last_4_keys = list(data.keys())[-4:]

    messagebox.showinfo(title="Typing Test Score", message=f"Congrats! Here are your stats. \nWPM: {wpm:.1f}"
                                                           f"\nAccuracy: {accuracy:.2f}%"
                                                           f"\nPerfect sentences: {PERFECT_SENTENCES}"
                                                           f"\nCommon misclick: {most_frequence_mistake}"
                        "\n \nHere are your last 4 attempt's WPM: "
                        "\n-earliest-                 -latest-"
                        f"\n{last_4_keys}")
    store_score(data_dictionary)
    refresh_leaderboard()

#Function to store the score in json
def store_score(data_dictionary):
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}  # Start with an empty dictionary if file is missing or corrupted

    data.update(data_dictionary) # Update JSON data
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

def refresh_leaderboard():
    json_list = []
    with open("data.json", "r") as file:
        diction = json.load(file)  # Load JSON as a dictionary
        for value in diction.values():  # Extract values from the dictionary
            json_list.append(value)

    # Sort data by WPM in descending order (highest WPM first)
    sorted_data_wpm = sorted(json_list, key=lambda x: float(x['WPM']), reverse=True)

    # Write top 5 to scoreboard.txt
    with open("scoreboard.txt", mode="w") as file:
        for entry in sorted_data_wpm[:5]:  # Get top 5
            file.write(json.dumps(str(entry)) + "\n")

    placing = {0:"1st",1:"2nd",2:"3rd",3:"4th",4:"5th"}
    counter = -1
    global wpm
    for entry in sorted_data_wpm[:5]:
        counter += 1
        if str(wpm) == entry["WPM"]:
            messagebox.showinfo(title="NEW RECORD!!",
                                message=f"Congratulation! Your attempt made it to the leaderboards!"
                                        f"\nYour WPM of {wpm:.1f} is now {placing[counter]} on the leaderboard ")


def display_leaderboard():
    global window2, window2_open, window3, window3_open
    if window3_open == True:
        window3.destroy()
        window3_open = False
    if window2_open == True:
        window2.destroy()
        window2_open = False
    window3_open = True
    window3 = Toplevel()
    window3.title('Leaderboard')
    window3.minsize(width=400, height=400)
    window3.config(pady=100, padx=100, bg="#baafa5")
    trophy = Canvas(window3, width=350, height=400, highlightthickness=0, bg= "#baafa5")
    trophy_img = PhotoImage(file="./trophy.png")
    trophy.img = trophy_img
    trophy.create_image(175,200, image=trophy.img)
    trophy.grid(row=0, column=0)
    try:
        with open("scoreboard.txt", "r") as file:
            list_of_scores = file.readlines()
            counter = 0
            for score in list_of_scores:
                counter += 1
                score_sentence = Label(window3,text=f"{(counter)}:  {score[2:len(score)-3]}", bg="#615751", fg="#baafa5", font=("Times New Roman", 14, "normal"), relief="raised", pady=5,padx=7)
                score_sentence.grid(row=counter, column=0)


    except:
        print("The scoreboard.txt file cannot be found")



#Functions to call count_down with the proper amount of time
def start_timer_thirty():
    global TIME
    TIME = 30
    count_down(30)
def start_timer_one():
    global TIME
    TIME = 60
    count_down(60)
def start_timer_two():
    global TIME
    TIME = 120
    count_down(120)


#Function to start timer and end the count
def count_down(count):
   window2.destroy()
   user_input.config(state="normal")
   start_test_button.config(state="disabled")
   count_min = math.floor(count / 60)
   count_sec = count % 60
   if count_sec < 10:
       count_sec = f"0{count_sec}"
   timer.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
   if count > 0:
       window.after(1000, count_down, count - 1)
   else:
       show_stats()

#Function to open up selection of time
def message_window():
    global window2, window2_open, window3, window3_open
    if window3_open == True:
        window3.destroy()
        window3_open = False
    if window2_open == True:
        window2.destroy()
        window2_open = False
    window2_open = True
    window2 = Toplevel()
    window2.title('Python Tkinter typing practice')
    window2.config(bg="#f2eeea")
    message = Label(window2,text="Choose your desired time limit", fg="#615751", bg="#f2eeea", font=("Times New Roman", 12, "bold"), padx=18,)
    message.grid(row=2,column=1)
    thirty_sec = Button(window2,text="30sec", command=start_timer_thirty, highlightthickness=2, bg="#615751", fg="#f2eeea", activebackground="#615751", activeforeground="#f2eeea", font=("Times New Roman", 10, "normal"), padx=2, pady=2)
    thirty_sec.grid(row=1, column=3)
    one_min = Button(window2,text="1min", command=start_timer_one, highlightthickness=2, bg="#615751", fg="#f2eeea", activebackground="#615751", activeforeground="#f2eeea", font=("Times New Roman", 10, "normal"), padx=4, pady=2)
    one_min.grid(row=2, column=3)
    two_min = Button(window2,text="2min", command=start_timer_two, highlightthickness=2, bg="#615751", fg="#f2eeea", activebackground="#615751", activeforeground="#f2eeea", font=("Times New Roman", 10, "normal"), padx=4, pady=2)
    two_min.grid(row=3, column=3)


#Initialize sentence
quiz_sentence = Label(text=SENTENCE, highlightthickness=1, highlightbackground="black", padx=10, pady=5, bg="#615751", fg="#f2eeea",font=("Times New Roman", 12, "normal"), relief="groove", height=1, anchor= "n")
quiz_sentence.grid(row=1,column=0, ipady=2, ipadx=10)
initialize_sentence()

#Initialise user input
v1 = StringVar()
v1.trace_add("write", checking)
user_input = Entry(width=50, textvariable=v1, state="disabled", disabledbackground="#615751", bg="#f2eeea", highlightthickness=1, font=("Times New Roman", 10, "normal") )
user_input.grid(row=2,column=0, ipadx=15, ipady=4)
user_input.focus()
user_input.bind("<Return>", storing_info)

#Intitialise canvas timer
timer = Canvas(width=200, height=224, highlightthickness=0, bg="#baafa5")
timer_img = PhotoImage(file="./stopwatch-png.png")
timer.create_image(100,112, image=timer_img)
timer_text = timer.create_text(100,125, text="0:00", fill="#926851", font=("Times New Roman", 27, "bold"))
timer.grid(row=0,column=1,columnspan=2, rowspan=2)

#Initialise time selection screen
start_test_button = Button(text='Start test', command=message_window, highlightthickness=2, bg="#615751", fg="#f2eeea", activebackground="#615751", activeforeground="#f2eeea", font=("Times New Roman", 10, "normal"), padx=2, pady=2)
start_test_button.grid(row=2, column=1)

#Initialise leaderboard button
leaderboard_button = Button(text='Leaderboard', command=display_leaderboard, highlightthickness=2, bg="#615751", fg="#f2eeea", activebackground="#615751", activeforeground="#f2eeea", font=("Times New Roman", 10, "normal"), padx=2, pady=2)
leaderboard_button.grid(row=2, column=2)


window.mainloop()
