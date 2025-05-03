import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation
import os


animation_descriptions = {
    "obesity": "\n🎬 Showing obesity progression.\nUse your keyboard:\n- Press 'n' to go to the next image\n- Press 'b' to go back\n- Close the window when you're done.",
    "adipokine": "\n🎬 Showing release of adipokines by adipose tissue.",
    "inflammation": "\n🎬 Showing immune response and inflammation in adipose tissue.",
    "insulin": "\n🎬 Showing insulin release and blood glucose regulation.",
    "insulin resistance": "\n🎬 Showing insulin resistance in peripheral tissues.",
    "hyperglycemia": "\n🎬 Showing excessive glucose in bloodstream.",
    "pancreas": "\n🎬 Showing the pancreas and its role in hormone production.",
    "beta": "\n🎬 Showing beta cells in the pancreas releasing insulin.",
    "type 2 diabetes": "\n🎬 Showing development of Type 2 Diabetes due to obesity and insulin resistance."
}

def obesity_animation():
    image_folder = "images"
    frames_files = [
        "person_eating.png",
        "no_exercise.png",
        "fataccumulation_obese.png"
    ]   
    frames = [mpimg.imread(os.path.join(image_folder, file)) for file in frames_files]

    # Get pixel size of the first image
    height, width, _ = frames[0].shape

    # Set figure size in inches based on pixel dimensions and desired DPI
    dpi = 100
    fig = plt.figure(figsize=(width / dpi, height / dpi), dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1])  # fill the entire figure with the image
    img_display = ax.imshow(frames[0])
    ax.axis("off")
    ax.set_aspect('auto')  # Maintain natural aspect ratio

    current_frame = [0]

    def on_key(event):
        if event.key == 'n':
            current_frame[0] = (current_frame[0] + 1) % len(frames)
        elif event.key == 'b':
            current_frame[0] = (current_frame[0] - 1) % len(frames)
        img_display.set_data(frames[current_frame[0]])
        fig.canvas.draw_idle()

    fig.canvas.mpl_connect('key_press_event', on_key)
    plt.show()
    
def adipokine_animation():
    image_folder = "images"
    frames_files = [
        "ad_1.png",
        "ad_2.png",
        "ad_3.png"
    ]   
    frames = [mpimg.imread(os.path.join(image_folder, file)) for file in frames_files]
    
    fig, ax = plt.subplots()
    img_display = ax.imshow(frames[0])
    ax.axis("off")  # Hide axes
    ax.set_aspect('auto')
    
    current_frame = [0]
    
    def on_key(event):
        if event.key == 'n':  # next
            current_frame[0] = (current_frame[0] + 1) % len(frames)
        elif event.key == 'b':  # back
            current_frame[0] = (current_frame[0] - 1) % len(frames)
        
        img_display.set_data(frames[current_frame[0]])
        fig.canvas.draw_idle()
    
    fig.canvas.mpl_connect('key_press_event', on_key)
    plt.show()
    
def inflammation_animation():
    image_folder = "images"
    frames_files = [
        "if_1.png",
        "if_2.png"
    ]   
    frames = [mpimg.imread(os.path.join(image_folder, file)) for file in frames_files]
    
    fig, ax = plt.subplots()
    img_display = ax.imshow(frames[0])
    ax.axis("off")  # Hide axes
    ax.set_aspect('auto')
    
    current_frame = [0]
    
    def on_key(event):
        if event.key == 'n':  # next
            current_frame[0] = (current_frame[0] + 1) % len(frames)
        elif event.key == 'b':  # back
            current_frame[0] = (current_frame[0] - 1) % len(frames)
        
        img_display.set_data(frames[current_frame[0]])
        fig.canvas.draw_idle()
    
    fig.canvas.mpl_connect('key_press_event', on_key)
    plt.show()

def insulin_animation():
    image_folder = "images"
    frames_files = [
        "insulin_1.png",
        "insulin_2.png",
        "insulin_3.png"
    ]   
    frames = [mpimg.imread(os.path.join(image_folder, file)) for file in frames_files]
    
    fig, ax = plt.subplots()
    img_display = ax.imshow(frames[0])
    ax.axis("off")  # Hide axes
    ax.set_aspect('auto')
    
    current_frame = [0]
    
    def on_key(event):
        if event.key == 'n':  # next
            current_frame[0] = (current_frame[0] + 1) % len(frames)
        elif event.key == 'b':  # back
            current_frame[0] = (current_frame[0] - 1) % len(frames)
        
        img_display.set_data(frames[current_frame[0]])
        fig.canvas.draw_idle()
    
    fig.canvas.mpl_connect('key_press_event', on_key)
    plt.show()
    
