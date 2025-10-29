import tkinter as tk
from tkinter import messagebox
import csv
import datetime
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
    

class GUI:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('450x430')
        self.window.configure(bg='lightgreen')
        self.window.title("sugar level logger")
        self.window.resizable(0,0)

        self.fileHandling()
    
       


#top label
        self.inputLabel = tk.Label(self.window, text="welcome", bg="turquoise")
        self.inputLabel.pack()


#frame
        input_frame = tk.Frame(self.window, bg='lightgreen')
        input_frame.pack()

        
# Left label
        self.inputLabel = tk.Label(input_frame, text="Enter level please:", bg="turquoise",height=5)
        self.inputLabel.grid(row=0, column=0, padx=10, pady=5)

# Right textbox
        self.textbox = tk.Text(input_frame, bg="darkgrey", font=('Arial', 16), height=5, width=10)
        self.textbox.grid(row=0, column=1, padx=10, pady=5)

#advice label
        self.adviceLabel = tk.Label(self.window, text="for the best graph please log your levels after once in a minute if possible.")
        self.adviceLabel.pack(pady=5)


        
#button
        self.enter = tk.Button(self.window, text="log sugar level",  command=self.getInfo, height=5, width=38)
        self.enter.pack(pady=50)


        

#straight to graph button
        self.enterGraph = tk.Button(self.window, text="check graph without new level", height=5, width=30, command=self.prepareGraph)
        self.enterGraph.pack(pady=5)



        self.window.mainloop()

    def fileHandling(self):
        if not os.path.exists("sugarlevels.csv"): #if the file does not exist create it
            with open("sugarlevels.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["date", "level"])

            
    def readSugarLevels(self):
        try:
            with open("sugarlevels.csv", "r") as data:
                reader = csv.reader(data) #reads contents of the csv file
            
        except FileNotFoundError:
            print("File not found.")

            # Function to add a sugar level entry
    def addSugarLevel(self, sugar_level):
        try:
            x = datetime.datetime.now().strftime(" %a/%H:%M")
            with open("sugarlevels.csv", "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([x,sugar_level])
        except ValueError:
            print("Invalid input. Please enter a numeric value.")



    def getInfo(self):
        user_text = self.textbox.get('1.0', tk.END)  # get text from the entry box

        try:
            sugar_level = float(user_text)  # convert to int
            self.addSugarLevel(sugar_level)  # call the addSugarLevel function with the integer value

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
            return  
    

        if sugar_level < 3.9:
            messagebox.showinfo(message="sugar level low! I recommend dextros fast acting tablets and taking a seat \n \n preparing graph")
            self.prepareGraph()
        elif 3.9 <= sugar_level <= 8.0:
            messagebox.showinfo(message="sugar level in range, well done! \n \n preparing graph")   
            self.prepareGraph()

        elif 8.0 <= sugar_level <= 13:
            messagebox.showinfo(message="sugar level is high, i recomend drinking some water and exercise to bring it down \n \n preparing graph")
            self.prepareGraph()
        else:
            messagebox.showinfo(message="too high, take a correction dose. \n \n preparing graph")
            self.prepareGraph()

    def prepareGraph(self):

        layout = plt.figure(figsize=(20, 7)) #sets the size of the graph

        df = pd.read_csv("sugarlevels.csv") #stores the csv file in a dataframe


        xpoints = df["date"].to_numpy()  #gets the date column from the dataframe
        ypoints = df["level"].to_numpy()  #gets the level column from the dataframe


        plt.plot(xpoints, ypoints,marker = 'o') #marker adds a circle at each point


        font1 = {'family':'serif','color':'blue','size':20}

        plt.title("sugar levels graph", fontdict=font1, loc='left')
        plt.xlabel("date")
        plt.ylabel("sugar level")


        plt.show()
        

GUI()
