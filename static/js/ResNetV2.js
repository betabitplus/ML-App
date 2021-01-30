$(document).ready(function () {
    // Init
    $('.image-section-ResNetV2').hide();
    $('.loaderResNetV2').hide();
    $('#resultResNetV2').hide();

    // Upload Preview
    function readURLResNetV2(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#imageUploadResNetV2").change(function () {
        $('.image-section-ResNetV2').show();
        $('#btn-predict-ResNetV2').show();
        $('#topOneResult').text('');
        $('#topTwoResult').text('');
        $('#topThreeResult').text('');
        $('#fileResult').text('');
        $('#resultResNetV2').hide();
        readURLResNetV2(this);
    });

    // Predict
    $('#btn-predict-ResNetV2').click(function () {
        var form_data = new FormData($('#upload-file-ResNetV2')[0]);

        // Show loading animation
        $(this).hide();
        $('.loaderResNetV2').show();

        // Make prediction by calling api /predictResNetV2
        $.ajax({
            type: 'POST',
            url: '/predictResNetV2',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('.loaderResNetV2').hide();
                $('#resultResNetV2').fadeIn(600);
                
                data = data.split('; ')
                
                $('#topOneResult').text(data[0])
                $('#topTwoResult').text(data[1])
                $('#topThreeResult').text(data[2])
                $('#fileResult').text(data[3])
                
                console.log('ResNetV2 Success!');
            },
        });
    });

});
