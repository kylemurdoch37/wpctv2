"""Subtitle Manager for handling automatic subtitle download and activation"""

import os
from pathlib import Path


class SubtitleManager:
    """Manages subtitle download and activation for video content"""
    
    def __init__(self):
        """Initialize the Subtitle Manager"""
        self.subtitle_extensions = ['.srt', '.sub', '.ass', '.ssa', '.vtt']
        
    def find_subtitle_file(self, video_path):
        """Find subtitle file for a given video
        
        Args:
            video_path: Path to the video file
            
        Returns:
            Path to subtitle file if found, None otherwise
        """
        video_path = Path(video_path)
        video_dir = video_path.parent
        video_name = video_path.stem
        
        # Check for subtitle files with same name as video
        for ext in self.subtitle_extensions:
            subtitle_path = video_dir / f"{video_name}{ext}"
            if subtitle_path.exists():
                return subtitle_path
                
        return None
        
    def download_subtitle(self, video_path, language='en'):
        """Download subtitle file for a video if not present
        
        Args:
            video_path: Path to the video file
            language: Subtitle language code (default: 'en')
            
        Returns:
            Path to downloaded subtitle file or None if download fails
            
        Note:
            This is a placeholder implementation. In production, integrate with
            subtitle APIs like OpenSubtitles, Subscene, or similar services.
        """
        video_path = Path(video_path)
        
        # Check if subtitle already exists
        existing_subtitle = self.find_subtitle_file(video_path)
        if existing_subtitle:
            print(f"Subtitle already exists: {existing_subtitle}")
            return existing_subtitle
            
        # Placeholder for subtitle download logic
        print(f"Searching for subtitle for: {video_path.name}")
        print(f"Language: {language}")
        
        # In production, implement API calls to subtitle services
        # Example services: OpenSubtitles API, Subscene, YIFY Subtitles
        # For now, return None to indicate download would be attempted
        
        return None
        
    def should_enable_subtitles(self, movie_metadata):
        """Determine if subtitles should be enabled based on movie metadata
        
        Args:
            movie_metadata: Dictionary with movie information
            
        Returns:
            True if subtitles should be enabled, False otherwise
        """
        # Enable subtitles for non-English content
        language = movie_metadata.get('language', 'en').lower()
        
        # Check if the primary language is not English
        if language != 'en' and language != 'english':
            return True
            
        return False
        
    def enable_subtitles_for_movie(self, video_path, movie_metadata=None):
        """Enable subtitles for a movie, downloading if necessary
        
        Args:
            video_path: Path to the video file
            movie_metadata: Optional dictionary with movie information
            
        Returns:
            Dictionary with subtitle status and path
        """
        result = {
            'subtitles_enabled': False,
            'subtitle_path': None,
            'auto_downloaded': False
        }
        
        # Check if subtitles should be enabled
        if movie_metadata:
            should_enable = self.should_enable_subtitles(movie_metadata)
        else:
            # If no metadata, always try to use subtitles for safety
            should_enable = True
            
        if not should_enable:
            return result
            
        # Try to find existing subtitle
        subtitle_path = self.find_subtitle_file(video_path)
        
        if subtitle_path:
            result['subtitles_enabled'] = True
            result['subtitle_path'] = str(subtitle_path)
        else:
            # Try to download subtitle
            language = movie_metadata.get('subtitle_language', 'en') if movie_metadata else 'en'
            downloaded_path = self.download_subtitle(video_path, language)
            
            if downloaded_path:
                result['subtitles_enabled'] = True
                result['subtitle_path'] = str(downloaded_path)
                result['auto_downloaded'] = True
                
        return result
