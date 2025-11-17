import json


def get_status():
    status_data = {
        "version": "1.0.0",
        "build_date": "2024-01-01T00:00:00Z",  # Fixed ISO date
        "status": "regular",
        "services": []
    }

    status_data["services"].append(add_firma_digitale())
    status_data["services"].append(add_autenticazione())

    return status_data

def add_firma_digitale():
    service = {
        "service": "firma digitale",
        "author": "mario rossi"
    }
    return service

def add_autenticazione():
    service = {
        "service": "autenticazione",
        "author": "luigi verdi"
    }
    return service

# Example usage
if __name__ == "__main__":
    print(json.dumps(get_status(), indent=4))
