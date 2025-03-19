import random
import os
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

# Irregular verbs: infinitive -> [past simple, past participle]
irregular_verbs = {
    "arise": ["arose", "arisen"],
    "awake": ["awoke", "awoken"],
    "be": ["was/were", "been"],
    "bear": ["bore", "borne"],
    "beat": ["beat", "beaten"],
    "become": ["became", "become"],
    "begin": ["began", "begun"],
    "bend": ["bent", "bent"],
    "bet": ["bet", "bet"],
    "bite": ["bit", "bitten"],
    "blow": ["blew", "blown"],
    "break": ["broke", "broken"],
    "bring": ["brought", "brought"],
    "build": ["built", "built"],
    "buy": ["bought", "bought"],
    "catch": ["caught", "caught"],
    "choose": ["chose", "chosen"],
    "come": ["came", "come"],
    "cost": ["cost", "cost"],
    "cut": ["cut", "cut"],
    "dig": ["dug", "dug"],
    "do": ["did", "done"],
    "draw": ["drew", "drawn"],
    "drink": ["drank", "drunk"],
    "drive": ["drove", "driven"],
    "eat": ["ate", "eaten"],
    "fall": ["fell", "fallen"],
    "feel": ["felt", "felt"],
    "fight": ["fought", "fought"],
    "find": ["found", "found"],
    "fly": ["flew", "flown"],
    "forget": ["forgot", "forgotten"],
    "forgive": ["forgave", "forgiven"],
    "freeze": ["froze", "frozen"],
    "get": ["got", "got/gotten"],
    "give": ["gave", "given"],
    "go": ["went", "gone"],
    "grow": ["grew", "grown"],
    "hang": ["hung", "hung"],
    "have": ["had", "had"],
    "hear": ["heard", "heard"],
    "hide": ["hid", "hidden"],
    "hit": ["hit", "hit"],
    "hold": ["held", "held"],
    "hurt": ["hurt", "hurt"],
    "keep": ["kept", "kept"],
    "know": ["knew", "known"],
    "lead": ["led", "led"],
    "leave": ["left", "left"],
    "lend": ["lent", "lent"],
    "let": ["let", "let"],
    "lie": ["lay", "lain"],
    "lose": ["lost", "lost"],
    "make": ["made", "made"],
    "mean": ["meant", "meant"],
    "meet": ["met", "met"],
    "pay": ["paid", "paid"],
    "put": ["put", "put"],
    "read": ["read", "read"],
    "ride": ["rode", "ridden"],
    "ring": ["rang", "rung"],
    "rise": ["rose", "risen"],
    "run": ["ran", "run"],
    "say": ["said", "said"],
    "see": ["saw", "seen"],
    "sell": ["sold", "sold"],
    "send": ["sent", "sent"],
    "set": ["set", "set"],
    "shake": ["shook", "shaken"],
    "shine": ["shone", "shone"],
    "shoot": ["shot", "shot"],
    "show": ["showed", "shown"],
    "shut": ["shut", "shut"],
    "sing": ["sang", "sung"],
    "sit": ["sat", "sat"],
    "sleep": ["slept", "slept"],
    "speak": ["spoke", "spoken"],
    "spend": ["spent", "spent"],
    "stand": ["stood", "stood"],
    "steal": ["stole", "stolen"],
    "swim": ["swam", "swum"],
    "take": ["took", "taken"],
    "teach": ["taught", "taught"],
    "tear": ["tore", "torn"],
    "tell": ["told", "told"],
    "think": ["thought", "thought"],
    "throw": ["threw", "thrown"],
    "understand": ["understood", "understood"],
    "wake": ["woke", "woken"],
    "wear": ["wore", "worn"],
    "win": ["won", "won"],
    "write": ["wrote", "written"]
}

class IrregularVerbsGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("✨ Irregular Verbs Game ✨")
        self.geometry("600x500")
        self.configure(bg="#F0F0F0")  # Neutral light gray background
        
        self.high_scores = self.load_high_scores()
        self.score = 0
        self.mistakes = []
        self.current_verb = None
        self.current_tense = None
        self.name = ""
        self.training_mode = False
        
        # Set custom fonts and colors
        self.title_font = ("Comic Sans MS", 20, "bold")
        self.normal_font = ("Comic Sans MS", 12)
        self.small_font = ("Comic Sans MS", 10)
        
        self.title_color = "#505050"  # Dark gray for titles
        self.text_color = "#333333"   # Dark gray for text
        self.button_bg = "#D0D0D0"    # Light gray for buttons
        self.button_fg = "#333333"    # Dark gray for button text
        
        # Create frames
        self.create_frames()
        
        # Start with welcome screen
        self.show_welcome_screen()
    
    def create_frames(self):
        # Create all frames for different screens
        self.welcome_frame = tk.Frame(self, bg="#F0F0F0")
        self.game_frame = tk.Frame(self, bg="#F0F0F0")
        self.result_frame = tk.Frame(self, bg="#F0F0F0")
    
    def show_welcome_screen(self):
        # Hide all frames and show welcome frame
        self.welcome_frame.pack(fill="both", expand=True)
        self.game_frame.pack_forget()
        self.result_frame.pack_forget()
        
        # Clear previous widgets
        for widget in self.welcome_frame.winfo_children():
            widget.destroy()
        
        # Create welcome screen widgets
        tk.Label(
            self.welcome_frame, 
            text="✨ Welcome to the\nIrregular Verbs Game! ✨",
            font=self.title_font,
            fg=self.title_color,
            bg="#F0F0F0",
            pady=20
        ).pack()
        
        tk.Label(
            self.welcome_frame,
            text="Enter your name:",
            font=self.normal_font,
            fg=self.text_color,
            bg="#F0F0F0",
            pady=10
        ).pack()
        
        self.name_entry = tk.Entry(
            self.welcome_frame,
            font=self.normal_font,
            width=20,
            bd=3,
            relief=tk.GROOVE
        )
        self.name_entry.pack(pady=10)
        self.name_entry.focus()
        
        # Training mode checkbox
        self.training_var = tk.BooleanVar()
        training_check = tk.Checkbutton(
            self.welcome_frame,
            text="Training Mode (Continue after mistakes)",
            variable=self.training_var,
            font=self.normal_font,
            fg=self.text_color,
            bg="#F0F0F0",
            selectcolor="#E0E0E0"
        )
        training_check.pack(pady=10)
        
        # Start button
        start_button = tk.Button(
            self.welcome_frame,
            text="Start Game! 🎮",
            command=self.start_game,
            font=self.normal_font,
            bg=self.button_bg,
            fg=self.button_fg,
            activebackground="#C0C0C0",
            relief=tk.RAISED,
            bd=3,
            padx=20,
            pady=10
        )
        start_button.pack(pady=20)
        
        # High scores section
        if self.high_scores:
            tk.Label(
                self.welcome_frame,
                text="🏆 High Scores 🏆",
                font=self.normal_font,
                fg=self.title_color,
                bg="#F0F0F0",
                pady=5
            ).pack()
            
            scores_frame = tk.Frame(self.welcome_frame, bg="#F0F0F0")
            scores_frame.pack(pady=10)
            
            # Show top 5 scores
            sorted_scores = sorted(self.high_scores.items(), key=lambda x: x[1], reverse=True)[:5]
            for i, (name, score) in enumerate(sorted_scores):
                tk.Label(
                    scores_frame,
                    text=f"{i+1}. {name}: {score}",
                    font=self.small_font,
                    fg=self.text_color,
                    bg="#F0F0F0"
                ).pack()
    
    def start_game(self):
        self.name = self.name_entry.get().strip()
        if not self.name:
            messagebox.showwarning("Name Required", "Please enter your name!")
            return
        
        self.training_mode = self.training_var.get()
        self.score = 0
        self.mistakes = []
        
        # Switch to game screen
        self.welcome_frame.pack_forget()
        self.game_frame.pack(fill="both", expand=True)
        
        # Clear previous widgets
        for widget in self.game_frame.winfo_children():
            widget.destroy()
        
        # Create game screen widgets
        self.score_label = tk.Label(
            self.game_frame,
            text="Score: 0",
            font=self.normal_font,
            fg=self.text_color,
            bg="#F0F0F0"
        )
        self.score_label.pack(pady=10)
        
        self.question_label = tk.Label(
            self.game_frame,
            text="",
            font=self.normal_font,
            fg=self.text_color,
            bg="#F0F0F0",
            wraplength=500
        )
        self.question_label.pack(pady=20)
        
        self.answer_entry = tk.Entry(
            self.game_frame,
            font=self.normal_font,
            width=20,
            bd=3,
            relief=tk.GROOVE
        )
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind("<Return>", lambda event: self.check_answer())
        
        self.submit_button = tk.Button(
            self.game_frame,
            text="Submit Answer ✓",
            command=self.check_answer,
            font=self.normal_font,
            bg=self.button_bg,
            fg=self.button_fg,
            activebackground="#C0C0C0",
            relief=tk.RAISED,
            bd=3,
            padx=20,
            pady=5
        )
        self.submit_button.pack(pady=10)
        
        # Feedback label
        self.feedback_label = tk.Label(
            self.game_frame,
            text="",
            font=self.normal_font,
            fg=self.text_color,
            bg="#F0F0F0"
        )
        self.feedback_label.pack(pady=10)
        
        # Next button (initially hidden)
        self.next_button = tk.Button(
            self.game_frame,
            text="Next Verb →",
            command=self.next_question,
            font=self.normal_font,
            bg=self.button_bg,
            fg=self.button_fg,
            activebackground="#C0C0C0",
            relief=tk.RAISED,
            bd=3,
            padx=20,
            pady=5
        )
        
        # Present the first question
        self.next_question()
    
    def next_question(self):
        # Hide the next button and feedback
        self.next_button.pack_forget()
        self.feedback_label.config(text="")
        
        # Select a random verb and tense
        self.current_verb = random.choice(list(irregular_verbs.keys()))
        self.current_tense = random.choice(["past", "participle"])
        
        # Update question text
        question_text = f"🔤 What is the {self.current_tense} form of the verb '{self.current_verb}'?"
        self.question_label.config(text=question_text)
        
        # Clear the answer entry and focus
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.focus()
    
    def check_answer(self):
        user_answer = self.answer_entry.get().lower().strip()
        if not user_answer:
            messagebox.showinfo("Empty Answer", "Please enter an answer!")
            return
        
        # Get the correct answer
        correct_answer = irregular_verbs[self.current_verb][0] if self.current_tense == "past" else irregular_verbs[self.current_verb][1]
        
        if user_answer == correct_answer.lower():
            # Correct answer
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.feedback_label.config(text="✅ Correct!", fg="green")
        else:
            # Wrong answer
            self.feedback_label.config(text=f"❌ Incorrect. The correct answer was: {correct_answer}", fg="red")
            self.mistakes.append((self.current_verb, self.current_tense, correct_answer))
            
            if not self.training_mode:
                # End game if not in training mode
                self.after(2000, self.show_results)
                return
        
        # Show next button
        self.next_button.pack(pady=10)
    
    def show_results(self):
        # Switch to results screen
        self.game_frame.pack_forget()
        self.result_frame.pack(fill="both", expand=True)
        
        # Clear previous widgets
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        
        # Create results screen widgets
        tk.Label(
            self.result_frame,
            text="🏁 Game Over 🏁",
            font=self.title_font,
            fg=self.title_color,
            bg="#F0F0F0",
            pady=20
        ).pack()
        
        tk.Label(
            self.result_frame,
            text=f"⭐ Final Score: {self.score}",
            font=self.normal_font,
            fg=self.text_color,
            bg="#F0F0F0"
        ).pack(pady=10)
        
        # Update high score if needed
        best_score = self.high_scores.get(self.name, 0)
        if self.score > best_score:
            tk.Label(
                self.result_frame,
                text=f"🎉 Congratulations, {self.name}!\nYou beat your previous high score of {best_score}!",
                font=self.normal_font,
                fg="green",
                bg="#F0F0F0"
            ).pack(pady=10)
            self.high_scores[self.name] = self.score
            self.save_high_scores(self.high_scores)
        else:
            tk.Label(
                self.result_frame,
                text=f"📈 Your best score is still {best_score}. Keep trying!",
                font=self.normal_font,
                fg=self.text_color,
                bg="#F0F0F0"
            ).pack(pady=10)
        
        # Show mistakes if any
        if self.mistakes:
            tk.Label(
                self.result_frame,
                text="📚 Review your mistakes:",
                font=self.normal_font,
                fg=self.text_color,
                bg="#F0F0F0",
                pady=10
            ).pack()
            
            mistakes_frame = tk.Frame(self.result_frame, bg="#F0F0F0")
            mistakes_frame.pack(pady=5)
            
            for verb, tense, correct in self.mistakes:
                tk.Label(
                    mistakes_frame,
                    text=f"• {verb} ({tense}) ➡️ {correct}",
                    font=self.small_font,
                    fg=self.text_color,
                    bg="#F0F0F0"
                ).pack(anchor="w")
        
        # Play again button
        play_again_button = tk.Button(
            self.result_frame,
            text="Play Again! 🔄",
            command=self.show_welcome_screen,
            font=self.normal_font,
            bg=self.button_bg,
            fg=self.button_fg,
            activebackground="#C0C0C0",
            relief=tk.RAISED,
            bd=3,
            padx=20,
            pady=10
        )
        play_again_button.pack(pady=20)
    
    def load_high_scores(self):
        scores = {}
        if os.path.exists("scores.txt"):
            with open("scores.txt", "r") as file:
                for line in file:
                    if ":" in line:
                        name, score = line.strip().split(":")
                        scores[name.strip()] = int(score.strip())
        return scores
    
    def save_high_scores(self, scores):
        with open("scores.txt", "w") as file:
            for name, score in scores.items():
                file.write(f"{name}: {score}\n")

# Start the application
if __name__ == "__main__":
    app = IrregularVerbsGame()
    app.mainloop()
