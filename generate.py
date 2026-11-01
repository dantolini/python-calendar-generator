import os
import importlib
import reportlab.lib.pagesizes as pagesizes
from datetime import date
from reportlab.platypus import BaseDocTemplate, NextPageTemplate

if __name__ == "__main__":

    # Pick paper size and template
    paper = importlib.import_module("a5")
    page_template = importlib.import_module("timesheet")

    # Setup output folder
    os.makedirs("generated", exist_ok=True)
    pdf_path = os.path.join("generated", "output.pdf")

    # Setup doc and story
    doc = BaseDocTemplate(
        pdf_path, 
        pagesize= pagesizes.portrait(paper.page_size)
    )
    story = []

    # Setup odd/even pages
    doc.addPageTemplates([paper.template_odd, paper.template_even])
    story.append(NextPageTemplate("OddPage"))
    story.append(NextPageTemplate(["EvenPage", "OddPage"]))

    # Start building the doc
    start_date = date.fromisoformat('2027-11-03')
    end_date = date.fromisoformat('2028-02-03')
    date_cursor = start_date

    while date_cursor < end_date:
        print(f"Creating page starting from {date_cursor}")
        date_cursor = page_template.generate_week(story, date_cursor)

    doc.build(story)
    print(f"Doc successfully compiled to: {pdf_path}")
