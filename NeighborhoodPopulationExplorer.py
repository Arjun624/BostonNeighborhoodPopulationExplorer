import json
import tkinter as tk

# Load the JSON data
with open('BostonNeighborhoodData(1950-2000).json') as f:
    data = json.load(f)

# Define the categories and groups
categories = ['Total', 'Age', 'Race', 'Education']
age_groups = ['0-9', '10-19', '20-34', '35-54', '55-64', '65+']
race_groups = ['White', 'Black/African American', 'Hispanic', 'Asian', 'Other']
education_groups = ['Less than High School', 'High School/GED', 'Some College', "Bachelor's Degree"]


# Helper to calculate percent difference
def calculate_percent_difference(population1, population2):
    try:
        return str(round(abs(population1 - population2) / ((population1 + population2) / 2) * 100, 2))
    except ZeroDivisionError:
        if population1 == 0:
            return str(round(abs(0.001 - population2) / ((0.001 + population2) / 2) * 100, 2))
        else:
            return str(round(abs(population1 - 0.001) / ((population1 + 0.001) / 2) * 100, 2))


# Helper to calculate percent change
def calculate_percent_change(population1, population2):
    try:
        return str(round(((population2 - population1) / population1) * 100, 2))
    except ZeroDivisionError:
        return "200.0"


