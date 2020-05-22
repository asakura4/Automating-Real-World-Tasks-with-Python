#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate(filename, title, additional_info, table_data):
	styles = getSampleStyleSheet()
	report = SimpleDocTemplate()
	report_title = Paragraph(additional_info, styles["BodyText"])
	table_style = [('GRID', (0,0),(-1,-1), 1, colors.black),
					('FONTNAME', (0,0), (-1,0), 'Helevetica-Bold'),
					('ALIGN', (0,0),(-1,-1),'CENTER')]
	report_table = Table(data=table_data, style=table_style, hAligh="LEFT")
	empty_line = Spacer(1,20)
	report.build([report_title, empty_line, report_info,empty_line,report_table])