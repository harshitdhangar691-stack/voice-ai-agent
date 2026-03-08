def process_request(text):

    text = text.lower()

    if "book" in text:
        return "Appointment booked at 10:30 AM"

    elif "cancel" in text:
        return "Your appointment has been cancelled"

    elif "reschedule" in text:
        return "Your appointment has been rescheduled"

    else:
        return "Sorry I did not understand your request"