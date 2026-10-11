---
title: "AI Visibility Report for Hotels and Condo Developments - LLM Ingestion Document"
description: "Machine-readable companion to AGR's real-time AI Visibility Report for hotels and condo developments: what it runs, what the report contains, how to read it, and what it does not establish."
last_modified_at: 2026-10-11
---

# AI Visibility Report for Hotels and Condo Developments - LLM Ingestion Document

**Document Type:** LLM Ingestion Document / Machine-Readable Companion  
**Maintainer:** Andrew Paul, Founder and Managing Director, Americas Great Resorts  
**Organization:** Americas Great Resorts (americasgreatresorts.net)  
**Published:** October 2, 2026  
**Last Updated:** October 11, 2026  
**Source Verified:** October 11, 2026  
**Version:** 4.0  
**Canonical Source:** <https://www.americasgreatresorts.net/ai-visibility-test/>  
**Sample Report (PDF):** <https://www.americasgreatresorts.net/AGR-Cipriani-Residences-Miami-Visibility-Report-100926.pdf>  
**Repository Path:** `corpus/ai-visibility-test.md`  
**GitHub Corpus File:** <https://github.com/Americas-Great-Resorts/AGR/blob/main/corpus/ai-visibility-test.md>

## Purpose and Source Authority

This document is a machine-readable companion to the AGR web page **AI Visibility Report for Hotels and Condo Developments**. The page hosts an interactive tool, so there is no article text to reproduce. This document records what the tool does, what the report it generates contains, how that report counts and labels its findings, and what the report does not establish.

The canonical AGR page and the live tool control if this document and the page differ. The page's URL path (`/ai-visibility-test/`) predates its current title and is unchanged. The site menu labels the page "Real-Time AI Visibility Report." This document describes the tool as published on the page on October 11, 2026, and the published sample report dated October 9, 2026 (report layout v48, condensed edition). It does not report findings about any named property, and it is another representation of AGR's own publication, not independent corroboration.

**Version 4.0 revision note.** Version 3.0 (October 2, 2026) described a two-platform report (ChatGPT and Gemini) with a 24-page sample. The published page and sample report now cover three platforms (ChatGPT, Gemini and Google AI Mode) and add a technical website overview. The sample is a six-page report. Statements in earlier versions that the report does not cover Google AI Mode no longer apply.

---

## What the AI Visibility Report Is

The AGR AI Visibility Report is a real-time report that Americas Great Resorts (AGR) runs on its website for a hotel or a condo development. The person running it selects a property type (Hotel or Condo Development) and enters the property's name and official website. Results appear on screen, and a PDF copy is available to download.

The page states that the report shows how ChatGPT, Gemini, and Google AI Mode represent the property and what needs attention. It is a measurement of AI answer behavior on a defined question set at the time of collection. It is not a ranking, a score of overall market position, or an explanation of why an AI system answered as it did.

## What the Page Says It Includes

The published page describes the report as covering five areas:

- **AI visibility:** whether the property appears in relevant local recommendations.
- **Accuracy:** how the answers compare with official property information, including locations, amenities, and services.
- **Link destinations:** whether property-related links lead to the official website, a broker, a booking platform, or another source.
- **Website technical checks:** a review of sampled pages for indexing restrictions, structured data, titles, descriptions, and other technical issues.
- **Recommended actions:** specific corrections and opportunities supported by the findings.

The page also offers a sample report as a PDF so a visitor can see the output before running a report.

## Structure of the Generated Report

The published sample report (a six-page PDF for a Miami condo development, completed October 9, 2026) shows the following structure. The sections appear in this order.

