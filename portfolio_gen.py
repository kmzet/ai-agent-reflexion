import os
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.units import inch

# Define the file name
file_name = "Operation-AI-Architect-Portfolio.pdf"

def generate_portfolio():
    doc = SimpleDocTemplate(file_name, pagesize=LETTER,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=72)
    styles = getSampleStyleSheet()
    
    # Custom Styles
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=24, spaceAfter=20, textColor=colors.HexColor("#1A73E8"))
    heading_style = ParagraphStyle('HeadingStyle', parent=styles['Heading2'], fontSize=16, spaceBefore=15, spaceAfter=10, textColor=colors.HexColor("#202124"))
    body_style = ParagraphStyle('BodyStyle', parent=styles['Normal'], fontSize=11, leading=14, spaceAfter=10)
    bold_body = ParagraphStyle('BoldBody', parent=body_style, fontName='Helvetica-Bold')
    quote_style = ParagraphStyle('QuoteStyle', parent=body_style, leftIndent=20, italic=True, textColor=colors.grey)

    content = []

    # Title & Header
    content.append(Paragraph("Technical Portfolio: Operation AI Architect", title_style))
    content.append(Paragraph("<b>Candidate:</b> Infrastructure TAM & AI Builder", body_style))
    content.append(Paragraph("<b>Objective:</b> Bridging the gap between Cloud Infrastructure (GKE/GPU) and Agentic AI Engineering.", body_style))
    content.append(HRFlowable(width="100%", thickness=1, color=colors.grey, spaceBefore=10, spaceAfter=20))

    # Executive Summary
    content.append(Paragraph("Executive Summary", heading_style))
    content.append(Paragraph(
        "This project documents a strategic pivot into AI Architecture, focusing on high-throughput model serving, "
        "distributed orchestration, and automated evaluation of agentic workflows. The focus is on reducing "
        "operational costs (OpEx) while increasing the reliability of non-deterministic AI systems.", body_style))

    # Table of Core Competencies
    data = [
        ["Domain", "Key Technology Stack", "Architectural Value"],
        ["Inference", "vLLM, GKE, NVIDIA L4", "High-throughput serving via PagedAttention"],
        ["Orchestration", "Ray.io, LangGraph", "Distributed compute and stateful agent logic"],
        ["Evaluation", "LangSmith, Python Sandboxing", "Automated 'Loss Function' for code execution"],
        ["Integration", "OpenAI SDK, Gemini 2.5", "Vendor-agnostic API design and private hosting"]
    ]
    t = Table(data, colWidths=[1.2*inch, 2.5*inch, 2.8*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F2F2F2")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    content.append(t)
    content.append(Spacer(1, 18))

    # Sprint 1
    content.append(Paragraph("Project 1: High-Throughput Inference with vLLM", heading_style))
    content.append(Paragraph(
        "<b>Problem:</b> Standard model serving is memory-inefficient, leading to high GPU fragmentation and OOM errors.", bold_body))
    content.append(Paragraph(
        "<b>Solution:</b> Deployed Meta-Llama-3-8B on Google Kubernetes Engine (GKE) using the vLLM engine. "
        "Implemented PagedAttention to manage VRAM like OS paging, allowing for 4x higher concurrency on a single NVIDIA L4 GPU.", body_style))

    # Sprint 2 & 3
    content.append(Paragraph("Project 2: Orchestration & Private API Architecture", heading_style))
    content.append(Paragraph(
        "<b>Solution:</b> Designed a vendor-agnostic architecture using the OpenAI Python SDK. By re-routing "
        "standard API calls to a private GKE endpoint, I enabled enterprise-grade data privacy while maintaining "
        "developer familiarity with the OpenAI spec.", body_style))

    # Sprint 4
    content.append(Paragraph("Project 3: Agentic Reflexion & Automated Evaluation", heading_style))
    content.append(Paragraph(
        "<b>Problem:</b> AI Agents are non-deterministic. Without a 'Loss Function,' it is impossible to guarantee "
        "code quality in production.", bold_body))
    content.append(Paragraph(
        "<b>Solution:</b> Built a <b>Reflexion Agent</b> using LangGraph that employs a 'Designer-Critic' loop. "
        "The system does not just output code; it critiques its own work and iterates until the code is valid.", body_style))
    content.append(Paragraph(
        "<b>Evaluation Harness:</b> Integrated <b>LangSmith</b> for real-time observability. Built a custom "
        "evaluator that runs generated code in an isolated sandbox to provide a binary Pass/Fail score. "
        "This transforms LLM outputs into verifiable engineering artifacts.", body_style))

    # Final ROI
    content.append(Spacer(1, 12))
    content.append(Paragraph("Strategic Outcome", heading_style))
    content.append(Paragraph(
        "By combining infrastructure knowledge with agentic design, I can build AI systems that are: "
        "1) Cost-optimized via efficient serving, 2) Private by hosting on-cluster, and 3) Reliable via "
        "automated evaluation pipelines.", body_style))

    doc.build(content)

generate_portfolio()
