import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

# Modern minimal color scheme - soft and easy on the eyes
COLORS = {
    'bg': '#f8f9fa',
    'gradient_start': '#f5f7fa',
    'gradient_end': '#e9ecef',
    'card': '#ffffff',
    'card_hover': '#f8f9fa',
    'card_glass': 'rgba(255, 255, 255, 0.25)',
    'primary': '#495057',
    'primary_hover': '#343a40',
    'primary_light': '#6c757d',
    'secondary': '#6c757d',
    'danger': '#868e96',
    'danger_hover': '#495057',
    'text': '#212529',
    'text_light': '#6c757d',
    'border': '#dee2e6',
    'border_light': '#f1f3f5',
    'complete': '#adb5bd',
    'input_bg': '#ffffff',
    'shadow': '#00000010',
    'main_bg': '#f1f3f5',
}

# --- Save & Load Tasks ---
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_text = task.strip()
                if task_text.startswith("[COMPLETE]"):
                    task_text = task_text[10:]  # Remove [COMPLETE] prefix
                    add_task_item(task_text, completed=True)
                else:
                    add_task_item(task_text, completed=False)
    except FileNotFoundError:
        open("tasks.txt", "w").close()

def save_tasks():
    with open("tasks.txt", "w") as file:
        for widget in task_container.winfo_children():
            if isinstance(widget, tk.Frame):
                # Get the checkbox and label
                checkbox = None
                label = None
                for child in widget.winfo_children():
                    if isinstance(child, tk.Checkbutton):
                        checkbox = child
                    elif isinstance(child, tk.Label):
                        label = child
                
                if checkbox and label:
                    task_text = label.cget("text")
                    var = checkbox.cget("variable")
                    if var:
                        is_checked = root.getvar(var)
                        if is_checked:
                            file.write("[COMPLETE]" + task_text + "\n")
                        else:
                            file.write(task_text + "\n")

# --- Task Management Functions ---
def add_task_item(task_text, completed=False):
    """Add a task item to the list"""
    # Glassmorphism card effect
    task_frame = tk.Frame(task_container, bg='white', relief='flat', bd=0)
    task_frame.pack(fill='x', padx=10, pady=6, ipady=12, ipadx=5)
    
    # Create a rounded effect with padding
    inner_frame = tk.Frame(task_frame, bg='white', relief='flat', bd=0)
    inner_frame.pack(fill='x', padx=5, pady=3)
    
    # Checkbox
    var = tk.BooleanVar(value=completed)
    checkbox = tk.Checkbutton(
        inner_frame,
        variable=var,
        bg='white',
        activebackground='white',
        selectcolor='white',
        command=lambda: toggle_task(task_frame, var),
        cursor='hand2',
        highlightthickness=0
    )
    checkbox.pack(side='left', padx=(15, 12))
    
    # Task label
    label = tk.Label(
        inner_frame,
        text=task_text,
        bg='white',
        fg=COLORS['text'],
        font=('Segoe UI', 12),
        anchor='w',
        cursor='hand2'
    )
    label.pack(side='left', fill='x', expand=True, padx=(0, 10))
    
    # Delete button with enhanced hover
    delete_btn = tk.Button(
        inner_frame,
        text='✕',
        command=lambda: remove_task(task_frame),
        bg='white',
        fg=COLORS['text_light'],
        activebackground=COLORS['danger'],
        activeforeground='white',
        font=('Segoe UI', 14, 'bold'),
        relief='flat',
        bd=0,
        cursor='hand2',
        padx=10,
        pady=2,
        width=2
    )
    delete_btn.pack(side='right', padx=(0, 10))
    
    # Enhanced hover effects with smooth transitions
    def on_enter(event):
        smooth_color_transition(task_frame, '#ffffff', COLORS['card_hover'], steps=5, duration=100)
        smooth_color_transition(inner_frame, '#ffffff', COLORS['card_hover'], steps=5, duration=100)
        for widget in [checkbox, label, delete_btn]:
            if isinstance(widget, tk.Checkbutton):
                widget.config(bg=COLORS['card_hover'], activebackground=COLORS['card_hover'], selectcolor=COLORS['card_hover'])
            else:
                widget.config(bg=COLORS['card_hover'])
        # Scale effect on delete button
        delete_btn.config(font=('Segoe UI', 16, 'bold'), fg=COLORS['danger'])
    
    def on_leave(event):
        smooth_color_transition(task_frame, COLORS['card_hover'], '#ffffff', steps=5, duration=100)
        smooth_color_transition(inner_frame, COLORS['card_hover'], '#ffffff', steps=5, duration=100)
        for widget in [checkbox, label, delete_btn]:
            if isinstance(widget, tk.Checkbutton):
                widget.config(bg='white', activebackground='white', selectcolor='white')
            else:
                widget.config(bg='white')
        delete_btn.config(font=('Segoe UI', 14, 'bold'), fg=COLORS['text_light'])
    
    task_frame.bind('<Enter>', on_enter)
    task_frame.bind('<Leave>', on_leave)
    for widget in [inner_frame, checkbox, label]:
        widget.bind('<Enter>', on_enter)
        widget.bind('<Leave>', on_leave)
    
    # Delete button hover
    def on_delete_enter(event):
        delete_btn.config(bg=COLORS['border'], fg=COLORS['danger'], font=('Segoe UI', 16, 'bold'))
    
    def on_delete_leave(event):
        delete_btn.config(bg=inner_frame.cget('bg'), fg=COLORS['text_light'], font=('Segoe UI', 14, 'bold'))
    
    delete_btn.bind('<Enter>', on_delete_enter)
    delete_btn.bind('<Leave>', on_delete_leave)
    
    # Store reference to label in task_frame for toggle
    task_frame.label = label
    task_frame.checkbox = checkbox
    task_frame.var = var
    task_frame.inner_frame = inner_frame
    
    if completed:
        toggle_task(task_frame, var, initial=True)

