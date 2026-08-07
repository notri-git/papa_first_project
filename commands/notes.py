import json

FILE = "storage/notes.json"


def load_notes():
    with open(FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_notes(notes):
    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)


def add_note(text):
    notes = load_notes()

    if notes:
        new_id = max(note["id"] for note in notes) + 1
    else:
        new_id = 1

    notes.append({
        "id": new_id,
        "text": text
    })

    save_notes(notes)
    print("Заметка создана. ID:", new_id)


def show_notes():
    notes = load_notes()

    if not notes:
        print("Заметок нет")
        return

    for note in notes:
        print(note["id"], "-", note["text"])


def show_note(note_id):
    notes = load_notes()

    for note in notes:
        if note["id"] == note_id:
            print(note["id"], "-", note["text"])
            return

    print("Заметка не найдена")


def delete_note(note_id):
    notes = load_notes()

    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка удалена")
            return

    print("Заметка не найдена")


def search_notes(text):
    notes = load_notes()

    found = False

    for note in notes:
        if text.lower() in note["text"].lower():
            print(note["id"], "-", note["text"])
            found = True

    if not found:
        print("Ничего не найдено")