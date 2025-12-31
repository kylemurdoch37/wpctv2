"""EPG Grid Component for displaying the Electronic Program Guide"""

import json
from pathlib import Path


class EPGGrid:
    """Electronic Program Guide Grid component"""
    
    def __init__(self):
        """Initialize the EPG Grid"""
        self.schedule_data = self._load_schedule()
        self.current_time_slot = None
        
    def _load_schedule(self):
        """Load schedule data from JSON file"""
        schedule_path = Path(__file__).parent.parent / 'data' / 'schedule.json'
        try:
            with open(schedule_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"programs": []}
            
    def render(self):
        """Render the EPG grid"""
        print("Rendering EPG Grid...")
        return self.schedule_data
        
    def update_time_slot(self, time_slot):
        """Update the current time slot"""
        self.current_time_slot = time_slot
        
    def get_programs_at_time(self, time):
        """Get programs airing at a specific time
        
        Note: This is a basic implementation. For production use,
        convert time strings to datetime objects for proper comparison.
        """
        programs = []
        for program in self.schedule_data.get('programs', []):
            # Simple string comparison - works for HH:MM format but should use datetime for production
            if program.get('start_time') <= time <= program.get('end_time'):
                programs.append(program)
        return programs
