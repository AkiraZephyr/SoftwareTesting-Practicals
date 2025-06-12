# Python Program that demonstrates CASE tool functionality by automating defect trackng and reporting using dictionary-based data storage

class DefectTracker:
    def __init__(self):
        self.defect_database = {}
        self.defect_id_counter = 1

    def add_defect(self, title, description, severity):
        self.defect_database[self.defect_id_counter] = {
            "Title": title,
            "Description": description,
            "Severity": severity,
            "Status": "Open"
        }
        print(f"Defect {self.defect_id_counter} added successfully!")
        self.defect_id_counter += 1

    def view_defects(self):
        if not self.defect_database:
            print("\nNo defects recorded yet.")
            return
        print("\nCurrent Defect List:")
        for defect_id, details in self.defect_database.items():
            print(
                f"ID: {defect_id} | Title: {details['Title']} | "
                f"Severity: {details['Severity']} | Status: {details['Status']}"
            )

    def close_defect(self, defect_id):
        if defect_id in self.defect_database:
            self.defect_database[defect_id]["Status"] = "Closed"
            print(f"Defect {defect_id} has been closed.")
        else:
            print("Invalid Defect ID!")

    def generate_report(self):
        total = len(self.defect_database)
        open_defects = sum(1 for d in self.defect_database.values() if d["Status"] == "Open")
        closed_defects = total - open_defects
        print("\n--- Defect Report ---")
        print(f"Total Defects: {total}")
        print(f"Open Defects: {open_defects}")
        print(f"Closed Defects: {closed_defects}")

def main():
    tracker = DefectTracker()
    menu = (
        "\n--- Defect Tracking System ---\n"
        "1. Add Defect\n"
        "2. View Defects\n"
        "3. Close Defect\n"
        "4. Generate Report\n"
        "5. Exit\n"
    )
    while True:
        print(menu)
        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            title = input("Enter defect title: ")
            description = input("Enter defect description: ")
            severity = input("Enter severity (Low/Medium/High): ")
            tracker.add_defect(title, description, severity)
        elif choice == '2':
            tracker.view_defects()
        elif choice == '3':
            try:
                defect_id = int(input("Enter Defect ID to close: "))
                tracker.close_defect(defect_id)
            except ValueError:
                print("Invalid input! Please enter a numeric Defect ID.")
        elif choice == '4':
            tracker.generate_report()
        elif choice == '5':
            print("Exiting Defect Tracking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 to 5.")

if __name__ == "__main__":
    main()
