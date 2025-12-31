"""Main entry point for WPC-TV application"""

import sys
from pathlib import Path

# Add the src directory to the path
src_dir = Path(__file__).parent
sys.path.insert(0, str(src_dir))

from components.epg_grid import EPGGrid
from components.channel_list import ChannelList
from components.program_banner import ProgramBanner
from components.main_menu import MainMenu
from components.subtitle_manager import SubtitleManager
from styles.wpc_theme import WPCTheme


class WPCTVApp:
    """Main application class for WPC-TV"""
    
    def __init__(self):
        """Initialize the WPC-TV application"""
        self.theme = WPCTheme()
        self.epg_grid = EPGGrid()
        self.channel_list = ChannelList()
        self.program_banner = ProgramBanner()
        self.main_menu = MainMenu()
        self.subtitle_manager = SubtitleManager()
        
    def run(self):
        """Run the application"""
        print("WPC-TV Application Starting...")
        print(f"Theme: {self.theme.name}")
        print(f"Total channels: {self.channel_list.get_channel_count()}")
        
        # Check for special channel features
        if self.channel_list.has_auto_subtitles(7):
            print("Channel 7 (WPC Movies): Auto-subtitles enabled")
        
        if self.channel_list.is_loop_channel(6):
            print("Channel 6 (The Simpsons Loop): Loop mode enabled")
        
        # Application main loop would go here
        

def main():
    """Main entry point"""
    app = WPCTVApp()
    app.run()


if __name__ == "__main__":
    main()
