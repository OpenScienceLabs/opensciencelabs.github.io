---
title: Public analytics
description:
  A transparent view of our measured website audience, for our community and
  potential sponsors.
template: analytics.html
section_label: Open Science Labs · Transparency
page_theme: about
hero_words: ["Measure", "Share", "Support"]
---

## How we measure

This is **OSL-published data sourced from Google Analytics 4 (GA4)** via the
Google Analytics Data API. It is not an independent audit or a guarantee of
sponsorship reach. Only the aggregate fields in the downloadable report are
published; no visitor identifiers or raw API responses are included.

- **Pageviews** (`screenPageViews`): counted website page views, including
  repeated views of the same page. The Web platform filter excludes app screens.
- **Active users** (`activeUsers`): distinct users GA4 classifies as active,
  based on engagement and applicable first-visit or engagement signals. This is
  queried over each entire 30-day period, not added from daily totals. It is not
  a count of all visitors or a census of individual people.
- **Sessions** (`sessions`): sessions that began during the reporting period, as
  measured by GA4. A user can have more than one session.

All dates are inclusive calendar dates in the **GA4 property's reporting
timezone**, shown above. The summary covers 30 completed days ending yesterday
at the time of the last successful refresh. Comparisons use the immediately
preceding 30 completed days in the same timezone, not the previous calendar
month. Percentage changes have no meaningful baseline when the previous count is
zero. The daily chart covers the summary period; monthly history covers up to 12
completed calendar months, excluding the current month. These are different
reporting windows, not directly comparable totals.

Missing dates and months are marked **Not reported**, with gaps in the chart;
they are not invented as zeros and may predate collection. Explicit zero counts
mean no measured traffic for that query, not necessarily no actual visits.

The hostname scope above is an exact allowlist, combined with a Web-only filter.
Other hostnames, including previews and localhost, and app traffic are excluded.
This is website traffic, not OSL's combined audience across social media,
community platforms, or other websites.

### Audience breakdowns

- **Countries** show pageviews by GA4's `country` dimension. This is approximate
  activity location, not nationality or residence. VPNs, proxies and location
  determination can affect it.
- **Devices** show pageviews by `deviceCategory` (such as desktop or mobile),
  not a count of distinct devices or people.
- **Channels** show sessions by `sessionDefaultChannelGroup`, GA4's rule-based
  classification of how sessions started. This is session acquisition, not a
  user's first-ever acquisition channel or a campaign attribution audit.

Each panel uses the same 30-day window and hostname scope as the headline. Up to
ten named categories are ranked by their additive metric. A category needs at
least ten `activeUsers` over the full period to be named; smaller, remaining and
unclassified categories are combined as **Other / unknown**. Those per-category
user counts are used only for grouping and are never published or summed into
headline users. Grouping reduces detail; it is not a formal anonymity guarantee.
No city, visitor, page-path or cross-category breakdowns are published.

Shares use each panel's returned total, including Other / unknown, not the
headline user count. Rounded shares may not add to exactly 100%. Dimensioned and
headline reports may differ during processing or because of reporting semantics;
we do not adjust them to force agreement. A retained older snapshot may lack
comparisons or audience panels; that absence is not zero traffic.

### Limitations and freshness

Measured traffic can exclude visits affected by **consent choices, blockers**,
disabled JavaScript, or collection errors. Identity settings, estimation, and
cross-device behavior can affect user counts. Recent figures may change during
GA4 processing. Every refresh re-queries the current and comparison windows,
daily and monthly histories, and all breakdowns, so earlier figures can be
revised too. A zero report warrants checking collection and scope before
concluding that nobody visited the site.

Refreshes are scheduled daily at **06:23 UTC**, but GitHub Actions scheduling
may be delayed. If a refresh fails, we retain the previous successful report and
its original timestamp. A report more than three days old is marked stale. If
GA4 explicitly signals a privacy threshold or metric access restriction for an
audience breakdown, that panel is marked **Not published**, not zero. A
restriction on core statistics, sampling, truncation, unavailable data, or a
failed request instead retains the entire previous report. We never publish
partially fetched rankings or label a failed attempt as a successful refresh.

Metric definitions follow Google's
[GA4 Data API schema](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema).
See also Google's
[data freshness guidance](https://support.google.com/analytics/answer/12233314).
The endpoint follows our [versioned JSON schema](schema.json). New exports use
version 2; older version 1 snapshots remain readable without changing their
original refresh timestamp.

## Support open science

Help sustain our open-source tools, mentorship, and community programs.
[Explore OSL sponsorship](../about/sponsorship/index.md).
