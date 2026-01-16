# test api curl https://book.anhtester.com/api/refetch-token \
#   --request POST \
#   --cookie 'refetchToken='
import allure
from api.refetch_token_api import RefetchTokenAPI

@allure.epic("API")
@allure.feature("Auth")
@allure.story("Refetch Token")

def test_refetch_token(api_context):
    # Đăng nhập để lấy refetch token cookie
    login_response = api_context.post(
        "/api/login",
        data={
            "email": "mainth1368@gmail.com",
            "password": "password123"
        }
    )
    # Kiêm tra login thành công
    assert login_response.status == 200
    # Khởi tạo RefetchTokenAPI
    refetch_token_api = RefetchTokenAPI(api_context)
    # Gửi request refetch token
    response = refetch_token_api.refetch_token()
    # Kiểm tra kết quả
    assert response.status == 200
    # Kiểm tra nội dung response
    data = response.json()
    # Kiểm tra đã trả về accessToken và exp
    assert "accessToken" in data
    assert "exp" in data
    assert data["msg"] == "Refetch token successfully."


def test_refetch_token_missing_cookie(api_context_no_cookie):
    response = api_context_no_cookie.post("/api/refetch-token")
    assert response.status in (400, 401, 422)

