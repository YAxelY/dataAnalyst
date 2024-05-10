import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from prettytable import PrettyTable
from tkinter import messagebox
import Style as st 
from communfunctions import gui_items as gui
from communfunctions import converter as ct
from tests.ProportionToTheoreticalTest import ProportionToTheoreticalTest
from tests.TwoProportionsTest import TwoProportionsTest
from tests.CochranTest import CochranTest
from tests.AnovaTwoWayR import AnovaTwoWayR
from tests.moyenneinfo import OneSampleMeanTestGinfo
from tests.Moyenne2 import OneSampleMeanTestG
from tests.BathlettTTEst import BartlettTest
from tests.Wilcoxon import Wilcoxon
from tests.MannWhitney import MannWhitney
from tests.kruskal import Kruskal
from tests.AnovaTwoWay import  AnovaTwoWay
from tests.AnovaOneWay import AnovaOneWay
from tests.StudentTest import StudentTest


# template
#item
#placement
#style
#dimensions
#binding(opt)

class DataAnalysisApp:
    def __init__(self,master):

        
        # main windows
        self.master=master
        self.master.geometry("1200x700") 
        self.master.minsize(500, 500)  # Set minimum width and height
        self.master.config(bg="white", bd=2, relief="groove", width=1200, height=700)
        self.master.title("Data Analysis")
       
        self.testTables=[]
        # end main windows

        # explicit attributes
        self.dataInputMode="tables"
        self.tmean=0
        self.already=1
        self.desc=""
        self.alpha=0.05
        self.data=[]
        self.selectedTest=" "
        self.selectedNature=" "
        self.validation = self.master.register(gui.validate_input)
        self.currentTest=AnovaOneWay(self.data)
       


        self.create_widgets(self.master)
    
    def create_widgets(self,master):
        # main menu bar
        self.menubar = tk.Menu(master) 
        #can't pack Menu widget is top-level-windows
        self.menubar.config(bg="white",bd=2,relief="groove")
        #can't resize Menu widget
        

        

        
        # Menu Fichier
        self.file_menu = tk.Menu(self.menubar, tearoff=1)
        self.file_menu.config(bg="white",fg="black")
        self.file_menu.add_command(label="New", command=lambda: None)
        self.file_menu.add_command(label="Ouvrir", command=lambda: self.open_file())
        self.file_menu.add_command(label="Sauvegarder", command=lambda: self.save_file())
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quitter", command=lambda: self.quit_app())
        self.menubar.add_cascade(label="Fichier", menu=self.file_menu)
        
        # Menu Paramètres
        self.parameters_menu = tk.Menu(self.menubar, tearoff=0)
        self.parameters_menu.config(bg="white",fg="black")
        
        # Sous-menu Thème
        self.theme_menu = tk.Menu(self.parameters_menu, tearoff=0)
        self.theme_menu.add_command(label="Dark", command=self.set_dark_theme)
        self.theme_menu.add_command(label="Light", command=self.set_light_theme)
        self.parameters_menu.add_cascade(label="Thème", menu=self.theme_menu)
        
        # Sous-menu Taille
        self.size_menu = tk.Menu(self.parameters_menu, tearoff=0)
        self.size_menu.add_command(label="+", command=self.increase_size)
        self.size_menu.add_command(label="-", command=self.decrease_size)
        self.size_menu.add_command(label="Renitialiser", command=self.reset_size)
        self.parameters_menu.add_cascade(label="Taille", menu=self.size_menu)
        
        # Sous-menu Langue
        self.language_menu = tk.Menu(self.parameters_menu, tearoff=0)
        self.language_menu.add_command(label="Anglais", command=self.set_language_english)
        self.language_menu.add_command(label="Francais", command=self.set_language_french)
        self.parameters_menu.add_cascade(label="Langue", menu=self.language_menu)
        
        # Sous-menu Préférences
        self.preferences_menu = tk.Menu(self.parameters_menu, tearoff=0)
        self.preferences_menu.add_command(label="Option 1", command=self.preference_option1)
        self.preferences_menu.add_command(label="Option 2", command=self.preference_option2)
        self.parameters_menu.add_cascade(label="Préférences", menu=self.preferences_menu)
        
        self.menubar.add_cascade(label="Paramètres", menu=self.parameters_menu)
        
        master.config(menu=self.menubar)

        # Ajouter des onglets Input et Output
        self.tab_control = ttk.Notebook(master)
        self.tab_input = ttk.Frame(self.tab_control)
        self.tab_input.configure(padding="0")
        self.tab_output = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_input, text='Entree')
        self.tab_control.add(self.tab_output, text='Sortie')
        self.tab_control.pack(expand=1, fill="both")
        
        self.c_input=tk.Frame(self.tab_input)
        self.c_input.pack(fill="both",padx=0,pady=0,ipadx=0,ipady=0)
        self.c_input.config(bg="white")
       
        
        
        #g_type style to be inserted
        self.g_type = tk.Frame(self.c_input)
        self.g_type.pack( expand="true",side="top", fill="x",anchor="nw", pady=0,padx=0,ipadx=0,ipady=0)
        self.g_type.config(bg="white",height=10,relief="solid",borderwidth=1)
       
    #g_type style to be inserted
        self.g_nature = tk.Frame(self.c_input)
       
        self.g_nature.config(bg="white",height=10,relief="solid",borderwidth=2)

    

        # Ajouter un label "Seuil de Signification" et son champ après les onglets
        self.label_nature = tk.Menubutton(self.g_nature, text="Test Nature >")
        self.label_nature.config(relief="ridge",bg="white",fg="black")
        self.label_nature.pack(side="left",padx=1)
    

        # Create a menu for the menubutton
        self.nature_menu = tk.Menu(self.label_nature, tearoff=1)
        self.nature_menu.config(relief="ridge",bg="white",fg="black")
        self.nature_menu.add_command(label="two-tail", command=lambda: self.select_nature("two-sided"))
        self.nature_menu.add_command(label="greater", command=lambda: self.select_nature("greater"))
        self.nature_menu.add_command(label="less", command=lambda: self.select_nature("less"))
        # Attach the menu to the menubutton
        self.label_nature.config(menu=self.nature_menu)
        self.entry_nature = tk.Entry(self.g_nature)
        self.entry_nature.pack(expand="true",side="left",anchor="w",padx="10")
        self.entry_nature.config(state="disabled")
        st.setRelativeSizeEntry(self.entry_nature,self.c_input,self.master,0.02)



      
        

        # Ajouter un label "Seuil de Signification" et son champ après les onglets
        self.label_type = tk.Menubutton(self.g_type, text="Type de test >")
        self.label_type.config(relief="ridge",bg="white",fg="black")
        self.label_type.pack(side="left",padx=1)
       

        # Create a menu for the menubutton
        self.test_menu = tk.Menu(self.label_type, tearoff=1)
        self.test_menu.config(relief="ridge",bg="white",fg="black")
        self.test_menu.add_command(label="MannWhitney", command=lambda: self.select_test("MannWhitney"))
        self.test_menu.add_command(label="t-test", command=lambda: self.select_test("t-test"))
        self.test_menu.add_command(label="Kruskal", command=lambda: self.select_test("Kruskal"))
        self.test_menu.add_command(label="Anova One way ", command=lambda: self.select_test("AnovaOneWay"))
        self.test_menu.add_command(label="Anova two way ", command=lambda: self.select_test("AnovaTwoWay"))
        self.test_menu.add_command(label="Anova two way with replication", command=lambda: self.select_test("AnovaTwoWayR"))
        self.test_menu.add_command(label="Student ", command=lambda: self.select_test("StudentTest"))
        self.test_menu.add_command(label="Wilcoxon ", command=lambda: self.select_test("Wilcoxon"))
        self.test_menu.add_command(label="BartlettTest", command=lambda: self.select_test("BartlettTest"))
        self.test_menu.add_command(label="Test de moyenne pour un échantillon", command=lambda: self.select_test("OneSampleMeanTestG"))
        self.test_menu.add_command(label="Test de cochran", command=lambda: self.select_test("CochranTest"))
        self.test_menu.add_command(label="ProportionToTheoric", command=lambda: self.select_test("ProportionToTheoreticalTest"))
        self.test_menu.add_command(label="test 2 proportions", command=lambda: self.select_test("TwoProportionsTest"))
        
        
        
        # Attach the menu to the menubutton
        self.label_type.config(menu=self.test_menu)
        
        self.entry_type = tk.Entry(self.g_type)
        self.entry_type.pack(expand="true",side="left",anchor="w",padx="10")
        self.entry_type.config(state="disabled")
        self.entry_type.config(highlightthickness=2)
        
        st.setRelativeSizeEntry(self.entry_type,self.c_input,self.master,0.02)



        # self.label_detect = tk.Button(self.g_type, text="Help to Detect ")
        # self.label_detect.config(relief="ridge",bg="white",fg="black")
        # self.label_detect.pack(side="left",padx=1)
       

        
        self.g_commun = tk.Frame(self.c_input)
        self.g_commun.pack( expand="true",side="top",anchor="ne", fill="x" ,padx=0,pady=10,ipadx=0,ipady=0)
        self.g_commun.config(bg="white")
        
        self.g_mean = tk.Frame(self.c_input)
     
        self.g_mean.config(bg="white")

        self.label_tmean = tk.Button(self.g_mean, text="moyenne  thérique (by default u=0)")
        self.label_tmean.config(relief="ridge",bg="white",fg="black")
        self.label_tmean.pack(side="left",padx=1)
    
        
        self.entry_tmean = tk.Entry(self.g_mean)
        self.entry_tmean.pack(expand="true",side="left",anchor="w",padx="10")
        self.entry_tmean.config(state="normal")
        st.setRelativeSizeEntry(self.entry_tmean,self.c_input,self.master,0.12)
        
        self.entry_tmean.bind("<KeyRelease>", lambda event:  self.set_tmean())
        self.g_mean.pack( expand="true",side="top", fill="x",anchor="nw", pady=0,padx=0,ipadx=0,ipady=0)
        # self.g_nature.pack( expand="true",side="top",anchor="ne", fill="x" ,padx=0,pady=10,ipadx=0,ipady=0)







        self.g_mode = tk.Frame(self.c_input)
      
        self.g_mode.config(bg="white",height=10,relief="solid",borderwidth=1)
        # Ajouter un label "Seuil de Signification" et son champ après les onglets
        self.label_mode = tk.Menubutton(self.g_mode, text="data input mode >")
        self.label_mode.config(relief="ridge",bg="white",fg="black")
        self.label_mode.pack(side="left",padx=1)
    

        # Create a menu for the menubutton
        self.mode_menu = tk.Menu(self.label_mode, tearoff=1)
        self.mode_menu.config(relief="ridge",bg="white",fg="black")
        self.mode_menu.add_command(label="table", command=lambda: self.select_mode("tables"))
        self.mode_menu.add_command(label="informations", command=lambda: self.select_mode("informations"))
        
        
        # Attach the menu to the menubutton
        self.label_mode.config(menu=self.mode_menu)
        
        self.entry_mode = tk.Entry(self.g_mode)
        self.entry_mode.pack(expand="true",side="left",anchor="w",padx="10")
        self.entry_mode.config(state="disabled")
        self.entry_mode.config(highlightthickness=2)
        
        st.setRelativeSizeEntry(self.entry_mode,self.c_input,self.master,0.02)

        #seuil de signification

        self.g_alpha = tk.Frame(self.c_input)
        self.g_alpha.pack( expand="true",side="top",anchor="ne", fill="x" ,padx=0,pady=10,ipadx=0,ipady=0)
        self.g_alpha.config(bg="white",height=10)

         # Ajouter un label "Seuil de Signification" et son champ après les onglets
        self.label_alpha = tk.Button(self.g_alpha, text="seuil de signification (α=0.05 by default) ")
        self.label_alpha.config(relief="ridge",bg="white",fg="black")
        self.label_alpha.pack(side="left",padx=1)
       
        
        self.entry_alpha = tk.Entry(self.g_alpha ,validate="key", validatecommand=(self.validation, "%P"))
        self.entry_alpha.pack(expand="true",side="left",anchor="w",padx="10")
        self.entry_alpha.config(state="normal")
        st.setRelativeSizeEntry(self.entry_alpha,self.c_input,self.master,0.01)
        
        self.entry_alpha.bind("<KeyRelease>", lambda event:  self.set_alpha())

        
        
        # # Ajout d'un tableau en bas avec deux labels et leurs champs d'entrée respectifs
        # table_frame = ttk.Frame(c_input)
        # table_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        # table_label = ttk.Label(table_frame, text="Tableau de données")
        # table_label.pack(pady=(0, 5))
        
        # # Création du tableau
        # table = ttk.Treeview(table_frame, columns=("Label", "Valeur"), show="headings")
        # table.heading("Label", text="Label")
        # table.heading("Valeur", text="Valeur")
        # table.pack(fill="both", expand=True)
        
        # # Ajout des labels et champs dans le tableau
        # table.insert("", "end", values=("Label 1", tk.Text(table, height=1)))
        # table.insert("", "end", values=("Label 2", tk.Text(table, height=1)))

        # data input code
        self.data_f,self.data_t,self.data_z=gui.createft("data input e.g: \n1 2 3(first sample )\n 1 2 3 (second sample)",self.c_input)
        self.data_f.pack(expand="true",side="bottom",fill="both")
        self.data_t.pack(expand="true",side="top",fill="both")
        self.data_z.pack(expand="true",side="top",fill="both")
         # Set up validation for data_z
        self.data_z.bind("<Key>", self.validate_input)
        st.setRelativeSize(self.master,self.data_z,self.master,0.02,0.01)

        self.data_fi,self.i_entries=gui.create_entry_frame(self,self.c_input,["entrer la taille de l 'echantillon:","entrer l'ecart-type de l'echantillon:","entrer la moyenne de l'echantillon:"],["taille","ecart","moy"])
      
     

        # end data input code

        # validation button norminal cases

        self.validV = tk.Frame(self.c_input)
        self.validV.pack(expand="true",side="bottom")

        # Create three buttons
        self.erase= tk.Button(self.validV, text="erase")
        self.erase.pack(expand="true",fill="x",side="left",anchor="w" ,padx=10)
        st.setRelativeSize(self.master,self.erase,self.master,0.001,0.02)
        self.run = tk.Button(self.validV, text="run")
        self.run.pack(expand="true",fill="x",side="left" , anchor="e")
        st.setRelativeSize(self.master,self.run,self.master,0.001,0.02)
        self.run.bind("<Button-1>", lambda event: self.runF())







        #output
        self.c_output=tk.Frame(self.tab_output)
        self.c_output.pack(fill="both",padx=0,pady=0,ipadx=0,ipady=0)
        self.c_output.config(bg="white")


        self.form_f,self.form_t,self.form_z=gui.createft("1-formulation d'hypothèse",self.c_output)
        self.form_f.pack(expand="true",side="top",fill="both")
        self.form_t.pack(expand="true",side="top",fill="both")
        self.form_z.pack(expand="true",side="top",fill="both")
        self.form_z.config(state="disabled")
        st.setRelativeSize(self.master,self.form_z,self.master,0.01,0.02)

        self.distro_f,self.distro_t,self.distro_z=gui.createft("2-choix de la loi",self.c_output)
        self.distro_f.pack(expand="true",side="top",fill="both")
        self.distro_t.pack(expand="true",side="top",fill="both")
        self.distro_z.pack(expand="true",side="top",fill="both")
        self.distro_z.config(state="disabled")
        st.setRelativeSize(self.master,self.distro_z,self.master,0.01,0.02)


        self.steps_f,self.steps_t,self.steps_z=gui.createft("3-valeurs du test",self.c_output)
        self.steps_f.pack(expand="true",side="top",fill="both")
        self.steps_t.pack(expand="true",side="top",fill="both")
        self.steps_z.pack(expand="true",side="top",fill="both")
        st.setRelativeSize(self.master,self.steps_z,self.master,0.01,0.02)
        self.steps_z.config(state="disabled")


        self.p_f,self.p_t,self.p_z=gui.createft("4- p-value ou interval de confiance",self.c_output)
        self.p_f.pack(expand="true",side="top",fill="both")
        self.p_t.pack(expand="true",side="top",fill="both")
        self.p_z.pack(expand="true",side="top",fill="both")
        self.p_z.config(state="disabled")
        st.setRelativeSize(self.master,self.p_z,self.master,0.01,0.02)


        self.con_f,self.con_t,self.con_z=gui.createft("5- prise de decision et conclusion",self.c_output)
        self.con_f.pack(expand="true",side="top",fill="both")
        self.con_t.pack(expand="true",side="top",fill="both")
        self.con_z.pack(expand="true",side="top",fill="both")
        st.setRelativeSize(self.master,self.con_z,self.master,0.01,0.02)
        self.con_z.config(state="disabled")

        
       
        

    
    def quit_app(self):
        self.master.destroy()
    
    # Méthodes pour les actions des menus déroulants
    
    def set_dark_theme(self):
        # Code pour définir le thème sombre
        pass
    
    def set_light_theme(self):
        # Code pour définir le thème clair
        pass
    
    def increase_size(self):
        # Code pour augmenter la taille
        pass
    
    def decrease_size(self):
        # Code pour diminuer la taille
        pass
    
    def reset_size(self):
        # Code pour réinitialiser la taille
        pass
    
    def set_language_english(self):
        # Code pour définir la langue sur l'anglais
        pass
    
    def set_language_french(self):
        # Code pour définir la langue sur le français
        pass
    
    def preference_option1(self):
        # Code pour l'option 1 des préférences
        pass
    
    def preference_option2(self):
        # Code pour l'option 2 des préférences
        pass
    
    def open_input_window(self):
        input_window = tk.Toplevel(self)
        input_window.title("Input")
        # Ajouter les éléments de l'interface pour l'onglet Input ici
    
    def open_output_window(self):
        output_window = tk.Toplevel(self)
        output_window.title("Output")
        # Ajouter les éléments de l'interface pour l'onglet Output ici

    def select_test(self,chosenTest):
        
        for child in self.g_commun.winfo_children():
            child.destroy()
        self.data_f.pack(expand="true",side="bottom",fill="both")
        self.data_fi.pack_forget()
        self.g_mode.pack_forget()
        self.g_mean.pack_forget( )
        
        self.g_nature.pack_forget()




        if self.already==1:

       
            #description

            #description



            self.g_desc = tk.Frame(self.c_input)
            self.g_desc.pack( expand="true",side="top",anchor="ne", fill="x" ,padx=0,pady=10,ipadx=0,ipady=0)
            self.g_desc.config(bg="white",height=10)

            # Ajouter un label "Seuil de Signification" et son champ après les onglets
            self.label_desc = tk.Button(self.g_desc, text="H0 enoncé (optional) ")
            self.label_desc.config(relief="ridge",bg="white",fg="black")
           # self.label_desc.pack(side="left",padx=1)
        
            
            self.entry_desc = tk.Entry(self.g_desc)
           # self.entry_desc.pack(expand="true",side="left",anchor="w",padx="10")
            self.entry_desc.config(state="normal")
            st.setRelativeSizeEntry(self.entry_desc,self.c_input,self.master,0.12)
            
            self.entry_desc.bind("<KeyRelease>", lambda event:  self.set_desc())
            self.already=0
        


    

        
        self.selectedTest=chosenTest
        self.Wilcoxon=0
        self.BartlettTest=0
        self.OneSampleMeanTestG=0
        self.anovaTwoWay=0
        self.anovaTwoWayR=0
        self.CochranTest=0
        self.ProportionToTheoreticalTest=0
        self.TwoProportionsTest=0
        gui.update_entry_text(self.entry_type,self.selectedTest)

        if self.selectedTest=="MannWhitney":
            self.currentTest=MannWhitney(self.data)
            self.g_mean.pack( expand="true",side="top",anchor="ne", fill="x" ,padx=0,pady=10,ipadx=0,ipady=0)
            
   

            # Ajouter un label "Seuil de Signification" et son champ après les onglets
            self.label_desc = tk.Button(self.g_commun, text="H0 enoncé (optional) ")
            self.label_desc.config(relief="ridge",bg="white",fg="black")
            self.label_desc.pack(side="left",padx=1)
        
            
            self.entry_desc = tk.Entry(self.g_commun)
            self.entry_desc.pack(expand="true",side="left",anchor="w",padx="10")
            self.entry_desc.config(state="normal")
            st.setRelativeSizeEntry(self.entry_desc,self.c_input,self.master,0.12)
            
            self.entry_desc.bind("<KeyRelease>", lambda event:  self.set_desc())
            self.already=0
        if self.selectedTest=="Kruskal":
            self.currentTest=Kruskal(self.data)
        if self.selectedTest=="AnovaOneWay":
            self.currentTest=AnovaOneWay(self.data)
        if self.selectedTest=="StudentTest":
           self.currentTest=StudentTest(self.data)  
        if self.selectedTest=="Wilcoxon":
            self.Wilcoxon=1
            self.currentTest=Wilcoxon(self.data)  
        if self.selectedTest=="BathlettTTEst":

           

            self.BartlettTest=1
            self.currentTest=BartlettTest(self.data)
        if self.selectedTest=="OneSampleMeanTestG":
            
            self.OneSampleMeanTestG=1
            self.currentTest=OneSampleMeanTestG(self.data)

            
            self.g_mean.pack( expand="true",side="top",anchor="ne", fill="x" ,padx=0,pady=10,ipadx=0,ipady=0)

             
            self.g_mode.pack( expand="true",side="top", fill="x",anchor="nw", pady=0,padx=0,ipadx=0,ipady=0)
            self.g_nature.pack( expand="true",side="top",anchor="ne", fill="x" ,padx=0,pady=10,ipadx=0,ipady=0)
            

        if self.selectedTest=="AnovaTwoWay":
            self.anovaTwoWay=1
            self.currentTest=AnovaTwoWay(self.data)
  

        if self.selectedTest=="AnovaTwoWayR":
           
            self.anovaTwoWayR=1
            self.currentTest=AnovaTwoWayR(self.data)
        if self.selectedTest=="CochranTest":
            
            self.CochranTest=1
            self.currentTest= CochranTest(self.data)

        if self.selectedTest=="ProportionToTheoreticalTest":
            
            self.ProportionToTheoreticalTest=1
            self.currentTest= ProportionToTheoreticalTest(self.data)
            self.g_mean.pack( expand="true",side="top",anchor="ne", fill="x" ,padx=0,pady=10,ipadx=0,ipady=0)

       
        if self.selectedTest=="TwoProportionsTest":
            
            self.TwoProportionsTest=1
            self.currentTest= TwoProportionsTest(self.data)
            self.g_mean.pack( expand="true",side="top",anchor="ne", fill="x" ,padx=0,pady=10,ipadx=0,ipady=0)

        
        self.previousTest=self.currentTest


           
            
           
        
    

    def select_nature(self,chosenNature):
        self.selectedNature=chosenNature
        gui.update_entry_text(self.entry_nature,self.selectedNature)
    
    def select_mode(self,chosenMode):
        self.selectedMode=chosenMode
        self.dataInputMode=chosenMode
        gui.update_entry_text(self.entry_mode,self.selectedMode)

        if self.selectedMode=="informations":
            self.data_f.pack_forget()
            self.data_fi.pack(expand="true",side="top",fill="both")
            if self.selectedTest=="OneSampleMeanTestG":
                self.currentTest=OneSampleMeanTestGinfo(self.data)
        if self.selectedMode=="tables":
            self.currentTest=self.previousTest
            self.data_f.pack(expand="true",side="bottom",fill="both")
            self.data_fi.pack_forget()
            # self.data_t.pack(expand="true",side="top",fill="both")
            # self.data_z.pack(expand="true",side="top",fill="both")


    def runF(self):
        if self.dataInputMode=="tables":
            if self.anovaTwoWayR==1:
                
                self.currentTest.data=ct.parse_input_stringr(self.data_z.get("1.0", "end-1c"))
                print(self.data)
            
            else:
                self.currentTest.data=ct.parse_input_string(self.data_z.get("1.0", "end-1c"))
            
            self.currentTest.datacontroller()
            if self.Wilcoxon==1:
                self.currentTest.datacontroller(self.selectedNature)
            if  self.OneSampleMeanTestG==1:
                self.currentTest.datacontroller(float(self.tmean))
            if  self.ProportionToTheoreticalTest==1:
                print("here")
                self.currentTest.datacontroller(float(self.tmean))

            if  self.TwoProportionsTest==1:
                print("here")
                self.currentTest.datacontroller(float(self.tmean))    

            

            formhyp = self.currentTest.formHyp()
            
            gui.display_formatted_text(formhyp,self.form_z)
            dist=self.currentTest.distribution()
            gui.display_formatted_text(dist,self.distro_z)
            steps=self.currentTest.steps(self.alpha)
            gui.display_formatted_text(steps,self.steps_z)
            testval = self.currentTest.testval()
            gui.display_formatted_text(testval,self.p_z)
            con = self.currentTest.conclusion(self.alpha,self.desc)
            gui.display_formatted_text(con,self.con_z)
            self.tab_control.select(self.tab_output)
        if self.dataInputMode=="informations":
            print(self.i_entries)
            self.data=ct.get_entry_valuesd(self.i_entries)
            if self.selectedTest=="OneSampleMeanTestG":
                
                
                self.data=self.data+[self.tmean]+[self.alpha]+[self.selectedNature]
                print(self.data)
            



                    
    def save_file(self):
        filename = filedialog.asksaveasfilename(defaultextension=".tst", filetypes=(("Text files", "*.tst"), ("All files", "*.*")))
        if filename:
            with open(filename, "w") as f:
                entries_and_texts = [
                    self.entry_type.get() if hasattr(self, "entry_type") else "",
                    self.entry_nature.get() if hasattr(self, "entry_nature") else "",
                    self.entry_desc.get() if hasattr(self, "entry_desc") else "",
                    self.entry_alpha.get() if hasattr(self, "entry_alpha") else "",
                    self.data_z.get("1.0", "end-1c") if hasattr(self, "data_z") else "",
                    self.form_z.get("1.0", "end-1c") if hasattr(self, "form_z") else "",
                    self.distro_z.get("1.0", "end-1c") if hasattr(self, "distro_z") else "",
                    self.steps_z.get("1.0", "end-1c") if hasattr(self, "steps_z") else "",
                    self.p_z.get("1.0", "end-1c") if hasattr(self, "p_z") else "",
                    self.con_z.get("1.0", "end-1c") if hasattr(self, "con_z") else "",
                    self.entry_tmean.get() if hasattr(self, "entry_tmean") else ""
                ]
                f.write("|".join(entries_and_texts))  # Join all entries with pipe delimiter
            print("File saved successfully.")


    def open_file(self):
        filename = filedialog.askopenfilename(filetypes=(("Text files", "*.tst"), ("All files", "*.*")))
        if filename:
            with open(filename, "r") as f:
                contents = f.read().split('|')  # Split contents by pipe delimiter
               
                self.select_test(contents[0])

                if hasattr(self, "entry_nature"):
                    self.entry_nature.delete(0, tk.END)
                    self.entry_nature.insert(0, contents[1])

                if hasattr(self, "entry_desc"):
                    self.entry_desc.delete(0, tk.END)
                    self.entry_desc.insert(0, contents[2])
                    self.set_desc()

                if hasattr(self, "entry_alpha"):
                    self.entry_alpha.delete(0, tk.END)
                    if contents[3] == "":
                        contents[3] = "0.05"
                    self.entry_alpha.insert(0, contents[3])
                    self.set_alpha()

                if hasattr(self, "data_z"):
                    self.data_z.delete("1.0", tk.END)
                    self.data_z.insert("1.0", contents[4])

                if hasattr(self, "form_z"):
                    self.form_z.delete("1.0", tk.END)
                    self.form_z.insert("1.0", contents[5])

                if hasattr(self, "distro_z"):
                    self.distro_z.delete("1.0", tk.END)
                    self.distro_z.insert("1.0", contents[6])

                if hasattr(self, "steps_z"):
                    self.steps_z.delete("1.0", tk.END)
                    self.steps_z.insert("1.0", contents[7])

                if hasattr(self, "p_z"):
                    self.p_z.delete("1.0", tk.END)
                    self.p_z.insert("1.0", contents[8])

                if hasattr(self, "con_z"):
                    self.con_z.delete("1.0", tk.END)
                    self.con_z.insert("1.0", contents[9])
                if hasattr(self, "entry_tmean"):
                    self.entry_tmean.delete(0, tk.END)
                    self.entry_tmean.insert(0, contents[10])
                    self.set_tmean()

                print("File opened successfully.")
           


    def set_desc(self):
        self.desc=self.entry_desc.get()
    
    def set_tmean(self):

        self.tmean=self.entry_tmean.get()
    
    def set_alpha(self):
        self.alpha=self.entry_alpha.get()
    def validate_input(self, event):
             # Allow normal processing for Backspace and Delete keys
            if event.keysym in ["BackSpace", "Delete"]:
                return
            # Get the current cursor position
            cursor_pos = self.data_z.index(tk.INSERT)
            # Split cursor position into line and column indices
            line, column = map(int, cursor_pos.split('.'))
            
            # Get the current text in the widget
            current_text = self.data_z.get("1.0", "end-1c")

            # Get the newly entered text
            new_text = event.char if event.char else ""

            # If text was selected, remove it from the current text
            if self.data_z.tag_ranges("sel"):
                start, end = self.data_z.tag_ranges("sel")
                current_text = current_text[:start] + current_text[end:]

            # Insert the newly entered text at the cursor position
            new_text = current_text[:line-1] + new_text + current_text[line-1:]

            # Validate the new text
            if not gui.validate_data_z(new_text):
                # Prevent the insertion of invalid text
                return "break"


    

if __name__ == "__main__":
  

    root = tk.Tk()
    app = DataAnalysisApp(root)
    root.mainloop()
