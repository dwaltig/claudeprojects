import os
import re

def find_lyrics(search_dirs, output_file):
    lyric_files = []
    
    # Regex to find Verse or Chorus markers (case insensitive)
    lyric_pattern = re.compile(r'(\[?Verse\s?\d*\]?|\[?Chorus\]?)', re.IGNORECASE)

    for root_dir in search_dirs:
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                if file.endswith(('.md', '.txt')):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            if lyric_pattern.search(content):
                                # Get title from first line or filename
                                title = file.replace('.md', '').replace('.txt', '')
                                first_line = content.split('\n')[0].strip()
                                if first_line.startswith('#'):
                                    title = first_line.lstrip('#').strip()
                                
                                relative_path = os.path.relpath(file_path, start=os.getcwd())
                                lyric_files.append({
                                    'title': title[:50], # Truncate for table
                                    'file': file,
                                    'path': relative_path
                                })
                    except Exception as e:
                        print(f"Skipping {file_path}: {e}")

    # Sort by title
    lyric_files.sort(key=lambda x: x['title'])

    # Write Index
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# 🎵 Master Lyric File Index\n\n")
        f.write(f"**Total Lyric Files Found:** {len(lyric_files)}\n\n")
        f.write("| Song / Title | Filename | Location |\n")
        f.write("|---|---|---|")
        for item in lyric_files:
            # Escape pipes in title/file to avoid breaking markdown table
            safe_title = item['title'].replace('|', '-')
            safe_file = item['file'].replace('|', '-')
            f.write(f"| {safe_title} | {safe_file} | `{item['path']}` |\n")

    print(f"Index created at {output_file} with {len(lyric_files)} entries.")

if __name__ == "__main__":
    search_directories = ['NotesArchive', 'SONG_CATALOG', 'Dhammapada']
    output_path = 'SONG_CATALOG/LYRIC_FILE_INDEX.md'
    find_lyrics(search_directories, output_path)
