import pandas as pd
import numpy as np

class DataCleansing:
    def __init__(self, data):
        self.data = data

    def remove_duplicates(self):
        self.data = self.data.drop_duplicates()
        return self.data

    def handle_missing_values(self, strategy='mean'):
        if strategy == 'mean':
            self.data = self.data.fillna(self.data.mean())
        elif strategy == 'median':
            self.data = self.data.fillna(self.data.median())
        elif strategy == 'mode':
            self.data = self.data.fillna(self.data.mode().iloc[0])
        elif strategy == 'drop':
            self.data = self.data.dropna()
        return self.data

    def normalize_data(self):
        self.data = (self.data - self.data.min()) / (self.data.max() - self.data.min())
        return self.data

    def standardize_data(self):
        self.data = (self.data - self.data.mean()) / self.data.std()
        return self.data

# Example usage
if __name__ == "__main__":
    # Sample data
    data = pd.DataFrame({
        'A': [1, 2, 2, np.nan, 4],
        'B': [5, np.nan, 7, 8, 8],
        'C': [10, 11, 12, 13, 13]
    })

    cleanser = DataCleansing(data)
    data_no_duplicates = cleanser.remove_duplicates()
    data_no_missing = cleanser.handle_missing_values(strategy='mean')
    normalized_data = cleanser.normalize_data()
    standardized_data = cleanser.standardize_data()

    print("Data without duplicates:\n", data_no_duplicates)
    print("Data without missing values:\n", data_no_missing)
    print("Normalized data:\n", normalized_data)
    print("Standardized data:\n", standardized_data)
