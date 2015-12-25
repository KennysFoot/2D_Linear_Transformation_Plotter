import math_utils as mu
import numpy as np
from tkinter import *
from tkinter import ttk

def calculate(vec_in_x, vec_in_y, mat11, mat12, mat21, mat22, vec_out_field):
    try:
        # Create input vector
        vec_in = mu.Vector(float(vec_in_x.get()), float(vec_in_y.get()))

        # Create matrix
        matrix = mu.Matrix(float(mat11.get()), float(mat12.get()), float(mat21.get()), float(mat22.get()))

        # Calculate output
        vec_out_raw = np.dot(matrix.matrix, vec_in.tuple)
        vec_out = mu.Vector(vec_out_raw.item(0), vec_out_raw.item(1))

        result = "(" + str(vec_out_raw.item(0)) + ", " + str(vec_out_raw.item(1)) + ")"
        print(result)
        vec_out_field.set(result)

        # Plot output
        vec_out.plot("Output")
    except ValueError:
        pass

def gui():
    # Set up main window
    root = Tk()
    root.title("2D Linear Transformation Plotter")

    # create main frame to hold everything
    main_frame = ttk.Frame(root, padding="3 3 3 3")
    main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    main_frame.columnconfigure(0, weight=1)
    main_frame.rowconfigure(0, weight=1)

    # text variables for numerical input and output
    vec_in_x = StringVar()
    vec_in_y = StringVar()

    mat11 = StringVar()
    mat12 = StringVar()
    mat21 = StringVar()
    mat22 = StringVar()

    vec_out_field = StringVar()

    # Set up entry fields, labels, and buttons
    FIELD_WIDTH = 10

    vec_in_x_entry = ttk.Entry(main_frame, width=FIELD_WIDTH, textvariable=vec_in_x)
    vec_in_x_entry.grid(column=1, row=2, sticky=(W, E))
    vec_in_y_entry = ttk.Entry(main_frame, width=FIELD_WIDTH, textvariable=vec_in_y)
    vec_in_y_entry.grid(column=2, row=2, sticky=(W, E))

    mat11_entry = ttk.Entry(main_frame, width=FIELD_WIDTH, textvariable=mat11)
    mat11_entry.grid(column=1, row=4, sticky=(W, E))
    mat12_entry = ttk.Entry(main_frame, width=FIELD_WIDTH, textvariable=mat12)
    mat12_entry.grid(column=2, row=4, sticky=(W, E))
    mat21_entry = ttk.Entry(main_frame, width=FIELD_WIDTH, textvariable=mat21)
    mat21_entry.grid(column=1, row=5, sticky=(W, E))
    mat22_entry = ttk.Entry(main_frame, width=FIELD_WIDTH, textvariable=mat22)
    mat22_entry.grid(column=2, row=5, sticky=(W, E))

    vec_out_label = ttk.Label(main_frame, textvariable=vec_out_field)
    vec_out_label.grid(column=3, row=2, stick=(W, E))

    ttk.Button(main_frame, text="Calculate", command=lambda: calculate(vec_in_x, vec_in_y, mat11, mat12, mat21, mat22,
                                                               vec_out_field)).grid(column=1, row=6, stick=W)

    # Set up static text labels
    ttk.Label(main_frame, text="Input:").grid(column=1, row=1, sticky=W)
    ttk.Label(main_frame, text="Matrix:").grid(column=1, row=3, sticky=W)
    ttk.Label(main_frame, text="Output:", width=30).grid(column=3, row=1, sticky=W)

    for child in main_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    # Bind enter button to calculate method
    root.bind("<Return>", lambda x: calculate(vec_in_x, vec_in_y, mat11, mat12, mat21, mat22, vec_out_field))

    # Set initial focus to input vector entry
    vec_in_x_entry.focus()

    root.mainloop()

gui()