def route_case(citizen_id):
    if citizen_id.startswith("5"):
        return "สถานีตำรวจ ลำปาง"
    elif citizen_id.startswith("1"):
        return "สถานีตำรวจ กรุงเทพ"
    return "สถานีตำรวจ ภูมิภาค"
