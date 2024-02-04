import json
import datetime

class TaskHandler:

	def __init__(self):
		self.tasks = self.load_file()
		

	def load_file(self):
			try:
				with open('data/tasks.json', 'r') as json_file: #reading file and loading as json file
					tasks = json.load(json_file)
				return tasks
			except FileNotFoundError: #no tasks found return empty list
				return {"tasks": []}
			except json.JSONDecodeError:
				return {"tasks": []} 

	def save_file(self):
		with open('data/tasks.json', 'w')as json_file: #saving data
				json.dump(self.tasks, json_file, indent = 1)
				
	def add_task(self):#adding of new tasks
		name = input("Enter task name: ")
		due_date = input("YYYY-MM-DD: ")
		priority = input("priority (High/Medium/Low): ")
		self.view_tasks()
		new_task = {
			"name": name,  # Use the correct key names
			"due_date": due_date,
			"priority": priority,
			"Done": False
		}
		self.tasks["tasks"].append(new_task)
		print("Task added")

	def view_tasks(self, priority=None):
		if not self.tasks["tasks"]:
			print("No tasks added yet.")
		else:
			print("Tasks:")
			filtered = self.tasks["tasks"]
			if priority:
				filtered = [task for task in filtered if task.get('priority') == priority]
			if not filtered:
				print("No tasks found.")
			else:
				for i, task in enumerate(filtered, start=1):
					done_indicator = "✅" if task["Done"] else "❌"
					print(f"{i}. {task['name']} (Due: {task['due_date']}, Priority: {task['priority']}, Done: {done_indicator})")

	
	def update_task(self, index_task):
		if not self.tasks["tasks"]:
			print("No tasks updated yet.")

		elif 1<= index_task <= len(self.tasks['tasks']):
			updated_tasks = self.tasks["tasks"][index_task - 1]

			updated_tasks["name"] = input("Enter new name:")
			updated_tasks["due_date"] = input("New due_date (YYYY-MM-DD)")
			updated_tasks["priority"] = input("Enter new priority (High/Medium/Low)")

			print("Task updated.")
			self.save_file()
		else:
			print("invalid index")

	def mark_task_done(self, index_task):
		if 1 <= index_task <= len(self.tasks["tasks"]):
			self.tasks["tasks"][index_task - 1]["Done"] = True
			print("Task marked as done.")
			self.save_file()
		else:
			print("Invalid index")


	def delete_task(self, index_task):
		if not self.tasks["tasks"]:
			print("No added task.")

		elif 1 <= index_task <= len(self.tasks["tasks"]):
			deleted_task = self.tasks["tasks"].pop(index_task - 1)
			print("f Deleted: {deleted_task}")
			print(f"Deleted task: {deleted_task}")
			self.save_file()  # Save the updated tasks
		else:
			print("Invalid index")