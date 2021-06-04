var timeoutId;
$('form input, form textarea').on('input propertychange change', function() {
    console.log('Textarea Change');
    
    clearTimeout(timeoutId);
    timeoutId = setTimeout(function() {
        // Runs 1 second (1000 ms) after the last change    
        saveToDB();
    }, 1000);
});

function saveToDB()
{
    console.log('Saving to the DB '+document.getElementById("fname").value);
    form = $('.contact-form');
	$.ajax({
		url: "/echo/json/",
		type: "POST",
		data: form.serialize(), // serializes the form's elements.
		beforeSend: function(xhr) {
            // Let them know we are saving
			$('.form-status-holder').html('Saving...');
		},
		success: function(data) {
			var jqObj = jQuery(data); // You can get data returned from your ajax call here. ex. jqObj.find('.returned-data').html()
            // Now show them we saved and when we did
            var d = new Date();
            $('.form-status-holder').html('Saved! Last: ' + d.toLocaleTimeString());
		},
	});
}

// This is just so we don't go anywhere  
// and still save if you submit the form
$('.contact-form').submit(function(e) {
	saveToDB();
	e.preventDefault();
});
