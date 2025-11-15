import requests


def test_get_user_details():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("API request failed or returned invalid data")
    
    
    
def main():
    try:
        username, country = test_get_user_details()
        print(f"Username: {username}, \nCountry: {country}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()