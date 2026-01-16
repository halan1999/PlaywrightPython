from utils.data_loader import load_json_data
from utils.data_factory.email_factory import generate_unique_email

def build_register_user(case_name):
    data = load_json_data("register_user.json")
    user = data[case_name]

    if "{{random_email}}" in user["email"]:
        user["email"] = generate_unique_email(case_name)

    return user