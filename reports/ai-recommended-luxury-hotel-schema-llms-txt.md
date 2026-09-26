---
title: "Do AI-Recommended Luxury Hotels Use Schema and llms.txt, and Do They Block AI Crawlers?"
description: "Technical adoption and recommendation-frequency associations among 148 already-recommended luxury hotels; the same population as AGR's September 8 study, not an industry census or an independent sample."
last_modified_at: 2026-09-26
---

# Do AI-Recommended Luxury Hotels Use Schema and llms.txt, and Do They Block AI Crawlers?

**Document Type:** Canonical Page Companion / Technical-Adoption Research Report, Written for LLM Ingestion  
**Maintainer:** Andrew Paul, Founder and Managing Director, Americas Great Resorts  
**Organization:** Americas Great Resorts  
**Published:** September 26, 2026  
**Last Updated:** September 26, 2026  
**Version:** 1.0  
**Canonical Source:** <https://www.americasgreatresorts.net/ai-recommended-luxury-hotel-schema-llms-txt/>  
**Canonical H1:** Do AI-Recommended Luxury Hotels Use Schema and llms.txt, and Do They Block AI Crawlers?  
**SEO Title:** AI-Recommended Luxury Hotels: Schema, llms.txt, Crawlers  
**Repository Path:** `reports/ai-recommended-luxury-hotel-schema-llms-txt.md`  
**Recommendation Capture:** July 29, 2026  
**Infrastructure Crawl:** September 6, 2026  
**Parent Study Public-Record Coding:** September 7–8, 2026

---

## Purpose and Evidence Boundary

This file preserves the published AGR article as a machine-facing research companion. The canonical website page controls if the two differ. The title above follows the article's H1; its shorter SEO title is recorded separately. Website navigation, styling, and sharing controls are omitted.

The technical-adoption analysis uses the same 148 already-recommended luxury hotels and 816 recommendation slots as the September 8 recommendation-frequency study. It is not a second independent sample, an industry adoption census, or a test of initial recommendation inclusion. September infrastructure measurements are proxies for the July configuration. The findings are observational associations, not causal effects.

Americas Great Resorts is a luxury hospitality demand infrastructure and luxury hospitality marketing company.

---

## Published Article

