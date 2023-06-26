class Document:
    def accept(self, visitor):
        raise NotImplementedError()


class PDFDocument(Document):
    def accept(self, visitor):
        visitor.visit_pdf_document(self)


class WordDocument(Document):
    def accept(self, visitor):
        visitor.visit_word_document(self)


class MarkdownDocument(Document):
    def accept(self, visitor):
        visitor.visit_markdown_document(self)


class DocumentStatisticsVisitor:
    def visit_pdf_document(self, document):
        print("Calculating statistics for PDF document.")

    def visit_word_document(self, document):
        print("Calculating statistics for Word document.")

    def visit_markdown_document(self, document):
        print("Calculating statistics for Markdown document.")


class TextExtractionVisitor:
    def visit_pdf_document(self, document):
        print("Extracting text from PDF document.")

    def visit_word_document(self, document):
        print("Extracting text from Word document.")

    def visit_markdown_document(self, document):
        print("Extracting text from Markdown document.")


# Usage
documents = [PDFDocument(), WordDocument(), MarkdownDocument()]

statistics_visitor = DocumentStatisticsVisitor()
extraction_visitor = TextExtractionVisitor()

for document in documents:
    document.accept(statistics_visitor)
    document.accept(extraction_visitor)

# Output:
# Calculating statistics for PDF document.
# Extracting text from PDF document.
# Calculating statistics for Word document.
# Extracting text from Word document.
# Calculating statistics for Markdown document.
# Extracting text from Markdown document.
