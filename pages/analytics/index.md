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
  queried once over the entire 30-day period, not added from daily totals. It is
  not a count of all visitors or a census of individual people.
- **Sessions** (`sessions`): sessions that began during the reporting period, as
  measured by GA4. A user can have more than one session.

All dates are inclusive calendar dates in the **GA4 property's reporting
timezone**, shown above. The summary covers 30 completed days ending yesterday
at the time of the last successful refresh. Monthly history covers up to 12
completed calendar months; the current month is excluded. Only months returned
by GA4 are shown. Missing months are not invented as zero: they may predate
collection or have no available rows. Returned zero counts mean no measured
traffic for that query, not necessarily no actual visits.

The hostname scope above is an exact allowlist, combined with a Web-only filter.
Other hostnames, including previews and localhost, and app traffic are excluded.
This is website traffic, not OSL's combined audience across social media,
community platforms, or other websites.

### Limitations and freshness

Measured traffic can exclude visits affected by **consent choices, blockers**,
disabled JavaScript, or collection errors. Identity settings, estimation, and
cross-device behavior can affect user counts. Recent figures may change during
GA4 processing. Every refresh re-queries both the rolling window and the full
historical window, so earlier figures can be revised too.

Refreshes are scheduled daily at **06:23 UTC**, but GitHub Actions scheduling
may be delayed. If a refresh fails, we retain the previous successful report and
its original timestamp. A report more than three days old is marked stale. If
GA4 signals thresholding, sampling, truncation, or unavailable data, we do not
replace the previous report with incomplete results or fabricated zeros.

Metric definitions follow Google's
[GA4 Data API schema](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema).
See also Google's
[data freshness guidance](https://support.google.com/analytics/answer/12233314).
The endpoint follows our [version 1 JSON schema](schema.json).

## Support open science

Help sustain our open-source tools, mentorship, and community programs.
[Explore OSL sponsorship](../about/sponsorship/index.md).
