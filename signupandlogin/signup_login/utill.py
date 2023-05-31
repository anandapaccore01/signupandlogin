from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string




def sendemail(users, pwd): 
      
    to = users.email
    name_f = users.first_name
    name_l = users.last_name
    name = name_f+" "+name_l  
    print("name:",name)  

    subject = 'Welcome to Real Returns Project'
    values = '<p>Hello #NAME#,</p><p>Your account has been created.</p><p>Your login credentials :</p><p>Email: #EMAIL#</p><p>Password: #PASSWORD#</p><p>Please click the link to verify your email.</p><p>Thank you,</p><p>&nbsp;</p>'
    values = values.replace('#NAME#',name)
    values = values.replace('#EMAIL#',to)
    values = values.replace('#PASSWORD#',pwd)
    
    activation_link = f'http://127.0.0.1:8000/emailactivate?user_id={users.id}&confirmation_token={users.verify_string}'
    
    html_content = render_to_string("email_welcome.html", {'content':values, 'content1':activation_link}) 

    email = EmailMultiAlternatives(subject, html_content, settings.EMAIL_HOST_USER, [users.email])
    email.attach_alternative(html_content,'text/html')
    email.send()


def  send_resetpasswordemail(users, token):
    to = users.email
    name_f = users.first_name
    name_l = users.last_name
    name = name_f+" "+name_l  
    print("name:",name)

    subject = 'Real returns:Reset Your Password'
    values = "<p>Hello #NAME#,</p><p>You've asked us to reset password.</p> <p>Please click on the below button to enter your new password</p><p>&nbsp;</p>"
    values = values.replace('#NAME#',name)
    
    Resetpassword_link = f'http://127.0.0.1:8000/resetpassword?user_id={users.id}&token={token}'
    html_content = render_to_string("email_password.html", {'content':values, 'content1':Resetpassword_link}) 

    email = EmailMultiAlternatives(subject, html_content, settings.EMAIL_HOST_USER, [users.email])
    email.attach_alternative(html_content,'text/html')
    email.send()


