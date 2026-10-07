# Design System

Source of truth: `prd.md`. These tokens are the single source of design values for the app.
All tokens live in `app/styles.py` (built in Task 2). Pages and components must reference tokens only — no hardcoded colors, spacing, radius, or font sizes.

Naming convention: `snake_case` Python constants grouped by category. A change to a token value here is the only sanctioned way to change the visual design (see PROMPTS.md "Design change").

## 1. Color tokens

### 1.1 Semantic palette (light theme)
| Token | Value | Use |
|---|---|---|
| `color_primary` | `#4F46E5` | Primary actions, active nav, links |
| `color_primary_hover` | `#4338CA` | Hover/pressed primary |
| `color_primary_soft` | `#EEF2FF` | Primary tint backgrounds |
| `color_accent` | `#0EA5E9` | Secondary highlight |
| `color_bg` | `#F8FAFC` | App background |
| `color_surface` | `#FFFFFF` | Cards, dialogs, sidebar |
| `color_border` | `#E2E8F0` | Borders, dividers |
| `color_text` | `#0F172A` | Primary text |
| `color_text_muted` | `#64748B` | Secondary text, labels |
| `color_success` | `#16A34A` | Done status, positive metric |
| `color_warning` | `#D97706` | Overdue/attention, medium priority |
| `color_danger` | `#DC2626` | Errors, delete, high priority, inline validation |
| `color_info` | `#2563EB` | In-progress status, info |

### 1.2 Semantic palette (dark theme)
| Token | Value | Use |
|---|---|---|
| `color_primary_dark` | `#818CF8` | Primary actions, active nav |
| `color_primary_hover_dark` | `#A5B4FC` | Hover/pressed primary |
| `color_primary_soft_dark` | `#312E81` | Primary tint backgrounds |
| `color_accent_dark` | `#38BDF8` | Secondary highlight |
| `color_bg_dark` | `#0B1120` | App background |
| `color_surface_dark` | `#111827` | Cards, dialogs, sidebar |
| `color_border_dark` | `#1F2937` | Borders, dividers |
| `color_text_dark` | `#F1F5F9` | Primary text |
| `color_text_muted_dark` | `#94A3B8` | Secondary text, labels |
| `color_success_dark` | `#4ADE80` | Done status, positive metric |
| `color_warning_dark` | `#FBBF24` | Overdue/attention, medium priority |
| `color_danger_dark` | `#F87171` | Errors, delete, high priority, inline validation |
| `color_info_dark` | `#60A5FA` | In-progress status, info |

### 1.3 Priority / status mapping
| Value | Token |
|---|---|
| Priority Low | `color_text_muted` |
| Priority Medium | `color_warning` |
| Priority High | `color_danger` |
| Status Todo | `color_text_muted` |
| Status In Progress | `color_info` |
| Status Done | `color_success` |

Inline validation errors use `color_danger` (prd.md §4.3).

### 1.4 Project color choices
Project `color` values are drawn from this fixed set so user-chosen project colors always stay on-palette:
`color_primary`, `color_accent`, `color_success`, `color_warning`, `color_danger`, `color_info`.

## 2. Spacing tokens

A 4px base scale. Use these names everywhere; no arbitrary pixel values.

| Token | Value |
|---|---|
| `space_0` | `0` |
| `space_1` | `4px` |
| `space_2` | `8px` |
| `space_3` | `12px` |
| `space_4` | `16px` |
| `space_5` | `20px` |
| `space_6` | `24px` |
| `space_8` | `32px` |
| `space_10` | `40px` |
| `space_12` | `48px` |

Common uses: card padding `space_6`; gap between form fields `space_4`; section separation `space_8`; page padding `space_6` (mobile) / `space_8` (desktop).

## 3. Radius tokens

| Token | Value | Use |
|---|---|---|
| `radius_sm` | `4px` | Inputs, small chips |
| `radius_md` | `8px` | Buttons, badges |
| `radius_lg` | `12px` | Cards, dialogs |
| `radius_full` | `9999px` | Pills, avatars |

## 4. Typography tokens

Font family: `Inter, system-ui, sans-serif` (`font_family`). Fallback to system fonts if Inter is unavailable.

| Token | Size | Line height | Weight | Use |
|---|---|---|---|---|
| `text_xs` | `12px` | `16px` | 400 | Captions, helper text |
| `text_sm` | `14px` | `20px` | 400 | Body small, labels |
| `text_base` | `16px` | `24px` | 400 | Body |
| `text_lg` | `18px` | `28px` | 500 | Card titles |
| `text_xl` | `20px` | `28px` | 600 | Section headings |
| `text_2xl` | `24px` | `32px` | 600 | Page titles |
| `text_3xl` | `30px` | `36px` | 700 | Dashboard metric values |

Weights: `weight_regular` 400, `weight_medium` 500, `weight_semibold` 600, `weight_bold` 700.

## 5. Elevation & borders
| Token | Value | Use |
|---|---|---|
| `shadow_sm` | `0 1px 2px rgba(15,23,42,0.06)` | Inputs, subtle cards |
| `shadow_md` | `0 4px 12px rgba(15,23,42,0.10)` | Cards, dropdowns |
| `shadow_lg` | `0 12px 32px rgba(15,23,42,0.16)` | Dialogs, drawer |
| `border_width` | `1px` | Default border width |

## 6. Breakpoints (responsive)
| Token | Value | Behavior |
|---|---|---|
| `bp_mobile` | `0–767px` | Drawer/hamburger nav, single column |
| `bp_tablet` | `768–1023px` | Collapsed sidebar |
| `bp_desktop` | `1024px+` | Persistent sidebar, multi-column |

## 7. Usage rules
- Reference tokens only. No raw hex, px, or font sizes in pages/components.
- Theme-dependent UI uses the light/dark token pair selected by `SettingsState`; both themes must stay readable and meet contrast expectations.
- Adding a new token means editing this doc first, then `app/styles.py`, then the code that uses it.
