from dataclasses import dataclass

import camelot


@dataclass
class ExtractedTable:
    page: int
    headers: list[str]
    rows: list[list[str]]

class TableExtractor:
    def extract(
        self,
        pdf_path: str,
        pages: str = "all",
        flavor: str = "stream"
    ) -> list[ExtractedTable]:

        tables = camelot.read_pdf(
            pdf_path,
            pages=pages,
            flavor=flavor
        )

        results = []

        for table in tables:
            df = table.df

            headers = df.iloc[0].tolist()
            rows = df.iloc[1:].values.tolist()

            results.append(
                ExtractedTable(
                    page=table.parsing_report["page"],
                    headers=headers,
                    rows=rows
                )
            )

        return results