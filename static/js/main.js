$(document).ready(function(){

    function readURL(input) {
        console.log('hey2')
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            console.log('hey3')
            reader.onload = function (e) {
                $('#img')
                    .attr('src', e.target.result);
            };

            reader.readAsDataURL(input.files[0]);
        }
    }
    $('#imageUpload').change(function(){
        readURL(this)
    })

});

