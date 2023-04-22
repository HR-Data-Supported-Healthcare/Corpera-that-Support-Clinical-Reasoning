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
    {"text": "Test normal", "style": {"name": "Normal"}},
    {"text": "Test normal", "style": {"name": "Normal"}},
    {"text": "Test normal", "style": {"name": "Normal"}},
]

expected_removed = [
    {"text": "Test Title", "style": "Title"},
    {"text": "Test heading 1", "style": "Heading 1"},
    {"text": "Test heading 2", "style": "Heading 2"},
    {"text": "Test heading 2.1", "style": "Heading 2"},
    {"text": "Test heading 3.1", "style": "Heading 3"},
    {"text": "Test heading 3.2", "style": "Heading 3"},
]

# expected_removed = [
#     Paragraph("Test Title", "Title"),
#     Paragraph("Test heading 1", "Heading 1"),
#     Paragraph("Test heading 2", "Heading 2"),
#     Paragraph("Test heading 2.1", "Heading 2"),
#     Paragraph("Test heading 3.1", "Heading 3"),
#     Paragraph("Test heading 3.2", "Heading 3"),
# ]


def test_remove_heading():
    kept, removed = ParagraphModifier.remove_headings(paragraphs)
    assert len(kept) == len(expected_kept)
    assert expected_kept[0]["text"] == kept[0].text
    assert expected_kept[1]["text"] == kept[1].text
    assert expected_kept[2]["text"] == kept[2].text
    assert removed == expected_removed
