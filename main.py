import pdfminer
from pdfminer.high_level import extract_text
import pyttsx3
import tkinter as tk
from tkinter import filedialog, messagebox

class PDFTextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Text to Speech")
        
        self.engine = pyttsx3.init()

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # PDF File Label and Browse Button
        self.pdf_label = tk.Label(self.root, text="PDF File:")
        self.pdf_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.pdf_entry = tk.Entry(self.root, width=40)
        self.pdf_entry.grid(row=0, column=1, padx=10, pady=10)

        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=0, column=2, padx=10, pady=10)

        # Page Number Label and Entry
        self.page_label = tk.Label(self.root, text="Start Page Number:")
        self.page_label.grid(row=1, column=0, padx=10, pady=10)
        
        self.page_entry = tk.Entry(self.root, width=10)
        self.page_entry.grid(row=1, column=1, padx=10, pady=10)

        # Page Interval Label and Entry
        self.interval_label = tk.Label(self.root, text="Page Interval:")
        self.interval_label.grid(row=2, column=0, padx=10, pady=10)
        
        self.interval_entry = tk.Entry(self.root, width=10)
        self.interval_entry.grid(row=2, column=1, padx=10, pady=10)

        # Start Button
        self.start_button = tk.Button(self.root, text="Start", command=self.start)
        self.start_button.grid(row=3, column=1, padx=10, pady=10)

    def browse_file(self):
        # Open file dialog to select PDF file
        pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if pdf_path:
            self.pdf_entry.delete(0, tk.END)
            self.pdf_entry.insert(0, pdf_path)

    def extract_text_from_pdf(self, pdf_path, page_number):
        # Open the PDF file
        with open(pdf_path, 'rb') as f:
            # Extract text from the specified page number (page_number-1 because pages are zero-indexed in pdfminer)
            text = extract_text(f, page_numbers=[page_number - 1])
        return text

    def text_to_speech(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def start(self):
        pdf_path = self.pdf_entry.get()
        try:
            start_page = int(self.page_entry.get())
            page_interval = int(self.interval_entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers for the page number and interval.")
            return

        if not pdf_path:
            messagebox.showerror("No file selected", "Please select a PDF file.")
            return

        current_page = start_page
        while True:
            for _ in range(page_interval):
                text = self.extract_text_from_pdf(pdf_path, current_page)
                if not text:
                    messagebox.showinfo("End of Document", f"No more text found after page {current_page}.")
                    return
                self.text_to_speech(text)
                current_page += 1

            next_page = messagebox.askyesno("Continue?", f"Do you want to continue to the next set of pages starting from page {current_page}?")
            if not next_page:
                break

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFTextToSpeechApp(root)
    root.mainloop()
