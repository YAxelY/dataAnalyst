import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

import Style as st 
from communfunctions import gui_items as gui


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
        # end main windows


        self.create_widgets(self.master)
    
    def create_widgets(self,master):
        # main menu bar
        menubar = tk.Menu(master) 
        #can't pack Menu widget is top-level-windows
        menubar.config(bg="lightblue",bd=2,relief="groove")
        #can't resize Menu widget
        

        

        
        # Menu Fichier
        file_menu = tk.Menu(menubar, tearoff=1)
        file_menu.config(bg="lightblue",fg="white")
        file_menu.add_command(label="New", command=lambda: None)
        file_menu.add_command(label="Ouvrir", command=self.open_file)
        file_menu.add_command(label="Sauvegarder", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Quitter", command=self.quit_app)
        menubar.add_cascade(label="Fichier", menu=file_menu)
        
        # Menu Paramètres
        parameters_menu = tk.Menu(menubar, tearoff=0)
        parameters_menu.config(bg="white",fg="black")
        
        # Sous-menu Thème
        theme_menu = tk.Menu(parameters_menu, tearoff=0)
        theme_menu.add_command(label="Dark", command=self.set_dark_theme)
        theme_menu.add_command(label="Light", command=self.set_light_theme)
        parameters_menu.add_cascade(label="Thème", menu=theme_menu)
        
        # Sous-menu Taille
        size_menu = tk.Menu(parameters_menu, tearoff=0)
        size_menu.add_command(label="+", command=self.increase_size)
        size_menu.add_command(label="-", command=self.decrease_size)
        size_menu.add_command(label="Reintialiser", command=self.reset_size)
        parameters_menu.add_cascade(label="Taille", menu=size_menu)
        
        # Sous-menu Langue
        language_menu = tk.Menu(parameters_menu, tearoff=0)
        language_menu.add_command(label="Anglais", command=self.set_language_english)
        language_menu.add_command(label="Francais", command=self.set_language_french)
        parameters_menu.add_cascade(label="Langue", menu=language_menu)
        
        # Sous-menu Préférences
        preferences_menu = tk.Menu(parameters_menu, tearoff=0)
        preferences_menu.add_command(label="Option 1", command=self.preference_option1)
        preferences_menu.add_command(label="Option 2", command=self.preference_option2)
        parameters_menu.add_cascade(label="Préférences", menu=preferences_menu)
        
        menubar.add_cascade(label="Paramètres", menu=parameters_menu)
        
        master.config(menu=menubar)

        # Ajouter des onglets Input et Output
        tab_control = ttk.Notebook(master)
        tab_input = ttk.Frame(tab_control)
        tab_input.configure(padding="0")
        tab_output = ttk.Frame(tab_control)
        tab_control.add(tab_input, text='Entree')
        tab_control.add(tab_output, text='Sortie')
        tab_control.pack(expand=1, fill="both")
        
        c_input=tk.Frame(tab_input)
        c_input.pack(fill="both",padx=0,pady=0,ipadx=0,ipady=0)
        c_input.config(bg="white")
       
        
        
        #g_type style to be inserted
        g_type = tk.Frame(c_input)
        g_type.pack( expand="true",side="top", fill="x",anchor="nw", pady=0,padx=0,ipadx=0,ipady=0)
        g_type.config(bg="white",height=10,relief="solid",borderwidth=1)
       
        #g_type style to be inserted



      
        

        # Ajouter un label "Seuil de Signification" et son champ après les onglets
        label_type = tk.Menubutton(g_type, text="Type de test >")
        label_type.config(relief="ridge",bg="white",fg="black")
        label_type.pack(side="left",padx=1)
       

        # Create a menu for the menubutton
        test_menu = tk.Menu(label_type, tearoff=1)
        test_menu.config(relief="ridge",bg="white",fg="black")
        test_menu.add_command(label="Anova one-way", command=lambda: select_test("Anova one-way"))
        test_menu.add_command(label="t-test", command=lambda: select_test("t-test"))
        
        # Attach the menu to the menubutton
        label_type.config(menu=test_menu)
        
        entry_type = tk.Entry(g_type)
        entry_type.pack(expand="true",side="left",anchor="w",padx="10")
        entry_type.config(state="disabled")
        st.setRelativeSizeEntry(entry_type,c_input,self.master,0.01)



        label_detect = tk.Button(g_type, text="Help to Detect ")
        label_detect.config(relief="ridge",bg="white",fg="black")
        label_detect.pack(side="left",padx=1)
       


        g_nature = tk.Frame(c_input)
        g_nature.pack( expand="true",side="top",anchor="ne", fill="x" ,padx=0,pady=10,ipadx=0,ipady=0)
        g_nature.config(bg="white",height=10,relief="solid",borderwidth=2)

         # Ajouter un label "Seuil de Signification" et son champ après les onglets
        label_nature = tk.Menubutton(g_nature, text="Test Nature >")
        label_nature.config(relief="ridge",bg="white",fg="black")
        label_nature.pack(side="left",padx=1)
       

        # Create a menu for the menubutton
        nature_menu = tk.Menu(label_nature, tearoff=1)
        nature_menu.config(relief="ridge",bg="white",fg="black")
        nature_menu.add_command(label="two-tail", command=lambda: select_nature("two-tail"))
        nature_menu.add_command(label="one-tail", command=lambda: select_nature("one-tail"))
        # Attach the menu to the menubutton
        label_nature.config(menu=nature_menu)
        entry_nature = tk.Entry(g_nature)
        entry_nature.pack(expand="true",side="left",anchor="w",padx="10")
        entry_nature.config(state="disabled")
        st.setRelativeSizeEntry(entry_nature,c_input,self.master,0.01)

        #description



        g_desc = tk.Frame(c_input)
        g_desc.pack( expand="true",side="top",anchor="ne", fill="x" ,padx=0,pady=10,ipadx=0,ipady=0)
        g_desc.config(bg="white",height=10)

         # Ajouter un label "Seuil de Signification" et son champ après les onglets
        label_desc = tk.Button(g_desc, text="H0 enoncé (optional) ")
        label_desc.config(relief="ridge",bg="white",fg="black")
        label_desc.pack(side="left",padx=1)
       
        
        entry_desc = tk.Entry(g_desc)
        entry_desc.pack(expand="true",side="left",anchor="w",padx="10")
        entry_desc.config(state="normal")
        st.setRelativeSizeEntry(entry_desc,c_input,self.master,0.01)

        #end description

        #seuil de signification

        g_alpha = tk.Frame(c_input)
        g_alpha.pack( expand="true",side="top",anchor="ne", fill="x" ,padx=0,pady=10,ipadx=0,ipady=0)
        g_alpha.config(bg="white",height=10)

         # Ajouter un label "Seuil de Signification" et son champ après les onglets
        label_alpha = tk.Button(g_alpha, text="seuil de signification ")
        label_alpha.config(relief="ridge",bg="white",fg="black")
        label_alpha.pack(side="left",padx=1)
       
        
        entry_alpha = tk.Entry(g_alpha)
        entry_alpha.pack(expand="true",side="left",anchor="w",padx="10")
        entry_alpha.config(state="normal")
        st.setRelativeSizeEntry(entry_alpha,c_input,self.master,0.01)

        
        
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


        data_f,data_t,data_z=gui.createft("data input",c_input)
        data_f.pack(expand="true",side="top",fill="both")
        data_t.pack(expand="true",side="top",fill="both")
        data_z.pack(expand="true",side="top",fill="both")
        st.setRelativeSize(self.master,data_z,self.master,0.03,0.02)


        validV = tk.Frame(c_input)
        validV.pack(expand="true",side="bottom")

        # Create three buttons
        erase= tk.Button(validV, text="erase")
        erase.pack(expand="true",fill="x",side="left",anchor="w" ,padx=10)
        run = tk.Button(validV, text="run")
        st.setRelativeSize(self.master,erase,self.master,0.001,0.02)
        run.pack(expand="true",fill="x",side="left" , anchor="e")
        st.setRelativeSize(self.master,run,self.master,0.001,0.02)






        #output
        c_output=tk.Frame(tab_output)
        c_output.pack(fill="both",padx=0,pady=0,ipadx=0,ipady=0)
        c_output.config(bg="white")


        form_f,form_t,form_z=gui.createft("1-formulation d'hypothèse",c_output)
        form_f.pack(expand="true",side="top",fill="both")
        form_t.pack(expand="true",side="top",fill="both")
        form_z.pack(expand="true",side="top",fill="both")
        st.setRelativeSize(self.master,form_z,self.master,0.01,0.02)

        distro_f,distro_t,distro_z=gui.createft("2-choix de la loi",c_output)
        distro_f.pack(expand="true",side="top",fill="both")
        distro_t.pack(expand="true",side="top",fill="both")
        distro_z.pack(expand="true",side="top",fill="both")
        st.setRelativeSize(self.master,distro_z,self.master,0.01,0.02)


        steps_f,steps_t,steps_z=gui.createft("3-valeurs du test",c_output)
        steps_f.pack(expand="true",side="top",fill="both")
        steps_t.pack(expand="true",side="top",fill="both")
        steps_z.pack(expand="true",side="top",fill="both")
        st.setRelativeSize(self.master,steps_z,self.master,0.01,0.02)


        p_f,p_t,p_z=gui.createft("4- p-value",c_output)
        p_f.pack(expand="true",side="top",fill="both")
        p_t.pack(expand="true",side="top",fill="both")
        p_z.pack(expand="true",side="top",fill="both")
        st.setRelativeSize(self.master,p_z,self.master,0.01,0.02)


        con_f,con_t,con_z=gui.createft("5- prise de decision et conclusion",c_output)
        con_f.pack(expand="true",side="top",fill="both")
        con_t.pack(expand="true",side="top",fill="both")
        con_z.pack(expand="true",side="top",fill="both")
        st.setRelativeSize(self.master,con_z,self.master,0.01,0.02)

        
       
        
        

    
    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            # Traiter le fichier ouvert
            print("Fichier ouvert :", file_path)
    
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            # Sauvegarder les données dans le fichier
            print("Fichier sauvegardé :", file_path)
    
    def quit_app(self):
        self.destroy()
    
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

if __name__ == "__main__":
    root = tk.Tk()
    app = DataAnalysisApp(root)
    root.mainloop()
