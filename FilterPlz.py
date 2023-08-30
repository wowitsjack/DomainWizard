# 📦 Importing necessary modules and packages 📦
import os
# 👆 Importing a package to use its functionalities
# 📦 Importing necessary modules and packages 📦
import json
# 👆 Importing a package to use its functionalities
# 📦 Importing necessary modules and packages 📦
import tkinter as tk
# 👆 Importing a package to use its functionalities
# 📦 Importing necessary modules and packages 📦
from tkinter import messagebox, ttk
# 👆 Importing a package to use its functionalities
# 📦 Importing necessary modules and packages 📦
from ttkbootstrap import Style
# 👆 Importing a package to use its functionalities

# 📋 Defining filenames for storing various data 📋
FILENAME = 'domains.txt'
# 👆 Setting up filenames for later use
SHORTLIST_FILE = 'shortlist.txt'
REJECT_FILE = 'rejected.txt'
SESSION_FILE = 'session.json'

# 🎬 Function Definitions 🎬
def load_session():
# 👆 Defining a new function to perform specific tasks
    if os.path.exists(SESSION_FILE):
# 👆 Conditional statement to make decisions
        with open(SESSION_FILE, 'r') as file:
# 👆 Opening a file and making sure it gets closed
            session = json.load(file)
            if 'rejected' not in session:
# 👆 Conditional statement to make decisions
                session['rejected'] = []
            return session
# 👆 Returning a value from the function
    else:
# 👆 Conditional statement to make decisions
        return {'pointer': 0, 'shortlist': [], 'rejected': []}
# 👆 Returning a value from the function

# 🎬 Function Definitions 🎬
def save_session(session):
# 👆 Defining a new function to perform specific tasks
    with open(SESSION_FILE, 'w') as file:
# 👆 Opening a file and making sure it gets closed
        json.dump(session, file)

# 🎬 Function Definitions 🎬
def load_domains(filename):
# 👆 Defining a new function to perform specific tasks
    with open(filename, 'r') as file:
# 👆 Opening a file and making sure it gets closed
        return [line.strip() for line in file.readlines()]
# 👆 Returning a value from the function

# 🎬 Function Definitions 🎬
def append_to_file(filename, domain):
# 👆 Defining a new function to perform specific tasks
    with open(filename, 'a') as file:
# 👆 Opening a file and making sure it gets closed
        file.write(domain + '\n')
        file.flush()
        os.fsync(file.fileno())

class App:
# 🎬 Function Definitions 🎬
    def __init__(self, root):
# 👆 Defining a new function to perform specific tasks
        self.root = root
# 📋 Defining filenames for storing various data 📋
        self.domains = load_domains(FILENAME)
# 👆 Setting up filenames for later use
        self.session = load_session()
        self.pointer = self.session['pointer']
        self.shortlist = self.session['shortlist']
        self.rejected = self.session['rejected']

        self.root.geometry('500x700')
        self.root.title("Domain Review")

        style = Style('cyborg')
        style.configure('TFrame', background='#2b2b2b')
        style.configure('TLabel', background='#2b2b2b', foreground='white', font=("Helvetica", 18))
        style.configure('TButton', font=("Helvetica", 18))

        self.title_label = ttk.Label(self.root, text="Domain Review")
        self.title_label.pack(pady=10)

        self.domain_label = ttk.Label(self.root, text="")
        self.domain_label.pack(pady=10)

        self.frame_label = ttk.Label(self.root, text="Click Frame: Left to Accept, Right to Reject", font=("Helvetica", 12))
        self.frame_label.pack(pady=10)

        self.confirm_frame = ttk.Frame(self.root, width=150, height=150)
        self.confirm_frame['borderwidth'] = 2
        self.confirm_frame['relief'] = "groove"
        self.confirm_frame.bind('<Any-Button>', self.frame_click)
        self.confirm_frame.pack(pady=10)

        self.progress_bar = ttk.Progressbar(self.root, length=200, mode='determinate')
        self.progress_bar.pack(pady=10)

        self.progress_label = ttk.Label(self.root, text="", font=("Helvetica", 16))
        self.progress_label.pack(pady=10)

        self.yes_button = ttk.Button(self.root, text="Shortlist", command=self.shortlist_domain)
        self.yes_button.pack(pady=10)

        self.no_button = ttk.Button(self.root, text="Skip", command=self.next_domain)
        self.no_button.pack(pady=10)

        self.history_button = ttk.Button(self.root, text="History", command=self.show_history)
        self.history_button.pack(pady=10)

        self.quit_button = ttk.Button(self.root, text="Quit", command=self.quit_app)
        self.quit_button.pack(pady=10)

        self.update_ui()

