#!/usr/bin/env python3
"""
Create professionally formatted PDF from manuscript with markdown italics.
Uses reportlab to generate PDF with proper academic formatting.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import re

def create_pdf_document(input_file, output_file):
    """Create a professionally formatted PDF from text file."""

    # Read the manuscript
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Create PDF document
    doc = SimpleDocTemplate(
        output_file,
        pagesize=letter,
        rightMargin=1*inch,
        leftMargin=1*inch,
        topMargin=1*inch,
        bottomMargin=1*inch
    )

    # Create styles
    styles = getSampleStyleSheet()

    # Title style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=12,
        leading=24,  # Double spacing (2x font size)
        alignment=TA_CENTER,
        fontName='Times-Roman',
        spaceAfter=0
    )

    # Section header style
    section_style = ParagraphStyle(
        'CustomSection',
        parent=styles['Heading2'],
        fontSize=12,
        leading=24,
        alignment=TA_LEFT,
        fontName='Times-Roman',
        spaceAfter=0,
        spaceBefore=0
    )

    # Body style (double-spaced)
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=12,
        leading=24,  # Double spacing
        alignment=TA_LEFT,
        fontName='Times-Roman',
        spaceAfter=0,
        spaceBefore=0
    )

    # Justified body style for most paragraphs
    justified_style = ParagraphStyle(
        'CustomJustified',
        parent=body_style,
        alignment=TA_JUSTIFY
    )

    # Build content
    story = []
    lines = content.split('\n')

    i = 0
    while i < len(lines):
        line = lines[i]

        # Skip empty lines but preserve spacing
        if not line.strip():
            story.append(Spacer(1, 12))  # Half line space
            i += 1
            continue

        # Determine paragraph type
        text = line.strip()

        if text == 'THE BLUES AS BUDDHIST EPISTEMOLOGY':
            formatted_text = format_text_with_italics(text)
            story.append(Paragraph(formatted_text, title_style))
        elif text.startswith('How African-American Musical Tradition'):
            formatted_text = format_text_with_italics(text)
            story.append(Paragraph(formatted_text, title_style))
        elif text in ['ABSTRACT', 'INTRODUCTION', 'DEFINING "SHARED EPISTEMOLOGY"',
                      'SECTION 1: PHILOSOPHICAL PARALLELS—THE SHARED EPISTEMOLOGY',
                      'SECTION 2: HISTORICAL EVIDENCE AND PRECEDENT',
                      'SECTION 3: TRANSLATION AS EPISTEMOLOGICAL BRIDGE',
                      'SECTION 4: IMPLICATIONS FOR CONTEMPORARY PRACTICE',
                      'CONCLUSION', 'NOTES', 'WORKS CITED']:
            formatted_text = format_text_with_italics(text)
            story.append(Paragraph(formatted_text, section_style))
        else:
            formatted_text = format_text_with_italics(text)
            # Use justified alignment for body paragraphs
            story.append(Paragraph(formatted_text, justified_style))

        i += 1

    # Build PDF
    doc.build(story)
    print(f"PDF saved to: {output_file}")

def format_text_with_italics(text):
    """Convert markdown italics to HTML italics for reportlab."""

    # Convert *text* to <i>text</i>
    text = re.sub(r'\*([^*]+)\*', r'<i>\1</i>', text)

    # Fix en-dashes in page ranges
    text = re.sub(r'(\d+)-(\d+)', r'\1–\2', text)

    # Escape special characters for XML
    text = text.replace('&', '&amp;')
    # But restore our italics tags
    text = text.replace('&amp;lt;i&amp;gt;', '<i>')
    text = text.replace('&amp;lt;/i&amp;gt;', '</i>')

    return text

if __name__ == '__main__':
    input_file = '/Users/williamaltig/claudeprojects/Lotus_Sutra/05_SCHOLARLY_ARTICLES/ARTICLE_4_Blues_Buddhist_Epistemology_BLIND_FOR_SUBMISSION.txt'
    output_file = '/Users/williamaltig/claudeprojects/Lotus_Sutra/05_SCHOLARLY_ARTICLES/The_Blues_as_Buddhist_Epistemology.pdf'

    create_pdf_document(input_file, output_file)
    print("PDF formatting complete!")
    print("- Times New Roman, 12pt font")
    print("- Double spacing throughout")
    print("- 1-inch margins")
    print("- Markdown italics converted to actual italics")
    print("- Ready for academic journal submission")
