class Bully:
    def __init__(self, max_processes):
        self.max_processes = max_processes
        self.processes = [True] * max_processes
        self.coordinator = max_processes
        print("Creating processes..")
        for i in range(max_processes):
            print(f"P{i + 1} created")
        print(f"Process P{self.coordinator} is the coordinator")

    def display_processes(self):
        for i, status in enumerate(self.processes):
            print(f"P{i + 1} is {'up' if status else 'down'}")
        print(f"Process P{self.coordinator} is the coordinator")

    def up_process(self, process_id):
        if not self.processes[process_id - 1]:
            self.processes[process_id - 1] = True
            print(f"Process {process_id} is now up.")
        else:
            print(f"Process {process_id} is already up.")

    def down_process(self, process_id):
        if not self.processes[process_id - 1]:
            print(f"Process {process_id} is already down.")
        else:
            self.processes[process_id - 1] = False
            print(f"Process {process_id} is down.")

    def run_election(self, process_id):
        self.coordinator = process_id
        keep_going = True
        for i in range(process_id, self.max_processes):
            print(f"Election message sent from process {process_id} to process {i + 1}")
            if self.processes[i]:
                keep_going = False
                self.run_election(i + 1)
        self.display_processes()


max_processes = 0
choice = 0

while True:
    print("Bully Algorithm")
    print("1. Create processes")
    print("2. Display processes")
    print("3. Up a process")
    print("4. Down a process")
    print("5. Run election algorithm")
    print("6. Exit Program")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        max_processes = int(input("Enter the number of processes: "))
        bully = Bully(max_processes)
    elif choice == 2:
        bully.display_processes()
    elif choice == 3:
        process_id = int(input("Enter the process number to up: "))
        bully.up_process(process_id)
    elif choice == 4:
        process_id = int(input("Enter the process number to down: "))
        bully.down_process(process_id)
    elif choice == 5:
        process_id = int(input("Enter the process number to perform election: "))
        bully.run_election(process_id)
    elif choice == 6:
        break
    else:
        print("Error in choice. Please try again.")
