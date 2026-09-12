# YYC Daycare Management System

A command-line application for managing child enrollment and daily attendance at a daycare facility. Built with Python using object-oriented programming principles.

## Features

- **Child Registration** — Add and remove child records with ID, age group, and daily fee
- **Check-In / Check-Out** — Track attendance by recording the guardian name at drop-off and clearing it at pick-up
- **Attendance Summary** — View all children with a breakdown of checked-in vs. not checked-in counts
- **CSV Persistence** — Data is loaded from and saved to `child.csv` on startup and exit

## Project Structure

```
├── child.py          # Child class with encapsulated attributes and attendance methods
├── management.py     # Main application: menu system, CRUD operations, file I/O
├── test_child.py     # Driver program testing Child class methods (getters, setters, check-in/out)
├── child.csv         # Data file storing child records
└── Test Plan/        # Screenshots documenting test cases
```

## Usage

```bash
python management.py
```

Navigate the menu to add/remove children, check in/out, or view records. Data is automatically saved on exit.

## Age Groups & Validation

| Age Group   | Accepted Values   |
|-------------|-------------------|
| Toddler     | `Toddler`         |
| Preschool   | `Preschool`       |
| School Age  | `School Age`      |

- Child IDs are case-insensitive and must be unique
- Daily fee must be greater than 0
- Guardian name is required for check-in

## Built With

- Python 3.10+ (uses `match`/`case` syntax)
