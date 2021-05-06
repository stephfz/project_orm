$(document).ready(function(){
    $("#email").blur(checkEmail)
})

function checkEmail(){
    var data = $("#formRegister").serialize()
    alert("focus out")
    $.ajax({
        method: "POST",
        url: "/checkEmail",
        data: data,
        dataType: "JSON",
 
    })   
    .done (function (response) {
        var size = Object.keys(response['errors']).length;
        if (size > 0) {
            console.log(response['errors'])
        }
        else {
            console.log('Correo Valido')
        }
        
    })
}
