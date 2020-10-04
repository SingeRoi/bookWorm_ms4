
var $stars;

jQuery(document).ready(function ($) {

    // Custom whitelist to allow for using HTML tags in popover content
    var myDefaultWhiteList = $.fn.tooltip.Constructor.Default.whiteList
    myDefaultWhiteList.textarea = [];
    myDefaultWhiteList.button = [];

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

    $stars.on('click', function () {
        $stars.popover('hide');
    });

    // Submit, you can add some extra custom code here
    // ex. to send the information to the server
    $('#rateMe').on('click', function() {

        var yeslen = document.getElementsByClassName("amber-text").length;
        var starinput = document.getElementById("starinput");
        starinput.setAttribute("value", yeslen);
        $("#rating-form").submit();
    });



});


