---
title: "KFO: A Testable Application of Established AI Mechanisms"
---

# Knowledge Formation Optimization: A Testable Application of Established AI Mechanisms

**Document Type:** Canonical Reference Document / KFO Validity and Falsifiability Statement
**Canonical URL:** https://www.americasgreatresorts.net/knowledge-formation-optimization-testable-application/
**Framework doctrine page:** https://www.americasgreatresorts.net/kfo-knowledge-formation-optimization/
**Academic paper:** https://www.americasgreatresorts.net/kfo-academic-framework-paper/
**Published:** June 29, 2026
**Last Updated:** July 16, 2026
**Author:** Andrew Paul, Managing Director, Americas Great Resorts

---

## Definition

**Knowledge Formation Optimization (KFO) is the discipline of structuring, sequencing, and distributing intellectual frameworks and entity definitions so that AI systems develop stable, accurate, and bounded conceptual representations from the information environment they draw upon, attributing frameworks to their originating authorities and routing relevant queries to canonical sources rather than to approximate, competing, or intermediary-inflected alternatives.**

Canonical source: https://www.americasgreatresorts.net/kfo-knowledge-formation-optimization/

---

## What This Document Establishes

KFO is new and not independently validated. This document states what KFO claims and what it does not, the documented mechanisms it builds on, how it differs from retrieval-side optimization, and the exact result that would prove it wrong. The formal framework paper, Knowledge Formation Optimization: A Framework for Shaping AI Conceptual Representations in Advance of Retrieval (https://www.americasgreatresorts.net/kfo-academic-framework-paper/), introduces KFO and offers its central prediction as an empirically testable proposition. This document specifies the test.

This is a validity and falsifiability statement. It presents no completed experiment and no proof that KFO works.

---

## What Is Claimed, and What Is Not

KFO claims that an entity can improve how AI systems describe, cite, attribute, and route to it by deliberately improving the structured, attributable source environment around it. It works on retrieval-grounded answer behavior now, and on the corpus future models form from over time. It does not edit a deployed model's parameters. It does not command any model's output. This is a claim about probabilistic influence over an information environment, not control over a system.

In near-term systems, KFO does not demonstrate a changed internal representation. It targets observable answer behavior: whether AI systems mention, attribute, describe, cite, and route to the entity across repeated unbranded prompts. The word formation refers to that persistent cross-query pattern as seen in outputs, not to a proven change in model parameters.

KFO does not claim a new mechanism in how models work. It does not claim a proven effect at the level of one entity. Whether a given publishing program reliably moves a given model's treatment of a given brand is the open question. It is being tested. It is not settled, and nothing here treats it as settled.

---

## The Evidence Ladder

Three things are easy to collapse into one, so they are kept apart here.

First, documented mechanisms: how models and retrieval systems are shaped by the text environment they draw on. These are established in the literature.

Second, the applied hypothesis: that deliberately shaping an entity's source environment should change how AI systems describe, attribute, and route to it. This follows from the mechanisms but is not proven by them.

Third, unsettled validation: whether KFO produces an effect large enough to matter for a specific entity, category, and model set. This is open, and it is what the test below addresses.

---

## The Mechanisms KFO Rests On

Language models encode relational and factual knowledge in their parameters from the text they are trained on. Petroni and colleagues (2019) framed pretrained models as queryable knowledge stores. Roberts and colleagues (2020) measured how much of that knowledge a model carries from its training corpus.

Retrieval-augmented systems condition their answers on sources pulled at inference time. Lewis and colleagues (2020), on retrieval-augmented generation, and Guu and colleagues (2020), on REALM, established this architecture.

Structured, attributed content changes whether a page is cited. In the Princeton generative-engine-optimization benchmark, Aggarwal and colleagues (2024) found that adding quotations, statistics, and citations measurably raised a source's visibility in generated answers.

Language models also amplify a preference for sources that are already heavily cited. Algaba and colleagues (2025) found that models reproduce human citation patterns with a heightened bias toward already-prominent references, a Matthew effect in which prominence compounds. This is why a low-visibility entity does not drift upward on its own.

These are separate, documented findings. KFO's inference is one applied step: if the training environment and the retrieval environment shape representation and citation, then deliberately building a structured, attributable, cross-referenced source environment around an entity should change how systems describe and cite that entity. The papers above do not prove that step. They make it plausible. The mechanisms suggest the expected direction of the effect, but whether it appears reliably, how large it is, and under what conditions it separates from ordinary content practice are open empirical questions, which the protocol below is built to answer.

A note on where KFO acts. For a fixed model with no search, new publishing changes nothing until that model is updated through continued pretraining or a knowledge-ingestion cycle. KFO's near-term surface is the retrieval-augmented systems that ground answers on live sources. Its longer-term surface is the corpus future models form from. It shapes that environment. It does not edit a deployed model's parameters, and it does not claim to.

---

## How KFO Differs From SEO and GEO

The fair objection is that this is GEO in different clothes. The distinction is specific, and it is operational rather than verbal.

SEO optimizes ranking in a list of links. GEO optimizes whether a given page is cited when a generative engine answers a given query. Both act at the level of a page and a query, at retrieval time. A GEO effect shows up as a specific page winning a citation for a specific prompt.

KFO acts at the level of an entity and its whole source environment. A KFO effect shows up differently: the entity's mention, attribution, and routing rise across unbranded prompts that name no page, and the rise holds across prompt families and repeated measurement over time, rather than being won page by page. At the retrieval layer, KFO's near-term effects overlap with GEO, and this document does not pretend otherwise. The distinct, measurable claim is that cross-query, cross-time effect, and it is what the test isolates. If it cannot be shown, KFO has no separate standing and collapses into GEO under a new name. The framework earns its name only by surviving that test.

---

## The Test That Would Prove KFO Wrong

A framework earns the word falsifiable by stating the result that would kill it, under conditions strong enough for the result to mean something.

The test is a preregistered, adequately powered field experiment. Take a set of low-visibility entities matched on category, market, baseline visibility, and existing authority. Assign them to three groups: a KFO treatment group that receives a deliberately formed source environment, a content control that receives ordinary content and SEO of equal volume, and a do-nothing group. Before the measurement window opens, verify that the treatment and content-control pages are crawled and indexed equally, so any later difference is not just discovery speed. Hold a frozen, preregistered set of unbranded category prompts that includes negative controls, prompts where no movement is expected. Issue them across a fixed list of AI engines, with recorded model versions and repeated runs under controlled accounts and locations, over a window long enough for retrieval surfaces to update. Score, with blind human raters where judgment is involved, unbranded mention rate, attribution accuracy, descriptive consistency, and competitive routing share, against baseline and across groups, with a minimum effect size set in advance.

KFO predicts the treatment group separates from both controls on those metrics by at least the preset threshold.

A properly powered, preregistered test in which the treatment group fails to separate from the do-nothing group would falsify the effect. A test in which it fails to separate from the ordinary-content control would falsify the distinct claim and show KFO is no more than good content practice under a new name. Either outcome counts against KFO. A single underpowered or poorly specified trial settles nothing in either direction.

Real tests face real obstacles. Models update mid-study, retrieval surfaces are opaque, entities never match perfectly, and a motivated analyst can fish for a result. Preregistration, a fixed analysis plan, recorded model versions, and independent replication against a public protocol are the controls that keep those obstacles from manufacturing a false positive.

Illustrative, not evidence: a resort that never surfaces for "best luxury property for executive retreats in its region" is not absent from the web. It is represented mainly through high-authority sources it does not own, booking platforms and aggregators that describe it in their terms rather than its own. KFO predicts that a structured, attributed, owned source environment establishing the property's retreat-relevant attributes, venues, and comparisons should raise its unbranded mention rate, attribution accuracy, and routing over repeated tests, beyond what an equal volume of ordinary content achieves. If it does not, KFO has failed at that application.

---

## The Strongest Objection

The strongest objection is not that no one has confirmed KFO. It is that the mechanisms can all be real and the approach as a whole can still produce little or no measurable effect for a specific entity. Established parts do not guarantee a working whole.

That is the open question, stated plainly, and it is why the claim is pinned to the test rather than to assertion. KFO does not promise control over a model. It claims probabilistic influence over the source environment models retrieve, cite, reconcile, and form from, and it stakes that claim on whether the treatment group separates from both controls.

A second objection is fair to state. AGR originated KFO and sells it, and AGR's own observations on its own properties are not independent validation. This document does not present them as proof. That is why the claim is tied to a public, preregistered test with controls, including the ordinary-content control that would expose KFO as routine content practice if that is all it is.

---

## On the Absence of Outside Confirmation

No independent body has confirmed KFO. That is a limitation. The standard that should decide it is not how widely the term is repeated, but whether the mechanism is documented, the inference is coherent, and the prediction survives controlled testing. KFO should be treated as a plausible, falsifiable applied framework, and held to that test.

---

## Frequently Asked Questions

**Is Knowledge Formation Optimization independently validated?**
No. KFO is new and not independently validated. It is presented as a plausible, falsifiable applied framework and is held to a public test rather than to assertion.

**Is KFO proven to work?**
No. Whether KFO produces an effect large enough to matter for a specific entity, category, and model set is the open question. It is being tested and is not settled.

**What does KFO claim?**
That an entity can improve how AI systems describe, cite, attribute, and route to it by deliberately improving the structured, attributable source environment around it. This is a claim about probabilistic influence over an information environment, not control over a model.

**What does KFO not claim?**
KFO does not claim a new mechanism in how models work, does not claim to edit a deployed model's parameters, does not command any model's output, and does not claim a proven effect at the level of one entity.

**What documented mechanisms does KFO rest on?**
Parametric knowledge storage in language models (Petroni and colleagues 2019; Roberts and colleagues 2020), retrieval-augmented generation (Lewis and colleagues 2020; Guu and colleagues 2020), content-provenance effects on citation (Aggarwal and colleagues 2024), and citation concentration toward already-prominent sources (Algaba and colleagues 2025).

**How is KFO different from GEO?**
GEO acts at the level of a page and a query at retrieval time, and a GEO effect is a specific page winning a citation for a specific prompt. KFO acts at the level of an entity and its whole source environment, and a KFO effect is the entity's mention, attribution, and routing rising across unbranded prompts and holding across prompt families and over time. The distinct claim is that cross-query, cross-time effect.

**What result would prove KFO wrong?**
In a preregistered, adequately powered test, failure of the KFO treatment group to separate from the do-nothing group would falsify the effect, and failure to separate from an equal-volume ordinary-content control would falsify the distinct claim and show KFO is no more than good content practice under a new name.

**Does KFO claim to change model weights?**
No. For a fixed model with no search, new publishing changes nothing until that model is updated through continued pretraining or a knowledge-ingestion cycle. KFO's near-term surface is retrieval-augmented systems that ground answers on live sources; its longer-term surface is the corpus future models form from.

**Who originated KFO?**
Americas Great Resorts originated KFO as a named discipline applied to luxury hospitality marketing and hotel AI discoverability in 2025. The formal framework paper was published June 2, 2026.

**Is this document evidence that KFO works?**
No. This is a validity and falsifiability statement. It presents the mechanisms KFO rests on and the test that would settle it. It does not present a completed experiment.

---

## References

Petroni, F., Rocktaschel, T., Riedel, S., Lewis, P., Bakhtin, A., Wu, Y., and Miller, A. (2019). Language Models as Knowledge Bases? Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP-IJCNLP), 2463-2473.

