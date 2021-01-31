def submit_request(request):
    context = {}
    sent = False
    nuid_r = request.user.username
    adminemail = "gargi.nandy111@gmail.com"
    email_r = request.user.email_user
    # If post action form from find_room page, all form informaiton is gather and a booking is created and email information
    if request.method == 'POST':
        # gathers form fields

        # creates email information for user and admin
        subject: str = "UNO Guest House Booking Request"
        message = f"Your booking request has been submitted \nOnce your request is processed you should recieve another email.\n\nThank you, UNOGHB Staff. "
        message2 = f"New booking request has been submitted for {nuid_r} ."
        msg1 = (subject, message, 'gargi.nandy111@gmail.com', [email_r])
        msg2 = (subject, message2, 'gargi.nandy111@gmail.com', [adminemail])
        send_mass_mail((msg1, msg2), fail_silently=False)
        sent = True
        return render(request, 'submit_request.html', {'sent': sent, 'email_r': email_r})
    else:
        # if post form was not a success send email error message admin and display error msg to user on submit_booking page
        context[
            "error"] = "Sorry, something went wrong when submitting your booking request. Someone will be in touch with you within 24-48 hours."
        subject: str = "UNO Guest House Booking Request Error"
        error_msg = f"New booking request has errored for {nuid_r}. Please contact them within 24-48 hours."
        send_mail(subject, error_msg, 'gargi.nandy111@gmail.com', [adminemail])
        return render(request, 'submit_request.html', {'sent': sent, 'context': context})