# ComfyUI Replace Text (Bulk Regex)

ComfyUI custom node that runs multiple regexes against the starting string.

## Installation

1. Clone this repository into your ComfyUI `custom_nodes` folder:
   ```bash
   git clone https://github.com/roybeast/ComfyUI-Replace-Text-Bulk-Regex.git
   ```
2. Restart ComfyUI.

The node should now appear in the `utils` category.

## Inputs

* `string`: The starting text to apply regex replacements to.
* `regex_patterns_and_replacements`: A multiline string containing regex patterns and their corresponding replacements, formatted as `pattern,replacement` per line.
* `case_insensitive`: If `true`, matching is case-insensitive.
* `multiline`: If `true`, allows `^` and `$` to match the start and end of each line.
* `dotall`: If `true`, allows the dot `.` character to match newlines.
* `count`: The maximum number of replacements to perform for each pattern. Set to `0` to replace all occurrences.

## Outputs

* `output_string`: The final text after all regex patterns have been applied.

## Usage

The `regex_patterns_and_replacements` input expects a multiline string where each line defines a replacement rule in the format:
`regex_pattern,replacement_text`

### Example

**Input String:**
`The quick brown fox jumps over the lazy dog 123.`

**Regex Patterns and Replacements:**
```
fox,cat
[0-9],#
```

**Resulting Output:**
`The quick brown cat jumps over the lazy dog ###.`

### Notes

* **Delimiter**: The first comma on each line is used as the delimiter between the pattern and its replacement.
* **Multiple Replacements**: Replacements are applied sequentially.
* **Regex Flags**: You can control `case_insensitive`, `multiline`, and `dotall` behavior via the advanced inputs.
* **Count**: If `count` is set to 0, all occurrences of the pattern will be replaced.
