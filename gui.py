import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import pickle
from predict import predict_review
from utils import clean_text

class ReviewPredictorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Amazon Review Sentiment Analyzer")
        self.root.geometry("600x400")
        self.root.configure(bg='#f0f0f0')
        
        # Title
        title_label = tk.Label(root, text="Amazon Review Sentiment Analyzer", 
                              font=("Arial", 16, "bold"), bg='#f0f0f0', fg='#FF9900')
        title_label.pack(pady=10)
        
        # Frame for input
        input_frame = tk.Frame(root, bg='#f0f0f0')
        input_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=False)
        
        # Label for review input
        label = tk.Label(input_frame, text="Enter Your Review:", font=("Arial", 10, "bold"), bg='#f0f0f0')
        label.pack(anchor=tk.W)
        
        # Text input area
        self.review_text = scrolledtext.ScrolledText(input_frame, height=8, width=70, 
                                                      font=("Arial", 10), wrap=tk.WORD)
        self.review_text.pack(pady=5, fill=tk.BOTH, expand=True)
        
        # Button frame
        button_frame = tk.Frame(root, bg='#f0f0f0')
        button_frame.pack(pady=10)
        
        # Predict button
        predict_btn = tk.Button(button_frame, text="Predict Sentiment", 
                               command=self.predict, font=("Arial", 11, "bold"),
                               bg='#FF9900', fg='white', padx=20, pady=10, cursor="hand2")
        predict_btn.pack(side=tk.LEFT, padx=5)
        
        # Clear button
        clear_btn = tk.Button(button_frame, text="Clear", 
                             command=self.clear, font=("Arial", 11, "bold"),
                             bg='#555555', fg='white', padx=20, pady=10, cursor="hand2")
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Result frame
        result_frame = tk.LabelFrame(root, text="Prediction Result", font=("Arial", 11, "bold"),
                                     bg='#f0f0f0', fg='#333333', relief=tk.SUNKEN, borderwidth=2)
        result_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=False)
        
        # Result label
        self.result_label = tk.Label(result_frame, text="", font=("Arial", 14, "bold"),
                                     bg='#f0f0f0', fg='#333333')
        self.result_label.pack(pady=20)
        
        # Status bar
        self.status_label = tk.Label(root, text="Ready", font=("Arial", 9),
                                     bg='#e0e0e0', fg='#666666', relief=tk.SUNKEN)
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)
    
    def predict(self):
        review = self.review_text.get("1.0", tk.END).strip()
        
        if not review:
            messagebox.showwarning("Warning", "Please enter a review!")
            return
        
        try:
            self.status_label.config(text="Processing...", fg='#FF9900')
            self.root.update()
            
            prediction = predict_review(review)
            
            # Display result with color and emoji
            if prediction == "Positive":
                sentiment = "POSITIVE ✓"
                color = '#28a745'  # Green
                emoji = "😊"
            else:
                sentiment = "NEGATIVE ✗"
                color = '#dc3545'  # Red
                emoji = "😞"
            
            result_text = f"{emoji} {sentiment}"
            self.result_label.config(text=result_text, fg=color)
            self.status_label.config(text="Prediction complete!", fg='#28a745')
            
        except Exception as e:
            messagebox.showerror("Error", f"Prediction failed: {str(e)}")
            self.status_label.config(text=f"Error: {str(e)}", fg='#dc3545')
    
    def clear(self):
        self.review_text.delete("1.0", tk.END)
        self.result_label.config(text="")
        self.status_label.config(text="Ready", fg='#666666')

if __name__ == "__main__":
    root = tk.Tk()
    app = ReviewPredictorGUI(root)
    root.mainloop()
