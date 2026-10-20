import requests

def get_user_with_id(user_id):
    try:
        response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}", timeout=10)

    except requests.exceptions.Timeout:
        return {
            "success": False,
            "user": None,
            "error": {
                "code": None,
                "message": "Request timed out"
            }
        }
    
    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "user": None,
            "error": {
                "code": None,
                "message": f"Network error: {e}"
            }
        }

    if response.status_code == 200:
        user = response.json()
        return {
            "success": True,
            "user": {
                "id": user["id"],
                "name": user["name"]
            },
            "error": None
        }
    elif response.status_code == 404:
        return {
            "success": False,
            "user": None,
            "error": {
                "code": 404,
                "message": "User not found"
            }
        }
    else:
        return {
            "success": False,
            "user": None,
            "error": {
                "code": response.status_code,
                "message": "An unexpected error occurred"
            }
        }

def display_user_result(result):
    if result["success"]:
        print(f"User name: {result['user']['name']}")
    else:
        print(f"Error: {result['error']['message']} (Code: {result['error']['code']})")

validuser = get_user_with_id(1)
invaliduser = get_user_with_id(999)
display_user_result(validuser)
print()
display_user_result(invaliduser)