import json

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

	def save_file(self):
		with open('data/tasks.json', 'w')as json_file: #saving data
				json.dump(self.tasks, json_file, indent = 1)
				
	def add_tasks(self):#adding of new tasks
		name = input("Enter task name: ")
		due_date = input("YYYY-MM-DD: ")
		priority = input("priority (High/Medium/Low): ")
		self.view_tasks()
		new_task = {
			"new_name" : "name",
			"new_due_date" : "due_date",
			"new_priority" : "priority",
			"Done": "False"
		}
		self.tasks["tasks"].append(new_task)
		print("Task added")

	def view_tasks(self, priority=None, due_date=None):
		if not self.tasks["tasks"]:
			print("No task added yet.")
		else:
			print("Tasks:")
		filtered = self.tasks["tasks"]

		if priority:
			filtered = [task for task in filtered if task.get('priority') == priority]
		
		if due_date:
			filtered = [task for task in filtered if task.get('due_date') == due_date]
		
		if not filtered:
			print("No matching found.")
		else:
			for i, task in enumerate(filtered, start = 1):
				print(f"{i}. {task}")

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