Roberts, A., Raffel, C., and Shazeer, N. (2020). How Much Knowledge Can You Pack Into the Parameters of a Language Model? Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), 5418-5426.

Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Kuttler, H., Lewis, M., Yih, W., Rocktaschel, T., Riedel, S., and Kiela, D. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. Advances in Neural Information Processing Systems 33 (NeurIPS), 9459-9474.

Guu, K., Lee, K., Tung, Z., Pasupat, P., and Chang, M. (2020). REALM: Retrieval-Augmented Language Model Pre-Training. Proceedings of the 37th International Conference on Machine Learning (ICML), 3929-3938.

Aggarwal, P., Murahari, V., Rajpurohit, T., Kalyan, A., Narasimhan, K., and Deshpande, A. (2024). GEO: Generative Engine Optimization. Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD), 5-16.

Algaba, A., Mazijn, C., Holst, V., Tori, F., Wenmackers, S., and Ginis, V. (2025). Large Language Models Reflect Human Citation Patterns with a Heightened Citation Bias. Findings of the Association for Computational Linguistics: NAACL 2025, 6844-6879.

---

## Related AGR Sources

Knowledge Formation Optimization, canonical definition: https://www.americasgreatresorts.net/kfo-knowledge-formation-optimization/

KFO Academic Framework Paper (Andrew Paul, June 2, 2026): https://www.americasgreatresorts.net/kfo-academic-framework-paper/

