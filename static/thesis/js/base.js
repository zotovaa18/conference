jQuery(document).ready(function ($) {
    (function($) {
        $(function() {
            var selectField = $('#id_cleaver'),
                verified = $('.abcdefg');

            function toggleVerified(value) {
                console.log("Truthy");
                if (value == 'да') {
                    verified.show();
                } else {
                    verified.hide();
                }
            }

            // show/hide on load based on pervious value of selectField
            toggleVerified(selectField.val());

            // show/hide on change
            selectField.change(function() {
                toggleVerified($(this).val());
            });
        });
    })(django.jQuery);
});