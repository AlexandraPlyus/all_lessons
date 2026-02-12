from smartphone import Smartphone

catalog = [
    Smartphone("Nokia", "3310", "+7-999-000-99-00"),
    Smartphone("HUAWEI", "Mate XT", "+7-997-347-47-47"),
    Smartphone("HONOR", "X7d", "+7-945-567-55-77"),
    Smartphone("Infinix", "SMART", "+7-944-444-44-44"),
    Smartphone("Tecno", "SPARK GO", "+7-900-444-00-22")
]
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
