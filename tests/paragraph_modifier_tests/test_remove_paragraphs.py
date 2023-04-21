from modifiers.paragraph_modifier import ParagraphModifier


class ParagraphStyle:
    name: str

    def __init__(self, name) -> None:
        self.name = name


class Paragraph:
    text: str
    style: ParagraphStyle

    def __init__(self, text: str, style_name: str) -> None:
        self.text = text
        self.style = ParagraphStyle(style_name)


paragraphs = [
    Paragraph("Test Title", "Title"),
    Paragraph("Test heading 1", "Heading 1"),
    Paragraph("Test heading 2", "Heading 2"),
    Paragraph("Test heading 2.1", "Heading 2"),
    Paragraph("Test heading 3.1", "Heading 3"),
    Paragraph("Test heading 3.2", "Heading 3"),
    Paragraph("Test normal", "Normal"),
    Paragraph("Test normal", "Normal"),
    Paragraph("Test normal", "Normal"),
]

expected_kept = [
    Paragraph("Test normal", "Normal"),
    Paragraph("Test normal", "Normal"),
    Paragraph("Test normal", "Normal"),
]

expected_removed = [
    Paragraph("Test Title", "Title"),
    Paragraph("Test heading 1", "Heading 1"),
    Paragraph("Test heading 2", "Heading 2"),
    Paragraph("Test heading 2.1", "Heading 2"),
    Paragraph("Test heading 3.1", "Heading 3"),
    Paragraph("Test heading 3.2", "Heading 3"),
]

def test_remove_heading():
    kept, removed = ParagraphModifier.remove_headings(paragraphs)
    assert kept == expected_kept
    assert removed == expected_removed