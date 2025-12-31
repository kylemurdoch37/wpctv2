"""WPC Theme styling configuration"""


class WPCTheme:
    """West Palm Club TV Theme"""
    
    def __init__(self):
        """Initialize the WPC Theme"""
        self.name = "WPC-TV Theme"
        self.colors = {
            'primary': '#1E3A8A',      # Dark blue
            'secondary': '#3B82F6',    # Blue
            'accent': '#10B981',       # Green
            'background': '#0F172A',   # Dark slate
            'surface': '#1E293B',      # Slate
            'text_primary': '#F1F5F9', # Light text
            'text_secondary': '#94A3B8', # Gray text
            'highlight': '#FBBF24',    # Amber
            'error': '#EF4444',        # Red
        }
        
        self.fonts = {
            'family': 'Arial, sans-serif',
            'size_small': 12,
            'size_normal': 14,
            'size_large': 18,
            'size_xlarge': 24,
        }
        
        self.spacing = {
            'xs': 4,
            'sm': 8,
            'md': 16,
            'lg': 24,
            'xl': 32,
        }
        
        self.border_radius = {
            'small': 4,
            'medium': 8,
            'large': 12,
        }
        
    def get_color(self, color_name):
        """Get a color value by name"""
        return self.colors.get(color_name, self.colors['primary'])
        
    def get_font_size(self, size_name):
        """Get a font size by name"""
        return self.fonts.get(f'size_{size_name}', self.fonts['size_normal'])
        
    def apply_theme(self):
        """Apply the theme to the application"""
        print(f"Applying {self.name}...")
        return self.colors
