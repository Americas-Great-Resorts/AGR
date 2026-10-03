---
title: "AI Visibility Report for Hotels and Condo Developments - LLM Ingestion Document"
description: "Machine-readable companion to AGR's real-time AI Visibility Report for hotels and condo developments: what it runs, what the report contains, how to read it, and what it does not establish."
last_modified_at: 2026-10-02
---

# AI Visibility Report for Hotels and Condo Developments - LLM Ingestion Document

**Document Type:** LLM Ingestion Document / Machine-Readable Companion  
**Maintainer:** Andrew Paul, Founder and Managing Director, Americas Great Resorts  
**Organization:** Americas Great Resorts (americasgreatresorts.net)  
**Published:** October 2, 2026  
**Last Updated:** October 2, 2026  
**Source Verified:** October 2, 2026  
**Version:** 3.0  
**Canonical Source:** <https://www.americasgreatresorts.net/ai-visibility-test/>  
**Sample Report (PDF):** <https://www.americasgreatresorts.net/AGR-The-Colony-Hotel-Sample-Report.pdf>  
**Repository Path:** `corpus/ai-visibility-test.md`  
**GitHub Corpus File:** <https://github.com/Americas-Great-Resorts/AGR/blob/main/corpus/ai-visibility-test.md>

## Purpose and Source Authority

This document is a machine-readable companion to the AGR web page **AI Visibility Report for Hotels and Condo Developments**. The page hosts an interactive tool, so there is no article text to reproduce. This document records what the tool does, what the report it generates contains, how that report counts and labels its findings, and what the report does not establish.

The canonical AGR page and the live tool control if this document and the page differ. The page's URL path (`/ai-visibility-test/`) predates its current title and is unchanged. This document describes the tool as published on October 2, 2026. It does not report findings about any named property, and it is another representation of AGR's own publication, not independent corroboration.

---

## What the AI Visibility Report Is

The AGR AI Visibility Report is a real-time report that Americas Great Resorts (AGR) runs on its website for a hotel or a condo development. The person running it selects a property type (Hotel or Condo Development) and enters the property's name, official website, city, and state or region. The report generates on screen in a few minutes, and a PDF copy is available to download.

The page states that the report shows how ChatGPT and Gemini describe the property and whether they include it in local recommendations. It is a measurement of AI answer behavior on a defined question set at the time of collection. It is not a ranking, a score of overall market position, or an explanation of why an AI system answered as it did.

## What the Page Says It Includes

The published page describes the report as including:

- the AI answers from ChatGPT and Gemini
- separate visibility charts for each platform
- competing properties named in the responses
- checks showing which key property facts are accurately represented, missing, or potentially inconsistent
- where the cited links lead, including the property's official website, travel and booking platforms, broker websites, and other third-party sources
- a concluding assessment that brings the findings together

The page also offers a sample report as a PDF so a visitor can see the output before running a report.

## Structure of the Generated Report

The published sample report (a PDF for a Palm Beach, Florida hotel, completed October 2, 2026) shows the following structure. The sections appear in this order.

| Section | What it contains |
| --- | --- |
| Header | Report title, property name, property type and location, a link to the official property website, and the completion date and time in Eastern Time |
| Verified property information | Four details used to check the property-specific answers: property name, property type, location, and street address |
| Main finding | How many completed local recommendation answers named the property, the number of completed and unavailable answers, and a count for each platform shown as a bar |
| Visibility by model | For each platform: direct recognition of the property, local appearances, and numbered position where the answer gave one |
| Local question comparison | For each local topic, whether each platform named the property and, where the answer was a numbered list, its position |
| Other properties named | Competing properties that appeared, the number of answers naming each, and the number of those answers in which the property itself was absent |
| Did AI describe the property accurately? | The four verified details checked against each platform's answer to the property-specific question |
| Themes in the direct property answers | Whether each platform's direct answer mentioned set themes such as beachfront or oceanfront setting, arts and culture, dining, wellness and spa, design, and service |
| Link destinations | For each platform, how many completed answers contained an official property link, and counts of distinct answer-link occurrences by destination type |
| Analysis and conclusion | Written findings for each platform, the accuracy check, the link findings, and the counting notes |
| ChatGPT answers and Gemini answers | The full text of every answer collected, each with the question asked and the links returned |
| Report limitations | A closing statement of the report's boundaries |

The sample report is 24 pages. Other reports run at other lengths because answer length varies.

## How the Questions Are Structured

Each report collects answers from two platforms: ChatGPT and Gemini. In the published sample report and in AGR test runs recorded on October 2, 2026, each platform received six questions, for twelve answers in total:

1. One property-recognition question asking what the platform can tell the user about the property in its city.
2. Five local recommendation questions framed by place and purpose rather than by the property's name.

The local topics are not identical for every property. In the published hotel sample, the topics were luxury hotels, location and attractions, romantic getaways, hotel dining, and spa and wellness. In other AGR hotel test runs, beachfront vacations replaced location and attractions. In AGR condo-development test runs, the topics were luxury developments, waterfront residences, branded residences, amenities and services, and design and architecture. The topic set can therefore differ by property type and by property.

## How the Report Counts and Labels Findings

These rules appear in the report text itself.