def toggle_task(task_frame, var, initial=False):
    """Toggle task completion state"""
    label = task_frame.label
    inner_frame = task_frame.inner_frame
    if var.get():
        label.config(
            fg=COLORS['complete'],
            font=('Segoe UI', 12, 'overstrike')
        )
        smooth_color_transition(task_frame, task_frame.cget('bg'), '#f3f4f6', steps=5, duration=100)
        smooth_color_transition(inner_frame, inner_frame.cget('bg'), '#f3f4f6', steps=5, duration=100)
        task_frame.checkbox.config(bg='#f3f4f6', activebackground='#f3f4f6', selectcolor='#f3f4f6')
        label.config(bg='#f3f4f6')
        # Update delete button bg
        for child in inner_frame.winfo_children():
            if isinstance(child, tk.Button) and child.cget('text') == '✕':
                child.config(bg='#f3f4f6')
    else:
        label.config(
            fg=COLORS['text'],
            font=('Segoe UI', 12)
        )
        smooth_color_transition(task_frame, task_frame.cget('bg'), 'white', steps=5, duration=100)
        smooth_color_transition(inner_frame, inner_frame.cget('bg'), 'white', steps=5, duration=100)
        task_frame.checkbox.config(bg='white', activebackground='white', selectcolor='white')
        label.config(bg='white')
        # Update delete button bg
        for child in inner_frame.winfo_children():
            if isinstance(child, tk.Button) and child.cget('text') == '✕':
                child.config(bg='white')
    
    if not initial:
        save_tasks()

def remove_task(task_frame):
    """Remove a task from the list"""
    task_frame.destroy()
    save_tasks()

def add_task():
    """Add a new task"""
    task = task_entry.get().strip()
    if task:
        add_task_item(task, completed=False)
        task_entry.delete(0, tk.END)
        save_tasks()
        # Clear focus from entry
        root.focus()
    else:
        messagebox.showwarning("Warning", "Please enter a task before adding!")

def clear_all_tasks():
    """Clear all tasks"""
    if len(task_container.winfo_children()) > 0:
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
            for widget in task_container.winfo_children():
                widget.destroy()
            save_tasks()

def on_entry_enter(event):
    """Handle Enter key press in entry field"""
    add_task()

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    """Convert RGB tuple to hex color"""
    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))

def create_gradient_background(canvas, width, height, start_color, end_color):
    """Create a gradient background on canvas"""
    start_rgb = hex_to_rgb(start_color)
    end_rgb = hex_to_rgb(end_color)
    
    for i in range(height):
        ratio = i / height
        r = start_rgb[0] * (1 - ratio) + end_rgb[0] * ratio
        g = start_rgb[1] * (1 - ratio) + end_rgb[1] * ratio
        b = start_rgb[2] * (1 - ratio) + end_rgb[2] * ratio
        color = rgb_to_hex((r, g, b))
        canvas.create_line(0, i, width, i, fill=color, width=1)

def smooth_color_transition(widget, from_color, to_color, steps=10, duration=150):
    """Smooth color transition effect"""
    from_rgb = hex_to_rgb(from_color)
    to_rgb = hex_to_rgb(to_color)
    
    def transition_step(step):
        if step <= steps:
            ratio = step / steps
            r = from_rgb[0] * (1 - ratio) + to_rgb[0] * ratio
            g = from_rgb[1] * (1 - ratio) + to_rgb[1] * ratio
            b = from_rgb[2] * (1 - ratio) + to_rgb[2] * ratio
            color = rgb_to_hex((r, g, b))
            try:
                widget.config(bg=color)
            except tk.TclError:
                pass  # Widget might have been destroyed
            if step < steps:
                root.after(duration // steps, lambda s=step+1: transition_step(s))
    
    transition_step(1)

# --- UI Setup ---
root = tk.Tk()
root.title("To-Do List")
root.geometry("600x700")
root.resizable(False, False)

# Create gradient background canvas
bg_canvas = tk.Canvas(root, highlightthickness=0, bd=0)
bg_canvas.pack(fill='both', expand=True)

def update_gradient(event=None):
    """Update gradient when window is resized"""
    bg_canvas.delete("all")
    width = root.winfo_width()
    height = root.winfo_height()
    if width > 1 and height > 1:
        create_gradient_background(
            bg_canvas,
            width,
            height,
            COLORS['gradient_start'],
            COLORS['gradient_end']
        )

root.bind('<Configure>', update_gradient)
root.update()
create_gradient_background(
    bg_canvas, 
    root.winfo_width(), 
    root.winfo_height(),
    COLORS['gradient_start'],
    COLORS['gradient_end']
)

# Main container with transparent background for gradient
main_container = tk.Frame(bg_canvas, bg=COLORS['main_bg'])
main_container.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.95, relheight=0.95)

