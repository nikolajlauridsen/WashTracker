from jinja2 import Template
import pdfkit
import time
from . import format_time


class Receipt:
    def __init__(self, entries):
        self.entries = entries

    def pack_entries(self):
        formatted_entries = list()
        for wash in self.entries:
            # TODO: fetch price from future config file
            entry = {
                "date": format_time(wash[0]),
                "price": 10
            }
            formatted_entries.append(entry)
        self.entries = formatted_entries

    def pack_data(self):
        data = dict()
        # Pack and add entries
        self.pack_entries()
        data["washes"] = self.entries
        data["wash_count"] = len(self.entries)
        data["total"] = data["wash_count"] * 10  # TODO: Fetch price from config
        data["currency"] = "kr"  # TODO: Currency as well
        data["date"] = format_time(time.time(), t_format='%d/%m/%y')
        return data

    @staticmethod
    def get_template():
        with open('receipt_template.html', mode="r") as html_file:
            html = "".join(html_file.readlines())
        return Template(html)

    def save_receipt(self, name=None):
        print("Creating and rendering template")
        template = self.get_template()
        rendered_template = template.render(self.pack_data())
        if not name:
            receipt_name = "Washing Receipt " + format_time(time.time(), t_format='%d-%m-%y %H;%M') + ".pdf"
        else:
            receipt_name = name + ".pdf"

        print("Generating pdf, saving as: ", receipt_name)
        pdfkit.from_string(rendered_template, receipt_name)