# Main GUI Class
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    # Create labels and dropdowns
    def create_widgets(self):
        # Neighborhood selection
        self.neighborhood_label = tk.Label(self, text="Select neighborhoods:")
        self.neighborhood_label.grid(row=0, column=0, sticky=tk.W)

        self.neighborhood1_var = tk.StringVar(value="Allston")
        self.neighborhood1_dropdown = tk.OptionMenu(self, self.neighborhood1_var, *data.keys())
        self.neighborhood1_dropdown.grid(row=1, column=0)

        self.neighborhood2_var = tk.StringVar(value="Allston")
        self.neighborhood2_dropdown = tk.OptionMenu(self, self.neighborhood2_var, *data.keys())
        self.neighborhood2_dropdown.grid(row=1, column=1)

        # Year selection
        self.year_label = tk.Label(self, text="Select years:")
        self.year_label.grid(row=2, column=0, sticky=tk.W)

        self.year1_var = tk.StringVar(value="1950")
        self.year1_dropdown = tk.OptionMenu(self, self.year1_var, *data[self.neighborhood1_var.get()].keys())
        self.year1_dropdown.grid(row=3, column=0)

        self.year2_var = tk.StringVar(value="1950")
        self.year2_dropdown = tk.OptionMenu(self, self.year2_var, *data[self.neighborhood2_var.get()].keys())
        self.year2_dropdown.grid(row=3, column=1)

        # Category selection
        self.category_label = tk.Label(self, text="Select category:")
        self.category_label.grid(row=4, column=0, sticky=tk.W)

        self.category_var1 = tk.StringVar(value="Total")
        self.category_dropdown1 = tk.OptionMenu(self, self.category_var1, *categories, command=self.update_group1)
        self.category_dropdown1.grid(row=5, column=0)

        self.category_var2 = tk.StringVar(value="Total")
        self.category_dropdown2 = tk.OptionMenu(self, self.category_var2, *categories, command=self.update_group2)
        self.category_dropdown2.grid(row=5, column=1)

        # Group selection
        self.group_label = tk.Label(self, text="Select group:")
        self.group_label.grid(row=6, column=0, sticky=tk.W)

        self.group_var1 = tk.StringVar()
        self.group_dropdown1 = tk.OptionMenu(self, self.group_var1, *age_groups)
        self.group_dropdown1.configure(state="disabled")
        self.group_dropdown1.grid(row=7, column=0)

        self.group_var2 = tk.StringVar()
        self.group_dropdown2 = tk.OptionMenu(self, self.group_var2, *age_groups)
        self.group_dropdown2.configure(state="disabled")
        self.group_dropdown2.grid(row=7, column=1)

        # Submit button
        self.submit_button = tk.Button(self, text="Show Stats", command=self.display_data)
        self.submit_button.grid(row=8, column=0, columnspan=2)

        # Output labels
        self.neighborhood1_output_label = tk.Label(self, text="")
        self.neighborhood1_output_label.grid(row=9, column=0, columnspan=2)

        self.neighborhood2_output_label = tk.Label(self, text="")
        self.neighborhood2_output_label.grid(row=10, column=0, columnspan=2)

        # Difference info label
        self.difference_label = tk.Label(self, text="")
        self.difference_label.grid(row=11, column=0, columnspan=2)

        # Percent change label
        self.change_label = tk.Label(self, text="")
        self.change_label.grid(row=12, column=0, columnspan=2)

    # Update dropdown group 1 after category is picked
    def update_group1(self, category):
        # Clear previous group options
        self.group_dropdown1['menu'].delete(0, 'end')
        self.group_dropdown1.configure(state="normal")

        # Update group options based on selected category
        if category == 'Age':
            for group in age_groups:
                self.group_dropdown1['menu'].add_command(label=group, command=tk._setit(self.group_var1, group))
            self.group_var1.set(age_groups[0])
        elif category == 'Race':
            for group in race_groups:
                self.group_dropdown1['menu'].add_command(label=group, command=tk._setit(self.group_var1, group))
            self.group_var1.set(race_groups[0])
        elif category == 'Education':
            for group in education_groups:
                self.group_dropdown1['menu'].add_command(label=group, command=tk._setit(self.group_var1, group))
            self.group_var1.set(education_groups[0])
        elif category == 'Total':
            self.group_dropdown1.configure(state="disabled")
            self.group_var1.set(None)

    # Update dropdown group 2 after category is picked
    def update_group2(self, category):
        # Clear previous group options
        self.group_dropdown2['menu'].delete(0, 'end')
        self.group_dropdown2.configure(state="normal")

        # Update group options based on selected category
        if category == 'Age':
            for group in age_groups:
                self.group_dropdown2['menu'].add_command(label=group, command=tk._setit(self.group_var2, group))
            self.group_var2.set(age_groups[0])
        elif category == 'Race':
            for group in race_groups:
                self.group_dropdown2['menu'].add_command(label=group, command=tk._setit(self.group_var2, group))
            self.group_var2.set(race_groups[0])
        elif category == 'Education':
            for group in education_groups:
                self.group_dropdown2['menu'].add_command(label=group, command=tk._setit(self.group_var2, group))
            self.group_var2.set(education_groups[0])
        elif category == 'Total':
            self.group_dropdown2.configure(state="disabled")
            self.group_var2.set(None)

    # Display the data on the GUI
    def display_data(self):
        # Get selected options
        neighborhood1 = self.neighborhood1_var.get()
        neighborhood2 = self.neighborhood2_var.get()
        year1 = self.year1_var.get()
        year2 = self.year2_var.get()
        category1 = self.category_var1.get()
        category2 = self.category_var2.get()
        group1 = self.group_var1.get()
        group2 = self.group_var2.get()

        # Check for total population (No Group) and get data accordingly
        if category1 == "Total" and category2 == "Total":
            data1 = data[neighborhood1][year1][category1]
            data2 = data[neighborhood2][year2][category2]
            self.neighborhood1_output_label.config(
                text=f"1) {neighborhood1} in {year1} {category1} Population: {data1}")
            self.neighborhood2_output_label.config(
                text=f"2) {neighborhood2} in {year2} {category2} Population: {data2}")
            self.difference_label.config(
                text=f" Difference is {abs(data1 - data2)} ({calculate_percent_difference(data1, data2)}% difference)")
            self.change_label.config(text=f"Changed by {calculate_percent_change(data1, data2)}%")
        elif category1 == "Total":
            data1 = data[neighborhood1][year1][category1]
            data2 = data[neighborhood2][year2][category2][group2]
            self.neighborhood1_output_label.config(
                text=f"1) {neighborhood1} in {year1} {category1} Population: {data1}")
            self.neighborhood2_output_label.config(text=f"2) {neighborhood2} in {year2} {category2} {group2}: {data2}")
            self.difference_label.config(
                text=f" Difference is {abs(data1 - data2)} ({calculate_percent_difference(data1, data2)}% difference)")
            self.change_label.config(text=f"Changed by {calculate_percent_change(data1, data2)}%")
        elif category2 == "Total":
            data1 = data[neighborhood1][year1][category1][group1]
            data2 = data[neighborhood2][year2][category2]
            self.neighborhood1_output_label.config(text=f"1) {neighborhood1} in {year1} {category1} {group1}: {data1}")
            self.neighborhood2_output_label.config(
                text=f"2) {neighborhood2} in {year2} {category2} Population: {data2}")
            self.difference_label.config(
                text=f" Difference is {abs(data1 - data2)} ({calculate_percent_difference(data1, data2)}% difference)")
            self.change_label.config(text=f"Changed by {calculate_percent_change(data1, data2)}%")
        else:
            data1 = data[neighborhood1][year1][category1][group1]
            data2 = data[neighborhood2][year2][category2][group2]
            self.neighborhood1_output_label.config(text=f"1) {neighborhood1} in {year1} {category1} {group1}: {data1}")
            self.neighborhood2_output_label.config(text=f"2) {neighborhood2} in {year2} {category2} {group2}: {data2}")
            self.difference_label.config(
                text=f" Difference is {abs(data1 - data2)} ({calculate_percent_difference(data1, data2)}% difference)")
            self.change_label.config(text=f"Changed by {calculate_percent_change(data1, data2)}%")


# Start main GUI loop
root = tk.Tk()
root.title("Population Explorer")
app = Application(master=root)
app.mainloop()
