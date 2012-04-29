<?php
//By hvn@familug.com
//at  Sun Apr 29 21:01:59 ICT 2012

/**
 * Return string with format DD-MM-YYYY */
function timestampToStringDMY ($timestamp)
{
		    $todayArr = getdate($timestamp);
		    $string =  $todayArr["mday"]. "-" . $todayArr["mon"] . "-" . $todayArr["year"];
		    return $string;
}//timestampToStringDMY

/**
 * Return string with format YYYY-MM-DD */
function timestampToStringYMD ($timestamp)
{
		    $todayArr = getdate($timestamp);
		    $string =  $todayArr["year"] . "-" .  $todayArr["mon"] . "-" . $todayArr["mday"] ;
		    return $string;
}//timestampToStringYMD
