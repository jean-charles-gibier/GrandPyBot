$(document).ready(function() {
    var $newItemForm = $('#papyForm');
    $newItemForm.on('submit', function(e) {
        e.preventDefault();
        var serialized = $(this).serialize();
        var text = $('input:text').val();
        $('#papyChat').append( '<div class="row"> <div class="col-lg-10"> <div class="alert text-left" style="background: #0a2929; color: #c1f0f0;">'+ text +'</div></div></div>');
        $('input:text').val('');

       $.ajax({
            data: serialized,
            type: 'POST',
            url: '/ask',
//            dataType : 'json' ,
            beforeSend: function () {
               $('.loader').show();
               $('#buttonsearch').hide();
            },
            complete: function (resultat, statut) {
                $('.loader').hide();
                $('#buttonsearch').show();
                },
            success: function(code_html, statut){
                console.log(' Success !');
               },
            error : function(resultat, statut, erreur){
                console.log(' Error :"'+ erreur +'".');
               }
        })
        .done(function (data) {
                $('#papyChat').append( '<div class="row"><div class="offset-2 col-lg-10 text-lg-right"><div class="alert text-right" style="background: #c1f0f0; color: #0a2929;">' + data.output + '</div></div></div>');
		    });
            // Just to maintain scroll  down
        $('#papyChat').scrollTop = $('#papyChat').scrollHeight;
    });
 });