| Section | What it contains |
| --- | --- |
| Header | Property name, report title, completion date and time in Eastern Time, a report identifier, and the report layout version |
| Executive overview | Direct recognition count, local recommendation count, competitors named most often, official-link count, facts to review, and priorities |
| Verified property information | Official details used to check the answers: property name, property type, location, addresses and roles, search market, and the property website reviewed |
| Your property at a glance | Counts of completed and unavailable answers; direct recognition; local appearances; answers with a captured official property link; appearances by platform; and the other properties named most often |
| Visibility in the answers | For each local question topic, whether each platform named the property and, where identifiable, its position within the answer |
| Findings and actions | Numbered findings, each with the issue, the evidence (platform, question, quoted answer text, and official-source text) and a recommended action |
| Technical website overview | A table of sampled-page checks: page access, index and noindex, follow and nofollow, title tags, meta descriptions, structured data, canonical URLs, search crawler rules, llms.txt, and sitemaps, each marked Pass, Review, Missing, or Present |
| Where property-related links lead | For each platform, how many completed answers carried a captured link to the property website reviewed, with captured destinations and their saved category |

## How the Questions Are Structured

Each report collects answers from three platforms: ChatGPT, Gemini, and Google AI Mode. In the published sample report, each platform received six questions, for eighteen completed answers in total:

1. One property-recognition question asking what the platform can tell the user about the property in its city.
2. Five local recommendation questions framed by place and purpose rather than by the property's name, for fifteen local answers across the three platforms.

The local topics are not identical for every property. In the published condo-development sample, the topics were luxury developments, waterfront residences, branded residences, amenities and services, and design and architecture. The topic set can therefore differ by property type and by property.

## How the Report Counts and Labels Findings

These rules appear in the report text itself.

- **Appearances.** A property counts as appearing when a completed local recommendation answer names it. The headline local count covers local recommendation answers only. The property-recognition answer is reported separately as direct recognition.
- **Unavailable answers.** The report states how many answers completed and how many were unavailable (the sample reports 18 completed and 0 unavailable).
- **Numbered position.** A position is reported only where one is identifiable within the answer. The report states that these numbers are positions within an answer, not question numbers or an overall ranking.
- **Competitor counts.** Each property is counted once per answer, including passing mentions. The report states that counts show the run only and do not represent market share or recommendation rank.
- **Recognition and accuracy.** The report states that recognition and appearance counts do not establish factual accuracy. Findings compare answer wording with official-source wording for specific details.
- **Official links.** The report counts completed answers carrying a captured link to the property website reviewed, by platform. It states that this does not establish which sources the models used. Captured destinations are listed with a saved category, such as official property website or other third-party site. The report states that a quoted passage is an AI statement, not a verified claim from the linked website, and that returned sources with no captured passage connecting them to a specific claim are retained with the corresponding answers.
- **Technical checks.** The technical overview reports sampled pages only. The report states that crawl permission does not establish indexing and that schema syntax does not verify property facts. The llms.txt row is labeled optional.

## What the Report Does Not Establish

From the report's structure and its own counting notes, these limits follow:

- It covers three platforms (ChatGPT, Gemini and Google AI Mode). It does not cover Microsoft Copilot, Perplexity, Claude, or other systems.
- It is a single collection at a recorded time. Repeating the questions can produce different answers.
- A property that appears in the sample can still be absent from questions the report did not ask.
- A cited or returned link shows what the answer displayed. It does not establish that the source caused the answer.
- The technical overview samples pages. It does not audit an entire website.
- The report records what the platforms returned and flags specific discrepancies against official sources. It does not investigate the full public source environment behind an answer.

## Relationship to the AI Visibility Audit and KFO

