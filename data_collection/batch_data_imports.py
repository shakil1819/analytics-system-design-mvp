import pandas as pd

class BatchDataImporter:
    def __init__(self, file_path):
        self.file_path = file_path

    def import_data(self):
        try:
            data = pd.read_csv(self.file_path)
            print("Data imported successfully")
            return data
        except Exception as e:
            print(f"Error importing data: {e}")
            return None

    def process_data(self, data):
        # Placeholder for data processing logic
        processed_data = data  # Modify this as needed
        return processed_data

    def save_data(self, data, output_path):
        try:
            data.to_csv(output_path, index=False)
            print("Data saved successfully")
        except Exception as e:
            print(f"Error saving data: {e}")

# Example usage
if __name__ == "__main__":
    importer = BatchDataImporter("input_data.csv")
    data = importer.import_data()
    if data is not None:
        processed_data = importer.process_data(data)
        importer.save_data(processed_data, "output_data.csv")
