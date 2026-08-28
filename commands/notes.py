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
    return "Заметка создана. ID: " + str(new_id)


def show_notes():
    notes = load_notes()

    if not notes:
        return "Заметок нет"

    result = ""

    for note in notes:
        result += str(note["id"]) + " - " + note["text"] + "\n"

    return result


def show_note(note_id):
    notes = load_notes()

    for note in notes:
        if note["id"] == note_id:
            return str(note["id"]) + " - " + note["text"]

    return "Заметка не найдена"


def delete_note(note_id):
    notes = load_notes()

    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            return "Заметка удалена"

    return "Заметка не найдена"


def search_notes(text):
    notes = load_notes()

    result = ""

    for note in notes:
        if text.lower() in note["text"].lower():
            result += str(note["id"]) + " - " + note["text"] + "\n"

    if result == "":
        return "Ничего не найдено"

    return result