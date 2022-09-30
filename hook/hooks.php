<?php
/**
 * REDCap Hooks for eInclusion
 * Authors: David Baudoin (david.baudoin@aphp.fr) and Bastien Rance (bastien.rance@aphp.fr)
 * Date: 2020-06-22
 */
//error_reporting(E_ALL);

require_once '/var/www/html/redcap_connect.php'; # for Plugin; adjust path as needed
$user_id = USERID;

function redcap_data_entry_form($project_id, $record, $instrument, $event_id, $group_id, $repeat_instance) {
    $ip_address_port = 'http://10.149.219.161:5000';

	//1 recherche des differentes variables dans Einclusion
	$nip = file_get_contents($ip_address_port.'/ipp/'.$record.'/'.$project_id);
	$firstname = file_get_contents($ip_address_port.'/firstname/'.$record.'/'.$project_id);
	$lastname = file_get_contents($ip_address_port.'/lastname/'.$record.'/'.$project_id);
	$dateofbirth = file_get_contents($ip_address_port.'/dateofbirth/'.$record.'/'.$project_id);
	//on peut directement envoyer via php le user_id et le project_id
	$data_instrument = $instrument;
	//2 transmission a redcap
    print '<script type="text/javascript">
	re = document.getElementById("record_id-tr");

	// ajout des lignes identifiantes
	// 1 le NIP
	var tr = document.createElement("tr");
	tr.id = "tr-NIP-hook";
	var td_label = document.createElement("td");
	td_label.className="labelrc col-7";
	td_label.innerText = "IPP";
	var td_data = document.createElement("td");
	td_data.className="data col-5";
	var input = document.createElement("input");
	input.className="x-form-text x-form-field ";
	input.id="NIP-hook";
	input.readOnly = false;
	input.value = "'.$nip.'";
	td_data.appendChild(input);
	tr.appendChild(td_label);
	tr.appendChild(td_data);
	re.after(tr);

	// 2 firstname
	var tr2 = document.createElement("tr");
	tr2.id = "tr-firstname-hook";
	var td_label2 = document.createElement("td");
	td_label2.className="labelrc col-7";
	td_label2.innerText = "firstname";
	var td_data2 = document.createElement("td");
	td_data2.className="data col-5";
	var input2 = document.createElement("input");
	input2.className="x-form-text x-form-field ";
	input2.id="firstname-hook";
	input2.readOnly = false;
	input2.value = "'.$firstname.'";
	td_data2.appendChild(input2);
	tr2.appendChild(td_label2);
	tr2.appendChild(td_data2);
	re.after(tr2);

	// 3 name
	var tr3 = document.createElement("tr");
	tr3.id = "tr-lastname-hook";
	var td_label3 = document.createElement("td");
	td_label3.className="labelrc col-7";
	td_label3.innerText = "lastname";
	var td_data3 = document.createElement("td");
	td_data3.className="data col-5";
	var input3 = document.createElement("input");
	input3.className="x-form-text x-form-field ";
	input3.id="lastname-hook";
	input3.readOnly = false;
	input3.value = "'.$lastname.'";
	td_data3.appendChild(input3);
	tr3.appendChild(td_label3);
	tr3.appendChild(td_data3);
	re.after(tr3);

	// 4 date de naissance
	var tr4 = document.createElement("tr");
	tr4.id = "tr-dateofbirth-hook";
	var td_label4 = document.createElement("td");
	td_label4.className="labelrc col-7";
	td_label4.innerText = "dateofbirth";
	var td_data4 = document.createElement("td");
	td_data4.className="data col-5";
	var input4 = document.createElement("input");
	input4.className="x-form-text x-form-field ";
	input4.id="dateofbirth-hook";
	input4.readOnly = false;
	input4.value = "'.$dateofbirth.'";
	td_data4.appendChild(input4);
	tr4.appendChild(td_label4);
	tr4.appendChild(td_data4);
	re.after(tr4);

	// 5 recuperation du record_id
	re = document.getElementById("record_id-tr").getElementsByClassName("data col-5")[0].innerHTML;
	var record_id = "";
	$record_id = String(document.getElementById("record_id-tr").getElementsByClassName("data col-5")[0].innerHTML);

	// save data
	var timeoutId;
    $(\'#NIP-hook\').on(\'input propertychange change\', function() {
        console.log(\'NIP Change\');
    clearTimeout(timeoutId);
    timeoutId = setTimeout(function() {
        // Runs 1 second (1000 ms) after the last change
        saveToDB();
    }, 1000);
    });


    function saveToDB()
    {
    console.log(\'Saving to the DB \'+document.getElementById("NIP-hook").value);
    record_id = String(document.getElementById("record_id-tr").getElementsByClassName("data col-5")[0].innerHTML);
    //console.log("record_id:"+record_id)
	$.ajax({
		url: "'.$ip_address_port.'/identification/nip/",
		type: "POST",
		//data: document.getElementById("NIP-hook").serialize(), // serializes the form\'s elements.
		data: {ipp : $(\'#NIP-hook\').val(), record : record_id, user : "'.USERID.'", project : "'.$project_id.'", lastname : $(\'#lastname-hook\').val(), firstname : $(\'#firstname-hook\').val(), date_of_birth : $(\'#dateofbirth-hook\').val(), source : "redcap" },
		beforeSend: function(xhr) {
            // Let them know we are saving
			$(\'.form-status-holder\').html(\'Saving...\');
			console.log($(\'#NIP-hook\').val());
		},
		success: function(data) {
			var jqObj = jQuery(data); // You can get data returned from your ajax call here. ex. jqObj.find(\'.returned-data\').html()
            // Now show them we saved and when we did
            var d = new Date();
            $(\'.form-status-holder\').html(\'Saved! Last: \' + d.toLocaleTimeString());
		}
	});
    }
    //       end
    </script>';
}
?>
