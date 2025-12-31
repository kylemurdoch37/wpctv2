"""Main Menu Component for navigation"""


class MainMenu:
    """Main Menu component for application navigation"""
    
    def __init__(self):
        """Initialize the Main Menu"""
        self.menu_items = [
            {'id': 'guide', 'label': 'TV Guide', 'action': 'show_guide'},
            {'id': 'channels', 'label': 'Channels', 'action': 'show_channels'},
            {'id': 'favorites', 'label': 'Favorites', 'action': 'show_favorites'},
            {'id': 'settings', 'label': 'Settings', 'action': 'show_settings'},
            {'id': 'exit', 'label': 'Exit', 'action': 'exit_app'},
        ]
        self.selected_index = 0
        
    def render(self):
        """Render the main menu"""
        print("Rendering Main Menu...")
        return self.menu_items
        
    def navigate_up(self):
        """Navigate to the previous menu item"""
        self.selected_index = (self.selected_index - 1) % len(self.menu_items)
        return self.menu_items[self.selected_index]
        
    def navigate_down(self):
        """Navigate to the next menu item"""
        self.selected_index = (self.selected_index + 1) % len(self.menu_items)
        return self.menu_items[self.selected_index]
        
    def select_current(self):
        """Select the current menu item"""
        return self.menu_items[self.selected_index]
        
    def get_selected_action(self):
        """Get the action for the selected menu item"""
        return self.menu_items[self.selected_index].get('action')
