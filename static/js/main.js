$(document).ready(function(){
        // function myFunction(input) {
        //     console.log(input.files[0].mozFullPath);
        // }
        // $("#input_file").on("change", myfunction)
        
        // $('input[type=file]').change(function () {
        //     console.log(this.files[0].mozFullPath);
        // });
        // $('#button_Classify').click(function(e){
        //     var e2 = $('#input_file')
        //     console.log(e2.file[o].mozfullpath)
        // })
    function readURL(input) {
        console.log('hey2')
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            console.log('hey3')
            reader.onload = function (e) {
                // $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
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

