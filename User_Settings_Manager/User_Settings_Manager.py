test_settings = {
    'theme': 'black',
    'language': 'english',
    'notification': 'off'
}

def add_setting(test_setting, setting_pair):
    key, value = setting_pair
    lower_key = key.lower()
    lower_value = value.lower()

    if lower_key in test_setting:
        return f"Setting '{lower_key}' already exists! Cannot add a new setting with this name."
    

    test_setting[lower_key] = lower_value
    return f"Setting '{lower_key}' added with value '{lower_value}' successfully!"

def update_setting(test_setting,updated_pair):
    key,value=updated_pair
    lower_key= key.lower()
    lower_value=value.lower()
    if lower_key in test_setting:
        test_setting[lower_key]= lower_value
        return f"Setting '{lower_key}' updated to '{lower_value}' successfully!"
    else:
        return f"Setting '{lower_key}' does not exist! Cannot update a non-existing setting."

def delete_setting(test_setting, delete_pair):
    if isinstance(delete_pair, (tuple, list)):
        key = delete_pair[0]
    else:
        key = delete_pair
        
    lower_key = key.lower() if isinstance(key, str) else key
    
    if lower_key in test_setting:
        del test_setting[lower_key]
        return f"Setting '{lower_key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."
    
    result = "Current User Settings:\n"
    for key, value in settings.items():
        formatted_key = key[0].upper() + key[1:]
        result += f"{formatted_key}: {value}\n"      
    return result
result = add_setting(test_settings, ('THEME', 'dark'))
print(result)

print(add_setting({'theme': 'light'}, ('volume', 'high')))
print(update_setting({'theme': 'light'}, ('volume', 'high')))
print(view_settings(test_settings))
