---
title: "Hotel Schema Markup: An Implementation and Validation Guide"
description: "Guide to Hotel and HotelRoom structured data: types, JSON-LD examples, field reference, Google Hotels price markup, validation and maintenance."
last_modified_at: 2026-10-11
---

# Hotel Schema Markup: An Implementation and Validation Guide

**Document Type:** Canonical Page Companion / Implementation Guide  
**Maintainer:** Andrew Paul, Founder and Managing Director, Americas Great Resorts  
**Organization:** Americas Great Resorts  
**Published:** October 6, 2026  
**Last Updated:** October 11, 2026  
**Source Verified:** October 11, 2026  
**Version:** 1.0  
**Canonical Source:** <https://www.americasgreatresorts.net/hotel-schema-markup/>  
**Repository Path:** `corpus/hotel-schema-markup.md`

## Purpose and Evidence Boundary

This file preserves the published AGR guide as a companion, including its code examples, field reference and validation checklist. The canonical website page controls if the two differ. This is another representation of the same AGR publication, not independent corroboration. Website navigation, styling and sharing controls are omitted.

The guide's standards references were checked October 6, 2026. Example Harbor Hotel and its room and price details are fictional teaching data; all example values must be replaced before production use. The code is teaching material for hotel websites and is not AGR's own lodging identity. The guide describes implementation and validation of structured data. It does not establish that schema markup causes search placement, AI recommendation inclusion or bookings. AGR's own measurement of schema among AI-recommended hotels is the [schema and llms.txt study](../reports/ai-recommended-luxury-hotel-schema-llms-txt.md).

## Published Article

Hotel schema markup uses Schema.org types such as `Hotel` and `HotelRoom` to describe a property, its rooms, and their relationship in machine-readable form. A useful implementation helps software distinguish the hotel from its accommodations and keeps those records consistent with the facts guests see. This guide provides linked JSON-LD examples, a field reference, and checks for common errors. It also explains Google Hotels’ separate price-markup requirements, so your team can choose the correct format and validation tool before commissioning the work.

## What is hotel schema markup?

Hotel schema markup is structured data added to a hotel website to describe the property in a format search engines can read. It labels facts such as the hotel’s name, address, contact details, check-in and checkout times, amenities, and room information. Those details should match what guests can see on the website.

The main types serve different purposes:

- **Hotel** describes the property, including its location, contact information, and amenities.
- **HotelRoom** describes a room or accommodation type, including features such as beds, size, and permitted occupancy.
- **Offer** describes the commercial terms of an accommodation offer, when those terms can be kept accurate.

For hotel SEO, the purpose is to make the property and its accommodations easier to interpret consistently. The guide below shows how to connect those records, add the markup to the appropriate pages, and check the implementation.

**In this guide**

