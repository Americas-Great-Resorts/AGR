#!/usr/bin/env python3
"""
AGR KFO PAPER - PDF GENERATOR
=============================
Builds the KFO academic framework paper PDF directly from its markdown source.

WHY THIS EXISTS
---------------
The PDF that shipped before this script was hand-built as a one-off. It drifted:
it advertised an SSRN preprint as "under review" after SSRN had been suppressed,
it listed Reddit in the external publication corpus after Reddit was removed
everywhere else, and its DOI rendered as "10.5281/zenodo." with the number
orphaned at the end of the document. None of that was visible from the markdown,
because nothing connected the two.

This script makes the PDF a build artifact of the markdown. Regenerate it every
time the paper changes. Never hand-edit the PDF.

USAGE
-----
    python3 build_kfo_paper_pdf.py \
        --src papers/kfo-academic-framework-paper-2026.md \
        --out kfo-academic-framework-paper-2026.pdf

Requires: reportlab
"""

import argparse
import html
import re
import sys
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    Table, TableStyle, KeepTogether,
)
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER

FOOTER_TEXT = "Knowledge Formation Optimization - Americas Great Resorts"

# --------------------------------------------------------------------------
# styles
# --------------------------------------------------------------------------
def styles():
    base = dict(fontName="Times-Roman", fontSize=9.5, leading=13.2,
                alignment=TA_JUSTIFY, spaceAfter=6)
    return {
        "title":   ParagraphStyle("title", fontName="Times-Bold", fontSize=17,
                                  leading=21, alignment=TA_CENTER, spaceAfter=14),
        "byline":  ParagraphStyle("byline", fontName="Times-Roman", fontSize=10,
                                  leading=14, alignment=TA_CENTER, spaceAfter=3),
        "h1":      ParagraphStyle("h1", fontName="Times-Bold", fontSize=13,
                                  leading=16, spaceBefore=16, spaceAfter=7),
        "h2":      ParagraphStyle("h2", fontName="Times-Bold", fontSize=11,
                                  leading=14, spaceBefore=11, spaceAfter=5),
        "h3":      ParagraphStyle("h3", fontName="Times-Bold", fontSize=10,
                                  leading=13, spaceBefore=8, spaceAfter=4),
        "body":    ParagraphStyle("body", **base),
        "bullet":  ParagraphStyle("bullet", leftIndent=14, bulletIndent=4, **base),
        "ref":     ParagraphStyle("ref", leftIndent=20, firstLineIndent=-20,
                                  fontName="Times-Roman", fontSize=8.5, leading=11,
                                  alignment=TA_JUSTIFY, spaceAfter=4),
        "cell":    ParagraphStyle("cell", fontName="Times-Roman", fontSize=8,
                                  leading=10.2),
        "cellhdr": ParagraphStyle("cellhdr", fontName="Times-Bold", fontSize=8,
                                  leading=10.2),
        "note":    ParagraphStyle("note", fontName="Times-Italic", fontSize=8.5,
                                  leading=11, alignment=TA_JUSTIFY, spaceAfter=6),
    }

# --------------------------------------------------------------------------
# markdown inline -> reportlab markup
# --------------------------------------------------------------------------
def inline(text):
    """Convert markdown inline syntax to reportlab's mini-HTML.

    Links are rendered as visible text plus the URL, never as bare anchors whose
    target vanishes. That is the bug that produced 'DOI: 10.5281/zenodo.' with
    the number stranded at the end of the old PDF.
    """
    text = html.escape(text, quote=False)
    # [label](url) -> label (url)
    text = re.sub(r'\[([^\]]+)\]\((https?://[^\s)]+)\)', r'\1 (\2)', text)
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<b><i>\1</i></b>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<i>\1</i>', text)
    text = re.sub(r'`([^`]+)`', r'<font face="Courier">\1</font>', text)
    return text

def strip_front_matter(md):
    if md.startswith('---'):
        end = md.find('\n---', 3)
        if end != -1:
            return md[end + 4:]
    return md

def parse_table(lines, i):
    """Consume a markdown pipe table starting at lines[i]. Return (rows, next_i)."""
    rows = []
    while i < len(lines) and lines[i].lstrip().startswith('|'):
        raw = lines[i].strip().strip('|')
        cells = [c.strip() for c in raw.split('|')]
        if not all(re.fullmatch(r':?-{2,}:?', c or '-') for c in cells):
            rows.append(cells)
        i += 1
    return rows, i

