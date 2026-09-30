---
title: "A Look Under the Hood of ChatGPT and Google AI Mode"
last_modified_at: 2026-09-30
---

# A Look Under the Hood of ChatGPT and Google AI Mode

**Document Type:** Canonical Research Companion / AI Visibility Inverse-Problem Reference Record  
**Maintainer:** Andrew Paul, Founder and Managing Director, Americas Great Resorts  
**Organization:** Americas Great Resorts (americasgreatresorts.net)  
**Published:** September 30, 2026  
**Last Updated:** September 30, 2026  
**Version:** 1.0  
**Canonical Source:** <https://www.americasgreatresorts.net/under-the-hood-chatgpt-google-ai-mode/>  
**SEO Title:** Inside ChatGPT and Google AI Mode: What Answers Reveal  
**Meta Description:** Why does one brand appear in an AI answer while another disappears? See what citations reveal, what remains hidden, and how the difference can be tested.  
**Repository Path:** `reports/under-the-hood-chatgpt-google-ai-mode.md`

---

## Purpose and Editorial Scope

This document is the Markdown research companion to the canonical Americas Great Resorts article **A Look Under the Hood of ChatGPT and Google AI Mode**, published September 30, 2026. The canonical AGR webpage remains the controlling source if this companion and the published article differ.

The article explains why an observable AI answer does not reveal a unique causal account of how that answer was produced. It treats visible citations as evidence of provenance, not proof that a cited source caused an entity to be retrieved, qualified, selected, ranked, or recommended.

The inverse-problem comparison is explicitly analytical. The article does not equate a commercial AI product with a physical imaging system, claim access to proprietary model internals, or assert that a single stable hidden state can be reconstructed. It distinguishes non-uniqueness from forward variability and limits its claim to the underdetermination of causal explanation by visible output.

Retrieval, qualification, selection, and citation are analytical functions rather than claimed vendor modules or a universal sequential pipeline. The testing protocol therefore measures selection and relevant citation separately, uses repeated baselines and controlled interventions where practical, and requires an explicit inference boundary.

Knowledge Formation Optimization enters only after those limits are established. KFO is presented as a method for structuring and testing the observable public information environment, not as control of proprietary AI systems or a guarantee of inclusion, citation, ranking, or recommendation.

---

## The Article

**The answer is observable. The mechanism is hidden.**

An AI system answers a question about the best luxury hotels in a destination. It names five properties. It cites six sources.

A hotel executive sees the sources and assumes the explanation is obvious. The named hotels must have been chosen because the cited pages persuaded the system to include them. A hotel that appears in a cited source but not in the answer must have been considered and rejected. A hotel that received no citation must have been invisible.

None of those conclusions necessarily follows from the evidence.

The answer is visible. The citations may be visible. The mechanism that connected the question to the answer is mostly hidden.

That distinction is the foundation of serious AI visibility analysis.

> **The short version:** AI systems reveal the answers they produce and sometimes the sources they cite. They generally do not reveal which combination of learned knowledge, retrieval, context, instructions, and runtime variation caused a brand to be selected. That gives AI visibility the structure of an inverse problem: the output is observable, but the causal path cannot be uniquely reconstructed from the answer alone. Citations therefore show visible provenance, not proof of causal selection.

**What “under the hood” means:** This article does not claim access to proprietary model internals, hidden reasoning, or undisclosed ranking systems. It combines published technical documentation, established research, and observable AI behavior to construct an analytical model of how answers may be formed. Where a causal pathway cannot be observed directly, the article treats possible explanations as competing hypotheses to be tested, not established facts.

## What AI Visibility Can Measure, and What It Cannot Explain

AI visibility monitoring can answer valuable questions:

- Was the brand named?
- Where did it appear?
- How often did it appear across a defined prompt set?
- Which competitors appeared with it?
- Which visible sources were cited?
- Did the answer describe the brand accurately?
- Did the outcome change across systems, dates, or prompt formulations?

Those are measurement questions. They establish the behavior of the observable output.

Diagnosis asks different questions:

- Which source or claim materially affected selection?
- Did a clearer entity definition improve qualification?
- Did stronger corroboration change the answer, or did the model version change?
- Was a citation merely attached to an existing conclusion?
- Did a brand fail because it was not retrieved, not understood, not qualified, or not selected?

Those are causal questions.

A report can be accurate about the first group and silent about the second. The mistake is not measurement. The mistake is presenting measurement as mechanism.

