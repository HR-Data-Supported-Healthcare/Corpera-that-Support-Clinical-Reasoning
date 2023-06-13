from modifiers.paragraph_modifier import ParagraphModifier
from data_classes.paragraph import Paragraph, ParagraphStyle

paragraphs = [
    Paragraph("Test heading 1", ParagraphStyle("Heading 1")),
    Paragraph("Test heading 2", ParagraphStyle("Heading 2")),
    Paragraph("Test heading 2.1", ParagraphStyle("Heading 2")),
    Paragraph("Test heading 3.1", ParagraphStyle("Heading 3")),
    Paragraph("Test heading 3.2", ParagraphStyle("Heading 3")),
    Paragraph("Test normal", ParagraphStyle("Normal")),
    Paragraph("Test normal", ParagraphStyle("Normal")),
    Paragraph("Test normal", ParagraphStyle("Normal")),
    Paragraph("Test Title", ParagraphStyle("Title"))
]

expected_kept = paragraphs[5:9]
expected_removed = paragraphs[0:5]

def test_remove_heading():
    kept, removed = ParagraphModifier.remove_headings(paragraphs)
    assert kept == expected_kept
    assert removed == expected_removed
