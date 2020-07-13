$(function() {
    var $list, $newItemForm;
    $list = $('#papyChat');
    $newItemForm = $('#papyForm');

    $newItemForm.on('submit', function(e) {
        e.preventDefault();
        var text = $('input:text').val();
        $list.append( '<div class="row"> <div class="col-lg-10"> <div class="alert text-left" style="background: #0a2929; color: #c1f0f0;">'
                          + text +
                        '</div></div></div>');
        $('input:text').val('');

        $.ajax({
            data: 'text',
            type: 'POST',
            url: '/ask',
//            dataType : 'json' ,
            beforeSend: function () {
                $('.loader').show();
//                $('#buttonsearch').hide();
//                $('#output').fadeOut()},
            },
            complete: function () {
                $('.loader').hide();
//                $('#buttonsearch').show();
//                $('#output').fadeIn();
//                $("ol:first").prepend("<li class='alert col-lg-6 text-lg-left text-md-left' style='background: #2c3e50; color: #19bc9c;'>" + $('#search').val()) + "</li>";
                    }
                })

        .done(function (data) {
                $('#papyChat').append( '<div class="row"> <div class="col-lg-10"> <div class="alert text-left" style="background: #0a2929; color: #c1f0f0;">'
                          + data.output +
                        '</div></div></div>');

        });
    });

});