def ir_animation():
    image_folder = "images"
    frames_files = [
        "ir_1.png",
        "ir_2.png",
        "ir_3.png"
    ]   
    frames = [mpimg.imread(os.path.join(image_folder, file)) for file in frames_files]
    
    fig, ax = plt.subplots()
    img_display = ax.imshow(frames[0])
    ax.axis("off")  # Hide axes
    ax.set_aspect('auto')
    
    current_frame = [0]
    
    def on_key(event):
        if event.key == 'n':  # next
            current_frame[0] = (current_frame[0] + 1) % len(frames)
        elif event.key == 'b':  # back
            current_frame[0] = (current_frame[0] - 1) % len(frames)
        
        img_display.set_data(frames[current_frame[0]])
        fig.canvas.draw_idle()
    
    fig.canvas.mpl_connect('key_press_event', on_key)
    plt.show()
    
def hyperglycemia_animation():
    image_folder = "images"
    frames_files = [
        "hg_1.png",
        "hg_2.png",
        "hg_3.png",
        "hg_4.png"
    ]   
    frames = [mpimg.imread(os.path.join(image_folder, file)) for file in frames_files]
    
    fig, ax = plt.subplots()
    img_display = ax.imshow(frames[0])
    ax.axis("off")  # Hide axes
    ax.set_aspect('auto')
    
    current_frame = [0]
    
    def on_key(event):
        if event.key == 'n':  # next
            current_frame[0] = (current_frame[0] + 1) % len(frames)
        elif event.key == 'b':  # back
            current_frame[0] = (current_frame[0] - 1) % len(frames)
        
        img_display.set_data(frames[current_frame[0]])
        fig.canvas.draw_idle()
    
    fig.canvas.mpl_connect('key_press_event', on_key)
    plt.show()    
    
def pancreas_animation():
    image_folder = "images"
    frames_files = [
        "pan_1.png",
        "pan_2.png",
        "pan_3.png"
    ]   
    frames = [mpimg.imread(os.path.join(image_folder, file)) for file in frames_files]
    
    fig, ax = plt.subplots()
    img_display = ax.imshow(frames[0])
    ax.axis("off")  # Hide axes
    ax.set_aspect('auto')
    
    current_frame = [0]
    
    def on_key(event):
        if event.key == 'n':  # next
            current_frame[0] = (current_frame[0] + 1) % len(frames)
        elif event.key == 'b':  # back
            current_frame[0] = (current_frame[0] - 1) % len(frames)
        
        img_display.set_data(frames[current_frame[0]])
        fig.canvas.draw_idle()
    
    fig.canvas.mpl_connect('key_press_event', on_key)
    plt.show() 
    
def beta_animation():
    image_folder = "images"
    frames_files = [
        "beta_1.png"
    ]   
    frames = [mpimg.imread(os.path.join(image_folder, file)) for file in frames_files]
    
    fig, ax = plt.subplots()
    img_display = ax.imshow(frames[0])
    ax.axis("off")  # Hide axes
    ax.set_aspect('auto')
    
    current_frame = [0]
    
    def on_key(event):
        if event.key == 'n':  # next
            current_frame[0] = (current_frame[0] + 1) % len(frames)
        elif event.key == 'b':  # back
            current_frame[0] = (current_frame[0] - 1) % len(frames)
        
        img_display.set_data(frames[current_frame[0]])
        fig.canvas.draw_idle()
    
    fig.canvas.mpl_connect('key_press_event', on_key)
    plt.show()       
    
def t2d_animation():
    image_folder = "images"
    frames_files = [
        "t2d_1.png"
    ]   
    frames = [mpimg.imread(os.path.join(image_folder, file)) for file in frames_files]
    
    fig, ax = plt.subplots()
    img_display = ax.imshow(frames[0])
    ax.axis("off")  # Hide axes
    ax.set_aspect('auto')
    
    current_frame = [0]
    
    def on_key(event):
        if event.key == 'n':  # next
            current_frame[0] = (current_frame[0] + 1) % len(frames)
        elif event.key == 'b':  # back
            current_frame[0] = (current_frame[0] - 1) % len(frames)
        
        img_display.set_data(frames[current_frame[0]])
        fig.canvas.draw_idle()
    
    fig.canvas.mpl_connect('key_press_event', on_key)
    plt.show()

animation_functions = {
    "obesity": obesity_animation,
    "adipokine": adipokine_animation,
    "inflammation": inflammation_animation,
    "insulin": insulin_animation,
    "insulin resistance": ir_animation,
    "hyperglycemia": hyperglycemia_animation,
    "pancreas": pancreas_animation,
    "beta": beta_animation,
    "type 2 diabetes": t2d_animation
}