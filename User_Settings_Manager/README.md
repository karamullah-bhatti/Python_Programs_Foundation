# User Settings Manager

A lightweight Python utility for managing dictionary-based user settings with case-insensitive handling and strict formatting.

## Features
- **Case-Insensitive Normalization**: Automatically standardizes keys and values to lowercase.
- **State Management**: Functions for adding, updating, deleting, and viewing settings with precise error/success messages.
- **Clean Formatting**: Displays settings with capitalized keys and newline-delimited output.

## Functions
- `add_setting(settings_dict, setting_pair)`
- `update_setting(settings_dict, updated_pair)`
- `delete_setting(settings_dict, delete_pair)`
- `view_settings(settings_dict)`

## Quick Example
```python
test_settings = {'theme': 'black', 'language': 'english'}

# Add a setting
print(add_setting(test_settings, ('VOLUME', 'high')))
# Output: Setting 'volume' added with value 'high' successfully!

# View formatted settings
print(view_settings(test_settings))
