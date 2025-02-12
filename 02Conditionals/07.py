# 7. Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

def customize_coffee(size, extra_shot=False):
    if size not in ["Small", "Medium", "Large"]:
        return "Invalid size"
    
    order = f"{size} coffee"
    
    if extra_shot:
        order += " with an extra shot of espresso"
    
    return order

# Example usage
print(customize_coffee("Medium", True))  # Output: Medium coffee with an extra shot of espresso
print(customize_coffee("Small"))         # Output: Small coffee