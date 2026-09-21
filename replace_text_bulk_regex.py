import re

class ReplaceTextBulkRegex:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", {"multiline": True}),
                "regex_patterns_and_replacements": ("STRING", {"multiline": True}),
                "case_insensitive": ("BOOLEAN", {"default": True}),
                "multiline": ("BOOLEAN", {"default": False}),
                "dotall": ("BOOLEAN", {"default": False}),
                "count": ("INT", {"default": 0, "min": 0, "max": 9999999999}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output_string",)
    FUNCTION = "replace_text"
    CATEGORY = "utils"

    def replace_text(self, string, regex_patterns_and_replacements, case_insensitive, multiline, dotall, count):
        result = string
        # Split the multiline string into individual pattern-replacement pairs
        lines = regex_patterns_and_replacements.strip().split('\n')
        
        for line in lines:
            # Skip empty lines
            if not line.strip():
                continue
            
            # We'll assume the format is "pattern,replacement"
            # We use split(',', 1) to only split on the first comma, 
            # allowing the replacement string to contain commas.
            if ',' not in line:
                continue
                
            pattern, replacement = line.split(',', 1)
            
            # Prepare regex flags
            flags = 0
            if case_insensitive:
                flags |= re.IGNORECASE
            if multiline:
                flags |= re.MULTILINE
            if dotall:
                flags |= re.DOTALL
            
            # Perform the replacement
            result = re.sub(pattern, replacement, result, count=count, flags=flags)
            
        return (result,)
