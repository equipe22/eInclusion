
e = document.getElementById("record_id-tr")

var tr = document.createElement("tr");
tr.id = "tr-NIP-hook"
var td_label = document.createElement("td");
td_label.className="labelrc col-7"
td_label.innerText = "NIP"
var td_data = document.createElement("td");
td_data.className="data col-5"
var input = document.createElement("input");
input.className="x-form-text x-form-field "
input.id="NIP-hook"
td_data.appendChild(input)
tr.appendChild(td_label)
tr.appendChild(td_data)

e.after(tr)

var timeoutId;
$('#NIP-hook').on('input propertychange change', function() {
    console.log('NIP Change');
    
    clearTimeout(timeoutId);
    timeoutId = setTimeout(function() {
        // Runs 1 second (1000 ms) after the last change    
        saveToDB();
    }, 1000);
});

function saveToDB()
{
    console.log('Saving to the DB '+document.getElementById("NIP-hook").value);
	$.ajax({
		url: "http://10.149.219.161:5000/identification/json/",
		type: "POST",
		data: document.getElementById("NIP-hook").serialize(), // serializes the form's elements.
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

