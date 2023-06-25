from django.http import HttpResponse
import csv


class Download:

    def download_csv_file(columns, data):
        response = HttpResponse(content_type="text/csv")
        response['Content-Disposition'] = "attachment; filename=download.csv"

        writer = csv.writer(response)
        writer.writerow(columns)
        writer.writerows(data)

    def download_excel_file():
        pass

    def download_zip_file():
        pass

    def download_pdf_file():
        pass
