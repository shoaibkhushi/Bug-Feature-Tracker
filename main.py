import pandas as pd
entries = []
def add_entry():
    title = input("Enter title: ").strip()

    if not title:
        print("Error: Title cannot be empty.")
        return

    entry_type = input("Type (Bug/Feature): ").strip().title()

    if entry_type not in ["Bug", "Feature"]:
        print("Invalid type. Choose Bug or Feature.")
        return
    
    priority = input("Priority (Low/Medium/High): ").strip().title()

    if priority not in ["Low", "Medium", "High"]:
        print("Invalid priority.")
        return
    status = input("Status (Open/Resolved): ").strip().title()
    if status not in ["Open", "Resolved"]:
        print("Invalid status.")
        return
    entry = {
        "title": title,
        "type": entry_type,
        "priority": priority,
        "status": status
    }

    entries.append(entry)
    print("Entry added successfully!")

def view_entries():
    if not entries:
        print("No entries found.")
        return

    for number, entry in enumerate(entries, start=1):
        print(f"\nEntry {number}")
        print("Title:", entry["title"])
        print("Type:", entry["type"])
        print("Priority:", entry["priority"])
        print("Status:", entry["status"])


def show_statistics():
    total = len(entries)
    bugs = sum(e["type"] == "Bug" for e in entries)
    features = sum(e["type"] == "Feature" for e in entries)
    open_entries = sum(e["status"] == "Open" for e in entries)
    resolved = sum(e["status"] == "Resolved" for e in entries)
    print("="*60)
    print("\n===== TRACKER STATISTICS =====")
    print("Total entries:", total)
    print("Bugs:", bugs)
    print("Feature requests:", features)
    print("Open entries:", open_entries)
    print("Resolved entries:", resolved)
    print("="*60)
def main():
    while True:
        print("\n===== BUG & FEATURE TRACKER =====")
        print("1. Add Entry")
        print("2. View All Entries")
        print("3. Display Statistics")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            show_statistics()
        elif choice == "4":
            print("Thank you for using the tracker!")
            break
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