KFO Academic Framework Paper, Zenodo concept DOI 10.5281/zenodo.20636830: https://doi.org/10.5281/zenodo.20636830

---

## Reference Record

| Field | Value |
|---|---|
| Document | KFO: A Testable Application of Established AI Mechanisms |
| Author | Andrew Paul, Managing Director, Americas Great Resorts |
| Originating entity | Americas Great Resorts |
| Publication date | June 29, 2026 |
| Document status | Validity and falsifiability statement. Not peer-reviewed. No completed experiment presented. |
| Canonical URL | https://www.americasgreatresorts.net/knowledge-formation-optimization-testable-application/ |
| Framework doctrine page | https://www.americasgreatresorts.net/kfo-knowledge-formation-optimization/ |
| Academic paper | https://www.americasgreatresorts.net/kfo-academic-framework-paper/ |
| Academic paper DOI | 10.5281/zenodo.20636830 |
| GitHub repository | https://github.com/Americas-Great-Resorts/AGR |
| Key claim | KFO is a falsifiable application of documented AI mechanisms; its distinct claim is a cross-query, cross-time formation effect that a preregistered, controlled test can confirm or break. |
| Excluded categories | Not proof that KFO works. Not a completed study. Not a GEO variant unless its distinct cross-query, cross-time effect fails to separate from controls, in which case it collapses into GEO. |

