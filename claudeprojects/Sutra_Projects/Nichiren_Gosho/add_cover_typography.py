from PIL import Image, ImageDraw, ImageFont
import os

# Project Path
BASE_DIR = "/Users/williamaltig/claudeprojects/Sutra_Projects/Nichiren_Gosho/03_FINAL_DOCUMENTS/COVER_ART"

# Standard Mac Fonts
TIMES = "/System/Library/Fonts/Supplemental/Times New Roman.ttf"
HELVETICA = "/System/Library/Fonts/Helvetica.ttc"
# Fallback
DEFAULT_FONT = None

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception as e:
        print(f"Could not load font {path}: {e}")
        return ImageFont.load_default()

configs = [
    {
        "input": "kaimoku_sho_classic_cover.png",
        "output": "kaimoku_sho_classic_final.png",
        "title": "KAIMOKU SHŌ",
        "subtitle": "ON OPENING THE EYES",
        "author": "NICHIREN",
        "font_path": TIMES,
        "color": (218, 165, 32), # Goldenrod/Gold
        "shadow": (0, 0, 0), # Black shadow
        "pos": "top"
    },
    {
        "input": "kaimoku_sho_blues_cover.png",
        "output": "kaimoku_sho_blues_final.png",
        "title": "OPENING YOUR EYES",
        "subtitle": "A BLUES INTERPRETATION",
        "author": "WILLIAM ALTIG",
        "font_path": HELVETICA,
        "color": (255, 255, 255), 
        "shadow": (0, 0, 0), 
        "pos": "bottom"
    },
    {
        "input": "kaimoku_sho_abstract_cover.png",
        "output": "kaimoku_sho_abstract_final.png",
        "title": "THE PILLAR",
        "subtitle": "KAIMOKU SHŌ",
        "author": "NICHIREN",
        "font_path": TIMES,
        "color": (255, 215, 0), # Gold text
        "shadow": (0, 0, 0), # Black shadow
        "pos": "center"
    },
    {
        "input": "kaimoku_sho_marketable_cover_tiantai.png",
        "output": "kaimoku_sho_marketable_final.png",
        "title": "OPENING THE EYES",
        "subtitle": "KAIMOKU SHŌ",
        "author": "WILLIAM ALTIG",
        "font_path": HELVETICA,
        "color": (255, 255, 255), 
        "shadow": (0, 0, 0), 
        "pos": "bottom"
    }
]

for cfg in configs:
    in_path = os.path.join(BASE_DIR, cfg["input"])
    out_path = os.path.join(BASE_DIR, cfg["output"])
    
    if not os.path.exists(in_path):
        print(f"Missing input: {in_path}")
        continue
        
    img = Image.open(in_path).convert("RGBA")
    
    # Enforce 1200x1800 Dimensions
    TARGET_W = 1200
    TARGET_H = 1800
    
    # Current size
    iw, ih = img.size
    
    # Desired aspect ratio
    target_aspect = TARGET_W / TARGET_H
    current_aspect = iw / ih
    
    if current_aspect > target_aspect:
        # Too wide, crop width
        new_w = int(ih * target_aspect)
        offset = (iw - new_w) // 2
        img = img.crop((offset, 0, offset + new_w, ih))
    else:
        # Too tall, crop height
        new_h = int(iw / target_aspect)
        offset = (ih - new_h) // 2
        img = img.crop((0, offset, iw, offset + new_h))
        
    # Resize to exact target
    img = img.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    
    draw = ImageDraw.Draw(img)
    W, H = img.size
    
    # Scale fonts
    title_size = int(W * 0.08)
    sub_size = int(W * 0.04)
    author_size = int(W * 0.03)
    
    title_font = get_font(cfg["font_path"], title_size)
    sub_font = get_font(cfg["font_path"], sub_size)
    author_font = get_font(cfg["font_path"], author_size)
    
    # Helper to draw centered text with shadow
    def draw_text_centered(text, font, y_pos, color, shadow_color):
        bbox = draw.textbbox((0, 0), text, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        x = (W - text_w) / 2
        
        # Shadow/Outline
        offset = 2
        draw.text((x+offset, y_pos+offset), text, font=font, fill=shadow_color)
        draw.text((x-offset, y_pos-offset), text, font=font, fill=shadow_color)
        draw.text((x+offset, y_pos-offset), text, font=font, fill=shadow_color)
        draw.text((x-offset, y_pos+offset), text, font=font, fill=shadow_color)
        
        # Main text
        draw.text((x, y_pos), text, font=font, fill=color)
        return y_pos + text_h + 20 # Return next Y pos
        
    # Layout Strategy
    current_y = 0
    
    if cfg["pos"] == "top":
        current_y = H * 0.1
        current_y = draw_text_centered(cfg["title"], title_font, current_y, cfg["color"], cfg["shadow"])
        current_y = draw_text_centered(cfg["subtitle"], sub_font, current_y, cfg["color"], cfg["shadow"])
        # Author at bottom? Or below title?
        draw_text_centered(cfg["author"], author_font, H * 0.85, cfg["color"], cfg["shadow"])
        
    elif cfg["pos"] == "bottom":
        # Start from bottom up?
        # Author at very bottom
        draw_text_centered(cfg["author"], author_font, H * 0.9, cfg["color"], cfg["shadow"])
        # Title above author
        title_y = H * 0.75
        draw_text_centered(cfg["title"], title_font, title_y, cfg["color"], cfg["shadow"])
        draw_text_centered(cfg["subtitle"], sub_font, title_y + title_size + 10, cfg["color"], cfg["shadow"])
        
    elif cfg["pos"] == "center":
        # Title in exact center
        start_y = (H / 2) - title_size
        draw_text_centered(cfg["title"], title_font, start_y, cfg["color"], cfg["shadow"])
        draw_text_centered(cfg["subtitle"], sub_font, start_y + title_size + 15, cfg["color"], cfg["shadow"])
        draw_text_centered(cfg["author"], author_font, H * 0.85, cfg["color"], cfg["shadow"])
        
    img.save(out_path)
    print(f"Saved {cfg['output']}")
