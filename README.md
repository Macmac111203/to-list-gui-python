# To-Do List Application

A modern, minimalist to-do list application built with Python and Tkinter. Features a clean, user-friendly interface with a soft color palette that's easy on the eyes.

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Features

- ✨ **Modern Design**: Clean, minimalist interface with a soft grey color scheme
- 🎨 **Smooth Animations**: Elegant hover effects and color transitions
- ☑️ **Task Management**: Add, complete, and delete tasks with ease
- 💾 **Auto-Save**: Tasks are automatically saved to a local file
- 📋 **Checkbox Completion**: Mark tasks as complete with checkboxes
- 🗑️ **Quick Actions**: Delete individual tasks or clear all at once
- ⌨️ **Keyboard Support**: Press Enter to quickly add tasks
- 📜 **Scrollable List**: Handles any number of tasks with smooth scrolling

## Screenshots

The application features:
- A soft grey gradient background
- White task cards with hover effects
- Clean typography and spacing
- Intuitive button placement
- Smooth color transitions on interactions

## Installation

### Prerequisites

- Python 3.6 or higher
- Tkinter (usually included with Python)

### Setup

1. Clone or download this repository
2. Ensure Python is installed on your system
3. No additional dependencies required - the app uses only Python's built-in libraries

## Usage

1. Run the application:
   ```bash
   python todo_ui.py
   ```

2. **Adding Tasks**:
   - Type your task in the input field
   - Click "➕ Add Task" or press Enter
   
3. **Completing Tasks**:
   - Click the checkbox next to any task to mark it as complete
   - Completed tasks appear with strikethrough text

4. **Deleting Tasks**:
   - Hover over a task to reveal the delete button (✕)
   - Click the delete button to remove a single task
   - Use "🗑️ Clear All Tasks" to remove all tasks at once

5. **Task Persistence**:
   - All tasks are automatically saved to `tasks.txt`
   - Your tasks will be restored when you restart the application

## File Structure

```
To-Do-List/
│
├── todo_ui.py          # Main application file
├── tasks.txt           # Task storage file (auto-generated)
└── README.md           # This file
```

## Project Details

### Technology Stack

- **Python**: Core programming language
- **Tkinter**: GUI framework
- **ttk**: Enhanced widget styling

### Key Components

- **Gradient Background**: Subtle grey gradient using canvas rendering
- **Task Cards**: White cards with smooth hover animations
- **Color Scheme**: Muted grey palette for a comfortable viewing experience
- **Data Persistence**: Simple text-based storage system

### Color Palette

The application uses a minimal, eye-friendly color scheme:
- Background: Soft grey gradient (`#f5f7fa` → `#e9ecef`)
- Primary: Dark grey (`#495057`)
- Text: Dark grey (`#212529`)
- Borders: Light grey (`#dee2e6`)
- Cards: White with light grey hover (`#f8f9fa`)

## Features in Detail

### Modern UI Elements

- **Glassmorphism Cards**: Task items displayed on clean white cards
- **Smooth Transitions**: Color transitions on hover and interactions
- **Focus States**: Visual feedback when interacting with input fields
- **Responsive Design**: Clean layout that adapts to content

### Task Management

- **Add Tasks**: Simple input with Enter key support
- **Complete Tasks**: Checkbox-based completion system
- **Delete Tasks**: Per-task and bulk delete options
- **Auto-Save**: Instant persistence to prevent data loss

## Future Enhancements

Potential improvements for future versions:
- [ ] Task priorities (High, Medium, Low)
- [ ] Due dates and reminders
- [ ] Task categories/tags
- [ ] Search and filter functionality
- [ ] Dark mode toggle
- [ ] Export/import functionality
- [ ] Undo/redo functionality
- [ ] Task reordering (drag and drop)

## Troubleshooting

### Common Issues

**Issue**: Tkinter not found
- **Solution**: Install tkinter using your package manager:
  - Ubuntu/Debian: `sudo apt-get install python3-tk`
  - macOS: Usually pre-installed with Python
  - Windows: Usually pre-installed with Python

**Issue**: Tasks not saving
- **Solution**: Ensure the application has write permissions in the directory

**Issue**: Window appears too small/large
- **Solution**: The window size is set to 600x700, but you can modify the geometry in `todo_ui.py`

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

## License

This project is open source and available under the MIT License.

## Author

Created as a modern, user-friendly to-do list application with a focus on simplicity and visual comfort.

---

**Enjoy staying organized! 🎯**

