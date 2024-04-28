import customtkinter as ctk

class TaxCalculator:
    def __init__(self):
        #initialize the window
        self.window = ctk.CTk() #create main application window instance
        self.window.title('Tax Calculator')
        self.window.geometry('380x300') #width x height of the window
        self.window.resizable(False, False)

        #widget padding
        self.padding: dict = {'padx': 20, 'pady':10}
        #dictionary used to specify the padding values for arranging widgets in the GUI layout.

        #income label and entry
        self.income_label = ctk.CTkLabel(self.window, text='Income')
        #positioning the income_label using grid layout manager w.r.t. parent container
        # **self.padding - unpacking the self.padding
        self.income_label.grid(row=0, column=0, **self.padding)

        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(row=0, column=1, **self.padding)

        #Tax label and entry
        self.tax_rate_label = ctk.CTkLabel(self.window, text='Percent')
        self.tax_rate_label.grid(row=1, column=0, **self.padding)
        self.tax_rate_entry = ctk.CTkEntry(self.window)
        self.tax_rate_entry.grid(row=1, column=1, **self.padding)

        #Result label and entry
        self.result_label = ctk.CTkLabel(self.window, text = 'Tax')
        self.result_label.grid(row=2, column=0, **self.padding)
        self.result_entry = ctk.CTkEntry(self.window)
        #setting default value for the tax entry
        self.result_entry.insert(0, '0')
        self.result_entry.grid(row=2, column=1, **self.padding)

        #calculate button
        self.calculate_button = ctk.CTkButton(self.window, text = 'Calculate', command = self.calculate_tax)
        self.calculate_button.grid(row = 3, column=1, **self.padding)

    def update_result(self, text: str):
        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, text)

    def calculate_tax(self):
        """Calcualte total tax based on income and percent"""
        try:
            # fetching the current text/value the user has entered
            income: float = float(self.income_entry.get())
            tax_rate: float = float(self.tax_rate_entry.get())
            self.update_result(f'💶{income * (tax_rate / 100):,.2f}')
        except ValueError:
            self.update_result('Invalid input')



    def run(self):
        #run the tkinter app
        self.window.mainloop()


if __name__ == '__main__':
    tc = TaxCalculator()
    tc.run()