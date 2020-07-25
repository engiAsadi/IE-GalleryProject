/*
$(function() {
    var selectedClass = "";
    $(".filter").click(function(){
        selectedClass = $(this).attr("data-rel");
        $("#gallery").fadeTo(100, 0.1);
        $("#gallery div").not("."+selectedClass).fadeOut().removeClass('animation');
        setTimeout(function() {
            $("."+selectedClass).fadeIn().addClass('animation');
            $("#gallery").fadeTo(300, 1);
        }, 300);
    });
});
*/
$(document).ready(function(){
    $("#id_username").attr('placeholder', 'Username');
    $("#id_username").attr('class', 'SignupInputs');
    
    $("#id_password").attr('placeholder', 'Password');
    $("#id_password").attr('class', 'SignupInputs');

    $("#id_password1").attr('placeholder', 'Password');
    $("#id_password1").attr('class', 'SignupInputs');

    $("#id_password2").attr('placeholder', 'Password');
    $("#id_password2").attr('class', 'SignupInputs');

    $("#id_email").attr('placeholder', 'error@mail.com');
    $("#id_email").attr('class', 'SignupInputs');
});
