
$(document).ready(function(){ 
    $('#registerForm').submit(function(event){
        event.preventDefault();
        
        loginBody = {};
        loginBody.fullname = $('#fullname').val();
        loginBody.account = $('#account').val();
        loginBody.login = $('#login').val();
        loginBody.password = $('#password').val();

        $.ajax({
            type: "POST",
            url: '/register',
            dataType: "json",
            data: loginBody,
            success: redirectLogin,
        });
    
        function redirectLogin(token, statusText, code) {
            if (code.status != 401) {
                window.location.replace('/');
            }
        } 
    });
});