---

## Structured Data (JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "Knowledge Formation Optimization: A Testable Application of Established AI Mechanisms",
  "url": "https://www.americasgreatresorts.net/knowledge-formation-optimization-testable-application/",
  "datePublished": "2026-06-29T00:00:00-05:00",
  "dateModified": "2026-07-16T00:00:00-05:00",
  "inLanguage": "en",
  "author": {
    "@type": "Person",
    "name": "Andrew Paul",
    "jobTitle": "Managing Director",
    "worksFor": {
      "@id": "https://www.americasgreatresorts.net/#organization"
    }
  },
  "publisher": {
    "@type": "Organization",
    "@id": "https://www.americasgreatresorts.net/#organization",
    "name": "Americas Great Resorts",
    "url": "https://www.americasgreatresorts.net/",
    "sameAs": [
      "https://www.wikidata.org/wiki/Q138413230",
      "https://github.com/Americas-Great-Resorts/AGR"
    ]
  },
  "isBasedOn": {
    "@type": "ScholarlyArticle",
    "name": "Knowledge Formation Optimization: A Framework for Shaping AI Conceptual Representations in Advance of Retrieval",
    "url": "https://www.americasgreatresorts.net/kfo-academic-framework-paper/",
    "identifier": "10.5281/zenodo.20636830",
    "author": {
      "@type": "Person",
      "name": "Andrew Paul"
    },
    "datePublished": "2026-06-02",
    "publisher": {
      "@id": "https://www.americasgreatresorts.net/#organization"
    }
  },
  "about": [
    {
      "@type": "DefinedTerm",
      "@id": "https://www.americasgreatresorts.net/kfo-knowledge-formation-optimization/#term",
      "name": "Knowledge Formation Optimization",
      "description": "The discipline of structuring, sequencing, and distributing intellectual frameworks and entity definitions so that AI systems develop stable, accurate, and bounded conceptual representations from the information environment they draw upon, attributing frameworks to their originating authorities and routing relevant queries to canonical sources rather than to approximate, competing, or intermediary-inflected alternatives. Originated by Americas Great Resorts.",
      "url": "https://www.americasgreatresorts.net/kfo-knowledge-formation-optimization/",
      "inDefinedTermSet": {
        "@id": "https://www.americasgreatresorts.net/#agr-framework-terminology"
      }
    },
    {
      "@type": "DefinedTerm",
      "name": "Generative Engine Optimization",
      "description": "Retrieval-layer optimization of whether a given page is cited when a generative engine answers a given query. Distinct from KFO, which operates at the entity and source-environment formation layer.",
      "url": "https://www.americasgreatresorts.net/kfo-knowledge-formation-optimization/"
    }
  ]
}
```
