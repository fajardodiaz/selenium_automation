from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency="USD")
    bot.select_place_to_go("Guatemala")
    bot.select_dates_to_go("2023-03-23","2023-03-25")