# 🎬 Function Definitions 🎬
    def shortlist_domain(self):
# 👆 Defining a new function to perform specific tasks
        domain = self.domains[self.pointer]
        self.shortlist.append(domain)
        append_to_file(SHORTLIST_FILE, domain)
        self.next_domain()

# 🎬 Function Definitions 🎬
    def next_domain(self):
# 👆 Defining a new function to perform specific tasks
        self.pointer += 1
        if self.pointer >= len(self.domains):
# 👆 Conditional statement to make decisions
            messagebox.showinfo("Info", "All domains have been reviewed.")
            self.quit_app()
        else:
# 👆 Conditional statement to make decisions
            self.update_ui()

# 🎬 Function Definitions 🎬
    def update_ui(self):
# 👆 Defining a new function to perform specific tasks
        domain = self.domains[self.pointer]
        self.domain_label['text'] = "Domain: " + domain
        self.progress_bar['value'] = (self.pointer / len(self.domains)) * 100
        self.progress_label['text'] = f"Processed: {self.pointer} | Remaining: {len(self.domains) - self.pointer}\nShortlisted: {len(self.shortlist)} | Rejected: {len(self.rejected)}"

# 🎬 Function Definitions 🎬
    def frame_click(self, event):
# 👆 Defining a new function to perform specific tasks
        if event.num == 1:
# 👆 Conditional statement to make decisions
            self.shortlist_domain()
        elif event.num == 3:
# 👆 Conditional statement to make decisions
            self.reject_domain()
        elif event.num == 2:
# 👆 Conditional statement to make decisions
            self.rewind_domain()

# 🎬 Function Definitions 🎬
    def reject_domain(self):
# 👆 Defining a new function to perform specific tasks
        domain = self.domains[self.pointer]
        self.rejected.append(domain)
        append_to_file(REJECT_FILE, domain)
        self.next_domain()

# 🎬 Function Definitions 🎬
    def rewind_domain(self):
# 👆 Defining a new function to perform specific tasks
        if self.pointer > 0:
# 👆 Conditional statement to make decisions
            self.pointer -= 1
            if self.domains[self.pointer] in self.shortlist:
# 👆 Conditional statement to make decisions
                self.shortlist.remove(self.domains[self.pointer])
            elif self.domains[self.pointer] in self.rejected:
# 👆 Conditional statement to make decisions
                self.rejected.remove(self.domains[self.pointer])
            self.update_ui()

# 🎬 Function Definitions 🎬
    def show_history(self):
# 👆 Defining a new function to perform specific tasks
        messagebox.showinfo("History", f"Shortlisted:\n{', '.join(self.shortlist)}\n\nRejected:\n{', '.join(self.rejected)}")

# 🎬 Function Definitions 🎬
    def quit_app(self):
# 👆 Defining a new function to perform specific tasks
        self.session['pointer'] = self.pointer
        self.session['shortlist'] = self.shortlist
        self.session['rejected'] = self.rejected
        save_session(self.session)

        self.root.quit()

if __name__ == "__main__":
# 👆 Conditional statement to make decisions
    root = tk.Tk()
    app = App(root)
    root.mainloop()
