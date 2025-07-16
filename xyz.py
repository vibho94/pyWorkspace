import qrcode

upi_id = input("Enter your UPI ID: ")

# Correct UPI URL format (pa = payee address, pn = payee name)
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name'
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name'

# Generate QR codes
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)
phonepe_qr = qrcode.make(phonepe_url)

# Save QR code images
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')
phonepe_qr.save('phonepe_qr.png')

# Display QR codes
paytm_qr.show()
google_pay_qr.show()
phonepe_qr.show()
