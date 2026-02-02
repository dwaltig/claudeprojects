from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING

def create_kdp_template(path):
    doc = Document()
    
    # 6x9 Page Setup
    section = doc.sections[0]
    section.page_width = Inches(6)
    section.page_height = Inches(9)
    
    # Margins
    section.top_margin = Inches(0.75)
    section.bottom_margin = Inches(0.75)
    section.left_margin = Inches(0.75) # Gutter
    section.right_margin = Inches(0.5)  # Outside
    
    # Define Styles
    styles = doc.styles
    
    # Normal Style
    normal_style = styles['Normal']
    normal_font = normal_style.font
    normal_font.name = 'Garamond'
    normal_font.size = Pt(11)
    
    normal_format = normal_style.paragraph_format
    normal_format.line_spacing = 1.2
    normal_format.space_after = Pt(6)
    normal_format.first_line_indent = Inches(0.25)
    
    # Heading 1
    h1_style = styles['Heading 1']
    h1_font = h1_style.font
    h1_font.name = 'Garamond'
    h1_font.size = Pt(18)
    h1_font.bold = True
    
    h1_format = h1_style.paragraph_format
    h1_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    h1_format.space_before = Pt(18)
    h1_format.space_after = Pt(12)
    h1_format.page_break_before = True
    
    # Heading 2
    h2_style = styles['Heading 2']
    h2_font = h2_style.font
    h2_font.name = 'Garamond'
    h2_font.size = Pt(14)
    h2_font.bold = True
    
    h2_format = h2_style.paragraph_format
    h2_format.space_before = Pt(12)
    h2_format.space_after = Pt(6)
    
    # Heading 3
    h3_style = styles['Heading 3']
    h3_font = h3_style.font
    h3_font.name = 'Garamond'
    h3_font.size = Pt(12)
    h3_font.bold = True
    
    h3_format = h3_style.paragraph_format
    h3_format.space_before = Pt(6)
    h3_format.space_after = Pt(3)

    # Save
    doc.save(path)

if __name__ == "__main__":
    create_kdp_template('Tiantai_Teachings_Project/01_TRANSLATIONS/The_Profound_Meaning/KDP_SUBMISSION/kdp_reference.docx')
