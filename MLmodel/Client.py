import httpx
import time
cat_path = "microsoft-catsvsdogs-dataset/PetImages/Cat/10001.jpg"
dog_path = "microsoft-catsvsdogs-dataset/PetImages/Dog/1002.jpg"
while True:
    index = int(input("Enter 1 for cat, 2 for dog: "))
    if index == 1:
        file_path = cat_path
    elif index == 2:
        file_path = dog_path
    with open(file_path, "rb") as file:
        files = {"file": file}
        start_time = time.time()
        response = httpx.post("http://127.0.0.1:8080/predict", files=files, timeout=10)
        end_time = time.time()
        response_time = end_time - start_time

    if response.status_code == 200:
        result = response.json()
        print(f"Predicted class: {result['class']}, response_time: {response_time}")
    else:
        print(f"Error: {response.status_code}, {response.json()}")