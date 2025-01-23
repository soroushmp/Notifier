from typing import Self

import pandas as pd


class ReadCSVDataMixin:
    """
    Mixin for reading CSV data and converting it to a list of instances of a class
    """

    @classmethod
    def convert_csv_to_bulk_instance(cls, csv_file: str) -> list[Self]:
        """
        Converts a CSV file to a list of instances of a class

        Args:
            csv_file (str): The path to the CSV file
        Returns:
            A list of instances of a class
        """
        df = pd.read_csv(csv_file)

        instances = [
            cls(**row.to_dict())
            for _, row in df.iterrows()
        ]
        return instances
