<?php
/**
 * REDCap Hooks for eInclusion
 * Authors: David Baudoin (david.baudoin@aphp.fr) and Bastien Rance (bastien.rance@aphp.fr)
 * Date: 2020-06-22
 */
//error_reporting(E_ALL);

require_once '/var/www/html/redcap_connect.php'; # for Plugin; adjust path as needed
$user_id = USERID;

function redcap_data_entry_form_top($project_id, $record, $instrument, $event_id, $group_id, $repeat_instance) {
    print '<div class="yellow">Hook - Data Entry Form Top : Special announcement text to display at the top of every data entry form.</div>';
    print '<script type="text/javascript">console.log(\'hello\');</script>';
	
}


function redcap_every_page_top($project_id) {
    print("Hello, current id is ".$project_id);
    print("<br />");
    print("Hello, current user is ".$user_id);
    print('<div class="yellow">Hook - Hello World</div>');
}

function redcap_save_record($project_id, $record=null, $instrument, $event_id, $group_id=null, $survey_hash=null, $response_id=null, $repeat_instance=1){
    print '<script type="text/javascript">console.log(\'hi new '.$record.'\');</script>';
    print '<script type="text/javascript">alert(\'hi new '.$record.'\');</script>';
    file_put_contents('/tmp/rc_'.date("j.n.Y").'.log', $record, FILE_APPEND);
    //file_get_contents('http://10.149.219.161:5000/'.$record);
}

?>
