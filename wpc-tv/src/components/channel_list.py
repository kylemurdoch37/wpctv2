"""Channel List Component for displaying available channels"""

import json
from pathlib import Path


class ChannelList:
    """Channel List component for browsing channels"""
    
    def __init__(self):
        """Initialize the Channel List"""
        self.channels = self._load_channels()
        self.selected_channel = None
        
    def _load_channels(self):
        """Load channels from JSON file"""
        channels_path = Path(__file__).parent.parent / 'data' / 'channels.json'
        try:
            with open(channels_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"channels": []}
            
    def render(self):
        """Render the channel list"""
        print("Rendering Channel List...")
        return self.channels
        
    def select_channel(self, channel_id):
        """Select a channel by ID"""
        for channel in self.channels.get('channels', []):
            if channel.get('id') == channel_id:
                self.selected_channel = channel
                return channel
        return None
        
    def get_channel_count(self):
        """Get the total number of channels"""
        return len(self.channels.get('channels', []))
