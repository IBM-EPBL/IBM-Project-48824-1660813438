<script>  
function validateform(){  
var name=document.myform.name.value;  
var email=document.myform.email.value;
var mobile=document.myform.mobile.value;
var password=document.myform.password.value;  
  
if (name==null || name==""){  
  alert("Name can't be blank");  
  return false;  
}else if(email==null || email==""){
   alert("E-mail can't be blank");
   return false;
}else if(mobile.length<=9){
   alert("Enter Mobile Number");
    return false;
}else if(password.length<6){  
alert("Password must be at least 8 characters long.");  
return false;  
  }
}  
</script>  