import calendar_utils as cal
from datetime import timedelta
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Table, TableStyle, PageBreak, Spacer, Paragraph, Preformatted
from reportlab.lib import colors

def generate_week(story, start_date):

    # Define the formatting
    title_style = ParagraphStyle('PlannerTitle', fontName='Helvetica-Bold', fontSize=8, leading=0)
    row_title_style = ParagraphStyle('PlannerLines', fontName='Helvetica-Bold', fontSize=10, leading=0)
    row_style = ParagraphStyle('PlannerLines', fontName='Helvetica', fontSize=10, leading=0)

    title_height = 5*mm
    row_height = 7.75*mm

    column_widths = [10*mm, 15*mm, 15*mm, 15*mm, 15*mm, 15*mm, 15*mm, 23*mm]
    row_heights = []
    tab_data = []
    tab_style = [
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('TOPPADDING', (0,0), (-1,-1), -1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]

    # Start the week on Monday
    pos = cal.get_monday(start_date)

    # Four weeks fit on a page
    for week_index in range(4):
        print (f'Week begining: {pos}')
        week = pos.strftime("%d %B")

        style_index = len(tab_data)
        tab_style.append(('SPAN', (1,style_index), (-2,style_index)))
        tab_style.append(('LINEBELOW', (0,style_index), (-1,style_index), 0.75, colors.darkgrey))
        row_heights.append(title_height)
        tab_data.append(['',Paragraph(week, title_style)])

        for day_index in range(5):
            style_index = len(tab_data)
            tab_style.append(('LINEBELOW', (0,style_index), (-1,style_index), 0.5, colors.lightgrey))
            tab_style.append(('LINEAFTER', (0,style_index), (-3,style_index), 0.5, colors.lightgrey))
            tab_style.append(('LINEAFTER', (-2,style_index), (-1,style_index), 0.75, colors.darkgray))
            row_heights.append(row_height)
            tab_data.append([Paragraph(pos.strftime('%a'), row_title_style),Preformatted(cal.get_event(pos) or '',row_style),'','','','','',''])
            pos += timedelta(days=1)

        # Skip the weekend
        pos += timedelta(days=2)

    # Style cumulative WFH cell
    row_heights.append(title_height)
    tab_data.append(['','','','','','',Paragraph('WFH total:', title_style),''])
    tab_style.append(('BOX', (-1,-1), (-1,-1), 0.75, colors.black))
    tab_style.append(('BACKGROUND', (-1,-1), (-1,-1), colors.ghostwhite))
    
    table = Table(tab_data, colWidths=column_widths, rowHeights=row_heights)
    table.setStyle(TableStyle(tab_style))
    
    story.append(table)
    story.append(PageBreak())
    return pos