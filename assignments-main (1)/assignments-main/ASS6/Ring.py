class Ring:
    def __init__(self, max_processes):
        self.max_processes = max_processes
        self.coordinator = max_processes
        self.processes = [True] * max_processes
        self.pid = []
        for i in range(max_processes):
            print(f"P{i + 1} created.")
        print(f"P{self.coordinator} is the coordinator")

    def display_processes(self):
        for i in range(self.max_processes):
            if self.processes[i]:
                print(f"P{i + 1} is up.")
            else:
                print(f"P{i + 1} is down.")
        print(f"P{self.coordinator} is the coordinator")

    def up_process(self, process_id):
        if not self.processes[process_id - 1]:
            self.processes[process_id - 1] = True
            print(f"Process P{process_id} is up.")
        else:
            print(f"Process P{process_id} is already up.")

    def down_process(self, process_id):
        if not self.processes[process_id - 1]:
            print(f"Process P{process_id} is already down.")
        else:
            self.processes[process_id - 1] = False
            print(f"Process P{process_id} is down.")

    def display_array_list(self, pid):
        print("[", end=" ")
        for x in pid:
            print(x, end=" ")
        print("]")

    def init_election(self, process_id):
        if self.processes[process_id - 1]:
            self.pid.append(process_id)

            temp = process_id

            print(f"Process P{process_id} sending the following list:- ", end="")
            self.display_array_list(self.pid)

            while temp != process_id - 1:
                if self.processes[temp]:
                    self.pid.append(temp + 1)
                    print(f"Process P{temp + 1} sending the following list:- ", end="")
                    self.display_array_list(self.pid)
                temp = (temp + 1) % self.max_processes

            self.coordinator = max(self.pid)
            print(f"Process P{process_id} has declared P{self.coordinator} as the coordinator")
            self.pid.clear()

def main():
    ring = None
    max_processes = 0
    process_id = 0

    while True:
        print("Ring Algorithm")
        print("1. Create processes")
        print("2. Display processes")
        print("3. Up a process")
        print("4. Down a process")
        print("5. Run election algorithm")
        print("6. Exit Program")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            max_processes = int(input("Enter the total number of processes: "))
            ring = Ring(max_processes)
        elif choice == 2:
            ring.display_processes()
        elif choice == 3:
            process_id = int(input("Enter the process to up: "))
            ring.up_process(process_id)
        elif choice == 4:
            process_id = int(input("Enter the process to down: "))
            ring.down_process(process_id)
        elif choice == 5:
            process_id = int(input("Enter the process which will initiate election: "))
            ring.init_election(process_id)
        elif choice == 6:
            exit(0)
        else:
            print("Error in choice. Please try again.")

if __name__ == "__main__":
    main()
