def analyze_case(text_data):
    if "ลงทุน" in text_data:
        return "investment", 0.92
    elif "รัก" in text_data:
        return "romance", 0.85
    else:
        return "call_center", 0.80
