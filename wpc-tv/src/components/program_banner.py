"""Program Banner Component for displaying current program information"""


class ProgramBanner:
    """Program Banner component showing current program details"""
    
    def __init__(self):
        """Initialize the Program Banner"""
        self.current_program = None
        self.visible = True
        
    def render(self):
        """Render the program banner"""
        print("Rendering Program Banner...")
        if self.current_program:
            return self._format_program_info()
        return "No program selected"
        
    def set_program(self, program):
        """Set the current program to display"""
        self.current_program = program
        
    def _format_program_info(self):
        """Format program information for display"""
        if not self.current_program:
            return ""
            
        title = self.current_program.get('title', 'Unknown')
        description = self.current_program.get('description', '')
        start_time = self.current_program.get('start_time', '')
        end_time = self.current_program.get('end_time', '')
        
        return f"{title} ({start_time} - {end_time})\n{description}"
        
    def toggle_visibility(self):
        """Toggle banner visibility"""
        self.visible = not self.visible
        
    def show(self):
        """Show the banner"""
        self.visible = True
        
    def hide(self):
        """Hide the banner"""
        self.visible = False
