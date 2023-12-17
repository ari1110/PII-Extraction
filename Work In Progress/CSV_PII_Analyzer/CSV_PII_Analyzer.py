import os
import pandas as pd
import pprint
from typing import List, Iterable, Optional

from presidio_analyzer import BatchAnalyzerEngine, DictAnalyzerResult
from presidio_anonymizer import BatchAnonymizerEngine

"""
Example implementing a CSV analyzer

This example shows how to use the Presidio Analyzer and Anonymizer
to detect and anonymize PII in a CSV file.
It uses the BatchAnalyzerEngine to analyze the CSV file, and 
BatchAnonymizerEngine to anonymize the requested columns.

Content of csv file:
id,name,city,comments
1,John,New York,called him yesterday to confirm he requested to call back in 2 days
2,Jill,Los Angeles,accepted the offer license number AC432223
3,Jack,Chicago,need to call him at phone number 212-555-5555

"""


class ExcelAnalyzer(BatchAnalyzerEngine):

    def analyze_excel(self, excel_file_name, language="en", keys_to_skip=None, **kwargs):
        # Construct the absolute path to the Excel file
        excel_full_path = os.path.join(os.path.dirname(__file__), excel_file_name)
        
        # Read the Excel file into a DataFrame
        df = pd.read_excel(excel_full_path)

        # Convert the DataFrame into a dictionary
        data_dict = df.to_dict('list')

        # Analyze the dictionary
        analyzer_results = self.analyze_dict(data_dict, language, keys_to_skip)

        return list(analyzer_results)
    
# class CSVAnalyzer(BatchAnalyzerEngine):
    # def analyze_csv(
    #     self,
    #     csv_full_path: str,
    #     language: str,
    #     keys_to_skip: Optional[List[str]] = None,
    #     **kwargs,
    # ) -> Iterable[DictAnalyzerResult]:

    #     with open(csv_full_path, 'r', encoding='utf-8') as csv_file:
    #         csv_list = list(csv.reader(csv_file))
    #         csv_dict = {header: list(map(str, values)) for header, *values in zip(*csv_list)}
    #         analyzer_results = self.analyze_dict(csv_dict, language, keys_to_skip)
    #         return list(analyzer_results)


if __name__ == "__main__":

    analyzer = ExcelAnalyzer()
    analyzer_results = analyzer.analyze_excel('/workspaces/PII-Extraction/tagger_parser_ud/CSV_PII_Analyzer/sample_data.csv',
                                            language="en")
    pprint.pprint(analyzer_results)

    anonymizer = BatchAnonymizerEngine()
    anonymized_results = anonymizer.anonymize_dict(analyzer_results)
    pprint.pprint(anonymized_results)