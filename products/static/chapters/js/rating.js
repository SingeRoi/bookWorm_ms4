/*
   Attaches or removes amber-text class.
   Submit form info.
*/
var $stars;

jQuery(document).ready(function ($) {

    $stars = $('.rate-popover');

    $stars.on('mouseover', function () {
        var index = $(this).attr('data-index');
        markStarsAsActive(index);
    });

    function markStarsAsActive(index) {
        unmarkActive();
        for (var i = 0; i <= index; i++) {
            $($stars.get(i)).addClass('amber-text');
        }
    }

    function unmarkActive() {
        $stars.removeClass('amber-text');
    }

    // Submit, sends the information to the server
    $('#rateMe').on('click', function() {
        var yeslen = document.getElementsByClassName("amber-text").length;
        var starinput = document.getElementById("starinput");
        starinput.setAttribute("value", yeslen);
        $("#rating-form").submit();
    });

});


