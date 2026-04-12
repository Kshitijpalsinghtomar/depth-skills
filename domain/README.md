# Domain Skills

> Process-level skills for specific engineering domains. These provide structured thinking for particular types of work — they complement the depth-skills (which change **how** the model reasons) by providing domain expertise for **what** the model reasons about.

## Why These Are Separate

The skills in `../skills/` are **cognitive-mode** skills — they change the model's thinking process regardless of domain. `deep-think` works on architecture, copywriting, and database design equally.

These domain skills are **context-mode** skills — they load expert-level mental models for a specific type of work. They tell the model "when doing X, think like an expert in X."

Both are valuable. They compose: use `deep-think` + `system-architect` for deep architectural reasoning. Use `adversary` + `copy-engineer` for critically-reviewed copywriting.

## Available Domain Skills

| Skill | Domain | Core Principle |
|---|---|---|
| `product-engineer` | Product thinking | Job-to-be-done first, features second |
| `system-architect` | Backend systems | Data models, service boundaries, failure modes |
| `copy-engineer` | Content & copy | Specific, honest, conversion-oriented writing |
| `api-designer` | Interface contracts | Developer-experience-first API design |
| `mobile-engineer` | Mobile development | Genuine mobile-first, not desktop-collapsed |
| `performance-engineer` | Performance work | Measure before optimize, profile before propose |
| `refactor-engineer` | Code refactoring | Behavior-preserving transformation |
