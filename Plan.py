#create a typing practice on Tkinter
#first is a pop-up, where it will ask if you want 30 second timer, 1 minute or 2 minute timer
#maybe can choose if you want with numbers and symbols, or don't include
#then when you click, it straight away starts.
#the sentence will show up, I can type and each word I can see if it matches with the sentence
#the text turns red color if its different, green if its all correct. I'm allowd to backspace
#the stored info will store the number of words that are correct, the number of times it turned red,
#Have a csv/json file that updates after clearing, recording WPM, number of mistakes (accuracy), no. of perfect sentences, most missed key,
#json file OR csv file can be opened to see record of all attempts, WPM and the day they were hit
#all ranked accordingly
#the pop up showing all the data of that run should have icons based on what placing you got on the leaderboard, or if you didn't




#resources:
#how to keep a function running constantly: https://stackoverflow.com/questions/55709840/python-tkinter-is-there-a-way-to-constantly-scan-the-inputs
#how to change color of text in a entry: https://www.geeksforgeeks.org/tkinter-colors/
#all about global variables: https://www.w3schools.com/python/python_variables_global.asp
#how to get the value inside a entry on keyboard command https://www.geeksforgeeks.org/how-to-get-the-value-of-an-entry-widget-in-tkinter/
#how to create your own pop-up window: https://stackoverflow.com/questions/16242782/change-words-on-tkinter-messagebox-buttons
#how to close a window: https://www.geeksforgeeks.org/how-to-close-a-window-in-tkinter/
#how to disable entry boxes: https://stackoverflow.com/questions/67387221/dynamically-enable-and-disable-textbox-python-tkinter
#& https://www.geeksforgeeks.org/how-to-disable-an-entry-widget-in-tkinter/
#how to get current time and date: https://www.geeksforgeeks.org/get-current-date-and-time-using-python/
#how to access last 4 items in a dict: https://www.google.com/search?q=how+to+obtain+the+last+4+keys+in+a+dicitonary&rlz=1C1GCEA_enSG1147SG1148&oq=how+to+obtain+the+last+4+keys+in+a+dicitonary&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKABMgkIAhAhGAoYoAEyBwgDECEYnwUyBwgEECEYjwLSAQg1MTUxajBqN6gCALACAA&sourceid=chrome&ie=UTF-8
#how to disable and able buttons: https://www.google.com/search?q=is+it+possible+to+disable+buttons+in+tkinter&rlz=1C1GCEA_enSG1147SG1148&oq=is+it+possible+to+disable+buttons+in+tkinter&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORigATIHCAEQIRigATIHCAIQIRiPAtIBCTEzMTQxajBqN6gCCLACAfEFVJvqwRB68gTxBVSb6sEQevIE&sourceid=chrome&ie=UTF-8
#chat gpt helped me code the refresh leaderboard code, finding out how to properly sort the WPM, while getting it to find the top 5 and how to convert it from json to the txt file
# https://www.geeksforgeeks.org/python-json-sort/ helped too
#check if a window is already open https://stackoverflow.com/questions/17371700/tkinter-check-to-see-if-a-window-is-open
#chatgpt helped to check why my inputs and sentence weren't considered equal, by normalizing them with an import
#how to find the most frequent element in a list: https://labex.io/tutorials/python-how-to-leverage-the-max-function-to-find-the-most-frequent-element-in-a-python-list-398036
#looked up in general how to change the color and fonts in tkinter
#how to edit labels indepth: https://www.studytonight.com/tkinter/python-tkinter-label-widget
# and https://stackoverflow.com/questions/39259264/is-there-an-option-to-edit-the-padding-inside-of-a-tkinter-entrybox/39509532