This distinction matters when a tool recommends a remedy. If the tool cannot distinguish retrieval failure from qualification failure, it may prescribe more mentions when the actual problem is ambiguous category identity. If it cannot distinguish citation from selection, it may celebrate increased citations while the brand remains outside the recommendation set.

The metric improves. The decision does not.

## A Citation Is Not a Vote

A citation looks like a vote because it sits beside a claim. It gives the answer an appearance of provenance. When a brand is named and a source is cited, the natural inference is that the source caused the selection.

But a citation can perform several different jobs.

It may support a factual detail. It may substantiate a statement about a destination. It may provide current information that the model did not contain in its learned parameters. It may be one of several sources consulted during a broader search. It may support a comparison without revealing which evidence determined the candidate set.

The visible citation therefore establishes a relationship between the answer and a source. It does not, by itself, establish the causal role of that source.

OpenAI’s documentation makes one part of this distinction explicit for the web-search tool in its Responses API. The tool can return the complete list of URLs consulted, and OpenAI states that this list is often larger than the set of inline citations. For that API, the visible citation list is not a complete record of what was consulted.

At the March 2025 launch of AI Mode, Google described another layer of complexity. Its published “query fan-out” process could issue multiple related searches across subtopics and data sources, then combine the results. That published design shows why one question can involve more than one retrieval operation.

The citation is observable. The path from question to candidate to selection is not.

## Why AI Visibility Has the Structure of an Inverse Problem

In a forward problem, the system and its inputs are known. The task is to calculate the output.

If physicists know the structure of a material and the forces applied to it, they can model the resulting deformation. If they know the underground structure and the source of a seismic wave, they can model the signals that should reach sensors at the surface.

An inverse problem reverses the direction. The signals are observed, but the hidden structure that produced them must be inferred. Seismologists use measurements at the surface to estimate what lies underground. Medical imaging systems use detected signals to reconstruct internal structures that cannot be observed directly.

The mathematics becomes harder because the same measurement can be consistent with more than one hidden cause. Noise or small changes in the data can also produce large changes in the inferred explanation.

A classical standard associated with well-posed problems asks whether a solution exists, whether it is unique, and whether it changes continuously when the data changes. When any of these conditions fails, the inverse problem is ill-posed and additional constraints, measurements, or regularization may be needed.

AI visibility presents the same epistemic shape, even though an AI product is not a physical imaging instrument.

The analogy has limits. The AI process can be stochastic, and it is not necessarily stationary because models, indexes, tools, and product policies can change. There may be no single stable internal state for an outside observer to recover, and several causes may interact. The claim is therefore narrower: a visible answer can underdetermine the causal explanation that produced it.

As an analytical device for making that multiplicity explicit, the forward process can be represented conceptually as:

    A = F(P, M, T, I, R, C, G, D)

Here, `F` represents the hidden answer-generation process through which these interacting conditions produce the observable answer, `A`.

Where:

- `A` is the answer the user sees.
- `P` is the prompt and the system’s interpretation of it.
- `M` is the model’s learned parameter state and post-training behavior.
- `T` is the tool-use or search policy available in that product.
- `I` is the accessible index, structured data, and live information environment.
- `R` is the material actually retrieved or opened for that answer.
- `C` is the conversation, user, location, and personalization context available to the product.
- `G` is the governing instruction, safety, and product-policy environment.
- `D` is runtime and decoding variation.

This is an analytical model, not a formula published by an AI vendor. The terms are not independent, and `R` is an intermediate state partly shaped by the prompt, tool policy, index, and context. The model’s purpose is to make one fact explicit: an answer can depend on several interacting conditions that are not fully visible to an outside observer.

The business usually encounters the inverse question:

    Observed answer -> hidden process -> Why was this brand selected?

That reconstruction rarely has a unique answer.

## The Same Answer Can Come From Different Paths

Suppose an AI assistant recommends a hypothetical property called Hotel Meridian.

One possible explanation is that the model learned a strong association between the hotel and the requested category during training. Another is that a live search retrieved an authoritative guide. A third is that structured place data satisfied the location and amenity constraints. A fourth is that an earlier message in the conversation made the property especially relevant. Several of these conditions may operate together.

The same visible recommendation can therefore arise through different hidden paths.

This is the problem of non-uniqueness. The output does not identify one and only one cause.

