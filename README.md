# WPC-TV

West Palm Club TV - A Python-based TV application with Electronic Program Guide (EPG) functionality.

## Project Structure

```
wpc-tv/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── components/
│   │   ├── __init__.py
│   │   ├── epg_grid.py
│   │   ├── channel_list.py
│   │   ├── program_banner.py
│   │   └── main_menu.py
│   ├── styles/
│   │   └── wpc_theme.py
│   ├── data/
│   │   ├── channels.json
│   │   └── schedule.json
│   └── assets/
│       ├── logos/
│       │   └── .gitkeep
│       └── sounds/
│           └── .gitkeep
├── requirements.txt
└── README.md
```

## Features

- **Electronic Program Guide (EPG)**: Browse TV schedules with an interactive grid
- **Channel List**: View and navigate through available channels
- **Program Banner**: Display current program information
- **Main Menu**: Easy navigation through the application
- **Custom Theme**: West Palm Club branded styling

## Components

### EPG Grid (`epg_grid.py`)
Displays the electronic program guide with schedule information loaded from `schedule.json`.

### Channel List (`channel_list.py`)
Shows available TV channels loaded from `channels.json` with channel selection functionality.

### Program Banner (`program_banner.py`)
Displays detailed information about the currently selected program.

### Main Menu (`main_menu.py`)
Provides navigation options including TV Guide, Channels, Favorites, Settings, and Exit.

## Installation

1. Navigate to the wpc-tv directory:
```bash
cd wpc-tv
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python src/main.py
```

## Configuration

### Channels
Edit `src/data/channels.json` to add or modify available channels.

### Schedule
Edit `src/data/schedule.json` to update program schedules.

### Theme
Customize colors and styling in `src/styles/wpc_theme.py`.

## Development

The application is structured with modular components for easy maintenance and extension:

- **Components**: UI elements in `src/components/`
- **Styles**: Theme configuration in `src/styles/`
- **Data**: Channel and schedule data in `src/data/`
- **Assets**: Logos and sounds in `src/assets/`

## License

Copyright © West Palm Club TV
