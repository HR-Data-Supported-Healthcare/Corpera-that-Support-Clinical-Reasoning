from modifiers.paragraph_modifier import ParagraphModifier
from data_classes.paragraph import Paragraph, ParagraphStyle
import unittest


class TestRemoveHeading(unittest.TestCase):
    def test_remove_headings(self):
        # ARRANGE 
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

        # ACT
        kept, removed = ParagraphModifier.remove_headings(paragraphs)

        # ASSERT
        expected_kept = paragraphs[5:9] # only the non-heading paragraphs should be kept
        expected_removed = paragraphs[0:5] # should contain all heading paragraphs

        assert kept == expected_kept
        assert removed == expected_removed

    def test_empty_list(self):
        # ARRANGE
        empty_list = []

        # ACT
        kept, removed = ParagraphModifier.remove_headings(empty_list)

        # ASSERT
        assert kept == []
        assert removed == []

    def test_list_only_headings(self):
        # ARRANGE 
        paragraphs = [
            Paragraph("Test heading 1", ParagraphStyle("Heading 1")),
            Paragraph("Test heading 2", ParagraphStyle("Heading 2")),
            Paragraph("Test heading 2.1", ParagraphStyle("Heading 2")),
            Paragraph("Test heading 3.1", ParagraphStyle("Heading 3")),
            Paragraph("Test heading 3.2", ParagraphStyle("Heading 3")),
        ]

        # ACT
        kept, removed = ParagraphModifier.remove_headings(paragraphs)

        assert kept == []
        assert removed == paragraphs[0:5]
