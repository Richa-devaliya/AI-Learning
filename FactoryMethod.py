from abc import ABC, abstractmethod

# Step 1: Abstract Product-- Exporter is the abstract product.
# It defines a contract/interface: all concrete exporters must implement the export() method.
class Exporter(ABC):
    @abstractmethod
    def export(self, data):
        pass


# Step 2: Concrete Exporters
class PDFExporter(Exporter):
    def export(self, data):
        print("Exporting to PDF:\n")
        headers = data[0].keys()    # Get column headers from the first row
        print("\t".join(headers))   # Print headers separated by tabs
        for row in data:
            print("\t".join(str(row[col]) for col in headers))  # Print each row's values


class DOCXExporter(Exporter):
    def export(self, data):
        print("Exporting to DOCX:\n")
        headers = data[0].keys()
        print(" | ".join(headers))  # Print headers with ' | ' separator
        print("-" * 40)     # Divider line
        for row in data:
            print(" | ".join(str(row[col]) for col in headers))


class CSVExporter(Exporter):
    def export(self, data):
        print("Exporting to CSV:\n")
        headers = data[0].keys()
        print(",".join(headers))  # Comma-separated headers
        for row in data:
            print(",".join(str(row[col]) for col in headers))


# Step 3: Abstract Factory
# Any concrete factory must implement the method create_exporter() that returns an Exporter.
class ExporterFactory(ABC):
    @abstractmethod
    def create_exporter(self):
        pass


# Step 4: Concrete Factories
#  These are the concrete creators in the Factory Method pattern.
# They encapsulate object creation logic.
class PDFExporterFactory(ExporterFactory):
    def create_exporter(self):
        return PDFExporter()

class DOCXExporterFactory(ExporterFactory):
    def create_exporter(self):
        return DOCXExporter()

class CSVExporterFactory(ExporterFactory):
    def create_exporter(self):
        return CSVExporter()


# Step 5: Client Code
def main():
    # Simulated report data
    report_data = [
        {"Product": "Laptop", "Units Sold": 30, "Unit Price": 50000, "Revenue": 1500000},
        {"Product": "Mouse", "Units Sold": 120, "Unit Price": 500, "Revenue": 60000},
        {"Product": "Keyboard", "Units Sold": 85, "Unit Price": 800, "Revenue": 68000},
    ]

    print("Welcome to the Document Exporter System")
    format_choice = input("Choose export format (pdf / docx / csv): ").lower()

    factory = None
    if format_choice == "pdf":
        factory = PDFExporterFactory()
    elif format_choice == "docx":
        factory = DOCXExporterFactory()
    elif format_choice == "csv":
        factory = CSVExporterFactory()
    else:
        print("Invalid format selected. Please choose from pdf/docx/csv.")
        return

    exporter = factory.create_exporter()
    exporter.export(report_data)


if __name__ == "__main__":
    main()





# | Concept                    | Meaning                                                                |
# | -------------------------- | ---------------------------------------------------------------------- |
# | `Exporter`                 | Abstract base class for all exporters (interface)                      |
# | `PDFExporter`, etc.        | Concrete classes implementing export logic                             |
# | `ExporterFactory`          | Abstract creator class                                                 |
# | `PDFExporterFactory`, etc. | Concrete factories that create exporters                               |
# | `main()`                   | Client code that uses the factory to get exporters based on user input |
