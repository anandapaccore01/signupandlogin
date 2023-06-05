function validate(){
    var fname=document.Registerform.first_name.value;
    var lname=document.Registerform.last_name.value;
    var uname=document.Registerform.username.value;
    var email=document.Registerform.email.value;
    var phone=document.Registerform.phone.value;
    var pwd=document.Registerform.password.value;
    var cpwd=document.Registerform.confirm_phone.value;
    var dob=document.Registerform.date_of_birth.value;
    var alphaExp=/^[a-zA-Z]+$/;
    var numExp=/^[0-9]+$/;
    var unameExp=/^[a-zA-Z0-9]+$/;
    var emailExp=/^[a-zA-Z0-9.]+@[a-zA-Z]+.[a-zA-Z]+$/;
    var pwdEXP=/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    var status= status1=status2=status3=status4= status5=status6=status7=false;
    if(fname==''){
        
        document.getElementById('fnamenote').innerHTML='please enter first name';
        status=false;
    }
    else{
        if(fname.match(alphaExp)){
            document.getElementById('fnamenote').innerHTML='';
            status=true;   
        }
        else{
            document.getElementById('fnamenote').innerHTML='please enter characters only';
            status=false;
        }
    }
    if(lname==''){
        
        document.getElementById('lnamenote').innerHTML='please enter first name';
        status1= false;
    }
    else{
        if(lname.match(alphaExp)){
            document.getElementById('lnamenote').innerHTML='';
            status1= true;   
        }
        else{
            document.getElementById('lnamenote').innerHTML='please enter characters only';
            status1= false;
        }
    }
    if(uname==""){
        document.getElementById('unote').innerHTML='please enter username';
        status2=false;
    }
    else{
        if(uname.match(unameExp)){
            document.getElementById('unote').innerHTML='';
            status2=true;                
            }
        
        else{
            document.getElementById('unote').innerHTML='please enter valid username';
            status2=false;
        }
    }
    if(email==""){
        document.getElementById('enote').innerHTML='please enter email';
        status3=false;
    }
    else{
        if(email.match(emailExp)){
            document.getElementById('enote').innerHTML='';
            status3=true;
        }
        else{
            document.getElementById('enote').innerHTML='please enter valid email id';
            status3=false;
        }
    }
    if (pwd==""){
        document.getElementById('pwdnote').innerHTML='please enter password';
        status4=false;
    }
    else{
        if(pwd.match(pwdEXP)){
            document.getElementById('pwdnote').innerHTML='';
            status4=true;          
        }
        else{
            document.getElementById('pwdnote').innerHTML='Must contain at least one number and one uppercase and lowercase letter and one special charater, and at least 8 or more characters';
            status4=false;
        }

    }
    if (cpwd==""){
        document.getElementById('cpwdnote').innerHTML='please enter confirm password';
        status5=false;
    }
    else{
        if(pwd == cpwd){
        document.getElementById('cpwdnote').innerHTML='';
        status5=true;} 
    else{
        document.getElementById('cpwdnote').innerHTML='password and confirm password are not same';
        status5=false;
    }
    }
    if(phone==""){
        document.getElementById('phonenote').innerHTML='please enter phone no';
         status6=false;
     }
     else{
         if(phone.match(numExp)){
             if(phone.length==10){
                document.getElementById('phonenote').innerHTML='';
                 status6=true;
             }
             else{
                document.getElementById('phonenote').innerHTML='phone no must have 10 digits';
                 status6=false;
             }
         }
         else{
            document.getElementById('phonenote').innerHTML='please enter valid phone no';
             status6=false;
         }
     }
    if(dob=''){
        document.getElementById('dobnote').innerHTML='please enter date of birth';
        status7=false;
    }
    else{
        document.getElementById('dobnote').innerHTML='';
        status7=true;
    }
    if(status==true && status1==true&& status2==true && status3 == true && status4 == true && status5==true&& status6==true && status7==true){
        return true
    }
    else{
        return false
    }
}

function passwordvalidate(){
 var pwd = document.changepasswordform.password.value;
 var cpwd = document.changepasswordform.cpassword.value;
 var pwdEXP=/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;  
 var status=status1=false; 
 if (pwd==""){
    document.getElementById('pwdnote').innerHTML='please enter password';
    status=false;
}
else{
    if(pwd.match(pwdEXP)){
        document.getElementById('pwdnote').innerHTML='';
        status=true;          
    }
    else{
        document.getElementById('pwdnote').innerHTML='Must contain at least one number and one uppercase and lowercase letter and one special charater, and at least 8 or more characters';
        status=false;
    }

}
if (cpwd==""){
    document.getElementById('cpwdnote').innerHTML='please enter confirm password';
    status1=false;
}
else{
    if(pwd == cpwd){
    document.getElementById('cpwdnote').innerHTML='';
    status1=true;} 
else{
    document.getElementById('cpwdnote').innerHTML='password and confirm password are not same';
    status1=false;
}
}
if(status==true && status1==true){
    return true;
}
else{
    return false;
}
}

function changeemailvalidate(){
    
    var email=document.changeemailform.email.value;
    var emailExp=/^[a-zA-Z0-9.]+@[a-zA-Z]+.[a-zA-Z]+$/;
    
    if(email==""){
        document.getElementById('enote').innerHTML='please enter email';
        return false;
    }
    else{
        if(email.match(emailExp)){
            document.getElementById('enote').innerHTML='';
            return true;
        }
        else{
            document.getElementById('enote').innerHTML='please enter valid email id';
            return false;
        }
    }

}