# Incremental company and official-job audit

1. Read the user's current Companies row, eligibility, all Open Jobs for that company, and matching Applications. Count historical `Applied`, `Skip`, `Closed` separately from unresolved `New`, `Interested`.
2. On each review, inspect the latest official company careers board/ATS (even if earlier decisions are complete). Discover newly posted job identities using exact official requisition IDs and normalized links; don't require the user to supply URLs.
3. If the company is Inactive or Cooldown, explain the gate and request an explicit one-run override. Never rewrite gate metadata to enable a review silently.
4. Verify unresolved and genuinely new roles for title, official URL, location, remote eligibility, minimum requirements and current application accessibility. Keep unverifiable jobs marked uncertain; site failures aren't proof of closure.
5. Deduplicate against current rows across title aliases, redirects, ATS IDs and URLs. Write only genuinely new, verified jobs and relevant truthful notes when authorized. Preserve previously processed decisions and first-seen timestamps.
6. Read Master Resume and Career Story Bank only when their live content is accessible; distinguish verified qualifications from assumptions. Rank high-fit unresolved roles using profile weights and career direction, usually recommending up to three with official links and concise caveats.
7. Deliver checked official source/date, existing counts, found/new/uncertain/closed categories, material skill gaps, eligibility concerns, and what data (if any) was actually changed. If nothing new or unresolved, say so and stop.
8. PAUSE for human choice before any resume generation. A user's preference to apply is not proof of submission. Do not claim a full scan when only a subset was reachable.
