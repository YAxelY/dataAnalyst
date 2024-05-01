
# Couleurs
primaryColor = "lightblue"
secondaryColor= "white"
textColor="white"
borderwidth=2
relwidth=0.5
relheight=0.5



def setRelativeSize(window,current_widget, parent_widget, rel_height=0.08, rel_width=0.08):
    parent_widget.update_idletasks()

    # Get the requested size of the parent widget
    requested_width = parent_widget.winfo_width()
    requested_height = parent_widget.winfo_height()

    # Calculate the new size based on relative height and width
    new_width = int(rel_width * requested_width)
    new_height = int(rel_height * requested_height)
 
    
    # Set the new size of the child widget using config
    current_widget.config(
        width=new_width,
        height=new_height,
       
        )
    window.update()

def setRelativeSizeText(child_widget, parent_widget,root, rel_height=0.08,rel_width=0.08):
    parent_widget.update_idletasks()

    # Get the requested size of the parent widget
    requested_width = parent_widget.winfo_width()
    requested_height = parent_widget.winfo_height()
   

    # Calculate the new size based on relative height and width
    new_width = int(rel_width * requested_width)
    new_height = int(rel_height * requested_height)
   
    
    # Set the new size of the child widget using config
    child_widget.config(
        width=new_width,
        height=new_height,
       
        )
    root.update()
def setRelativeSizeEntry(child_widget, parent_widget,root, rel_width=0.08,):
    parent_widget.update_idletasks()

    # Get the requested size of the parent widget
    requested_width = parent_widget.winfo_width()
   

  

    # Calculate the new size based on relative height and width
    new_width = int(rel_width * requested_width)
    
   

 
    
    # Set the new size of the child widget using config
    child_widget.config(
        width=new_width
       
       
        )
    root.update()

