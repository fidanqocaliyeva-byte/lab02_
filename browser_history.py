import datetime

class ActionNode:
    def __init__(self, action_id, action_name):
        self.action_id = action_id
        self.action_name = action_name
        self.time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.next = None  

class UndoStack:
    def __init__(self):
        self.top = None  

    def push_action(self, action_id, action_name):
        new_node = ActionNode(action_id, action_name)
        new_node.next = self.top
        self.top = new_node
        print(f"Əməliyyat əlavə olundu (Push): {action_name}")

    def undo_action(self):
        if not self.top:
            print("Stack boşdur, geri alınacaq (Undo) əməliyyat yoxdur.")
            return
        removed = self.top
        self.top = self.top.next
        print(f"Undo edildi (Pop): {removed.action_name}")

    def current_action(self):
        if not self.top:
            print("Cari səhifə yoxdur (Stack boşdur).")
            return
        print(f"Cari səhifə -> ID: {self.top.action_id} | Ad: {self.top.action_name} | Vaxt: {self.top.time}")

    def display_history(self):
        if not self.top:
            print("Tarixçə boşdur.")
            return
        print("\n--- BROWSER HISTORY (STACK) ---")
        print("TOP (Ən son edilən əməliyyat)")
        current = self.top
        while current:
            print(f"-> [ID: {current.action_id}] {current.action_name} ({current.time})")
            current = current.next
        print("-" * 35)

    def count_actions(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        print(f"Stack-də cəmi {count} əməliyyat var.")
        return count


if __name__ == "__main__":
    history_stack = UndoStack()
    
    while True:
        print("\n--- Browser History Menyu (Stack) ---")
        print("1. Perform Action (Push)")
        print("2. Undo Action (Pop)")
        print("3. View Current Action")
        print("4. Display Full History")
        print("5. Count Actions")
        print("6. Exit")
        
        choice = input("Seçiminizi daxil edin (1-6): ")
        
        if choice == "1":
            a_id = int(input("Action ID: "))
            a_name = input("Action Name / URL (məsələn, google.com): ")
            history_stack.push_action(a_id, a_name)
        elif choice == "2":
            history_stack.undo_action()
        elif choice == "3":
            history_stack.current_action()
        elif choice == "4":
            history_stack.display_history()
        elif choice == "5":
            history_stack.count_actions()
        elif choice == "6":
            print("Proqramdan çıxılır...")
            break
        else:
            print("Yanlış seçim, yenidən sınayın.")