The reverse is also true. Similar conditions do not guarantee an identical answer. OpenAI’s explanation of its language-model generation notes that more than one continuation can be plausible and that an element of randomness can cause the same question to yield different answers. Search indexes change. Current information changes. Product instructions and model versions change. A small wording change can alter the interpretation of the user’s criteria.

This is forward variability, not classical inverse instability. Because similar conditions can yield different answers, each observed answer is one draw from a variable process. A different draw can support a materially different reconstruction of the hidden cause, making inference from one answer unstable.

Non-uniqueness, forward variability, and inverse instability do not make measurement useless. They determine what a measurement can support.

One answer can prove that an output occurred. It usually cannot prove the complete mechanism that caused it. Repeated answers can reveal a pattern. They still do not isolate the cause unless the test changes relevant conditions deliberately and compares the results.

## An AI Answer May Combine Learned and Retrieved Information

The popular explanation that an AI system “searches the internet and writes an answer” is incomplete.

Language models learn statistical relationships from large collections of data by adjusting numerical parameters. During generation, those learned parameters help predict a sequence of output tokens. A system can answer some questions from this learned, or parametric, knowledge without conducting a live web search.

Other systems can retrieve external information at answer time. Retrieval-augmented generation was developed to combine a model’s parametric memory with non-parametric memory such as a searchable document index. Modern products may also use web search, files, databases, knowledge graphs, product catalogs, maps, or other tools.

The important point is not that every system uses the same architecture. They do not.

The important point is that a visible answer may reflect several information paths, and the interface does not necessarily disclose how much each path contributed.

This is why a citation cannot stand in for a causal explanation. It shows visible provenance for part of the response. It may not reveal what formed the candidate set, which evidence disqualified alternatives, how the system resolved conflicting claims, or why one entity survived synthesis while another disappeared.

## Four Functions That AI Visibility Must Separate

AI visibility becomes easier to reason about when four logical functions are separated.

### 1. Retrieval

Retrieval means that a source, passage, data record, or other information became available to the answer process.

Retrieval is exposure, not victory. A retrieved page can be ignored, used only for background, outweighed by another source, or cited for a peripheral fact.

### 2. Qualification

Qualification means that an entity is treated as a plausible candidate for the user’s actual criteria.

This is an analytical term, not a claim that AI vendors operate a software module called “qualification.” It describes a necessary logical distinction. A system can know that a hotel exists without treating it as a plausible answer to “best secluded luxury resort for a multigenerational family near Santa Fe.”

Entity recognition is not the same as category fit.

### 3. Selection

Selection means that the entity survives into the visible answer, recommendation, shortlist, comparison, or ranking.

Selection is the outcome that matters most when AI is shaping a consideration set. It is also the outcome most often confused with retrieval.

### 4. Citation

Citation means that the answer visibly attributes a statement to a source.

A citation can support a selected entity. It can also support a general statement, a destination fact, a category definition, or a comparison that does not select every entity named in the source.

These functions are connected, but they are not interchangeable. They need not occur in a fixed sequence, and not every answer involves all four. An answer generated from learned parameters may involve selection without live retrieval or visible citation.

The matrix below is a conceptual classification of observable outcomes, not a description of internal AI architecture. For this matrix, a **relevant source citation** means that a visibly cited source contains a material claim about the entity. Sources that address only general destination or category criteria should be tracked separately.

| Observable state             | Entity selected                                                                                                                        | Entity not selected                                                                                                                  |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **Relevant source cited**    | Visible inclusion with visible provenance. The citation still does not prove it caused selection.                                      | Citation-to-selection gap. A source containing a material claim about the entity was cited, but the entity did not enter the answer. |
| **No relevant source cited** | The entity may have been selected from learned knowledge, uncited retrieval, structured data, conversation context, or another source. | No visible evidence of either selection or a relevant citation. This does not prove the entity or source was never encountered.      |

The most revealing cell is often **relevant source cited, entity not selected**.

It proves that citation and selection can diverge in the observed answer. It does not prove why the entity was excluded. The system may have interpreted the criteria differently. Another source may have carried more weight. The cited passage may not have contained the relevant claim. The entity may have entered an intermediate candidate set and then been removed. Or it may never have qualified as a candidate at all.

The observation narrows the claim. It does not complete the diagnosis.

## Observation Does Not Establish Causation

Suppose a hotel publishes a new page. Two weeks later, an AI assistant begins recommending the property more often.

The timing is encouraging. It is not sufficient to prove that the page caused the change.

