import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        #self.root.configure(bg="white")

        # Initializing empty list to store contacts
        self.contacts = []

        # Create components for UI input fields
        self.title_label = tk.Label(root, text="Contact Book", font=("Helvetica", 16, "bold"))
        self.description_label = tk.Label(root, text="It helps you store your personal details.", font=("Helvetica", 10, "bold"))
        self.name_label = tk.Label(root, text="Name:")
        self.name_entry = tk.Entry(root)
        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_entry = tk.Entry(root)
        self.email_label = tk.Label(root, text="Email:")
        self.email_entry = tk.Entry(root)
        self.address_label = tk.Label(root, text="Address:")
        self.address_entry = tk.Entry(root)

        #components from the method defined
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.search_label = tk.Label(root, text="Search:")
        self.search_entry = tk.Entry(root)
        self.search_button = tk.Button(root, text="Search", command=self.search_contacts)
        self.update_button = tk.Button(root, text="Update", command=self.update_contact)
        self.delete_button = tk.Button(root, text="Delete", command=self.delete_contact)

		#listbox that allows one item to be selected at a time
        self.view_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.view_listbox.grid(row=12, column=0, columnspan=3, pady=10)
        
        # Components in the grid in order of appearance
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)
        self.description_label.grid(row=1, column=0, columnspan=2, pady=10)
        self.name_label.grid(row=2, column=0, sticky=tk.W)
        self.name_entry.grid(row=2, column=1)
        self.phone_label.grid(row=3, column=0, sticky=tk.W)
        self.phone_entry.grid(row=3, column=1)
        self.email_label.grid(row=4, column=0, sticky=tk.W)
        self.email_entry.grid(row=4, column=1)
        self.address_label.grid(row=5, column=0, sticky=tk.W)
        self.address_entry.grid(row=5, column=1)

        self.add_button.grid(row=6, column=0, columnspan=2, pady=10)
        self.view_button.grid(row=7, column=0, columnspan=2, pady=10)
        self.search_label.grid(row=8, column=0, sticky=tk.W)
        self.search_entry.grid(row=8, column=1)
        self.search_button.grid(row=9, column=0, columnspan=2, pady=10)
        self.update_button.grid(row=10, column=0, columnspan=2, pady=10)
        self.delete_button.grid(row=11, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email= self.email_entry.get()
        address = self.address_entry.get()

        if name and phone and email and address:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Please enter both fields.")

    def view_contacts(self):
        self.view_listbox.delete(0, tk.END)
        if not self.contacts:
            messagebox.showinfo("No contacts to display.")
            return

        contact_list = "\n".join(f"{x+1}. {contact['Name']}, {contact['Phone']}, {contact['Email']}, {contact['Address']}" for x, contact in enumerate(self.contacts))
        messagebox.showinfo("Contacts", contact_list)

    def search_contacts(self):
        search_term = self.search_entry.get().lower()
        matching_contacts = [contact for contact in self.contacts if search_term in contact['Name'].lower() or search_term in contact['Phone'].lower()]

        if matching_contacts:
            contact_list = "\n".join(f"{x+1}. {contact['Name']}, {contact['Phone']}" for x, contact in enumerate(matching_contacts))
            messagebox.showinfo("Matching Contacts", contact_list)
        else:
            messagebox.showinfo("No contacts match the searched.")
    #method for updating contact_book 
    def update_contact(self):
        selected_index = self.get_selected_index()#updating based on index selected by the user
        if selected_index is not None:
            updated_name = self.name_entry.get()
            updated_phone = self.phone_entry.get()
            updated_email = self.email_entry.get()
            updated_address = self.address_entry.get()
            if updated_name and updated_phone and updated_email and updated_address:
                   self.contacts[selected_index]['Name'] = updated_name
                   self.contacts[selected_index]['Phone'] = updated_phone
                   self.contacts[selected_index]['Email'] = updated_email
                   self.contacts[selected_index]['Address'] = updated_address
                   messagebox.showinfo("Success", "Contact updated successfully!")
                   self.view_contacts() #show updated list
                   self.clear_entries()
            else:
                messagebox.showerror("Kindly enter all fields.")
        else:
            messagebox.showerror("Select a contact to update.")

    def delete_contact(self):
        selected_index = self.get_selected_index()
        if selected_index is not None:
            del self.contacts[selected_index]
            messagebox.showinfo("Successfully deleted contact!")
            self.view_contacts()
            self.clear_entries()
        else:
            messagebox.showerror("Select a contact to delete.")
    #method for clearing the input fields
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)


    def get_selected_index(self):
        try:
            selected_index = int(self.view_listbox.curselection()[0])
            return selected_index
        except IndexError:
            return None

# Create the main window
root = tk.Tk()
app = ContactBookApp(root)

# Run the Tkinter event loop
root.mainloop()