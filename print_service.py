import datetime

class PrintJobNode:
    def __init__(self, job_id, document_name):
        self.job_id = job_id
        self.document_name = document_name
        self.time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.next = None  

class PrintQueue:
    def __init__(self):
        self.front = None  
        self.rear = None   

    def enqueue_job(self, job_id, document_name):
        new_node = PrintJobNode(job_id, document_name)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Çap tapşırığı növbəyə əlavə olundu: {document_name}")

    def dequeue_job(self):
        if not self.front:
            print("Növbə boşdur, çap ediləcək sənəd yoxdur.")
            return
        removed = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        print(f"Çap edildi (Dequeue): {removed.document_name}")

    def peek_next_job(self):
        if not self.front:
            print("Növbə boşdur.")
            return
        print(f"Növbədə gözləyən ilk sənəd -> ID: {self.front.job_id} | Ad: {self.front.document_name} | Vaxt: {self.front.time}")

    def display_queue(self):
        if not self.front:
            print("Çap növbəsi boşdur.")
            return
        print("\n--- PRINT QUEUE ---")
        print("FRONT (İlk çap olunacaq) --------> REAR (Ən son əlavə olunan)")
        current = self.front
        while current:
            print(f"[ID: {current.job_id} - {current.document_name}]", end=" -> ")
            current = current.next
        print("None\n" + "-" * 40)

    def count_jobs(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        print(f"Növbədə cəmi {count} çap tapşırığı var.")
        return count


if __name__ == "__main__":
    print_queue = PrintQueue()
    
    while True:
        print("\n--- Print Service Menyu (Queue) ---")
        print("1. Add Print Job (Enqueue)")
        print("2. Process Print Job (Dequeue)")
        print("3. View Next Job (Peek)")
        print("4. Display Queue")
        print("5. Count Jobs")
        print("6. Exit")
        
        choice = input("Seçiminizi daxil edin (1-6): ")
        
        if choice == "1":
            j_id = int(input("Job ID: "))
            j_name = input("Document Name (məsələn, lab_report.pdf): ")
            print_queue.enqueue_job(j_id, j_name)
        elif choice == "2":
            print_queue.dequeue_job()
        elif choice == "3":
            print_queue.peek_next_job()
        elif choice == "4":
            print_queue.display_queue()
        elif choice == "5":
            print_queue.count_jobs()
        elif choice == "6":
            print("Proqramdan çıxılır...")
            break
        else:
            print("Yanlış seçim, yenidən sınayın.")