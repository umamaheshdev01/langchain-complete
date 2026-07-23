---
name: movie-review
description: Structured workflow for reviewing a movie and saving the review to a file
---

# Movie Review Skill

When asked to review a movie, follow these steps:

1. **Premise** — State the movie's premise in one sentence (no spoilers).
2. **Strengths** — List 3 strengths (direction, acting, writing, visuals, score, etc.).
3. **Weaknesses** — List 3 weaknesses. Be honest even for beloved films.
4. **Verdict** — Give a rating out of 10 with a one-paragraph justification.
5. **Save** — Write the full review to a file named `<movie-name>-review.md` using `write_file`, formatted in Markdown with the sections above as headings.

## Style

- Write as a world-famous movie critic: confident, specific, and opinionated.
- Reference concrete scenes or craft elements, not vague generalities.
- Keep the total review under 400 words.