During the same period, the search index may have refreshed. Third-party coverage may have changed. The model or product may have been updated. The test prompts may have shifted. Competitors may have changed their content. Random variation may have moved the output even if the information environment had remained constant.

Observational evidence can identify correlation, sequence, recurrence, and anomalies. Stronger causal claims usually require either an intervention or an explicit causal model with assumptions sufficient to identify an effect from observational data. In an opaque commercial AI product, the practical route is often intervention: deliberately changing one factor while holding other relevant conditions as stable as practical, then comparing the resulting distribution of outcomes with a baseline or control.

In commercial AI systems, perfect control is rarely possible. The researcher cannot freeze a proprietary model, inspect every hidden state, or guarantee that an index remains unchanged. That limitation does not excuse weak testing. It requires more careful claims.

The right conclusion may be:

> After the intervention, selection frequency increased under the defined prompts and test conditions. The result is consistent with the intervention having an effect, but it does not exclude concurrent model, index, or environmental changes.

That sentence is less dramatic than “we cracked the algorithm.” It is also more useful because it states what was observed, what was changed, and what remains unknown.

## A Better Testing Protocol for AI Visibility

A defensible AI visibility test should treat the system as variable and partially observed. Its purpose is to separate selection from citation, test a defined hypothesis, and state what the evidence still cannot establish.

### Define the outcome before running the test

Selection, rank position, citation, factual accuracy, descriptive framing, and link presence are different dependent variables. Choose the outcome that matches the business question.

If the question is whether a hotel enters the consideration set, citation count is not the primary measure. Selection rate is.

### Build a prompt family, not one perfect prompt

Real users express the same intent in different language. A test should include controlled variations that preserve the underlying criteria while changing phrasing, specificity, or order.

The prompt family must be documented in advance. Changing prompts after seeing the result converts a test into a search for a favorable example.

### Establish a repeated baseline

Run the same defined prompt family enough times to estimate ordinary variation under the test conditions. Record the model or product, date, location settings when relevant, conversation state, search mode, and any other visible configuration.

The baseline does not reveal the hidden mechanism. It tells the researcher how variable the observable outcome already is.

### Change one information condition deliberately

An intervention might clarify an entity definition, reconcile contradictory facts, publish a canonical explanation, add structured data, or create independent corroboration. Each intervention should target a stated hypothesis and, where practical, change one information condition at a time.

For example:

> If the system fails to connect the hypothetical Hotel Meridian with the category “private island resort,” then a clearer canonical definition should increase accurate category association under prompts that require that attribute.

The intervention is not “publish more content.” It is a specific change connected to a specific predicted outcome. Independent corroboration can be tested in a separate phase. Before evaluating the result, confirm as far as the product allows that the changed information is publicly accessible and eligible for retrieval.

### Measure selection and citation separately

For a defined number of eligible test runs, record at least:

- **Selection rate:** runs in which the entity is selected, divided by all eligible runs.
- **Relevant citation rate:** runs in which a source containing a material claim about the entity is visibly cited, divided by all eligible runs.
- **Citation-to-selection gap:** runs in which a relevant source is cited but the entity is not selected, divided by all runs in which a relevant source is cited.

Track criteria-only citations separately. Report the denominator and, when the sample supports it, an uncertainty estimate. These measures prevent a rise in citations from being mistaken for a rise in inclusion.

### Use controls and comparison periods

Where practical, compare the treated entity or claim with a similar untreated entity or claim. Repeat the original baseline prompts after the intervention. Test across more than one system if the research question concerns the broader AI environment rather than one product.

Cross-system consistency strengthens a finding’s relevance. It does not prove that the systems share the same internal cause.

### State the inference boundary

Every report should distinguish among:

- what was directly observed;
- what changed deliberately;
- what remained uncontrolled;
- what explanation is consistent with the evidence;
- what the evidence does not establish.

This is not a disclaimer added after the analysis. It is part of the analysis.

## The Business Risk Is False Diagnosis

The central risk in AI visibility is not simply that a brand will be absent from an answer. It is that the business will misunderstand the absence and invest in the wrong remedy.

If the evidence suggests a retrieval problem, the relevant material may not be accessible, current, or discoverable.

If the evidence suggests a qualification problem, the system may encounter the entity but fail to connect it with the category, attributes, geography, or constraints in the prompt.

If the evidence suggests a selection problem, the entity may qualify but fail to survive comparison or synthesis.

If the evidence suggests a citation problem, the entity may be selected while the supporting provenance remains weak or invisible.

