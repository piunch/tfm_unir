$(document).ready(function(){ 
    $('#loginForm').submit(function(event){
        event.preventDefault();
        user = $('#user').val();
        pass = $('#password').val();
    
        loginBody = {};
        loginBody.user = user;
        loginBody.pass = pass;
        
        $.ajax({
            type: "POST",
            url: '/login',
            dataType: "json",
            data: loginBody,
            success: saveAuthToken,
        });
    
        function saveAuthToken(token, statusText, code) {
            if (code.status != 401) {
                window.location.replace('/');
            }
        } 
    });
});