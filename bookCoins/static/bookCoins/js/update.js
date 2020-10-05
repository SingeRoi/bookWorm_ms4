/*
   Updates the xx part of 'You will be charged xx'.
   Each time a user enter an coin amount, the amount will be updated,
   anf posted to update_coins in the views.py
*/
function update() {
    var one = document.getElementById('id_coins');
    var two = document.getElementById('chargeValue');
    two.innerHTML = "$" + one.value;

    var coinValue = one;
    var redirect_url = document.getElementById('redirect_url');
    var errorDiv = document.getElementById('coin-errors');

    if (coinValue.value < 5){
        var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>Sorry, the minimum topup is 5.</span>`;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
        var postData = {
            'current_coin': coinValue.value,
            'redirect_url': redirect_url.value,
            'client_secret': clientSecret,
        };

        var url = '/topup/update_coins';

        $.post(url, postData);
    }
}