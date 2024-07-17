jQuery(document).ready(function($) {
    var chatStarted = false;
    var name = '';
    var phone = '';
    var email = '';

    function appendMsg(msg) {
        $('.Messages_list').append('<div class="msg"><span class="avtr"><figure style="background-image: url(https://mrseankumar25.github.io/Sandeep-Kumar-Frontend-Developer-UI-Specialist/images/avatar.png)"></figure></span><span class="responsText">' + msg + '</span></div>');
        $("[name='msg']").val("");
    }
    jQuery(document).on('click', '.iconInner', function(e) {

        jQuery(this).parents('.botIcon').addClass('showBotSubject');
        $("[name='msg']").focus();

        if (!chatStarted) {
            appendMsg("Hi there!!! Welcome to Badger Skills International , May I know your good name?");
        
            chatStarted = true;
        }
    });

    // Function to handle closing the chatbox
    jQuery(document).on('click', '.closeBtn, .chat_close_icon', function(e) {
        jQuery(this).parents('.botIcon').removeClass('showBotSubject');
        jQuery(this).parents('.botIcon').removeClass('showMessenger');
    
        chatStarted = false;
        name = '';
        phone = '';
        email = '';
    });

// Function to handle form submission

$(document).on("submit", "#messenger", function(e) {
    e.preventDefault();

    var mainval = $("[name=msg]").val();

    if (!mainval.trim()) {
        appendMsg("Please enter a valid response.");
    } else if (!name) {
        name = mainval;
        appendMsg("Thank you, " + name + ". Please provide your phone number:");
    } else if (!isValidPhoneNumber(mainval) && !phone) {
        appendMsg("Please enter a valid phone number.");
    } else if (!phone) {
        phone = mainval;
        appendMsg("Thank you for providing your phone number. Please provide your email address:");
    } else if (!isValidEmail(mainval) && !email) {
        appendMsg("Please enter a valid email address.");
    } else if (!email) {
        email = mainval;
        appendMsg("Thank you for providing your email address. Please enter your message:");
    } else {
    
        appendMsg("Thank you for your message. Our admin will contact you soon. Have a great day!");
        
        submitQuery(name, phone, email, mainval);
    
        chatStarted = false;
        name = '';
        phone = '';
        email = '';
        
    
        setTimeout(function() {
            $('.Messages_list').empty(); 
            $('.botIcon').removeClass('showBotSubject'); 
        }, Math.floor(Math.random() * (5000 - 3000 + 1)) + 3000); 
    }

    var lastMsg = $('.Messages_list').find('.msg').last().offset().top;
    $('.Messages').animate({scrollTop: lastMsg}, 'slow');
});

function isValidPhoneNumber(phone) {

    return /^\d{10}$/.test(phone); 
}

function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email); 
}

// Ajax

function submitQuery(name, phone, email, message) {
    $.ajax({
        url: '/submit_query/',
        method: 'POST',
        data: {
            'name': name,
            'phone_number': phone,
            'email': email,
            'message': message,
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val() // Add CSRF token
        },
        success: function(response) {
            console.log(response); // Handle success response
        },
        error: function(xhr, status, error) {
            console.error(xhr.responseText); // Handle error response
        }
    });
}
});