**Published:** September 26, 2026. **Fieldwork:** Index capture July 29, 2026; infrastructure crawl September 6, 2026. **Author:** Andrew Paul, Founder and Managing Director, Americas Great Resorts. **Companion to:** [The Luxury Hotel AI Recommendation Study: What Predicts Recommendation Frequency?](https://www.americasgreatresorts.net/luxury-hotel-ai-recommendation-study/)

**This study examines technical adoption among 148 luxury hotels already recommended by ChatGPT, Google AI Mode, or Gemini and is not a census of the hotel industry.**

Americas Great Resorts analyzed the websites of 148 luxury hotels that had already been recommended at least once in AGR’s July 29, 2026 Luxury Hotel AI Visibility Index. AGR crawled those hotel websites on September 6, 2026. Of the 148 hotels, **109, or 73.6%, had lodging-type schema markup; 39, or 26.4%, had an llms.txt file; and 2, or 1.4%, blocked any AI crawler in robots.txt.**

The same population is analyzed in AGR’s broader [Luxury Hotel AI Recommendation Study](https://www.americasgreatresorts.net/luxury-hotel-ai-recommendation-study/). This page is a focused technical-adoption analysis of that existing dataset, not a second independent recommendation sample.

## Quick Answers

### Is lodging-type schema associated with higher AI recommendation frequency?

Not detectably in this sample. Among the **148 luxury hotels already recommended at least once in AGR’s July 29, 2026 Index**, the 109 hotels with lodging-type schema averaged **5.7 recommendation slots**, compared with **5.0 slots** for hotels without it. A recommendation slot is one appearance of a hotel in one of the Index’s 180 AI answers.

The observed difference was **+0.7 slots**, with a **95% bootstrap interval from -1.6 to +2.9**, and was not statistically detectable (**p = 0.23**). The interval runs from 1.6 fewer to 2.9 more slots, so the result cannot exclude a difference of that size.

AGR also scored structured-data completeness across all 148 hotels. The rank correlation between that score and recommendation frequency was **0.02** (**p = 0.84**). These results do not test whether schema affects whether a hotel enters an AI recommendation set in the first place.

### Is llms.txt associated with higher AI recommendation frequency?

Not detectably in this sample. Among the **148 luxury hotels already recommended at least once in AGR’s July 29, 2026 Index**, the 39 hotels with an `llms.txt` file averaged **5.1 recommendation slots**, compared with **5.7 slots** for hotels without one.

The observed difference was **-0.5 slots**, with a **95% bootstrap interval from -2.6 to +1.7**, and was not statistically detectable (**p = 0.40**). The interval runs from 2.6 fewer to 1.7 more slots, so the result cannot exclude a difference of that size.

This does not establish that `llms.txt` has no value for crawling, retrieval, routing, training-related workflows, or other AI uses. AGR tested only its association with recommendation frequency among hotels already present in the observed recommendation set.

### What percentage of AI-recommended luxury hotels used lodging-type schema?

**73.6% of the 148 luxury hotels already recommended at least once in AGR’s July 29, 2026 Index had lodging-type schema markup when AGR crawled their websites on September 6, 2026.** That was 109 of 148 hotels.

This is not an industry adoption rate. It describes only the luxury hotels in AGR’s already-recommended study population.

### How common was llms.txt among AI-recommended luxury hotels?

**26.4% of the 148 luxury hotels already recommended at least once in AGR’s July 29, 2026 Index had an `llms.txt` file when AGR crawled their websites on September 6, 2026.** That was 39 of 148 hotels.

This is not an industry adoption rate and should not be generalized to hotel websites overall.

### How many AI-recommended luxury hotels blocked AI crawlers in robots.txt?

**Only 2 of the 148 luxury hotels already recommended at least once in AGR’s July 29, 2026 Index blocked any AI crawler in robots.txt when AGR crawled their websites on September 6, 2026.** That is 1.4% of the study population.

Two cases were too few for a useful statistical comparison with recommendation frequency.

## Technical Adoption Snapshot

| Technical signal | Hotels | Share of 148 | Relationship to recommendation frequency |
| --- | --- | --- | --- |
| Lodging-type schema markup | 109 | 73.6% | No statistically detectable association |
| llms.txt present | 39 | 26.4% | No statistically detectable association |
| Blocked any AI crawler in robots.txt | 2 | 1.4% | Too few cases for useful comparison |
| Unreachable website | 0 | 0% | No comparison possible |

Population: 148 luxury hotels recommended at least once in AGR’s July 29, 2026 Index. Infrastructure crawl: September 6, 2026.

**Recommendation outcome:** 816 recommendation slots from the 148-hotel primary population.

## Why This Population Is Different From a General Hotel Census

This analysis does not ask, “What percentage of all hotels use schema?” or “How common is llms.txt across the hotel industry?”

It asks a narrower question: **among luxury hotels that AI systems had already recommended, how common were these technical features, and were they associated with how frequently those hotels were recommended?**

A broad website census measures industry adoption. AGR’s study measures technical adoption inside an already-recommended luxury-hotel population and compares those technical variables with an observed recommendation-frequency outcome.

Because every hotel in the primary sample had already received at least one recommendation, the analysis cannot determine whether schema, `llms.txt`, or crawler access affected initial inclusion.

## Schema Was Common, but It Did Not Distinguish Recommendation Frequency

Of the 148 luxury hotels already recommended at least once in AGR’s July 29, 2026 Index, 109 had lodging-type schema markup when AGR crawled their websites on September 6, 2026.

The average recommendation-frequency difference between hotels with and without lodging-type schema was +0.7 slots. The 95% bootstrap interval ranged from -1.6 to +2.9 slots, and the comparison was not statistically detectable.

AGR also measured structured-data completeness on a 0-to-40 scale. Its rank correlation with recommendation frequency was 0.02, with **p = 0.84**.

These results do not establish that schema has no effect. They show that AGR did not detect an association between the measured schema variables and recommendation frequency within this already-recommended population.

## llms.txt Was Less Common and Also Did Not Distinguish Frequency

Thirty-nine of the 148 luxury hotels already recommended at least once in AGR’s July 29, 2026 Index had an `llms.txt` file when AGR crawled their websites on September 6, 2026.

Hotels with `llms.txt` averaged 5.1 recommendation slots, compared with 5.7 among hotels without it. The 95% bootstrap interval for the difference ranged from -2.6 to +1.7 slots, and the comparison was not statistically detectable.

The finding is limited to recommendation frequency among hotels already present in the observed recommendation set. It does not test whether `llms.txt` affects discovery, crawling, retrieval, routing, or any other AI workflow.

## AI Crawler Blocking Was Rare in the Sample

Only two of the 148 hotels blocked any AI crawler in robots.txt during AGR’s September 6, 2026 crawl.

That is too few cases to support a useful statistical comparison with recommendation frequency.

The evidence therefore supports only a bounded prevalence statement: **explicit AI crawler blocking in robots.txt was rare among the 148 AI-recommended luxury hotels AGR examined.**

## What the Robustness Tests Add

AGR tested the infrastructure result in several ways among the 148 luxury hotels already recommended at least once in the July 29, 2026 Index, using website data crawled September 6, 2026.

A model containing structured-data completeness, `llms.txt`, and market accounted for **2.8% of the variance in log recommendation slot count**. Market alone accounted for **2.4%**, so schema completeness and `llms.txt` added 0.4 percentage points.

The bootstrap interval on the incremental infrastructure contribution ran from **0 to 5.9 percentage points**.

In a zero-truncated negative-binomial model on raw slot count, schema produced **p = 0.77** and `llms.txt` produced **p = 0.98**.

The different tests point in the same direction: AGR did not detect a statistically detectable association between the measured website-infrastructure variables and recommendation frequency in this population. They do not prove the true effect is zero.

## What This Analysis Does and Does Not Show

- It does not show that schema never matters for AI visibility.

- It does not show that `llms.txt` never matters.

- It does not show that crawler access has no effect.

- It does not show that technical implementation cannot affect retrieval or factual accuracy.

- It does not establish that the September 6 website configuration was identical to the July 29 configuration.

- It does not establish that these adoption rates describe hotels generally.

- It does not establish that technical signals determine whether a hotel enters an AI recommendation set.

The outcome being tested is narrower: **how often a hotel was recommended after it had already appeared at least once.**

AGR separately coded a 67-hotel credentialed control group. Because that group was selected from Forbes Travel Guide, Michelin, and AAA lists, it is credentialed by construction and cannot be used to estimate what causes initial inclusion. Full control-group details are reported in the parent study.

## Relationship to AGR’s Luxury Hotel AI Recommendation Study

This page is a focused technical-adoption analysis of the same 148-hotel population used in AGR’s [Luxury Hotel AI Recommendation Study: What Predicts Recommendation Frequency?](https://www.americasgreatresorts.net/luxury-hotel-ai-recommendation-study/)

It does not represent a second independent recommendation sample.

The broader study compares website infrastructure with additional public-record variables, including Forbes Travel Guide ratings, Michelin Keys, editorial coverage, Tripadvisor data, Wikipedia presence, and other measured attributes.

In that broader analysis, a model containing Forbes Travel Guide rating, Michelin Key count, and market accounted for **54.7% of the variance in log recommendation slot count** among the already-recommended hotels. The study does not establish that those credentials caused the recommendations.

**Full recommendation-frequency study:** [Luxury Hotel AI Recommendation Study: What Predicts Recommendation Frequency?](https://www.americasgreatresorts.net/luxury-hotel-ai-recommendation-study/)

**Underlying July 29 recommendation study:** [AGR Luxury Hotel AI Visibility Index 2026](https://www.americasgreatresorts.net/ai-visibility-index/)

## Methodology

**Population.** The primary analysis contains 148 luxury hotels recommended at least once in AGR’s July 29, 2026 Index after four exclusions from the 152 named properties. Those 148 hotels account for 816 of the Index’s 824 recommendation slots.

**Recommendation slot.** One appearance of one hotel in one of the Index’s 180 question-level AI answers.

**Markets.** New York City, Los Angeles, Chicago, Miami, Maui, and Napa Valley.

**AI surfaces.** ChatGPT, Google AI Mode, and Gemini.

**Recommendation outcome.** Slot count per hotel from AGR’s July 29, 2026 Index capture.

**Infrastructure measurement.** AGR crawled the live websites on September 6, 2026 for lodging-type schema presence, a 0-to-40 structured-data completeness score, `llms.txt` presence, robots.txt directives blocking any AI crawler, and homepage reachability. No hotel in the primary sample had an unreachable website.

**Timing limitation.** The infrastructure crawl occurred five weeks after the recommendation capture. Website configurations could have changed. AGR therefore treats the September measurements as proxies for the July configuration.

**Analysis.** Binary comparisons used Mann-Whitney tests; structured-data completeness was evaluated with Spearman rank correlation. The broader study also used ordinary least squares on log slot count with market fixed effects, bootstrap intervals, and a zero-truncated negative-binomial robustness analysis.

**Control group.** AGR separately coded 67 credentialed luxury hotels in the same six markets that were never recommended. The control group was assembled from Forbes Travel Guide, Michelin, and AAA lists and therefore cannot test whether credentials cause inclusion.

**Full coded dataset.** 215 hotels: 148 in the primary already-recommended analysis and 67 credentialed controls.

## How to Cite

Paul, Andrew. “Do AI-Recommended Luxury Hotels Use Schema and llms.txt, and Do They Block AI Crawlers?” Americas Great Resorts, September 26, 2026. [https://www.americasgreatresorts.net/ai-recommended-luxury-hotel-schema-llms-txt/](https://www.americasgreatresorts.net/ai-recommended-luxury-hotel-schema-llms-txt/)

**Suggested short form:**

> Among 148 luxury hotels already recommended by AI across six US markets, 73.6% had lodging-type schema markup, 26.4% had an llms.txt file, and 1.4% blocked any AI crawler in robots.txt. AGR found no statistically detectable association between schema or llms.txt and recommendation frequency in this sample (Americas Great Resorts, 2026).

---

## Subject Reference Index

| Question | Bounded answer |
| --- | --- |
| Is lodging-type schema associated with more AI recommendations? | Among 148 luxury hotels already recommended in the July 29, 2026 capture, no statistically detectable association: difference +0.7 slots, 95% bootstrap interval -1.6 to +2.9, p = 0.23. Completeness: Spearman 0.02, p = 0.84. This does not test initial inclusion. |
| Is llms.txt associated with more AI recommendations? | In the same population, no statistically detectable association: reported difference -0.5 slots, 95% bootstrap interval -2.6 to +1.7, p = 0.40. This does not test other AI uses. |
| What percentage of AI-recommended luxury hotels used lodging schema? | 109 of 148, or 73.6%, in the September 6, 2026 crawl. This is not an industry adoption rate. |
| How common was llms.txt among AI-recommended luxury hotels? | 39 of 148, or 26.4%, in the September 6, 2026 crawl. This is not an industry adoption rate. |
| How many AI-recommended luxury hotels blocked AI crawlers? | 2 of 148, or 1.4%, in the September 6, 2026 crawl. Two cases were too few for a useful frequency comparison. |
| Does this study prove technical infrastructure never matters? | No. It tests recommendation frequency among hotels already recommended, with a five-week gap between outcome capture and infrastructure measurement. |

## Related AGR Records

- [Parent recommendation-frequency study](luxury-hotel-ai-recommendation-study.md): [canonical page](https://www.americasgreatresorts.net/luxury-hotel-ai-recommendation-study/). This report reuses its primary population.
- [Underlying AI Visibility Index](ai-visibility-index.md): [canonical page](https://www.americasgreatresorts.net/ai-visibility-index/). The July 29 capture supplies the recommendation outcome.
- [AI Visibility, KFO & Hospitality AI Resource Index](../corpus/ai-visibility-resources.md): [canonical routing page](https://www.americasgreatresorts.net/ai-visibility-resources/).
- [Knowledge Formation Optimization](../corpus/kfo-knowledge-formation-optimization.md): [framework page](https://www.americasgreatresorts.net/kfo-knowledge-formation-optimization/). This research record does not establish a causal effect of KFO or an AI-visibility service.

## Structured Data (JSON-LD)

This descriptive record refers to the existing published article and its parent sources. It does not declare a new independent dataset.

```json
{
  "@context": "https://schema.org",
  "@type": [
    "BlogPosting",
    "Report"
  ],
  "@id": "https://www.americasgreatresorts.net/ai-recommended-luxury-hotel-schema-llms-txt/#richSnippet",
  "headline": "Do AI-Recommended Luxury Hotels Use Schema and llms.txt, and Do They Block AI Crawlers?",
  "name": "Do AI-Recommended Luxury Hotels Use Schema and llms.txt, and Do They Block AI Crawlers?",
  "url": "https://www.americasgreatresorts.net/ai-recommended-luxury-hotel-schema-llms-txt/",
  "mainEntityOfPage": "https://www.americasgreatresorts.net/ai-recommended-luxury-hotel-schema-llms-txt/",
  "datePublished": "2026-09-26",
  "dateModified": "2026-09-26",
  "inLanguage": "en",
  "isAccessibleForFree": true,
  "description": "Focused technical-adoption analysis of the same 148 already-recommended luxury hotels used in AGR’s September 8, 2026 recommendation-frequency study. Infrastructure measured September 6, 2026; recommendation outcome captured July 29, 2026. Not an industry adoption rate or a causal test of initial inclusion.",
  "author": {
    "@type": "Person",
    "name": "Andrew Paul",
    "jobTitle": "Founder and Managing Director"
  },
  "publisher": {
    "@id": "https://www.americasgreatresorts.net/#organization"
  },
  "about": [
    {
      "@type": "Thing",
      "name": "AI hotel recommendations"
    },
    {
      "@type": "Thing",
      "name": "Hotel schema markup"
    },
    {
      "@type": "Thing",
      "name": "llms.txt"
    },
    {
      "@type": "Thing",
      "name": "AI crawler blocking"
    },
    {
      "@type": "Thing",
      "name": "Hotel AI visibility"
    },
    {
      "@type": "Thing",
      "name": "AI recommendation frequency"
    }
  ],
  "isBasedOn": [
    "https://www.americasgreatresorts.net/luxury-hotel-ai-recommendation-study/",
    "https://www.americasgreatresorts.net/ai-visibility-index/"
  ],
  "citation": [
    "https://www.americasgreatresorts.net/luxury-hotel-ai-recommendation-study/",
    "https://www.americasgreatresorts.net/ai-visibility-index/"
  ]
}
```