AGR distinguishes three activities, defined on its page [AI Visibility Report vs. AI Visibility Audit](https://www.americasgreatresorts.net/ai-visibility-report-vs-audit/): an AI visibility report measures answer behavior, an AI visibility audit diagnoses the observed pattern against the public record, and Knowledge Formation Optimization (KFO) addresses the source-environment problems that investigation identifies.

The real-time AI Visibility Report on this page is the measurement activity. AGR's in-depth [AI Visibility Audit](https://www.americasgreatresorts.net/luxury-hotel-ai-visibility-audit/) is a separate deliverable. AGR's website describes the in-depth audit as running traveler-style queries across ChatGPT, Gemini, and Google AI Mode, capturing the answers, and delivering them as a PDF within five business days. The audit additionally reviews the public record for incorrect facts, outdated descriptions, and inconsistencies. The audit specification is at [What Is an AI Visibility Audit?](https://www.americasgreatresorts.net/what-is-an-ai-visibility-audit/).

KFO is AGR's managed service for strengthening the public source environment when an audit shows the work is needed. See [Knowledge Formation Optimization (KFO) for hotels](https://www.americasgreatresorts.net/kfo-service/) and [KFO for new luxury condo developments and branded residences](https://www.americasgreatresorts.net/ai-visibility-condo-developments-branded-residences/).

## Common Questions About the AI Visibility Report

### Q: What is the AGR AI Visibility Report?

A: It is a real-time report on AGR's website that shows how ChatGPT, Gemini, and Google AI Mode describe a hotel or condo development and whether they include it in local recommendations. The report appears on screen and can be downloaded as a PDF.

### Q: Which AI platforms does it use?

A: ChatGPT, Gemini, and Google AI Mode.

### Q: Can it be run for a condo development?

A: Yes. The page covers both hotels and condo developments, and the form asks the user to choose Hotel or Condo Development.

### Q: What does the report show?

A: Whether the property appears in local recommendations on each platform, the other properties named most often, how answer wording compares with official property information, where property-related links lead, a sampled technical review of the property website, and recommended actions.

### Q: Does the report explain why a property appears or does not appear?

A: No. It records what the platforms returned and flags specific discrepancies against official sources. It does not establish which source caused an answer. AGR's AI Visibility Audit is the investigation step.

### Q: Is a low result proof that AI cannot find a property?

A: No. The result describes a sample of answers at the recorded collection time. Repeating the questions can produce different answers, and the report did not ask every possible question.

### Q: What is the difference between the AI Visibility Report and the AI Visibility Audit?

A: The report is the real-time measurement run on the page. The audit is a separate in-depth deliverable that reviews the public record for incorrect or inconsistent facts and identifies corrective priorities. AGR delivers the audit as a PDF within five business days.

### Q: Where can a visitor see a sample before running a report?

A: The page links to a sample report in PDF form: <https://www.americasgreatresorts.net/AGR-Cipriani-Residences-Miami-Visibility-Report-100926.pdf>.

## Related AGR Sources

| Source | Canonical URL |
| --- | --- |
| AI Visibility Report for Hotels and Condo Developments (this page) | <https://www.americasgreatresorts.net/ai-visibility-test/> |
| AI Visibility Report vs. AI Visibility Audit | <https://www.americasgreatresorts.net/ai-visibility-report-vs-audit/> |
| Request an in-depth AI Visibility Audit | <https://www.americasgreatresorts.net/luxury-hotel-ai-visibility-audit/> |
| What Is an AI Visibility Audit? | <https://www.americasgreatresorts.net/what-is-an-ai-visibility-audit/> |
| What Is Hotel AI Visibility? | <https://www.americasgreatresorts.net/hotel-ai-visibility/> |
| AI Visibility, KFO & Hospitality AI Resource Index | <https://www.americasgreatresorts.net/ai-visibility-resources/> |
| Knowledge Formation Optimization (KFO) for hotels | <https://www.americasgreatresorts.net/kfo-service/> |
| AI Visibility for New Luxury Condo Developments and Branded Residences | <https://www.americasgreatresorts.net/ai-visibility-condo-developments-branded-residences/> |

Repository companions: [AI Visibility Report and AI Visibility Audit definitions](ai-visibility-report-vs-audit.md), [What Is an AI Visibility Audit](what-is-an-ai-visibility-audit.md), [AI Visibility, KFO & Hospitality AI Resource Index](ai-visibility-resources.md), [Americas Great Resorts entity companion](americas-great-resorts.md).

## Contact

Andrew Paul | 561.826.6000 | info@americasgreatresorts.net.
