<script>  
function validateform(){  
var name=document.myform.name.value;  
var password=document.myform.password.value;  
  
if (name==null || name==""){  
  alert("E-mail can't be blank");  
  return false;  
}else if(password.length<6){  
  alert("Password must be at least 8 characters long.");  
  return false;  
  }  
}  
</script>  