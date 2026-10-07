"""Design tokens for TaskFlow.

Single source of design values. Pages and components must reference these
tokens only; never hardcode colors, spacing, radius, or font sizes.

Values come from docs/DESIGN_SYSTEM.md. Adding a token means editing that doc
first, then this file, then the code that uses it.
"""

# --- Color tokens: light theme ---------------------------------------------
color_primary = "#4F46E5"
color_primary_hover = "#4338CA"
color_primary_soft = "#EEF2FF"
color_accent = "#0EA5E9"
color_bg = "#F8FAFC"
color_surface = "#FFFFFF"
color_border = "#E2E8F0"
color_text = "#0F172A"
color_text_muted = "#64748B"
color_success = "#16A34A"
color_warning = "#D97706"
color_danger = "#DC2626"
color_info = "#2563EB"

# --- Color tokens: dark theme ----------------------------------------------
color_primary_dark = "#818CF8"
color_primary_hover_dark = "#A5B4FC"
color_primary_soft_dark = "#312E81"
color_accent_dark = "#38BDF8"
color_bg_dark = "#0B1120"
color_surface_dark = "#111827"
color_border_dark = "#1F2937"
color_text_dark = "#F1F5F9"
color_text_muted_dark = "#94A3B8"
color_success_dark = "#4ADE80"
color_warning_dark = "#FBBF24"
color_danger_dark = "#F87171"
color_info_dark = "#60A5FA"

# --- Priority / status mapping ---------------------------------------------
priority_colors = {
    "Low": color_text_muted,
    "Medium": color_warning,
    "High": color_danger,
}

status_colors = {
    "Todo": color_text_muted,
    "In Progress": color_info,
    "Done": color_success,
}

# Fixed palette offered when choosing a project color.
project_colors = [
    color_primary,
    color_accent,
    color_success,
    color_warning,
    color_danger,
    color_info,
]

# --- Spacing tokens (4px base scale) ---------------------------------------
space_0 = "0"
space_1 = "4px"
space_2 = "8px"
space_3 = "12px"
space_4 = "16px"
space_5 = "20px"
space_6 = "24px"
space_8 = "32px"
space_10 = "40px"
space_12 = "48px"

# --- Radius tokens ----------------------------------------------------------
radius_sm = "4px"
radius_md = "8px"
radius_lg = "12px"
radius_full = "9999px"

# --- Typography tokens ------------------------------------------------------
font_family = "Inter, system-ui, sans-serif"

text_xs = "12px"
text_sm = "14px"
text_base = "16px"
text_lg = "18px"
text_xl = "20px"
text_2xl = "24px"
text_3xl = "30px"

line_xs = "16px"
line_sm = "20px"
line_base = "24px"
line_lg = "28px"
line_xl = "28px"
line_2xl = "32px"
line_3xl = "36px"

weight_regular = "400"
weight_medium = "500"
weight_semibold = "600"
weight_bold = "700"

# --- Elevation & borders ----------------------------------------------------
shadow_sm = "0 1px 2px rgba(15,23,42,0.06)"
shadow_md = "0 4px 12px rgba(15,23,42,0.10)"
shadow_lg = "0 12px 32px rgba(15,23,42,0.16)"
border_width = "1px"

# --- Breakpoints (responsive) ----------------------------------------------
bp_mobile = "0-767px"
bp_tablet = "768-1023px"
bp_desktop = "1024px"
