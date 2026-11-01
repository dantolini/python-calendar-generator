import reportlab.lib.pagesizes as pagesizes
from reportlab.lib.units import mm

from reportlab.platypus import (
    PageTemplate,
    Frame
)
from reportlab.lib.styles import getSampleStyleSheet

page_size = pagesizes.A5
paper_width, paper_height = page_size;
margin = 11*mm
binder_margin = 6*mm
usable_width = paper_width - 2*margin - binder_margin
usable_height = paper_height - 2*margin

# Frame for Odd (right) pages
frame_odd = Frame(margin + binder_margin,margin, usable_width, usable_height,
      id="odd_frame"
  )

  # Frame for Even (left) pages
frame_even = Frame(margin,margin, usable_width, usable_height,
    id="even_frame"
)

# Create PageTemplates
template_odd = PageTemplate(id="OddPage", frames=frame_odd)
template_even = PageTemplate(id="EvenPage", frames=frame_even)