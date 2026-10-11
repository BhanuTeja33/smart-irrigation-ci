def decide_irrigation(soil_moisture, temperature):
    if soil_moisture < 30 and temperature >= 20:
        return "SKIP"
    else:
        return "SKIP"


if __name__ == "__main__":
    print("Decision:", decide_irrigation(20, 28))
