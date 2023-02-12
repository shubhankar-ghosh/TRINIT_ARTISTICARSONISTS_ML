import pandas as pd

crops = pd.read_csv("Datasets/Crop_recommendation.csv")

crop_samples = ["apple", "banana", "blackgram", "chickpea", "coconut", "coffee", "cotton", "grapes", "jute",
                "kidneybeans", "lentil", "maize", "mango", "mothbeans", "mungbeans", "muskmelon", "orange", "papaya",
                "pigeonpeas", "pomegranate", "rice", "watermelon"]

def season(date):
    month = date[4:6]
    summer = ["chickpea", "coconut"]
    spring = ["chickpea", "coconut"]
    fall = ["apples", "blackgram", "coconut"]
    winter = ["coconut"]
    monsoon = ["banana", "blackgram", "coconut"]


def get_crop(rain):

    # print(round(crops["rainfall"]))
    # print(round(rain))
    # return list(pd.unique(crops[round(crops["rainfall"]) == round(rain)]["label"].values))

    lower = round(rain) - 5
    upper = round(rain) + 5

    crop_list = []

    for i in range(lower, upper+1):
        if round(rain)>=298.57:
            return ["Too much rain. Database exceeded."]

        crop_list.extend(list(pd.unique(crops[round(crops["rainfall"]) == round(i)]["label"].values)))


    return list(pd.unique(crop_list))