- [Choose JSON-LD, a Search feature, or hotel-price markup](#choose-the-right-structured-data-pathway)
- [Prepare hotel facts and stable identifiers](#start-with-the-facts-guests-can-actually-see)
- [Hotel and room field reference](#hotel-schema-field-reference)
- [Example 1: Hotel JSON-LD](#example-1-a-property-page-with-hotel-json-ld)
- [Example 2: HotelRoom graph and room-page code](#example-2-connect-two-rooms-to-the-same-hotel)
- [Example 3: Google Hotels price Microdata](#handle-google-hotels-price-validation-separately)
- [Place markup in website and booking templates](#put-the-markup-in-the-right-templates)
- [Validate hotel schema and record results](#validate-in-layers-and-record-what-passed)
- [Troubleshoot and maintain the implementation](#fix-common-failures-and-maintain-the-implementation)
- [Hotel schema questions and answers](#questions-hotel-teams-ask)

**Standards checked: October 6, 2026.** Example Harbor Hotel and its room and price details are fictional teaching data. Replace all example values before production. The code belongs on the appropriate hotel templates, never as AGR’s own lodging identity.

## Which format should you use for hotel schema markup?

**Use JSON-LD for the general hotel and room examples in this guide. Follow the relevant Google Search specification for a supported feature, and use Microdata for Google Hotels price-accuracy validation.** These are separate implementation tasks with different acceptance tests.

| Purpose | Format for this pathway | Appropriate check | What it does not establish |
| --- | --- | --- | --- |
| Describe the property and rooms | JSON-LD in these examples | JSON parser and Schema Markup Validator | Search placement, AI inclusion, or booking connectivity |
| Implement a documented Search feature, such as breadcrumbs | A format allowed by that feature | Rich Results Test and the feature’s requirements | Guaranteed display or eligibility for unrelated features |
| Reconcile Google Hotels prices | Microdata under the Hotels profile | Booking-flow checks and applicable partner diagnostics | General Search ranking or universal Schema.org conformance |

Google Search supports JSON-LD, Microdata, and RDFa, and generally recommends JSON-LD for ease of maintenance. That recommendation applies to Search structured data; it does not replace the separate Hotels price specification. [Google Search format guidance](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)

For example, a room page can use `BreadcrumbList` to describe its breadcrumb trail. That feature has its own requirements. A valid `Hotel` object alone does not establish eligibility for a dedicated hotel rich result. [Google breadcrumb documentation](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb)

In [AGR’s study of schema adoption among AI-recommended hotels](https://www.americasgreatresorts.net/ai-recommended-luxury-hotel-schema-llms-txt/), 109 of 148 luxury hotels already recommended by AI, or 73.6%, had lodging-type schema when their websites were crawled. AGR found no statistically detectable association between schema presence and recommendation frequency within that sample. The study does not establish whether adding schema affects initial inclusion, and the adoption rate does not represent all hotels. Treat implementation quality and subsequent visibility as separate measurements.

For broader work on access, reviews, business listings, and supporting information, use the [hotel AI recommendation playbook](https://www.americasgreatresorts.net/how-to-get-hotel-recommended-by-ai/).

## Start with the facts guests can actually see

### Build a property and room fact sheet

Get content, operations, and revenue staff to agree on the facts before requesting code. The following fictional fact sheet includes suggested owners and update triggers.

| Field and fictional value | Visible page | Content owner | Source of truth | Update trigger |
| --- | --- | --- | --- | --- |
| Example Harbor Hotel; `https://example.com/` | Property overview | Marketing | Approved property record | Rename or URL change |
| 100 Example Way, Santa Barbara, CA 93101, US | Property overview | Operations | Approved address | Address correction |
| 60 guest rooms | Property overview | Operations | Accommodation inventory | Inventory change |
| Check-in 15:00; checkout 11:00 | Property overview | Operations | Guest policy record | Policy change |
| Guest Wi-Fi; courtyard terrace | Property overview | Operations | Amenity record | Facility change |
| Courtyard King; one king bed; maximum two people; 32 square meters; courtyard view; Wi-Fi | Room listing and Courtyard King page | Rooms team | Approved room specifications | Configuration or amenity change |
| Garden Twin; two single beds; maximum two people; 28 square meters; garden view; Wi-Fi | Room listing and Garden Twin page | Rooms team | Approved room specifications | Configuration or amenity change |
| Courtyard King; January 15–16, 2027; two adults; no children; USD 242 total; breakfast excluded | Booking summary illustration | Revenue and booking team | Selected itinerary and rate record | Itinerary, price, or inclusion change |

Resolve conflicting facts before requesting code. If the room page promises two single beds but the inventory record says one king bed, the rooms team must confirm the marketed configuration and the content owner must correct the page. Leave an unknown fact out until it can be established.

Courtyard King and Garden Twin describe room categories. They do not imply that this 60-room hotel contains only two physical rooms or that either category is available for a particular stay.

Keep three quantities distinct: the hotel’s room count, the number of rooms within an accommodation, and its maximum guest capacity. The illustrated booking has two adults; that party size does not replace the room’s maximum occupancy.

### Assign stable identifiers

A page URL locates a page; `@id` identifies the entity described. Use `https://example.com/#hotel` for the hotel, `https://example.com/rooms/courtyard-king/#room` for Courtyard King, and `https://example.com/rooms/garden-twin/#room` for Garden Twin.

Reuse the same hotel ID across room pages. Give each distinct room description its own ID. Changing a page title does not create a new entity; if URLs or identifiers must change, document how the old and new records map to one another.

Keep the property, its brand, owner, and separately described restaurant distinct. The website’s publisher record must not accidentally become the lodging business. In this guide, AGR publishes the article and has no ownership relationship with the fictional hotel.

## Build the Hotel and HotelRoom examples

### Hotel and HotelRoom fields at a glance

Use this reference to read and adapt the hotel and room examples. Required fields depend on the system consuming the markup; the table explains each field’s purpose and the check that prevents a common mistake.

| Information | Schema field | Purpose | Implementation check |
| --- | --- | --- | --- |
| Hotel identity | `@type`, `@id`, `name`, `url` | Identify the property and its page. | Reuse the hotel ID when another page describes the same property. |
| Address | `address` with `PostalAddress` | Describe the physical address. | Match the approved address shown to guests. |
| Room relationships | `containsPlace` / `containedInPlace` | Connect the hotel and room entities. | Point to the correct IDs; do not create a new hotel for each room. |
| Beds | `bed` with `BedDetails` | Describe bed type and quantity. | One king bed and two single beds are different configurations. |
| Guest capacity | `occupancy` with `QuantitativeValue` | State the room’s maximum occupancy. | Use `maxValue` for the capacity in these examples, not the selected party size. |
| Floor area | `floorSize` with `QuantitativeValue` | State the area and its unit. | The examples use `MTK` for square meters. |
| Amenities | `amenityFeature` with `LocationFeatureSpecification` | Describe an available facility or service. | An amenity existing does not mean it is included in every rate. |
| Room count | `numberOfRooms` | Count rooms in the entity being described. | The hotel’s total is not the number of rooms inside each accommodation. |
| Arrival and departure | `checkinTime` / `checkoutTime` | Describe general check-in and checkout times on the hotel. | Dated booking itineraries are handled separately under the relevant booking profile. |

Add other fields only when the hotel can support and maintain them. Real contact details, photographs, coordinates, and official classifications may belong in a real implementation. They are omitted from these examples because the fictional fact sheet does not establish them. A hotel’s official `starRating` and an `aggregateRating` calculated from guest reviews describe different things.

### Example 1: A property page with Hotel JSON-LD

This fictional property example includes only the facts defined in the fact sheet. `Hotel` already inherits from `LodgingBusiness` and `LocalBusiness`; separate records for those parent types would not create additional businesses. [Hotel type hierarchy](https://schema.org/Hotel)

On the hotel’s property page, place the JSON-LD inside a `<script type="application/ld+json">` element. Google Search supports JSON-LD in the page head or body. Keep the matching guest-facing facts on the page as well.

**Example 1A: fictional property markup**

```
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Hotel",
  "@id": "https://example.com/#hotel",
  "name": "Example Harbor Hotel",
  "url": "https://example.com/",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "100 Example Way",
    "addressLocality": "Santa Barbara",
    "addressRegion": "CA",
    "postalCode": "93101",
    "addressCountry": "US"
  },
  "numberOfRooms": 60,
  "checkinTime": "15:00:00",
  "checkoutTime": "11:00:00",
  "amenityFeature": [
    {"@type": "LocationFeatureSpecification", "name": "Guest Wi-Fi", "value": true},
    {"@type": "LocationFeatureSpecification", "name": "Courtyard terrace", "value": true}
  ]
}
</script>
```

**Example 1B: matching fictional visible content**

```
<section>
  <h1>Example Harbor Hotel</h1>
  <p>Fictional teaching example. This is not an actual hotel listing.</p>
  <p>100 Example Way, Santa Barbara, CA 93101, United States.</p>
  <p>The hotel has 60 guest rooms, guest Wi-Fi, and a courtyard terrace.</p>
  <p>Check-in begins at 3:00 p.m. Checkout is by 11:00 a.m., local hotel time.</p>
  <a href="https://example.com/">Example Harbor Hotel overview</a>
</section>
```

The amenity records state that facilities exist. They do not establish that Wi-Fi is free or included in every rate. Preserve that distinction when adding commercial terms. [Hotel amenity definition](https://schema.org/Hotel)

### Example 2: Connect two rooms to the same hotel

An `@graph` groups related records in one JSON-LD document. The following fictional room-listing example includes a minimal hotel record and two room records. Use the example appropriate to each template, rather than installing every example together.

**Example 2A: fictional integrated graph**

```
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Hotel",
      "@id": "https://example.com/#hotel",
      "name": "Example Harbor Hotel",
      "url": "https://example.com/",
      "containsPlace": [
        {"@id": "https://example.com/rooms/courtyard-king/#room"},
        {"@id": "https://example.com/rooms/garden-twin/#room"}
      ]
    },
    {
      "@type": "HotelRoom",
      "@id": "https://example.com/rooms/courtyard-king/#room",
      "name": "Courtyard King",
      "url": "https://example.com/rooms/courtyard-king/",
      "description": "A room with a courtyard view.",
      "containedInPlace": {"@id": "https://example.com/#hotel"},
      "bed": {"@type": "BedDetails", "typeOfBed": "King", "numberOfBeds": 1},
      "occupancy": {"@type": "QuantitativeValue", "maxValue": 2, "unitCode": "C62"},
      "floorSize": {"@type": "QuantitativeValue", "value": 32, "unitCode": "MTK"},
      "amenityFeature": [
        {"@type": "LocationFeatureSpecification", "name": "Wi-Fi", "value": true}
      ]
    },
    {
      "@type": "HotelRoom",
      "@id": "https://example.com/rooms/garden-twin/#room",
      "name": "Garden Twin",
      "url": "https://example.com/rooms/garden-twin/",
      "description": "A room with a garden view.",
      "containedInPlace": {"@id": "https://example.com/#hotel"},
      "bed": {"@type": "BedDetails", "typeOfBed": "Single", "numberOfBeds": 2},
      "occupancy": {"@type": "QuantitativeValue", "maxValue": 2, "unitCode": "C62"},
      "floorSize": {"@type": "QuantitativeValue", "value": 28, "unitCode": "MTK"},
      "amenityFeature": [
        {"@type": "LocationFeatureSpecification", "name": "Wi-Fi", "value": true}
      ]
    }
  ]
}
</script>
```

**Example 2B: matching fictional visible content**

```
<section>
  <h1>Rooms at Example Harbor Hotel</h1>
  <p>Fictional teaching example. These are room categories, not available inventory.</p>
  <p><a href="https://example.com/">Example Harbor Hotel overview</a></p>
  <h2><a href="https://example.com/rooms/courtyard-king/">Courtyard King</a></h2>
  <p>One king bed, maximum two people, 32 square meters, courtyard view, and Wi-Fi.</p>
  <h2><a href="https://example.com/rooms/garden-twin/">Garden Twin</a></h2>
  <p>Two single beds, maximum two people, 28 square meters, garden view, and Wi-Fi.</p>
</section>
```

`containsPlace` points from the hotel to an accommodation; `containedInPlace` points back. The references reuse existing IDs rather than creating another hotel inside every room. Both directions are shown for teaching clarity. [ContainsPlace](https://schema.org/containsPlace) and [containedInPlace](https://schema.org/containedInPlace)

`BedDetails` expresses bed type and quantity explicitly. `floorSize` uses a numeric value with `MTK` for square meters. Views belong in supported descriptive fields, not an invented `roomView` property. [Bed details](https://schema.org/BedDetails) and [floor size](https://schema.org/floorSize)

For a room-detail page, include that room and the shared hotel identity. The following complete adaptation includes both the visible room description and its JSON-LD.

**Example 2C: fictional room-detail adaptation**

```
<section>
  <h1>Courtyard King at Example Harbor Hotel</h1>
  <p>Fictional teaching example. This is not an available room listing.</p>
  <p>One king bed, maximum two people, 32 square meters, courtyard view, and Wi-Fi.</p>
  <p><a href="https://example.com/">Example Harbor Hotel overview</a></p>
  <p><a href="https://example.com/rooms/courtyard-king/">Courtyard King details</a></p>
</section>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Hotel",
      "@id": "https://example.com/#hotel",
      "name": "Example Harbor Hotel",
      "url": "https://example.com/",
      "containsPlace": {"@id": "https://example.com/rooms/courtyard-king/#room"}
    },
    {
      "@type": "HotelRoom",
      "@id": "https://example.com/rooms/courtyard-king/#room",
      "name": "Courtyard King",
      "url": "https://example.com/rooms/courtyard-king/",
      "description": "A room with a courtyard view.",
      "containedInPlace": {"@id": "https://example.com/#hotel"},
      "bed": {"@type": "BedDetails", "typeOfBed": "King", "numberOfBeds": 1},
      "occupancy": {"@type": "QuantitativeValue", "maxValue": 2, "unitCode": "C62"},
      "floorSize": {"@type": "QuantitativeValue", "value": 32, "unitCode": "MTK"},
      "amenityFeature": [
        {"@type": "LocationFeatureSpecification", "name": "Wi-Fi", "value": true}
      ]
    }
  ]
}
</script>
```

### When an Offer belongs in the model

The room exists independently of a particular price. Keep durable descriptions separate from dates, availability, cancellation terms, and inclusions. A current commercial offer requires a maintained source for those facts.

Schema.org’s lodging guide demonstrates giving offered accommodation both `HotelRoom` and `Product` types, then connecting it to an `Offer`. For rental accommodation, it also specifies `businessFunction` with `http://purl.org/goodrelations/v1#LeaseOut`. [Lodging modeling guide](https://schema.org/docs/hotels.html)

There is a nuance: the `offers` definition permits use beyond its listed expected types, although `HotelRoom` is not explicitly listed. Multi-typing clarifies the generic lodging pattern; it is not permission to claim Google product-rich-result eligibility. [Offers definition](https://schema.org/offers)

Check each relationship before extending the examples: `makesOffer` connects an organization or person to an offer; `itemOffered` connects an offer to its offered item, with its own expected types. The static graphs above intentionally contain no generic Offer. [MakesOffer](https://schema.org/makesOffer) and [itemOffered](https://schema.org/itemOffered)

## Handle Google Hotels price validation separately

### What the current Microdata rule covers

Google’s Hotels specification recommends Microdata and deprecates JSON-LD for hotel price-accuracy validation. General hotel JSON-LD remains a separate use. The examples below follow the detailed Hotels specification and crawler guide, rather than the page’s autogenerated summary. [Google Hotels price specification](https://developers.google.com/hotels/hotel-prices/structured-data/hotel-price-structured-data)

This pathway applies to participating booking flows. Ask the booking or connectivity provider which landing page Google uses, who controls the final summary, and who manages the feed. Website developers and booking providers may need to coordinate; changing a marketing page will not update a separately managed checkout.

### A dated price example and reconciliation checklist

The example below follows the navigation guide’s preferred structure: a combined `Hotel`/`LodgingReservation` container holding the itinerary and one nested `Offer` with the total price. This is a booking-summary container for the Google Hotels profile, separate from the permanent property graph. [Google Hotels navigation guide](https://developers.google.com/hotels/hotel-prices/structured-data/generic-crawler-guide)

The fictional partner hotel identifier is `EHH-DEMO-001`. Stay dates use the navigation guide’s `content="YYYY-MM-DD"` pattern on visible date labels. Check-in and checkout times remain visible as local hotel times. The identifier is a teaching value, not a registered feed ID.

**Example 3: fictional final-page Microdata illustration**

```
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Fictional booking summary illustration</title>
</head>
<body data-nav-stage="checkout" data-nav-stage-final="true">
  <p>Fictional teaching example. This is not an available rate or a reservation.</p>
  <main itemscope
    itemtype="https://schema.org/Hotel https://schema.org/LodgingReservation">
    <h1 itemprop="name">Example Harbor Hotel</h1>
    <meta itemprop="identifier" content="EHH-DEMO-001">
    <h2>Courtyard King: one-night stay</h2>
    <p>Check-in:
      <span itemprop="checkinTime" content="2027-01-15">January 15, 2027</span>, 3:00 p.m. local hotel time.
    </p>
    <p>Checkout:
      <span itemprop="checkoutTime" content="2027-01-16">January 16, 2027</span>, 11:00 a.m. local hotel time.
    </p>
    <p>Guests: <span itemprop="numAdults">2</span> adults;
      <span itemprop="numChildren">0</span> children.</p>
    <p>Base: USD 200.00. Mandatory fee: USD 20.00. Tax: USD 22.00.</p>
    <div itemprop="makesOffer" itemscope itemtype="https://schema.org/Offer">
      <div itemprop="priceSpecification" itemscope
        itemtype="https://schema.org/CompoundPriceSpecification">
        <p>Total for the stay, including mandatory fee and tax:
          <span itemprop="priceCurrency">USD</span>
          <span itemprop="price">242.00</span>
        </p>
      </div>
    </div>
    <p>Breakfast is excluded.</p>
  </main>
</body>
</html>
```

This example tags the hotel-level total while showing the selected room and price breakdown. Its permanent room descriptions remain in the separate room graphs. Adding booking tags alone does not create a Google Hotels feed connection.

- **Identity:** Match the page’s hotel identifier to the real partner feed ID. A property URL is not a substitute.
- **Itinerary:** Preserve the selected room, January 15-16, 2027 stay, two adults, and no children through the booking journey.
- **Total:** Reconcile USD 200 base + USD 20 mandatory fee + USD 22 tax = **USD 242** for the stay. Breakfast is excluded.
- **Access:** The crawler must reach the final amount before personal or payment details are required.

Google specifies one tagged Hotel and one Offer on the final page. Its guide does not explain how a separate Hotel JSON-LD graph affects that limit. Have the booking provider inspect the complete output and resolve conflicting plugin markup. Earlier booking steps also need navigation tags appropriate to the flow. [Google Hotels crawler and final-page requirements](https://developers.google.com/hotels/hotel-prices/structured-data/generic-crawler-guide)

## Where to place hotel schema markup

Place property facts on the property template, room descriptions on the relevant room templates, and maintained itinerary prices in the booking flow. First inspect existing output: the theme, SEO plugin, custom code, and booking engine may already generate overlapping records.

| Template | Recommended scope | Responsible team | Release check |
| --- | --- | --- | --- |
| Property overview | Hotel and visible property facts | CMS developer and content owner | Address, policies, amenities, and inventory agree |
| Room listing | Hotel identity and listed room descriptions | CMS developer and rooms team | Each listed room points to the same hotel |
| Room detail | The specific room and shared hotel identity | CMS developer and rooms team | Beds, capacity, area, and visible text agree |
| Booking or availability | Selected itinerary and current commercial terms; Hotels profile when applicable | Booking developer and revenue team | Selection, dates, fees, currency, and total reconcile |

Repeated references to the same entity are expected. Investigate conflicting facts and competing IDs rather than deleting every repeated hotel reference. Assign one maintained source for each fact and an accountable owner for each output.

### What to give your developer

A hotel marketing director can commission the implementation with these six deliverables:

1. **Approved facts:** The property and room fact sheet, with content and operational owners.
2. **Identity map:** The hotel ID, room IDs, page URLs, and any booking-provider identifiers.
3. **Template inventory:** Representative pages, existing generators, and current CMS, plugin, and booking-engine versions.
4. **Output plan:** Which system generates each record and how content changes reach both the page and markup.
5. **Acceptance tests:** The pages, languages, booking scenarios, and tools included in the release check.
6. **Maintenance plan:** Named owners, update triggers, and a way to restore the previous working version.

Before deployment, save the current output of representative templates. Include both bed configurations, then demonstrate a content change and confirm that the visible page and markup update together. Retest the generating template, not just an isolated code fragment.

### Handle translations, rebrands, and booking providers

Translated pages should preserve the underlying hotel identity while using appropriate localized URLs and descriptions. During a rebrand, establish whether the same property continues before changing its ID. Keep a migration map when URLs change.

Remove discontinued room categories from active listings and stop generating their current offers. Refresh caches when content changes so visible descriptions and markup do not show different versions.

If JavaScript generates the data, inspect both the original response and rendered page. Different consumers may retrieve different output. For a booking engine on another domain, document who controls its templates and how property, room, and partner IDs correspond. The [ChatGPT hotel visibility checklist](https://www.americasgreatresorts.net/how-to-get-my-hotel-on-chatgpt/) covers broader access checks.

## How to validate hotel schema markup

**Validate syntax, vocabulary, visible facts, and the intended consumer separately.** A JSON parser checks syntax. Schema Markup Validator checks the vocabulary and graph. Google’s Rich Results Test addresses supported Search features. Google Hotels prices also need booking-flow and partner checks.

**Checks on these examples:** The three JSON-LD examples parse successfully. Vocabulary checks recorded on October 6, 2026 reported zero errors and warnings for the hotel, linked-room, room-detail, and final price examples. These are code-example checks; no live hotel feed or booking-price reconciliation was tested.

### Syntax and vocabulary

Parse the exact JSON between the script tags, then submit the complete example with its visible content to [Schema Markup Validator](https://validator.schema.org/). Inspect the recognized types, values, relationships, errors, and warnings. Passing the parser alone says nothing about whether a room points to the correct hotel.

Compare extracted values with the fact sheet. Check that Garden Twin has its own ID, two single beds, a two-person maximum, and 28 square meters, and that both room records point to the same hotel. Keep the tested input with its version and result; changed examples need new checks.

### Google feature checks and rendered pages

Use [Rich Results Test](https://search.google.com/test/rich-results) when implementing a supported Google Search feature. A result showing no eligible item does not establish that a generic Hotel graph is invalid. Use the vocabulary validator for that question.

Check representative property, room-listing, room-detail, and booking pages on desktop and mobile. Confirm that visible facts match the markup and that complete code examples can be copied. Record which templates and languages were tested; one passing room page does not cover the entire site.

For a deployed hotel site, inspect access and indexing separately through authorized Search Console access where available. Record checks that could not be performed. A local example test is not a production URL inspection. [Google structured data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)

### Price accuracy and release evidence

The booking team must compare actual selections, the feed record, and the final all-in price. Include supported currencies, mandatory charges, and meaningful booking-flow variations. A generic validator cannot establish that the crawler completed that journey or that the feed price matched.

Use a validation log like this template to preserve the input, result, remaining work, and evidence. These rows are placeholders for a hotel’s deployment records:

| Version | Tool/check | Date | Input | Result | Remaining issue | Evidence location |
| --- | --- | --- | --- | --- | --- | --- |
| Property template release | JSON parser | Record actual date | Exact deployed JSON | Record actual output | Vocabulary and facts still need review | Saved input and test record |
| Room template release | Schema Markup Validator | Record actual date | Rendered room page | Record errors and warnings | Live access is a separate check | Saved result and page version |
| Booking release | Partner diagnostics | Record actual date | Selected itinerary and feed record | Record observed reconciliation | Untested selections remain open | Private partner evidence |

Release the hotel implementation only against the agreed acceptance tests. Retain the exact tested version and identify untested configurations so later changes have a clear starting point.

## Fix common failures and maintain the implementation

Investigate the source of a mismatch before editing the emitted code. A manual correction in one template will be temporary if a plugin or inventory import restores the old value at the next update.

| Symptom | Likely cause | Check | Corrective action |
| --- | --- | --- | --- |
| Two hotel records disagree | Theme and plugin both generate facts | Inventory scripts and IDs | Select an authoritative output and reconcile the other generator |
| A room points to the wrong hotel | Copied or unstable ID | Follow containment references | Repair the identity map and affected templates |
| A property is unrecognized | Invented field or wrong expected type | Consult the property definition | Use a supported property and value, or omit it |
| Rate is stale | Cached or manually entered price | Compare source timestamps and selected stay | Repair rate sourcing and cache refresh |
| Total is too low | Mandatory fee omitted | Recalculate the complete stay | Include applicable charges in the reconciled total |
| Capacity changes with bookings | Party size copied into room capacity | Compare room policy and itinerary fields | Keep permitted occupancy and selected guests separate |
| Markup makes a hidden claim | Old policy or embellished description | Compare visible page and source record | Correct the content and markup together |
| Currency differs between steps | Conversion or formatting mismatch | Trace feed, selection, and checkout | Use the selected currency consistently |
| Rich Results Test finds no eligible item | Generic type lacks that feature’s eligibility | Identify the intended Google feature | Use vocabulary validation and the appropriate feature rules |

For example, a plugin update might change every room’s hotel reference while leaving the property page on the old ID. Restore the approved configuration or repair the generator, refresh affected caches, and retest the property and both room configurations. Editing one cached output will not fix the source of the mismatch.

Content owns the public facts, development owns generation and deployment, and revenue or booking operations owns itinerary pricing. Recheck after material changes to policies, rooms, templates, plugins, inventory, or rate systems. Set a periodic review that matches the hotel’s update frequency and record the last verified version.

## Hotel schema markup: common questions

### Should a hotel use Hotel or LodgingBusiness?

Use `Hotel` for a hotel. It is a more specific subtype of `LodgingBusiness` and inherits its applicable properties. You do not need a duplicate business record for each parent type. Other lodging properties should use an appropriate supported subtype.

### Is JSON-LD deprecated for hotels?

JSON-LD is deprecated for Google Hotels price-accuracy validation, where the checked specification recommends Microdata. It remains supported for general hotel descriptions and applicable Google Search structured-data features. Choose the format for the system that will consume it.

### Why does Rich Results Test find no eligible item?

A generic Hotel or HotelRoom graph may not correspond to a supported rich-result feature. Check its vocabulary in Schema Markup Validator and use Rich Results Test for the specific Search feature you are implementing.

### Do room pages need separate identifiers?

Use a stable identifier for each distinct room description and reuse the hotel’s identifier. The room ID should continue to identify that accommodation description when its page heading changes.

### Should static room pages display dated rates?

Only when the site can maintain the relevant dates, party, inclusions, and price accurately. A static room description can stand without a rate. Put itinerary-dependent terms in a maintained booking flow.

### Do review and FAQ markup create extra Google results for hotels?

Not automatically. Google excludes self-serving local-business review stars on the reviewed business’s own website, including embedded third-party review widgets. Google also stopped showing FAQ rich results in May 2026. Useful guest reviews and visible FAQs still serve readers; their presence does not establish eligibility for those Search displays. [Review-snippet eligibility](https://developers.google.com/search/docs/appearance/structured-data/review-snippet); [Google FAQ feature update](https://developers.google.com/search/updates)

### Does valid schema guarantee AI recommendations?

No. Valid markup describes information; it does not prove that an AI system will retrieve the page or recommend the hotel. Google says its AI Overviews and AI Mode require no special Schema.org markup. Keep hotel information accessible and consistent with the visible page, and measure visibility separately. [Google AI-feature guidance](https://developers.google.com/search/docs/appearance/ai-features)

### Before release

- Confirm the deployed output matches the exact version that was tested.
- Check the visible facts and markup on representative desktop and mobile pages.
- Record passed checks, remaining limitations, and the owner responsible for each follow-up.

Independent luxury hotel and resort teams can [request a free AI Visibility Audit](https://www.americasgreatresorts.net/luxury-hotel-ai-visibility-audit/) to see how ChatGPT, Gemini, and Google AI Mode describe their property. Findings arrive within five business days and cover observed AI visibility and any errors found in the property’s public record.

---

## How to Cite

Paul, Andrew. "Hotel Schema Markup: An Implementation and Validation Guide" Americas Great Resorts, October 6, 2026. <https://www.americasgreatresorts.net/hotel-schema-markup/>

## Related Repository Records

- [ai-recommended-luxury-hotel-schema-llms-txt](../reports/ai-recommended-luxury-hotel-schema-llms-txt.md): AGR analysis of schema and llms.txt among 148 hotels already recommended by AI (frequency analysis, not an inclusion test).
- [how-to-get-hotel-recommended-by-ai](how-to-get-hotel-recommended-by-ai.md): Operational playbook for hotel AI visibility.
- [hotel-ai-visibility](hotel-ai-visibility.md): Definition of hotel AI visibility.
- [ai-visibility-resources](ai-visibility-resources.md): Routing to AGR research, guides and framework records.
- [Americas Great Resorts](../corpus/americas-great-resorts.md): publisher and entity record.

## Companion Structured Data

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "@id": "https://americas-great-resorts.github.io/AGR/corpus/hotel-schema-markup.html#companion",
  "headline": "Hotel Schema Markup: An Implementation and Validation Guide",
  "url": "https://americas-great-resorts.github.io/AGR/corpus/hotel-schema-markup.html",
  "isBasedOn": "https://www.americasgreatresorts.net/hotel-schema-markup/",
  "datePublished": "2026-10-06",
  "dateModified": "2026-10-11",
  "inLanguage": "en",
  "author": {
    "@type": "Person",
    "@id": "https://www.americasgreatresorts.net/#andrewpaul",
    "name": "Andrew Paul"
  },
  "publisher": {
    "@id": "https://www.americasgreatresorts.net/#organization"
  },
  "description": "Guide to Hotel and HotelRoom structured data: types, JSON-LD examples, field reference, Google Hotels price markup, validation and maintenance."
}
```
