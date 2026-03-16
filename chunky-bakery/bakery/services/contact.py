def validate_inquiry(form_data):
    name = form_data.get("name", "").strip()
    phone = form_data.get("phone", "").strip()
    message = form_data.get("message", "").strip()

    if not name or not phone or not message:
        return None, "Please complete all contact form fields."

    inquiry = {
        "name": name,
        "phone": phone,
        "message": message,
    }
    return inquiry, None
