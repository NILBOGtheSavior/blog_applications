import cv2
from PIL import Image, ImageTk
import tkinter as tk

def runmonitor():
    cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    webcap.imgtk = imgtk
    webcap.configure(image=imgtk)
    webcap.after(20, runmonitor)

def main():
    global cap, webcap  # Make 'cap' and 'webcap' global so that they can be accessed in other functions
    cap = cv2.VideoCapture(0)  # Initialize capture variable with camera index 0
    # If multiple cameras are connected, the index must be changed to the desired camera index.

    root = tk.Tk()
    root.title("Webcam Example")

    cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    
    webcap = tk.Label(root, image=imgtk)
    webcap.imgtk = imgtk
    webcap.pack()

    root.after(20, runmonitor)  # Start the webcam monitoring loop

    root.mainloop()

if __name__ == "__main__":
    main()

