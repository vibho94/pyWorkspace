
"""
Step1;- input user upi id
step2:- payment URL to be generated
step3:- Generate QR code for every payment
step4:- Save generated qr code image in the local machine
step5:-Display generated QR code using pillow function
payment url :- upi://pay?pn=UPI_ID&apn=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE
"""
import qrcode
upi_id=input("Enter your upi id:")

paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name'
google_pay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name'
phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name'

paytm_qr=qrcode.make(paytm_url)
google_pay_qr=qrcode.make(google_pay_url)
phonepe_qr=qrcode.make(phonepe_url)

paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')
phonepe_qr.save('phonepe_qr.png')

paytm_qr.show()
google_pay_qr.show()
phonepe_qr.show()