# Header
header_frame = tk.Frame(main_container, bg=COLORS['main_bg'])
header_frame.pack(fill='x', pady=(0, 25))

title = tk.Label(
    header_frame,
    text="My Tasks",
    font=('Segoe UI', 32, 'bold'),
    bg=COLORS['main_bg'],
    fg=COLORS['text']
)
title.pack()

subtitle = tk.Label(
    header_frame,
    text="Stay organized and productive",
    font=('Segoe UI', 12),
    bg=COLORS['main_bg'],
    fg=COLORS['text_light']
)
subtitle.pack(pady=(8, 0))

# Input section
input_frame = tk.Frame(main_container, bg='white', relief='flat', bd=0)
input_frame.pack(fill='x', pady=(0, 20), ipady=18)

# Entry field with modern styling
entry_container = tk.Frame(input_frame, bg='white')
entry_container.pack(fill='x', padx=18, pady=8)

task_entry = tk.Entry(
    entry_container,
    font=('Segoe UI', 13),
    bg=COLORS['input_bg'],
    fg=COLORS['text'],
    relief='flat',
    bd=0,
    insertbackground=COLORS['text'],
    highlightthickness=2,
    highlightcolor=COLORS['primary'],
    highlightbackground=COLORS['border']
)
task_entry.pack(side='left', fill='x', expand=True, padx=(0, 12), ipady=12, ipadx=18)
task_entry.bind('<Return>', on_entry_enter)

# Enhanced entry hover
def on_entry_focus_in(event):
    task_entry.config(highlightcolor=COLORS['primary'], highlightbackground=COLORS['primary_light'])

def on_entry_focus_out(event):
    task_entry.config(highlightcolor=COLORS['primary'], highlightbackground=COLORS['border'])

task_entry.bind('<FocusIn>', on_entry_focus_in)
task_entry.bind('<FocusOut>', on_entry_focus_out)

# Add button with modern styling
add_button = tk.Button(
    entry_container,
    text="➕ Add Task",
    command=add_task,
    bg=COLORS['primary'],
    fg='white',
    font=('Segoe UI', 12, 'bold'),
    relief='flat',
    bd=0,
    cursor='hand2',
    padx=24,
    pady=12,
    activebackground=COLORS['primary_hover'],
    activeforeground='white'
)
add_button.pack(side='right')

def on_add_hover_enter(event):
    smooth_color_transition(add_button, COLORS['primary'], COLORS['primary_hover'], steps=5, duration=100)

def on_add_hover_leave(event):
    smooth_color_transition(add_button, COLORS['primary_hover'], COLORS['primary'], steps=5, duration=100)

add_button.bind('<Enter>', on_add_hover_enter)
add_button.bind('<Leave>', on_add_hover_leave)

# Tasks container with scrollbar
tasks_section = tk.Frame(main_container, bg=COLORS['main_bg'])
tasks_section.pack(fill='both', expand=True)

# Canvas and scrollbar for scrolling
canvas = tk.Canvas(tasks_section, bg=COLORS['main_bg'], highlightthickness=0, bd=0)
scrollbar = ttk.Scrollbar(tasks_section, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg=COLORS['main_bg'])

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

task_container = scrollable_frame

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Update canvas scroll region when mousewheel is used
def on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind_all("<MouseWheel>", on_mousewheel)

# Footer with clear button
footer_frame = tk.Frame(main_container, bg=COLORS['main_bg'])
footer_frame.pack(fill='x', pady=(15, 0))

clear_button = tk.Button(
    footer_frame,
    text="🗑️ Clear All Tasks",
    command=clear_all_tasks,
    bg=COLORS['danger'],
    fg='white',
    font=('Segoe UI', 11),
    relief='flat',
    bd=0,
    cursor='hand2',
    padx=18,
    pady=10,
    activebackground=COLORS['danger_hover'],
    activeforeground='white'
)
clear_button.pack(side='right')

def on_clear_hover_enter(event):
    smooth_color_transition(clear_button, COLORS['danger'], COLORS['danger_hover'], steps=5, duration=100)

def on_clear_hover_leave(event):
    smooth_color_transition(clear_button, COLORS['danger_hover'], COLORS['danger'], steps=5, duration=100)

clear_button.bind('<Enter>', on_clear_hover_enter)
clear_button.bind('<Leave>', on_clear_hover_leave)

# Load existing tasks on start
load_tasks()

# Focus on entry field when app starts
task_entry.focus()

root.mainloop()