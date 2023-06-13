from dataclasses import dataclass

@dataclass
class ParagraphStyle():
    name: str

@dataclass
class Paragraph():
    text: str
    style: ParagraphStyle