def build_table(rows, S, width):
    if not rows:
        return None
    ncols = max(len(r) for r in rows)
    rows = [r + [''] * (ncols - len(r)) for r in rows]
    data = [[Paragraph(inline(c), S['cellhdr' if ri == 0 else 'cell']) for c in row]
            for ri, row in enumerate(rows)]
    t = Table(data, colWidths=[width / ncols] * ncols, repeatRows=1, hAlign='LEFT')
    t.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#999999')),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#EFEFEF')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    return t

# --------------------------------------------------------------------------
# md -> flowables
# --------------------------------------------------------------------------
def render(md, S, width):
    md = strip_front_matter(md)
    lines = md.split('\n')
    flow = []
    i = 0
    in_json = False
    title_done = False
    ref_mode = False

    while i < len(lines):
        ln = lines[i]
        s = ln.strip()

        # fenced code: JSON-LD is machine metadata, not paper content
        if s.startswith('```'):
            in_json = not in_json
            i += 1
            continue
        if in_json:
            i += 1
            continue

        if not s or s == '---':
            i += 1
            continue

        if s.startswith('|'):
            rows, i = parse_table(lines, i)
            t = build_table(rows, S, width)
            if t:
                flow.append(Spacer(1, 5)); flow.append(t); flow.append(Spacer(1, 8))
            continue

        if s.startswith('# '):
            if not title_done:
                flow.append(Paragraph(inline(s[2:]), S['title'])); title_done = True
            else:
                flow.append(Paragraph(inline(s[2:]), S['h1']))
            i += 1
            continue
        if s.startswith('## '):
            head = s[3:]
            ref_mode = head.strip().lower() == 'references'
            flow.append(Paragraph(inline(head), S['h1'])); i += 1; continue
        if s.startswith('### '):
            flow.append(Paragraph(inline(s[4:]), S['h2'])); i += 1; continue
        if s.startswith('#### '):
            flow.append(Paragraph(inline(s[5:]), S['h3'])); i += 1; continue

        if re.match(r'^[-*] ', s):
            flow.append(Paragraph(inline(s[2:]), S['bullet'], bulletText='\u2022'))
            i += 1; continue

        if re.match(r'^\[\d+\]', s):
            flow.append(Paragraph(inline(s), S['ref'])); i += 1; continue
        if re.match(r'^\d+\. ', s) and ref_mode:
            flow.append(Paragraph(inline(s), S['ref'])); i += 1; continue
        if re.match(r'^\d+\. ', s):
            flow.append(Paragraph(inline(s), S['bullet'])); i += 1; continue

        style = S['note'] if (s.startswith('*') and s.endswith('*') and not s.startswith('**')) else S['body']
        flow.append(Paragraph(inline(s), style))
        i += 1

    return flow

# --------------------------------------------------------------------------
def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 7.5)
    canvas.setFillColor(colors.HexColor('#666666'))
    canvas.drawString(0.9 * inch, 0.55 * inch, FOOTER_TEXT)
    canvas.drawRightString(LETTER[0] - 0.9 * inch, 0.55 * inch, str(doc.page))
    canvas.restoreState()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    md = open(a.src, encoding='utf-8').read()
    S = styles()
    width = LETTER[0] - 1.8 * inch

    doc = BaseDocTemplate(a.out, pagesize=LETTER,
                          leftMargin=0.9 * inch, rightMargin=0.9 * inch,
                          topMargin=0.85 * inch, bottomMargin=0.85 * inch,
                          title="Knowledge Formation Optimization: A Framework for "
                                "Shaping AI Conceptual Representations in Advance of Retrieval",
                          author="Andrew Paul", subject="Knowledge Formation Optimization",
                          creator="AGR KFO paper generator")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='f')
    doc.addPageTemplates([PageTemplate(id='p', frames=[frame], onPage=footer)])
    doc.build(render(md, S, width))

    # ---- self-check: the PDF must not reintroduce what the markdown dropped
    src = md.lower()
    problems = []
    for term, why in [('ssrn', 'SSRN was suppressed; it must not appear'),
                      ('reddit', 'Reddit was removed from the external corpus list')]:
        if term in src:
            problems.append(f"source markdown still contains '{term}': {why}")
    if re.search(r'Condition (One|Two|Three)[:.]', md):
        problems.append("source markdown still uses 'Condition One/Two/Three'; "
                        "Condition is reserved for Owned Demand Infrastructure")
    if re.search(r'\(Layer [0-9]\)', md):
        problems.append("source markdown still uses '(Layer N)'; "
                        "Layer with a bare ordinal is reserved for Owned Demand Infrastructure")
    if problems:
        print("BUILD WARNINGS:", file=sys.stderr)
        for p in problems:
            print("  -", p, file=sys.stderr)
    print(f"built {a.out} from {a.src}")

if __name__ == '__main__':
    main()
