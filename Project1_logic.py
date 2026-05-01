from PyQt6.QtWidgets import *
from Project1_GUI import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """This is the initialization function which is in charge of initializing the submit button, I also have a click counter here."""
        super().__init__()
        self.setupUi(self)
        self.clicks = 0
        self.Submit_button.clicked.connect(self.submit)


    def submit(self):
        """So this function is in charge of basically everything validating, ect"""
        self.warning_label.setStyleSheet("color: red;") # I tried changing it by default in Qt Designer and for some reason it didn't work so I just left it here
        self.clicks += 1
        if self.clicks >= 1:
            self.warning_label.setText("Voted!")
        # below here is where I check which button go pressed and since I grouped them in Qt Designer
        # I don't have to worry about anything and even have something in place incase they dont vote
        id_num = self.ID_input.text().strip()
        if self.Josh_can.isChecked():
            vote = "Voted for Josh"
        elif self.Jake_can.isChecked():
            vote = "Voted for Jake"
        else:
            vote = "Didn't Vote"

        if id_num == "":
            self.warning_label.setText("Type in a proper ID number")
            return
        elif any(char.isalpha() for char in id_num):
            self.warning_label.setText("Type in a proper ID number")
            return
        # Now my reason for making it so that the ID is only a number and doesn't really matter
        # how long is because I did a search and saw that state ID's aren't all the same
        # and that some are a specific length and some  only have numbers like Texas which
        # is 8 numbers long.

        #Below is the way I look for duplicates by going through each row and then
        # adding them to the set so that I can refer to the set when comparing
        duplicates = set()

        with open("dataa.csv", "r", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    duplicates.add(row[0])

        if id_num in duplicates:
            self.warning_label.setText("This ID has already voted")
            return


        #this sends the finalized and Validated data to the csv file dataa
        # (I already have several files called "data" and its getting confusing)
        with open("dataa.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([id_num,vote])