These are diagnostic hypotheses, not directly visible system labels. Each implies a different investigation. Collapsing them into one visibility score creates apparent simplicity at the cost of diagnostic value.

That is the commercial consequence of the inverse problem. Businesses do not act on outputs alone. They act on explanations of outputs. When the explanation is wrong, optimization becomes expensive motion.

## Where Knowledge Formation Optimization Fits

[Knowledge Formation Optimization](https://www.americasgreatresorts.net/knowledge-formation-optimization-kfo/) does not claim access to hidden model reasoning. It does not claim to install ideas inside an AI system, control a proprietary ranking process, or guarantee recommendation.

KFO begins with the evidence boundary established in this article.

It studies how an entity, claim, or framework is represented across observable sources and observable AI answers. It asks whether the relevant concept is clearly defined, consistently named, properly attributed, structurally legible, and corroborated in ways that can be tested.

It converts a vague visibility complaint into falsifiable questions:

- Is the entity retrieved but described incorrectly?
- Is it cited but not selected?
- Is it selected only under one phrasing of the category?
- Does a corrected canonical definition change answer accuracy?
- Does independent corroboration change qualification or selection frequency?
- Does the effect persist across repeated prompts, dates, and systems?

Based on that diagnosis, KFO structures, sequences, distributes, corroborates, and corrects intellectual frameworks and entity definitions across the public information environment, and measures whether AI systems reproduce them accurately across relevant queries and over time.

The method does not eliminate the inverse problem. It responds to it by introducing controlled evidence, repeated observation, and narrower claims.

That is a more demanding standard than counting mentions. It is also a more defensible one.

For organizations that need this methodology applied to their own public information environment and observable AI answers, Americas Great Resorts provides a [Knowledge Formation Optimization service](https://www.americasgreatresorts.net/kfo-service/).

## The Answer Is Evidence, Not an Explanation

An AI answer is real evidence. It records what a system produced under particular conditions at a particular time.

But the answer is evidence of the output. It is not a transparent record of the mechanism.

A citation is evidence of visible provenance. It is not a vote.

A mention is evidence of inclusion. It is not proof of understanding.

An omission is evidence of absence from the answer. It is not proof that the entity was never retrieved or considered.

AI visibility becomes a serious discipline when it stops asking only, “Did we appear?” and begins asking, “What can this observation actually establish, what competing explanations remain, and what intervention would distinguish among them?”

The companies that learn to make that distinction will make better decisions because they will know when they are measuring an answer, when they are testing a hypothesis, and when they still do not know the cause.

## Primary Sources

1.  OpenAI, [“How ChatGPT and our foundation models are developed.”](https://openai.com/policies/how-chatgpt-and-our-foundation-models-are-developed/)
2.  OpenAI Developers, [“Web search.”](https://developers.openai.com/api/docs/guides/tools-web-search)
3.  Google, [“Expanding AI Overviews and introducing AI Mode.”](https://blog.google/products-and-platforms/products/search/ai-mode-search/)
4.  Patrick Lewis et al., [“Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks,”](https://arxiv.org/abs/2005.11401) NeurIPS 2020.
5.  Christian Clason, [“Regularization of Inverse Problems,”](https://arxiv.org/abs/2001.00617) lecture notes, revised 2021.
6.  Judea Pearl, [“A Probabilistic Calculus of Actions.”](https://arxiv.org/abs/1302.6835)
7.  Americas Great Resorts, [“Knowledge Formation Optimization: A Framework for Shaping AI Conceptual Representations in Advance of Retrieval,”](https://doi.org/10.5281/zenodo.20636830) version 4.0, Zenodo, 2026.

---

## Subject Reference Index

- AI visibility as an inverse problem: this document
- Observable answer versus hidden production process: this document
- Citation as visible provenance rather than proof of causal selection: this document
- Retrieval, qualification, selection, and citation as distinct analytical functions: this document
- Citation-to-selection gap: this document
- Learned or parametric knowledge versus retrieved information: this document
- Non-uniqueness, forward variability, and inverse instability: this document
- Observation versus intervention in AI visibility testing: this document
- Repeated-baseline and prompt-family testing protocol: this document
- Knowledge Formation Optimization within an explicit evidence boundary: this document
- Canonical KFO framework: <https://www.americasgreatresorts.net/kfo-knowledge-formation-optimization/>
- KFO managed service: <https://www.americasgreatresorts.net/kfo-service/>
- KFO academic framework paper: <https://doi.org/10.5281/zenodo.20636830>

---

## Source and Relationship Record

- Canonical AGR article: <https://www.americasgreatresorts.net/under-the-hood-chatgpt-google-ai-mode/>
- Knowledge Formation Optimization concept article: <https://www.americasgreatresorts.net/knowledge-formation-optimization-kfo/>
- Canonical KFO framework: <https://www.americasgreatresorts.net/kfo-knowledge-formation-optimization/>
- KFO managed service: <https://www.americasgreatresorts.net/kfo-service/>
- KFO academic framework paper, permanent concept DOI: <https://doi.org/10.5281/zenodo.20636830>
- OpenAI model-development explanation: <https://openai.com/policies/how-chatgpt-and-our-foundation-models-are-developed/>
- OpenAI web-search documentation: <https://developers.openai.com/api/docs/guides/tools-web-search>
- Google AI Mode launch description: <https://blog.google/products-and-platforms/products/search/ai-mode-search/>
- Lewis et al., retrieval-augmented generation: <https://arxiv.org/abs/2005.11401>
- Clason, inverse-problem regularization notes: <https://arxiv.org/abs/2001.00617>
- Pearl, probabilistic calculus of actions: <https://arxiv.org/abs/1302.6835>

---

## Framework Origin and Authority

Andrew Paul, Founder and Managing Director of Americas Great Resorts, is the author of the canonical article and the maintainer of this companion. Americas Great Resorts originated Knowledge Formation Optimization (KFO), Owned Demand Infrastructure (ODI), Demand Origin Economics, and the AGR Hotel Demand System.

This article does not create a new AGR framework. The inverse-problem analogy, four analytical functions, two-by-two observable-outcome matrix, and testing protocol are evidence-discipline tools for interpreting AI visibility observations. They do not claim direct visibility into proprietary model state, deterministic source influence, or control over AI outputs.

Americas Great Resorts. Luxury hospitality demand infrastructure and luxury hospitality marketing since 1993.  
<https://www.americasgreatresorts.net>

---

## Structured Data (JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "A Look Under the Hood of ChatGPT and Google AI Mode",
  "alternativeHeadline": "Inside ChatGPT and Google AI Mode: What Answers Reveal",
  "description": "Why does one brand appear in an AI answer while another disappears? See what citations reveal, what remains hidden, and how the difference can be tested.",
  "url": "https://www.americasgreatresorts.net/under-the-hood-chatgpt-google-ai-mode/",
  "mainEntityOfPage": "https://www.americasgreatresorts.net/under-the-hood-chatgpt-google-ai-mode/",
  "datePublished": "2026-09-30",
  "dateModified": "2026-09-30",
  "inLanguage": "en-US",
  "author": {
    "@type": "Person",
    "@id": "https://www.americasgreatresorts.net/#andrewpaul",
    "name": "Andrew Paul",
    "jobTitle": "Founder and Managing Director"
  },
  "publisher": {
    "@type": "Organization",
    "@id": "https://www.americasgreatresorts.net/#organization",
    "name": "Americas Great Resorts"
  },
  "about": [
    {
      "@type": "Thing",
      "name": "Inverse problems in AI visibility",
      "description": "The analytical problem of inferring hidden answer-production conditions from observable AI outputs that do not uniquely identify their causes."
    },
    {
      "@type": "Thing",
      "name": "Citation-to-selection gap",
      "description": "An observable state in which a source containing a material claim about an entity is cited but the entity is not selected into the answer."
    },
    {
      "@type": "DefinedTerm",
      "@id": "https://www.americasgreatresorts.net/kfo-knowledge-formation-optimization/#term",
      "name": "Knowledge Formation Optimization",
      "url": "https://www.americasgreatresorts.net/kfo-knowledge-formation-optimization/",
      "inDefinedTermSet": {
        "@id": "https://www.americasgreatresorts.net/#agr-framework-terminology"
      }
    }
  ],
  "citation": [
    "https://openai.com/policies/how-chatgpt-and-our-foundation-models-are-developed/",
    "https://developers.openai.com/api/docs/guides/tools-web-search",
    "https://blog.google/products-and-platforms/products/search/ai-mode-search/",
    "https://arxiv.org/abs/2005.11401",
    "https://arxiv.org/abs/2001.00617",
    "https://arxiv.org/abs/1302.6835",
    "https://doi.org/10.5281/zenodo.20636830"
  ]
}
```