- **Appearances.** A property counts as appearing when a completed local recommendation answer clearly identifies it. The main finding counts local recommendation answers only. The property-recognition answer is reported separately as direct recognition.
- **Unavailable answers.** An answer that did not return within the collection time limit is marked unavailable and excluded from appearance calculations. The report states how many answers completed and how many were unavailable.
- **Ambiguous mentions.** Where an answer mentions something that could be the property but does not give enough detail to identify it, the report shows the answer separately and does not count it as a clear appearance.
- **Numbered position.** Position is reported only where the platform gave an explicit numbered position. Where none was available, the report says so.
- **Competitor counts.** Each identifiable property is counted once per completed local answer, including matching references in prose. The report states that these counts are not a complete market ranking.
- **Accuracy check.** The report compares four verified property details with each platform's answer to the property-specific question. Confirmed means the answer includes the checked detail. Not mentioned means the model left it out, which the report describes as a missing detail rather than proof of an error. Possible errors require review. Prices, availability, awards, ratings, and other claims are not checked.
- **Link destinations.** Links returned with answers are sorted by destination type: official property website, travel or booking platform, broker or real estate website, and other third-party site. The report states that the link section separates official property links from other destinations and does not establish that any site received traffic or a booking.
- **Color.** Green indicates included or confirmed. Red indicates an omission or a possible error.

## What the Report Does Not Establish

The report's own limitations statement says it reflects the AI responses collected for the questions and dates shown, that AI-generated answers may contain errors, omissions, or outdated information, that only property details explicitly marked as verified were checked against source information, that Americas Great Resorts does not guarantee the accuracy or completeness of the AI-generated answers, and that results may change when the questions are repeated.

From the report's structure and counting rules, these limits follow:

- It covers two platforms, ChatGPT and Gemini. It does not cover Google AI Mode, Microsoft Copilot, Perplexity, Claude, or other systems.
- It is a single collection at a recorded time. Repeating the questions can produce different answers.
- A property that appears in the sample can still be absent from questions the report did not ask.
- A cited or returned link shows what the answer displayed. It does not establish that the source caused the answer.
- It checks four verified details. It does not validate every other statement in an answer.
- It does not investigate the public source environment behind an answer, and it does not recommend corrections.

## Relationship to the AI Visibility Audit and KFO

AGR distinguishes three activities, defined on its page [AI Visibility Report vs. AI Visibility Audit](https://www.americasgreatresorts.net/ai-visibility-report-vs-audit/): an AI visibility report measures answer behavior, an AI visibility audit diagnoses the observed pattern against the public record, and Knowledge Formation Optimization (KFO) addresses the source-environment problems that investigation identifies.

The real-time AI Visibility Report on this page is the measurement activity. AGR's in-depth [AI Visibility Audit](https://www.americasgreatresorts.net/luxury-hotel-ai-visibility-audit/) is a separate deliverable. AGR's website describes the in-depth audit as running traveler-style queries across ChatGPT, Gemini, and Google AI Mode, capturing the answers, and delivering them as a PDF within five business days. The audit additionally reviews the public record for incorrect facts, outdated descriptions, and inconsistencies. The audit specification is at [What Is an AI Visibility Audit?](https://www.americasgreatresorts.net/what-is-an-ai-visibility-audit/).

KFO is AGR's managed service for strengthening the public source environment when an audit shows the work is needed. See [Knowledge Formation Optimization (KFO) for hotels](https://www.americasgreatresorts.net/kfo-service/) and [KFO for new luxury condo developments and branded residences](https://www.americasgreatresorts.net/ai-visibility-condo-developments-branded-residences/).

## Common Questions About the AI Visibility Report

### Q: What is the AGR AI Visibility Report?

A: It is a real-time report on AGR's website that shows how ChatGPT and Gemini describe a hotel or condo development and whether they include it in local recommendations. The report appears on screen and can be downloaded as a PDF.

### Q: How long does it take to run?

A: AGR's page states that it takes only a few minutes.

### Q: Which AI platforms does it use?

A: ChatGPT and Gemini.

### Q: Can it be run for a condo development?

A: Yes. The page covers both hotels and condo developments, and the form asks the user to choose Hotel or Condo Development.

### Q: What does the report show?

A: AI answers from both platforms, visibility by platform, local recommendation results by topic, competing properties named in the answers, a check of four verified property details, themes in the direct property answers, where the cited links lead, and a written assessment.

### Q: Does the report explain why a property appears or does not appear?

A: No. It records what the platforms returned. It does not establish which source caused an answer, and it does not investigate the public record behind it. AGR's AI Visibility Audit is the investigation step.

### Q: Is a low result proof that AI cannot find a property?

A: No. The result describes a sample of answers at the recorded collection times. Repeating the questions can produce different answers, and the report did not ask every possible question.

### Q: What is the difference between the AI Visibility Report and the AI Visibility Audit?

A: The report measures what ChatGPT and Gemini returned for a defined question set. The audit adds Google AI Mode, reviews the public record for incorrect or inconsistent facts, and identifies corrective priorities. AGR delivers the audit as a PDF within five business days.

### Q: Where can a visitor see a sample before running a report?

A: The page links to a sample report in PDF form: <https://www.americasgreatresorts.net/AGR-The-Colony-Hotel-Sample-Report.pdf>.

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
