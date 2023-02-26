import tkinter as tk
import tkinter.font as tkFont

class Application:
    def __init__(self, root):
        root.title("CubesProject")
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GListBox_List=tk.Listbox(root)
        GListBox_List["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_List["font"] = ft
        GListBox_List["fg"] = "#333333"
        GListBox_List["justify"] = "center"
        GListBox_List.place(x=20,y=30,width=80,height=25)

        GLabel_entryID=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_entryID["font"] = ft
        GLabel_entryID["fg"] = "#333333"
        GLabel_entryID["justify"] = "center"
        GLabel_entryID["text"] = "label"
        GLabel_entryID.place(x=300,y=30,width=70,height=25)

        GLabel_prefix=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_prefix["font"] = ft
        GLabel_prefix["fg"] = "#333333"
        GLabel_prefix["justify"] = "center"
        GLabel_prefix["text"] = "label"
        GLabel_prefix.place(x=440,y=30,width=70,height=25)

        GLabel_first_name=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_first_name["font"] = ft
        GLabel_first_name["fg"] = "#333333"
        GLabel_first_name["justify"] = "center"
        GLabel_first_name["text"] = "label"
        GLabel_first_name.place(x=300,y=70,width=70,height=25)

        GLabel_last_name=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_last_name["font"] = ft
        GLabel_last_name["fg"] = "#333333"
        GLabel_last_name["justify"] = "center"
        GLabel_last_name["text"] = "label"
        GLabel_last_name.place(x=440,y=70,width=70,height=25)

        GLabel_logo=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_logo["font"] = ft
        GLabel_logo["fg"] = "#333333"
        GLabel_logo["justify"] = "center"
        GLabel_logo["text"] = "label"
        GLabel_logo.place(x=300,y=110,width=70,height=25)

        GLabel_team_name=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_team_name["font"] = ft
        GLabel_team_name["fg"] = "#333333"
        GLabel_team_name["justify"] = "center"
        GLabel_team_name["text"] = "label"
        GLabel_team_name.place(x=300,y=160,width=70,height=25)

        GLabel_email=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_email["font"] = ft
        GLabel_email["fg"] = "#333333"
        GLabel_email["justify"] = "center"
        GLabel_email["text"] = "label"
        GLabel_email.place(x=300,y=200,width=70,height=25)

        GLabel_jersey_Color=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_jersey_Color["font"] = ft
        GLabel_jersey_Color["fg"] = "#333333"
        GLabel_jersey_Color["justify"] = "center"
        GLabel_jersey_Color["text"] = "label"
        GLabel_jersey_Color.place(x=300,y=250,width=70,height=25)

        GLabel_phone_number=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_phone_number["font"] = ft
        GLabel_phone_number["fg"] = "#333333"
        GLabel_phone_number["justify"] = "center"
        GLabel_phone_number["text"] = "label"
        GLabel_phone_number.place(x=300,y=290,width=70,height=25)

        GCheckBox_coach=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_coach["font"] = ft
        GCheckBox_coach["fg"] = "#333333"
        GCheckBox_coach["justify"] = "center"
        GCheckBox_coach["text"] = "CheckBox"
        GCheckBox_coach.place(x=450,y=120,width=70,height=25)
        GCheckBox_coach["offvalue"] = "0"
        GCheckBox_coach["onvalue"] = "1"
        GCheckBox_coach["command"] = self.GCheckBox_coach_command

        GCheckBox_head_coach=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_head_coach["font"] = ft
        GCheckBox_head_coach["fg"] = "#333333"
        GCheckBox_head_coach["justify"] = "center"
        GCheckBox_head_coach["text"] = "CheckBox"
        GCheckBox_head_coach.place(x=450,y=160,width=70,height=25)
        GCheckBox_head_coach["offvalue"] = "0"
        GCheckBox_head_coach["onvalue"] = "1"
        GCheckBox_head_coach["command"] = self.GCheckBox_head_coach_command

        GCheckBox_waterboys=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_waterboys["font"] = ft
        GCheckBox_waterboys["fg"] = "#333333"
        GCheckBox_waterboys["justify"] = "center"
        GCheckBox_waterboys["text"] = "CheckBox"
        GCheckBox_waterboys.place(x=450,y=200,width=70,height=25)
        GCheckBox_waterboys["offvalue"] = "0"
        GCheckBox_waterboys["onvalue"] = "1"
        GCheckBox_waterboys["command"] = self.GCheckBox_waterboys_command

        GCheckBox_doctor=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_doctor["font"] = ft
        GCheckBox_doctor["fg"] = "#333333"
        GCheckBox_doctor["justify"] = "center"
        GCheckBox_doctor["text"] = "CheckBox"
        GCheckBox_doctor.place(x=450,y=240,width=70,height=25)
        GCheckBox_doctor["offvalue"] = "0"
        GCheckBox_doctor["onvalue"] = "1"
        GCheckBox_doctor["command"] = self.GCheckBox_doctor_command

        GCheckBox_eighteen_thru_thirty=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_eighteen_thru_thirty["font"] = ft
        GCheckBox_eighteen_thru_thirty["fg"] = "#333333"
        GCheckBox_eighteen_thru_thirty["justify"] = "center"
        GCheckBox_eighteen_thru_thirty["text"] = "CheckBox"
        GCheckBox_eighteen_thru_thirty.place(x=450,y=280,width=70,height=25)
        GCheckBox_eighteen_thru_thirty["offvalue"] = "0"
        GCheckBox_eighteen_thru_thirty["onvalue"] = "1"
        GCheckBox_eighteen_thru_thirty["command"] = self.GCheckBox_eighteen_thru_thirty_command

        GCheckBox_thrity_thru_forty=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_thrity_thru_forty["font"] = ft
        GCheckBox_thrity_thru_forty["fg"] = "#333333"
        GCheckBox_thrity_thru_forty["justify"] = "center"
        GCheckBox_thrity_thru_forty["text"] = "CheckBox"
        GCheckBox_thrity_thru_forty.place(x=450,y=320,width=70,height=25)
        GCheckBox_thrity_thru_forty["offvalue"] = "0"
        GCheckBox_thrity_thru_forty["onvalue"] = "1"
        GCheckBox_thrity_thru_forty["command"] = self.GCheckBox_thrity_thru_forty_command

        GCheckBox_forty_thru_fifty=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_forty_thru_fifty["font"] = ft
        GCheckBox_forty_thru_fifty["fg"] = "#333333"
        GCheckBox_forty_thru_fifty["justify"] = "center"
        GCheckBox_forty_thru_fifty["text"] = "CheckBox"
        GCheckBox_forty_thru_fifty.place(x=450,y=360,width=70,height=25)
        GCheckBox_forty_thru_fifty["offvalue"] = "0"
        GCheckBox_forty_thru_fifty["onvalue"] = "1"
        GCheckBox_forty_thru_fifty["command"] = self.GCheckBox_forty_thru_fifty_command

    def GCheckBox_coach_command(self):
        print("command")


    def GCheckBox_head_coach_command(self):
        print("command")


    def GCheckBox_waterboys_command(self):
        print("command")


    def GCheckBox_doctor_command(self):
        print("command")


    def GCheckBox_eighteen_thru_thirty_command(self):
        print("command")


    def GCheckBox_thrity_thru_forty_command(self):
        print("command")


    def GCheckBox_forty_thru_fifty_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
