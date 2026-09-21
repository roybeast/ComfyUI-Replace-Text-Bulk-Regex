# ComfyUI Replace Text (Bulk Regex)

ComfyUI custom node that runs multiple regexes against the starting string.

## Inputs

* `string`: starting string
* `regex_patterns_and_replacements`: multiline string containing regex patterns and replacements
* `case_insensitive`: default `true`
* `multiline`: default `false`
* `dotall`: default `false`
* `count`: default `0` (0 means replace all occurrences)

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
