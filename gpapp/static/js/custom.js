$(document).ready(function() {
    var $newItemForm = $('#papyForm');
    $newItemForm.on('submit', function(e) {
        e.preventDefault();
        var serialized = $(this).serialize();
        var text = $('input:text').val();
        var $theLast = $('#papyChat #anchor');
            $theLast.before( '<div class="row"> <div class="col-lg-10"> <div class="alert text-left" style="background: #0a2929; color: #c1f0f0;">'+ text +'</div></div></div>');
        $('#papyChat').scrollTop($('#papyChat').height() +10000);
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
                var $theLast = $('#papyChat #anchor');
                $theLast.before( '<div class="row"><div class="offset-2 col-lg-10 text-lg-right"><div class="alert text-right" style="background: #c1f0f0; color: #0a2929;">' + data.output + '</div></div></div>');
                $('#papyChat').scrollTop($('#papyChat').height() +10000);
		    });
            // Just to maintain scroll  down
    });
 });

// Initialize and add the map
function initMap( lat, lng, elt_id) {
  // The location of center
  var center = {lat: lat, lng: lng};
  // The map, centered at center
  map = new google.maps.Map(
      document.getElementById(elt_id), {zoom: 12, center: center});
  // The marker, positioned at center
  var marker = new google.maps.Marker({position: center, map: map});
}
