## 2024-05-21 - Interaction Timing on State Changes
**Learning:** When transforming an element (like "No" -> "Yes") just before hiding its container, a delay (e.g., 600ms) is essential. Without it, the user misses the delightful transformation entirely.
**Action:** Always check if a visual transition has enough "breathing room" before a major DOM removal or page switch.
