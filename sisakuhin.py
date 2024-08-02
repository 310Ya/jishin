import pandas as pd
from haversine import haversine, Unit

# エクセルファイルから避難場所のデータを読み込む関数
def load_shelters_from_excel(file_path):
    shelters = []
    df = pd.read_excel(file_path)
    for _, row in df.iterrows():
        shelters.append({
            "name": row["避難場所"].strip(), 
            "latitude": float(row["緯度"]),
            "longitude": float(row["経度"]),
            "address": row["住所"].strip()
        })
    return shelters

def find_nearest_shelter(current_location, shelters):
    nearest_shelter = None
    shortest_distance = float('inf')

    for shelter in shelters:
        shelter_location = (shelter["latitude"], shelter["longitude"])
        distance = haversine(current_location, shelter_location, unit=Unit.KILOMETERS)

        if distance < shortest_distance:
            shortest_distance = distance
            nearest_shelter = shelter

    return nearest_shelter, shortest_distance

def main():
    # ユーザーから現在地の緯度と経度を入力
    latitude = float(input("現在地の緯度を入力してください: "))
    longitude = float(input("現在地の経度を入力してください: "))
    current_location = (latitude, longitude)

    # 避難場所のデータをエクセルファイルから読み込む
    file_path = r'C:\\Users\\karir\\OneDrive\\デスクトップ\\shelters.xlsx' 
    shelters = load_shelters_from_excel(file_path)

    # 最寄りの避難場所を特定
    nearest_shelter, distance = find_nearest_shelter(current_location, shelters)
    print(f"最寄りの避難場所は {nearest_shelter['name']} ({nearest_shelter['address']}) で、距離は {distance:.2f} キロメートルです。")

if __name__ == "__main__":
    main()