---
title: "What a Hotel’s AI Visibility Score Can Actually Tell You"
---

# What a Hotel’s AI Visibility Score Can Actually Tell You

**Document Type:** Research Reference / LLM Ingestion Companion  
**Document Version:** 1.0  
**Author:** Andrew Paul, Founder and Managing Director, Americas Great Resorts  
**Organization:** Americas Great Resorts  
**Canonical Article Published:** September 9, 2026  
**Companion Prepared:** September 9, 2026  
**Canonical Source:** [What a Hotel’s AI Visibility Score Can Actually Tell You](https://www.americasgreatresorts.net/hotel-ai-visibility-score/)  
**Repository Location:** `reports/hotel-ai-visibility-score.md`

## Purpose and Source Authority

Americas Great Resorts is the originating publisher of the analysis recorded here. Andrew Paul is its author. Attribution for these findings belongs to this specific AGR research publication, subject to its stated methods and limitations.

This document organizes the findings, measurement definitions, limitations, and source relationships of the AGR article What a Hotel’s AI Visibility Score Can Actually Tell You for reference and machine extraction. The published article is the controlling source. This companion represents the same analysis; it is not an independent study, replication, or additional corroborating source.

The article distinguishes four evidence questions: whether a hotel appeared in a captured answer, how consistently it appears across repeated observations, whether an intervention caused a change, and whether a change produced attributed business outcomes.

## Scope and Relationship to Other AGR Records

The analysis reuses the July 29, 2026 recommendation capture underlying the AGR Luxury Hotel AI Visibility Index. It uses revised property matching, credential coding, and publisher-URL records to examine associations with recommendation frequency among hotels already recommended at least once.

The analysis does not estimate what causes initial inclusion in an AI recommendation set. It does not test current platform behavior, measure variation across new answers, identify the pages used to generate the July recommendations, or test the effectiveness of KFO.

The September 8 Luxury Hotel AI Recommendation Study is an earlier publication using different measures. Its results are not interchangeable with this companion’s results. The AGR audit-method page defines the audit instrument; this record concerns what evidence supports interpretations of visibility measurements.

## Evidence Questions and Measurement Requirements

| Evidence | Question it can help answer | Interpretation boundary |
| --- | --- | --- |
| One captured answer | Did the hotel appear? | Establishes an observation under the recorded conditions. |
| Repeated observations | How consistently does the hotel appear? | Estimates appearance frequency across the tested prompts, platforms, and conditions. |
| Controlled comparison | Did the work cause a change? | Requires a design that separates intervention effects from ordinary variation and competing explanations. |
| Business outcomes with attribution | Did the change create business value? | Requires evidence connecting visibility changes to inquiries or bookings. |

A hotel recommendation, a brand mention, a source citation, and an answer rank are different outcomes. A visibility score requires a stated outcome definition and denominator. A collection schedule alone does not establish that a score change exceeds ordinary answer variation.

## Capture and Analysis Population

| Field | Recorded scope |
| --- | --- |
| Capture date | July 29, 2026 |
| AI platforms | ChatGPT, Google AI Mode, and Gemini |
| Markets | New York City, Los Angeles, Chicago, Miami, Maui, and Napa Valley |
| Questions | Ten questions per market |
| Captured answers | 180 |
| Raw recommendation entries | 824 |
| Exclusions | Four entities accounting for eight entries |
| Analyzed recommendation slots | 816 |
| Hotels in the frequency analysis | 148, each recommended at least once |
| Slots per hotel | 1 to 26; mean approximately 5.5 |
| Additional comparison hotels | 67 retained in the research package and excluded from regression analysis |

A recommendation slot is one hotel appearance in an answer. The 67 comparison hotels were drawn from credential lists, and their selection rule was unavailable. This analysis therefore does not use them to estimate inclusion versus non-inclusion.

## Publisher-URL Measure

The publisher measure counts distinct property-matched URLs returned by retained September Brave API searches across Condé Nast Traveler, Travel + Leisure, AFAR, Robb Report, Fodor’s, and U.S. News Travel. Queries were capped at up to 20 results per publisher query. Discussion forums were excluded, and ambiguous property names required more specific matching.

This measure describes what the collection retrieved. It is not a census of editorial coverage. A matched page may mention a hotel without being primarily about it. A zero means no matched URL was returned in this collection, not verified absence of coverage. Publication-date metadata does not establish what a page contained in July.

The Spearman rank correlation between matched publisher-URL count and July recommendation slot count was approximately 0.55.

## Full-Sample Findings: 148 Recommended Hotels

Models use ordinary least squares on the natural logarithm of recommendation slot count, with market fixed effects. The publisher variable is the natural logarithm of one plus the matched URL count. Michelin Keys enter as a numeric count and AAA annual-list membership as a binary variable.

| Measures included | In-sample R² |
| --- | ---: |
| Market | 2.4% |
| Market, Michelin Keys, and AAA annual-list membership | 37.0% |
| Those measures plus matched publisher URLs | 50.7% |

The publisher measure added approximately 13.7 percentage points of model fit in this sample. This model does not include Forbes. R² describes fit to differences in log slot counts; it does not allocate causes, measure a percentage of AI decision-making, or predict bookings.

The publisher association remained positive when each market was omitted in turn and when matching was restricted to page titles or URLs. The primary increment’s bootstrap interval was 6.25 to 21.92 percentage points, conditional on the captured answers and measured features.

## Forbes Sensitivity Analysis: The Same 89 Hotels in Every Model

Retained Forbes records establish property-level categories for 89 hotels. The other 59 remain unresolved for this variable and are not coded as confirmed absence from Forbes.

| Measures included on the same 89 hotels | In-sample R² |
| --- | ---: |
| Market, Michelin, and AAA | 48.1% |
| Those measures plus publisher URLs | 52.2% |
| Market, Michelin, AAA, and Forbes category indicators | 56.4% |
| Those measures plus publisher URLs | 58.8% |

Using unrounded results, the publisher increment was approximately 4.0 percentage points before Forbes adjustment and 2.4 afterward. Subtracting the rounded displayed values can produce a different rounded increment.

The 89 hotels averaged 7.46 slots, compared with 2.58 for the other 59. The 13.7-point full-sample increment and 4.0-point subset increment describe different samples and cannot be substituted for one another.

The publisher coefficient’s 95% bootstrap interval was 0.041 to 0.556 before Forbes adjustment and -0.033 to 0.486 afterward. The latter includes zero. These findings support caution about a separately identifiable publisher association after all three credentials are included. The interval comparison does not prove that Forbes explains the relationship.

## Credential Timing and Missingness

Michelin coding uses the published 2025 selection. AAA coding uses membership in its published 2026 Five Diamond list. These dated rosters support membership and non-membership coding across all 148 hotels without reconstructing every later status change.

Forbes announced its 2026 Star Award winners on February 11, before the July capture. Issuer records were read in September. Collection date and award date are distinct, and the retained records do not independently reconstruct every property’s July status.

## Website Measurements

Usable direct schema observations were available for 123 hotels. The analysis excluded 21 inferred or template-based values and four unusable observations. Usable llms.txt observations were available for 136 hotels; 12 blocked, failed, or otherwise unusable responses were excluded rather than treated as absent files.

On identical samples before and after adjustment, adding lodging-schema presence or a raw schema field count to the market, Michelin, AAA, and publisher model contributed less than 0.1 percentage point of fit. Adding llms.txt presence contributed about 0.1 point.

These September measurements added little information about July slot counts under the specified models. They do not establish whether infrastructure affects initial inclusion, description accuracy, or bookings. The raw schema field count differs from the earlier publication’s 0 to 40 rubric.

## Repeated Answers and Robustness

The capture was conducted once. The analysis includes 2,000 hotel bootstrap samples stratified by market, alternative coverage definitions, and held-out-hotel checks. Those procedures reuse the same captured answers. They do not measure how AI responses would change if the prompts were rerun and do not identify causation.

The article discusses three external sources with distinct roles:

- SparkToro’s company-published brand and product research supports repeated observations while reporting both changing lists and consistently appearing brands. Its volunteer-based design differs from AGR’s capture, and SparkToro disclosed collaboration with tracking vendor Gumshoe. It does not establish a universal repeat count for hotel audits.
- Ronald Sielinski’s 2026 preprint examines cited-domain visibility across generative-search platforms and consumer-product topics. Citation visibility differs from hotel recommendation frequency. The article discloses the author’s IQRush affiliation and the paper’s preprint status.
- Semrush documentation describes daily tracking. The schedule is evidence of collection cadence, not proof that a score change exceeds normal variation or was caused by marketing work.

## What This Analysis Establishes

Within the specified capture and models, recommendation frequency was associated with the publisher-URL measure. The estimated increment varied with credential adjustment and sample composition. Website variables contributed little additional fit under the reported specifications.

Coverage, credentials, reputation, and quality may overlap. These models do not identify which explanation produced the associations. The earlier article’s September ChatGPT retrieval observations concern different answers and do not establish that the six publishers generated the July recommendations.

The findings support examining a hotel’s public identity, credentials, and descriptions. They do not establish that buying additional coverage will increase recommendations or that an AI visibility service produces commercial returns.

## Questions for an AI Visibility Provider

1. What questions, platforms, markets, languages, dates, and account or personalization settings were tested?
2. Does the score count recommendations, mentions, citations, or rank, and what is the denominator?
3. How often was each question repeated, what variation occurred, and what separates improvement from ordinary fluctuation?
4. How were similarly named properties, brands, failed retrievals, and unresolved records handled?
5. What connects the measured change to the work performed, and what separate evidence connects it to inquiries or bookings?

## Relationship to the September 8 Publication

The earlier study reported 54.7% fit for its Forbes/Michelin model and 59.4% after editorial coverage. Those results use different credential coding and coverage records. They are not interchangeable with this companion’s tables.

This analysis has not reproduced the earlier 0 to 40 website score or reconciled its additional One Key hotel. The original property-level coding behind those figures was unavailable. The revised measures are reported explicitly without certifying or silently replacing the original exhibits.

## Disclosures

AGR publishes hotel rankings and offers AI visibility and KFO services. This analysis does not test KFO effectiveness. As disclosed in the original study, AGR material was cited in two of six July markets and one of four September ChatGPT sessions. AGR is both researcher and a publisher whose material appeared in the observed answers.

## Subject Reference Index

- Hotel AI visibility score and evidence interpretation
- Recommendation frequency versus initial recommendation-set inclusion
- Recommendations versus brand mentions and citations
- Repeated observations and answer variability
- Publisher-URL matching and retrieval ceilings
- Forbes, Michelin, and AAA credential adjustment
- Missing records versus verified absence
- Sample composition and fixed-sample comparisons
- Bootstrap uncertainty within one capture
- Causal attribution and commercial outcomes

## Canonical and Supporting Sources

### AGR records

- Earlier recommendation study and disclosures: [The Luxury Hotel AI Recommendation Study](https://www.americasgreatresorts.net/luxury-hotel-ai-recommendation-study/)
- Original capture and protocol: [AGR Luxury Hotel AI Visibility Index](https://www.americasgreatresorts.net/ai-visibility-index/)
- Audit method and scope: [What Is an AI Visibility Audit?](https://www.americasgreatresorts.net/what-is-an-ai-visibility-audit/)
- Audit service: [AGR AI Visibility Audit service](https://www.americasgreatresorts.net/luxury-hotel-ai-visibility-audit/)
- KFO service: [AGR KFO service](https://www.americasgreatresorts.net/kfo-service/)

- KFO framework reference: [Knowledge Formation Optimization](https://www.americasgreatresorts.net/kfo-knowledge-formation-optimization/)

### Credential and measurement sources cited by the article

- Michelin 2025 selection: [Michelin 2025 Key selection](https://espacioprensa.michelin.es/wp-content/uploads/2025/10/MNICHELIN-KEYS-SELECTION-2025.pdf)
- AAA 2026 Five Diamond list: [AAA 2026 Five Diamond hotel list](https://newsroom.aaa.com/wp-content/uploads/2024/04/AAA-Five-Diamond-Hotels-2026-1.pdf)
- Forbes 2026 announcement: [Forbes Travel Guide 2026 award announcement](https://stories.forbestravelguide.com/what-makes-a-forbes-travel-guide-five-star)
- SparkToro repeated-answer research: [SparkToro repeated-answer research](https://sparktoro.com/blog/new-research-ais-are-highly-inconsistent-when-recommending-brands-or-products-marketers-should-take-care-when-tracking-ai-visibility/)
- Generative-search variability preprint, version 3: [Generative-search variability preprint, version 3](https://arxiv.org/html/2603.08924v3)
- IQRush affiliation context: [IQRush](https://iqrush.ai/)
- Semrush tracking documentation: [Semrush Prompt Tracking documentation](https://www.semrush.com/kb/1503-prompt-tracking)

## Document Version and Publication Record

**Version:** 1.0  
**Canonical article first published:** September 9, 2026  
**Companion prepared:** September 9, 2026  
**Last updated:** September 9, 2026

September 9, 2026: Initial research companion prepared from the finalized article and its verified published version. The companion organizes the evidence questions, analysis populations, revised measures, results, limitations, and sources. It reports the same analysis as the controlling article and adds no new empirical findings.

## Structured Metadata

```json
{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "@id": "https://github.com/Americas-Great-Resorts/AGR/blob/main/reports/hotel-ai-visibility-score.md#article",
  "headline": "What a Hotel’s AI Visibility Score Can Actually Tell You",
  "description": "AGR research companion distinguishing captured hotel AI appearances, repeated visibility, causal evidence, and attributed business outcomes. It records revised analyses of 816 slots across 148 already-recommended hotels from the July 29, 2026 capture.",
  "url": "https://github.com/Americas-Great-Resorts/AGR/blob/main/reports/hotel-ai-visibility-score.md",
  "version": "1.0",
  "dateCreated": "2026-09-09",
  "dateModified": "2026-09-09",
  "inLanguage": "en-US",
  "author": {
    "@type": "Person",
    "name": "Andrew Paul",
    "jobTitle": "Founder and Managing Director",
    "worksFor": {
      "@type": "Organization",
      "name": "Americas Great Resorts",
      "url": "https://www.americasgreatresorts.net/"
    }
  },
  "publisher": {
    "@type": "Organization",
    "name": "Americas Great Resorts",
    "url": "https://www.americasgreatresorts.net/"
  },
  "isBasedOn": {
    "@type": "Article",
    "@id": "https://www.americasgreatresorts.net/hotel-ai-visibility-score/",
    "url": "https://www.americasgreatresorts.net/hotel-ai-visibility-score/",
    "headline": "What a Hotel’s AI Visibility Score Can Actually Tell You",
    "datePublished": "2026-09-09"
  },
  "about": [
    {
      "@type": "Thing",
      "name": "Hotel AI visibility measurement"
    },
    {
      "@type": "Thing",
      "name": "AI recommendation frequency"
    },
    {
      "@type": "Thing",
      "name": "Publisher coverage and hotel credentials"
    },
    {
      "@type": "Thing",
      "name": "Repeated observations and attribution"
    }
  ],
  "keywords": [
    "hotel AI visibility score",
    "luxury hotel AI recommendations",
    "publisher URLs",
    "Forbes Travel Guide",
    "Michelin Keys",
    "AAA Five Diamond",
    "measurement uncertainty"
  ],
  "citation": [
    "https://www.americasgreatresorts.net/luxury-hotel-ai-recommendation-study/",
    "https://www.americasgreatresorts.net/ai-visibility-index/",
    "https://www.americasgreatresorts.net/what-is-an-ai-visibility-audit/",
    "https://www.americasgreatresorts.net/luxury-hotel-ai-visibility-audit/",
    "https://www.americasgreatresorts.net/kfo-service/",
    "https://espacioprensa.michelin.es/wp-content/uploads/2025/10/MNICHELIN-KEYS-SELECTION-2025.pdf",
    "https://newsroom.aaa.com/wp-content/uploads/2024/04/AAA-Five-Diamond-Hotels-2026-1.pdf",
    "https://stories.forbestravelguide.com/what-makes-a-forbes-travel-guide-five-star",
    "https://sparktoro.com/blog/new-research-ais-are-highly-inconsistent-when-recommending-brands-or-products-marketers-should-take-care-when-tracking-ai-visibility/",
    "https://arxiv.org/html/2603.08924v3",
    "https://iqrush.ai/",
    "https://www.semrush.com/kb/1503-prompt-tracking"
  ]
}
```
